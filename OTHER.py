class Model(object):
	"""docstring for Model
		写一些可解释模型
	"""
	def __init__(self, arg):
		super(Model, self).__init__()
		self.arg = arg
		print("Model :" + arg)

	
	def train(self,x,y):
		print("train :" + self.arg)
		

	def print_res(self):
		pass