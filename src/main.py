from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import engine, Base
import os



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="infra-monitoring-api-1780125906525",
    description="A FastAPI + PostgreSQL project: infra-monitoring-api-1780125906525",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


    app.include_router(webhooks_router.router, prefix="/webhooks", tags=["webhooks"])

@app.get("/health")
async def health():
    return {"status": "ok", "service": "infra-monitoring-api-1780125906525"}
