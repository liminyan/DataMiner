class Fill_Average(object):
	"""docstring for Fill_Average"""
	def __init__(self, arg):
		super(Fill_Average, self).__init__()
		self.arg = arg
		print("Process:",arg)

	def x(self):
		pass

	def y(self):
		pass

class ML(object):
	"""docstring for ML"""
	def __init__(self, arg):
		super(ML, self).__init__()
		self.arg = arg
		print("Process:",arg)


	def x(self):
		pass

	def y(self):
		pass

class Fill_Median(object):
	"""docstring for Fill_Median"""
	def __init__(self, arg):
		super(Fill_Median, self).__init__()
		self.arg = arg
		print("Process:",arg)


	def x(self):
		pass

	def y(self):
		pass

class Del_Miss(object):
	"""docstring for Del_Miss"""
	def __init__(self, arg):
		super(Del_Miss, self).__init__()
		self.arg = arg
		print("Process:",arg)

	def x(self):
		pass

	def y(self):
		pass

class None_Process(object):
	"""docstring for None_Process"""
	def __init__(self, arg):
		super(None_Process, self).__init__()
		self.arg = arg
		print("Process:",arg)
		

	def x(self):
		pass

	def y(self):
		pass

class Process(object):
	"""docstring for Process"""
	def __init__(self, arg):
		super(Process, self).__init__()

		self.arg = arg
		if arg == "None":
			self.process = None_Process(arg)
		if arg == "ML":
			self.process = ML(arg)
		if arg == "Fill_Median":
			self.process = Fill_Median(arg)
		if arg == "Fill_Average":
			self.process = Fill_Average(arg)
		if arg == "Del_Miss":
			self.process = Del_Miss(arg)
			
	def x(self):
		return self.process.x()

	def y(self):
		return self.process.y()
		
