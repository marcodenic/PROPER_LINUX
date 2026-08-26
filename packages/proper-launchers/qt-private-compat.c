#define _GNU_SOURCE
#include <dlfcn.h>
#include <stddef.h>

typedef void (*mark_fn)(void *, void *);

static mark_fn resolve_mark(const char *name)
{
    return (mark_fn)dlvsym(RTLD_NEXT, name, "Qt_6.11_PRIVATE_API");
}

void mark_qobject(void *object, void *stack)
    __asm__("_ZN11QQmlPrivate18AOTCompiledContext4markEP7QObjectPN3QV49MarkStackE");
void mark_qobject(void *object, void *stack)
{
    mark_fn fn = resolve_mark("_ZN11QQmlPrivate18AOTCompiledContext4markEP7QObjectPN3QV49MarkStackE");
    if (fn) fn(object, stack);
}

void mark_variant(const void *variant, void *stack)
    __asm__("_ZN11QQmlPrivate18AOTCompiledContext4markERK8QVariantPN3QV49MarkStackE");
void mark_variant(const void *variant, void *stack)
{
    mark_fn fn = resolve_mark("_ZN11QQmlPrivate18AOTCompiledContext4markERK8QVariantPN3QV49MarkStackE");
    if (fn) fn((void *)variant, stack);
}
