from transformers import pipeline
import gradio as gr


def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary


if __name__ == "__main__":
    model = pipeline("summarization")

    with gr.Blocks() as demo:
        textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
        gr.Interface(fn=predict, inputs=textbox, outputs="text")

    demo.launch()
