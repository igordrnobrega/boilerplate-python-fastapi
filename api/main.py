from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/_healthcheck", response_class=PlainTextResponse)
async def healthcheck():
    return "OK"
