from fastapi import FastAPI

from src import endpoints

app = FastAPI()
app.include_router(endpoints.router)
