import types
from typing import get_type_hints, get_origin, get_args

class CheckTypesMeta(type):
    @staticmethod
    def check_arg_types(func, args, arg_types):
        for arg_name, arg in zip(arg_types.keys(), args):
            if arg_name in arg_types:
                expected_type = arg_types[arg_name]
                if get_origin(expected_type) is list:
                    if not isinstance(arg, list) or not all(isinstance(item, get_args(expected_type)[0]) for item in arg):
                        raise TypeError(f"Argument {arg_name} is not of type {expected_type}")
                elif not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {arg_name} is not of type {expected_type}")

    @staticmethod
    def check_kwarg_types(kwargs, arg_types):
        for key, value in kwargs.items():
            if key in arg_types:
                expected_type = arg_types[key]
                if get_origin(expected_type) is list:
                    if not isinstance(value, list) or not all(isinstance(item, get_args(expected_type)[0]) for item in value):
                        raise TypeError(f"Argument {key} is not of type {expected_type}")
                elif not isinstance(value, expected_type):
                    raise TypeError(f"Argument {key} is not of type {expected_type}")

    @staticmethod
    def check_types_decorator(func):
        def wrapper(self, *args, **kwargs):
            arg_types = get_type_hints(func)
            CheckTypesMeta.check_arg_types(func, args, arg_types)
            CheckTypesMeta.check_kwarg_types(kwargs, arg_types)
            return func(self, *args, **kwargs)
        return wrapper

    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = CheckTypesMeta.check_types_decorator(attr_value)
        return super().__new__(mcs, name, bases, attrs)
