from fastapi import FastAPI

from app.application.controllers import router

app = FastAPI()

app.include_router(router=router, prefix="/api/users")
