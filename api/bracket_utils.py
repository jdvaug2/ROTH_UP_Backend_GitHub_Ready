
def get_adjusted_brackets(year, current_year, filing_status, inflation_pct, rate_shift_pct, override=None):
    IRS_BRACKETS = {
        "married": [
            (0, 22000, 0.10),
            (22001, 89450, 0.12),
            (89451, 190750, 0.22),
            (190751, 364200, 0.24),
        ],
        "single": [
            (0, 11000, 0.10),
            (11001, 44725, 0.12),
            (44726, 95375, 0.22),
            (95376, 182100, 0.24),
        ]
    }
    if override:
        return override

    base = IRS_BRACKETS[filing_status]
    years_forward = year - current_year
    brackets = []
    for lower, upper, rate in base:
        adj_lower = lower * ((1 + inflation_pct) ** years_forward)
        adj_upper = upper * ((1 + inflation_pct) ** years_forward)
        adj_rate = rate * (1 + rate_shift_pct)
        brackets.append((adj_lower, adj_upper, adj_rate))
    return brackets
