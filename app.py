import gradio as gr
def greet(name):
    return 'Hi, ' + name

app = gr.Interface(
    fn=greet,
    inputs= "text",
    outputs="text"
)

app.launch(share=True)