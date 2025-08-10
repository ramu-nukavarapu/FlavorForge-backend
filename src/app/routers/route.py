from fastapi import APIRouter, Body
from typing import List, Dict, Any
import pandas as pd

from app.models.schemas import AiSuggestion, Competitor, DashboardData, Product, TrendsData


router = APIRouter()

DATA_PATH = "data/"

@router.get("/dashboard", response_model=DashboardData)
async def get_dashboard():
    df = pd.read_csv(f"{DATA_PATH}dashboard.csv")
    metrics = df.iloc[0][[
        "totalProducts", "successRate", "activeUsers", "trendingCategories",
        "productsGrowth", "successRateGrowth", "usersGrowth"
    ]].to_dict()
    chart_data = df[["month", "beverages", "snacks", "dairy"]].to_dict(orient="records")
    return {
        **metrics,
        "growthMetrics": {
            "productsGrowth": metrics["productsGrowth"],
            "successRateGrowth": metrics["successRateGrowth"],
            "usersGrowth": metrics["usersGrowth"]
        },
        "chartData": chart_data
    }

@router.get("/products", response_model=List[Product])
async def get_products():
    return pd.read_csv(f"{DATA_PATH}products.csv").to_dict(orient="records")

@router.get("/trends", response_model=TrendsData)
async def get_trends():
    ingredients = pd.read_csv(f"{DATA_PATH}trends_ingredients.csv").to_dict(orient="records")
    regional = pd.read_csv(f"{DATA_PATH}trends_regional.csv").to_dict(orient="records")
    timeline = pd.read_csv(f"{DATA_PATH}trends_timeline.csv").to_dict(orient="records")
    return {
        "trendingIngredients": ingredients,
        "regionalData": regional,
        "timelineData": timeline
    }

@router.get("/competitors", response_model=List[Competitor])
async def get_competitors():
    return pd.read_csv(f"{DATA_PATH}competitors.csv").to_dict(orient="records")

@router.post("/ai-suggestions", response_model=List[AiSuggestion])
async def get_ai_suggestions(formData: Dict[str, Any] = Body(...)):
    print("Received form data for AI suggestions:", formData)
    return pd.read_csv(f"{DATA_PATH}ai_suggestions.csv").to_dict(orient="records")
