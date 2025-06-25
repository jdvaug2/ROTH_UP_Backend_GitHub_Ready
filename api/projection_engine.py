from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal, List
from api.utils.tax_brackets import get_adjusted_brackets

router = APIRouter()

class ProjectionInput(BaseModel):
    filing_status: Literal["single", "married"]
    current_year: int
    bracket_inflation_pct: float
    bracket_rate_shift_pct: float
    custom_future_brackets: List[List[float]]
    retirement_income_future: float
    conversion: float
    rmd: float

@router.post("/project")
def simulate_projection(data: ProjectionInput):
    brackets = get_adjusted_brackets(
        data.current_year,
        data.current_year,
        data.filing_status,
        data.bracket_inflation_pct,
        data.bracket_rate_shift_pct,
        data.custom_future_brackets
    )

    taxable_income = data.retirement