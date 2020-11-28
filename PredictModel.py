import ML
import OTHER

class None_Model(object):
	"""docstring for None_Model"""
	def __init__(self,arg):
		super(None_Model, self).__init__()
		self.arg = arg
		print("Model :" + arg)
	def train(self,input_x,input_y):
		print("train :" + self.arg)

	def print_res(self):
		pass


class Model(object):
	"""docstring for Model"""
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg
		if arg == "ML":
			self.Model = ML.Model(arg)

		if arg == "OTHER":
			self.Model = OTHER.Model(arg)

		if arg == "None":
			self.Model = None_Model(arg)


	def train(self,input_x,input_y):
		return self.Model.train(input_x,input_y)


	def print_res(self):
		return self.Model.print_res()
		