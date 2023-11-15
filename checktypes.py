import types

class CheckTypesMeta(type):
	@staticmethod
	def check_arg_types(func, args, arg_types):
		for arg_name, arg in zip(arg_types.keys(), args):
			if not isinstance(arg, arg_types[arg_name]):
				raise TypeError(f"Argument {arg_name} is not of type {arg_types[arg_name]}")

	@staticmethod
	def check_kwarg_types(kwargs, arg_types):
		for key, value in kwargs.items():
			if key in arg_types and not isinstance(value, arg_types[key]):
				raise TypeError(f"Argument {key} is not of type {arg_types[key]}")

	@staticmethod
	def check_types_decorator(func):
		def wrapper(self, *args, **kwargs):
			arg_types = func.__annotations__
			arg_names = list(func.__code__.co_varnames)
			arg_names.remove("self")
			for arg_name in arg_names:
				if arg_name not in arg_types:
					raise TypeError(f"Argument {arg_name} does not have a type annotation")
			CheckTypesMeta.check_arg_types(func, args, arg_types)
			CheckTypesMeta.check_kwarg_types(kwargs, arg_types)
			return func(self, *args, **kwargs)
		return wrapper

	def __new__(mcs, name, bases, attrs):
		for attr_name, attr_value in attrs.items():
			if isinstance(attr_value, types.FunctionType):
				attrs[attr_name] = CheckTypesMeta.check_types_decorator(attr_value)
		return super().__new__(mcs, name, bases, attrs)
