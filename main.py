from fastapi import FastAPI
# from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from starlette.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from routes.index import router
from config.db import SessionLocal

app = FastAPI()

origins = [
    "http://192.168.1.62:8080/",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router)
# @app.get('/')
# def home():
#     return {"key": "Hello"}
