import gradio as gr
from applications.cam import CamApp

c = CamApp()

inp = gr.inputs.Image(label="Input Image", shape=(512,512))
out = gr.outputs.Image(label="Pose")
title="Pose Estimation"
description="Upload a picture of yourself or another person, and the Openpose algorithm will identify . Handles " \
            "multiple people."
examples = [
    ["obama.jpg"],
    ["uswnt.jpg"]
]
thumbnail = "https://github.com/gradio-app/hub-openpose/blob/master/screenshot.png?raw=true"
gr.Interface(c.process_frame, inp, out, title=title, thumbnail=thumbnail,
             description=description,
             examples=examples).launch()

