// SPDX-License-Identifier: GPL-3.0-or-later

import QtQuick

Item {
    id: graph

    property var downloadHistory: []
    property var uploadHistory: []
    property color downloadColor: "#79eadb"
    property color uploadColor: "#91b4ff"

    onDownloadHistoryChanged: canvas.requestPaint()
    onUploadHistoryChanged: canvas.requestPaint()
    onWidthChanged: canvas.requestPaint()
    onHeightChanged: canvas.requestPaint()

    Canvas {
        id: canvas
        anchors.fill: parent
        antialiasing: true

        function maximum(first, second) {
            let result = 1;
            for (const values of [first, second]) {
                for (let index = 0; index < values.length; ++index) {
                    result = Math.max(result, Number(values[index]) || 0);
                }
            }
            return result;
        }

        function points(values, left, right, top, bottom, maximumValue) {
            const result = [];
            const step = (right - left) / Math.max(1, values.length - 1);
            for (let index = 0; index < values.length; ++index) {
                result.push({
                    x: left + index * step,
                    y: bottom - Math.min(1, (Number(values[index]) || 0) / maximumValue) * (bottom - top)
                });
            }
            return result;
        }

        function trace(context, values, left, right, top, bottom, maximumValue) {
            const path = points(values, left, right, top, bottom, maximumValue);
            if (path.length < 2) {
                return path;
            }
            context.moveTo(path[0].x, path[0].y);
            for (let index = 1; index < path.length; ++index) {
                const previous = path[index - 1];
                const current = path[index];
                context.quadraticCurveTo(previous.x, previous.y, (previous.x + current.x) / 2, (previous.y + current.y) / 2);
            }
            const last = path[path.length - 1];
            context.lineTo(last.x, last.y);
            return path;
        }

        function strokeTrace(context, values, color, lineWidth, left, right, top, bottom, maximumValue) {
            context.beginPath();
            const path = trace(context, values, left, right, top, bottom, maximumValue);
            if (path.length < 2) {
                return path;
            }
            context.lineWidth = lineWidth;
            context.strokeStyle = color;
            context.stroke();
            return path;
        }

        onPaint: {
            const context = getContext("2d");
            context.reset();
            const left = 2;
            const right = width - 2;
            const top = 8;
            const bottom = height - 8;
            const maximumValue = maximum(graph.downloadHistory, graph.uploadHistory);

            context.strokeStyle = "rgba(166,175,189,0.11)";
            context.lineWidth = 1;
            for (const ratio of [0.25, 0.5, 0.75]) {
                const y = Math.round(top + (bottom - top) * ratio) + 0.5;
                context.beginPath();
                context.moveTo(left, y);
                context.lineTo(right, y);
                context.stroke();
            }

            const downloadPoints = points(graph.downloadHistory, left, right, top, bottom, maximumValue);
            if (downloadPoints.length >= 2) {
                context.beginPath();
                trace(context, graph.downloadHistory, left, right, top, bottom, maximumValue);
                context.lineTo(right, bottom);
                context.lineTo(left, bottom);
                context.closePath();
                const fill = context.createLinearGradient(0, top, 0, bottom);
                fill.addColorStop(0, "rgba(121,234,219,0.24)");
                fill.addColorStop(1, "rgba(121,234,219,0.015)");
                context.fillStyle = fill;
                context.fill();
            }

            const downloadPath = strokeTrace(context, graph.downloadHistory, graph.downloadColor, 1.7, left, right, top, bottom, maximumValue);
            const uploadPath = strokeTrace(context, graph.uploadHistory, graph.uploadColor, 1.35, left, right, top, bottom, maximumValue);

            for (const endpoint of [
                { path: downloadPath, color: graph.downloadColor },
                { path: uploadPath, color: graph.uploadColor }
            ]) {
                if (endpoint.path.length === 0) {
                    continue;
                }
                const last = endpoint.path[endpoint.path.length - 1];
                context.fillStyle = endpoint.color;
                context.beginPath();
                context.arc(last.x, last.y, 3, 0, Math.PI * 2);
                context.fill();
            }
        }
    }
}
