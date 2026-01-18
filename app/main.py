from fastapi import FastAPI

app = FastAPI(title="Mobile Analytics BE")

@app.get("/health")
async def health():
    return {"status": "ok"}