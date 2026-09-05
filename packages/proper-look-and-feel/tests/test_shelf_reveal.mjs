import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import test from 'node:test';

const source = fs.readFileSync(new URL('../proper-shelf-reveal/contents/code/main.js', import.meta.url), 'utf8');
function harness(scale = 1) {
    const animations = [];
    let windowAdded;
    vm.runInNewContext(source, {
        effects: { windowAdded: { connect: callback => { windowAdded = callback; } } },
        Effect: { Opacity: 0, WindowAddedGrabRole: 1 },
        QEasingCurve: { InExpo: 0 },
        animationTime: duration => duration * scale,
        animate: settings => animations.push(settings)
    });
    return { animations, add: windowAdded };
}

function shelf(visible = true) {
    return { dock: true, visible, windowClass: 'plasmashell plasmashell',
        windowHiddenChanged: { connect(callback) { this.emit = callback; } } };
}

test('only a Plasma dock receives a finite reveal', () => {
    const h = harness();
    h.add({ dock: false, windowClass: 'plasmashell plasmashell' });
    h.add({ dock: true, windowClass: 'another dock' });
    assert.equal(h.animations.length, 0);
    h.add(shelf());
    assert.equal(h.animations.length, 1);
    assert.equal(h.animations[0].to, 1);
    assert.ok(h.animations[0].duration < 1000);
});

test('respects reduced motion', () => {
    const reduced = harness(0);
    reduced.add(shelf());
    assert.equal(reduced.animations[0].duration, 0);
});

test('waits for the first visible surface and never delays later unhiding', () => {
    const h = harness();
    const window = shelf(false);
    h.add(window);
    assert.equal(h.animations.length, 0);
    window.visible = true;
    window.windowHiddenChanged.emit(window);
    assert.equal(h.animations.length, 1);
    window.visible = false;
    window.windowHiddenChanged.emit(window);
    window.visible = true;
    window.windowHiddenChanged.emit(window);
    assert.equal(h.animations.length, 1);
});
