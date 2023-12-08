import random
import sys, time
from dvclive import Live
from PIL import Image
import numpy as np

with Live(save_dvc_exp=True) as live:
    epochs = int(10)
    sleep_time = 1.1
    image_size = "ten"
    data_size = 1
    live.log_param("epochs", epochs)
    live.log_param("sleep_time", sleep_time)
    live.log_param("image_size", image_size)
    live.log_param("data_size", data_size)
    for epoch in range(epochs):
        time.sleep(int(sleep_time))
        live.log_metric("train/accuracy", epoch + random.random())
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy",epoch + random.random() )
        live.log_metric("val/loss", epochs - epoch - random.random())
        data = ["Dummy data "] * 95300
        live.log_metric("data", ''.join(data))
        with open('new-file955.txt', 'w') as f: f.write(''.join(data))
        # live.log_image("image.jpg", Image.open(image_size + "-mb.jpg"))
