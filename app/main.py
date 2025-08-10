from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import route

app = FastAPI(
    title="Simple API Backend",
    description="Serves mock data from CSV files for a frontend application.",
    version="1.0.0",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register router
app.include_router(route.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API is running. See /docs for endpoints."}
