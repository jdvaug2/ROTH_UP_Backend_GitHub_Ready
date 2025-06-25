def get_adjusted_brackets(filing_status: str, year: int, inflation_rate: float, rate_shift: float):
    base_brackets = {
        "married": [
            (0, 22000, 0.10),
            (22001, 89450, 0.12),
            (89451, 190750, 0.22),
            (190751, 364200, 0.24),
            (364201, 462500, 0.32),
            (462501, 693750, 0.35),
            (693751, float("inf"), 0.37),
        ],
        "single": [
            (0, 11000, 0.10),
            (11001, 44725, 0.12),
            (44726, 95375, 0.22),
            (95376, 182100, 0.24),
            (182101, 231250, 0.32),
            (231251, 578125, 0.35),
            (578126, float("inf"), 0.37),
        ]
    }

    adjusted = []
    for low, high, rate in base_brackets[filing_status]:
        adjusted.append((
            round(low * (1 + inflation_rate) ** (year - 2025)),
            round(high * (1 + inflation_rate) ** (year - 2025)),
            round(rate * (1 + rate_shift), 4)
        ))
    return adjusted