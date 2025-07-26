from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.get("/")
async def root(request: Request):
    print(f"Request received: {request.method} {request.url}")
    
    request_info = {
            "method": request.method,
            "url": str(request.url),
            "headers": dict(request.headers),
            "query_params": dict(request.query_params)
        }
        
    print("Request JSON: ", json.dumps(request_info, indent=2))

    return {f"Request received {json.dumps(request_info)}"}