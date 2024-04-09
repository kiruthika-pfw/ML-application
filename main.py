from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Define a Pydantic model for the request body
class SummarizationRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: SummarizationRequest):
    # Initialize the summarization pipeline with the specified model
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    
    # Generate the summary for the input text
    summary = summarizer(request.text, max_length=150, min_length=50, do_sample=False)
    
    # Extract the summary text from the generated summary
    summary_text = summary[0]['summary_text'] if summary else "No summary generated"
    
    # Return the summary as a JSON response
    return {"summary": summary_text}
