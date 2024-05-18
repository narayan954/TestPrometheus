from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"Hello": "World"}

@app.get("/metrics")
def get_metrics():
    return PlainTextResponse(generate_latest())
