from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from moto_service.routers import motorcycle_router
from moto_service.routers import client_router
from moto_service.services.db import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    print('startup')
    yield
    await database.disconnect()
    print('shutdown')

app = FastAPI(lifespan=lifespan)
app.include_router(client_router.router, tags=['clients'])
app.include_router(motorcycle_router.router, tags=['motorcycle'])


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def index():
    return RedirectResponse(url='/docs')
