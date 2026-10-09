from fastapi import FastAPI

app = FastAPI()

POSITIVE = {"good", "great", "love", "awesome", "happy","amazing"}
NEGATIVE = {"bad", "terrible", "hate", "awful", "sad"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(text: str):
    words = set(text.lower().split())
    score = len(words & POSITIVE) - len(words & NEGATIVE)
    label = "positive" if score > 0 else "negative" if score < 0 else "neutral"
    return {"text": text, "label": label, "score": score}

