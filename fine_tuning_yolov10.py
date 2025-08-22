from ultralytics import YOLO

model = YOLO('yolov10n.pt')
print(model.info())
YAML_PATH = r'../Safety_Helmet_Dataset/data.yaml'
EPOCHS = 20
IMG_SIZE = 416
BATCH_SIZE = 32

model.train(
    data = YAML_PATH,
    epochs = EPOCHS,
    batch = BATCH_SIZE,
    imgsz = IMG_SIZE
)