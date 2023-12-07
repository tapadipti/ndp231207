import random
import sys, time
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    epochs = int(10)
    live.log_param("epochs", epochs)
    for epoch in range(epochs):
        live.log_metric("train/accuracy", epoch + random.random())
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy",epoch + random.random() )
        live.log_metric("val/loss", epochs - epoch - random.random())
        time.sleep(3)
        live.next_step()