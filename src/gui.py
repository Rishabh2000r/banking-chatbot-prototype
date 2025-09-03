import gradio as gr
from chatbot import get_answer
import json

def read_log(filename="api_logs.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data
    
    except Exception as e:
        print(f"Unexpected error reading file: {e}")
        return []



def directQuery(query):
  return get_answer(query)



with gr.Blocks() as demo:
  
  with gr.Row("User Interaction"):
    query_input = gr.Textbox(label="Enter your Query")
    answer_output = gr.Textbox(label="Answer")
    query_input.submit(fn=directQuery, inputs=query_input, outputs=answer_output)

  #live api feed
  with gr.Row("API calls"):
    query_input = gr.Textbox(label="API Query", interactive=False,value=lambda :read_log()['Query'], every=0.2)   #very fast
    answer_output = gr.Textbox(label="Answer", interactive=False, value=lambda :read_log()['Answer'], every=0.2)





if __name__ == "__main__":
    demo.launch()