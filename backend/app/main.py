from fastapi import FastAPI

app = FastAPI(title="Flix Exchange")

@app.get("/health")
def health():
    return {"status": "ok"}
