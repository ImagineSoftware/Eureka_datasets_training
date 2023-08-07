from ultralytics import YOLO

import sys
sys_args = sys.argv

try:
    no_of_epochs = int(sys_args[1])
except:
     no_of_epochs = 1

# # Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# # # Use the model
results = model.train(data="config.yaml", epochs=no_of_epochs)  # train the model