import uvicorn
from fastapi import FastAPI
from pydantic import BaseSettings


class ServerSettings(BaseSettings):
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 7000
    RELOAD: bool = True


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello From NCP"}


@app.get("/health")
async def health_check():
    return {"status": "UP"}


if __name__ == "__main__":
    server = ServerSettings()
    uvicorn.run(
        "main:app",
        host=server.SERVER_HOST,
        port=server.SERVER_PORT,
        reload=server.RELOAD,
    )
