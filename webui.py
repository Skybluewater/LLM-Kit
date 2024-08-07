import torch
import os

torch.cuda.device_count()
import gradio as gr
from ui import data, train, apply, chat
from utils.ui_utils import load_javascript
from utils.language_switch_utils import Localizer
import argparse

parser = argparse.ArgumentParser(description="Language")
parser.add_argument("--language", type=str, default="auto", help="auto/en_UK")
arg = parser.parse_args()

localizer = Localizer(arg.language)


# I save the base64 code below into a file named logo.txt, and I want to read out the content of the file via an method
# please write it for me
def read_logo_base64():
    with open("img/logo", "r") as f:
        return f.read()


with gr.Blocks(analytics_enabled=False) as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=100):
            logo_base64 = read_logo_base64()
            gr.HTML(f'''
                <div id="logo_container">
                    <img src="data:image/png;base64,{logo_base64}" id="logo" />
                    <div id="lab_name">数字表演与仿真实验室</div>
                </div>
            ''')
        with gr.Column(scale=15):
            with gr.Tab(localizer("聊天")):
                chat.chat_page(localizer)
            with gr.Tab(localizer("数据")):
                data.data_page(localizer)
            with gr.Tab(localizer("应用")):
                apply.apply_page(localizer)
            with gr.Tab(localizer("训练")):
                train.train_page(localizer)

load_javascript()
allowed_path = f"{os.getcwd()}/data/config/styles"
print(allowed_path)

demo.queue(concurrency_count=3).launch(_frontend=False, inbrowser=True,
                                       allowed_paths=[allowed_path])
