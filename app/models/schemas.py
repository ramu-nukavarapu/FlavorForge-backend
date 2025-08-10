from pydantic import BaseModel
from typing import List, Dict, Any

class GrowthMetrics(BaseModel):
    productsGrowth: int
    successRateGrowth: int
    usersGrowth: int

class DashboardData(BaseModel):
    totalProducts: int
    successRate: int
    activeUsers: int
    trendingCategories: int
    growthMetrics: GrowthMetrics
    chartData: List[Dict[str, Any]]

class Product(BaseModel):
    id: int
    name: str
    category: str
    score: int
    status: str
    created: str

class TrendingIngredient(BaseModel):
    name: str
    score: int
    growth: str

class RegionalData(BaseModel):
    region: str
    percentage: int

class TimelineData(BaseModel):
    month: str
    healthy: int
    organic: int
    plantBased: int
    functional: int

class TrendsData(BaseModel):
    trendingIngredients: List[TrendingIngredient]
    regionalData: List[RegionalData]
    timelineData: List[TimelineData]

class Competitor(BaseModel):
    company: str
    products: int
    score: int
    trend: str

class AiSuggestion(BaseModel):
    name: str
    score: int
    description: str
