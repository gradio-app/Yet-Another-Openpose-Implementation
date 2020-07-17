import gradio as gr
from applications.cam import CamApp

c = CamApp()

inp = gr.inputs.Image(label="Input Image", shape=(512,512))
out = gr.outputs.Image(label="Pose")
title="Pose Estimation"
description="A Tensorflow implementation of the Openpose algorithm. Handles " \
            "multiple people."
examples = [
    ["obama.jpg"],
    ["uswnt.jpg"]
]
gr.Interface(c.process_frame, inp, out, title=title,
             description=description,
             examples=examples).launch()

