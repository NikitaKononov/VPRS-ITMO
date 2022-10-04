from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "OK"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', workers=1, port=3001)

