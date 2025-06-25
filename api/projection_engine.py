from api.utils.tax_brackets import get_adjusted_brackets
# In projection loop
brackets = get_adjusted_brackets(
    data.current_year, data.current_year, data.filing_status,
    data.bracket_inflation_pct, data.bracket_rate_shift_pct,
    data.custom_future_brackets
)
taxable_income = data.retirement_income_future + conversion + rmd
tax = calculate_tax(taxable_income, brackets)
