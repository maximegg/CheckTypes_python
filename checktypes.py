import types

class CheckTypesMeta(type):
	@staticmethod
	def check_types_decorator(func):
		def wrapper(self, *args, **kwargs):
			arg_types = func.__annotations__
			for arg_name, arg in zip(arg_types.keys(), args):
				if not isinstance(arg, arg_types[arg_name]):
					raise TypeError(f"L'argument {arg_name} n'est pas du type {arg_types[arg_name]}")
			for key, value in kwargs.items():
				if key in arg_types and not isinstance(value, arg_types[key]):
					raise TypeError(f"L'argument {key} n'est pas du type {arg_types[key]}")
			return func(self, *args, **kwargs)
		return wrapper

	def __new__(mcs, name, bases, attrs):
		for attr_name, attr_value in attrs.items():
			if isinstance(attr_value, types.FunctionType):
				attrs[attr_name] = CheckTypesMeta.check_types_decorator(attr_value)
		return super().__new__(mcs, name, bases, attrs)
