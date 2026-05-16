from fastapi import FastAPI

from app.routes.chat import router as chat_router


app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(chat_router)