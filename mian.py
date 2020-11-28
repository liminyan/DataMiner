import DataProcess
import PredictModel

# DataProcess 
method = "None"
myDataProcess = DataProcess.Process(method)
input_x = myDataProcess.x()
input_y = myDataProcess.y()

# PrecdicModel
model = "None"
myModel = PredictModel.Model(model)
myModel.train(input_x,input_y)
myModel.print_res()


