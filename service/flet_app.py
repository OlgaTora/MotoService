from contextlib import asynccontextmanager

import flet as ft
import flet.fastapi as flet_fastapi
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

app = FastAPI(lifespan=lifespan)

async def main(page: ft.Page):
    await page.add_async(ft.Text("Hello, Flet!"))

app.mount("/flet-app", flet_fastapi.app(main))