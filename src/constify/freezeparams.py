import copy
import inspect
import functools
from typing import Any, Callable


def freezeparams(func: Callable[..., Any]):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        parameters = inspect.signature(func).parameters
        default_kwargs = {
            key: value
            for key, param in parameters.items()
            if (value := param.default) != inspect.Parameter.empty
        }

        args_to_kwargs = {}
        if args:
            args = copy.deepcopy(args)
            bound_arguments = inspect.signature(func).bind(*args)
            bound_arguments.apply_defaults()
            args_to_kwargs = bound_arguments.arguments
            args = ()

        kwargs = copy.deepcopy(default_kwargs | args_to_kwargs | kwargs)

        return func(*args, **kwargs)

    return wrapper
