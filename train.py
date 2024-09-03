from ultralytics import YOLO

def train(model_name):
    model = YOLO(f'{model_name}/yolov8n.pt')  
    model.train(
        task = "detect",
        mode = "train",
        data = f"{model_name}/{model_name}.config.yaml",
        epochs = 150,
        patience = 20,
        batch = 32,
        imgsz = 640,
        workers = 8,
        optimizer = "Adam",
        lr0 = 0.001,
        lrf = 0.01,
        weight_decay = 0.0001,
        warmup_epochs = 10.0,
        warmup_momentum = 0.8,
        warmup_bias_lr = 0.1,
        conf = 0.1,
        iou = 0.1,
        augment = True,
        overlap_mask = True,
        dropout = 0.1,
        val = True,
        box = 0.1,
        cls = 0.1,
        label_smoothing = 0.1,
    )
    return
