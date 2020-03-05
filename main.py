import uvicorn
from fastapi import FastAPI
from app.router import api_router


app = FastAPI(docs_url=None,redoc_url=None)
app.include_router(api_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')