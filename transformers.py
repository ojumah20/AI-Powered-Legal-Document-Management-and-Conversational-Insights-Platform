from transformers import pipeline

summarizer = pipeline("summarization")

@app.post("/summarize/")
def summarize_document(path: str):
    with open(path, "r") as file:
        text = file.read()
    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
    return {"summary": summary[0]['summary_text']}
