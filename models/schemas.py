
from pydantic import BaseModel
from typing import Literal, Optional, List, Tuple

class ProjectionInput(BaseModel):
    filing_status: Literal["single", "married"]
    current_year: int
    age1: int
    age2: int
    life_expectancy1: int
    life_expectancy2: int
    trad_ira_start: float
    roth_ira_start: float
    taxable_start: float
    current_income_spouse1: float
    current_income_spouse2: float
    retirement_income_future: float
    conversion_amount: float
    growth_rate: float
    tax_drag: float
    pay_tax_out_of_pocket: bool
    bracket_inflation_pct: float
    bracket_rate_shift_pct: float
    custom_future_brackets: Optional[List[Tuple[float, float, float]]]
