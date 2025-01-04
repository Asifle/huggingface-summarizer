from transformers import pipeline

# Cache the summarizer model to avoid repeated loading
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summarize_text(text, max_length=300, min_length=80):
    try:
        # Limit the input size for efficiency
        if len(text) > 1024:
            text = text[:1024]

        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text'], None
    except Exception as e:
        return None, f"Error during summarization: {e}"
