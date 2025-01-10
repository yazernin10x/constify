from ._freezeparams import freezeparams

# Adjust __module__ to show objects as part of the current package
for value in list(locals().values()):
    if getattr(value, "__module__", "").startswith(__name__):
        value.__module__ = __name__
