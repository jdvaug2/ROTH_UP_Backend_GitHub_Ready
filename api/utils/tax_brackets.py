def get_adjusted_brackets(
    filing_status: str,
    year: int,
    inflation_rate: float,
    rate_shift: float,
    custom_brackets: list = None
):
    if custom_brackets and len(custom_brackets) > 0:
        return custom_brackets

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
        ],
    }

    MAX_INFLATION = 0.50   # 50%
    MAX_RATE_SHIFT = 0.50  # 50%

    # Clamp values
    inflation = min(inflation_rate, MAX_INFLATION)
    rate_shift = min(rate_shift, MAX_RATE_SHIFT)

    adjusted = []
    for low, high, rate in base_brackets[filing_status]:
        new_low = round(low * (1 + inflation) ** (year - 2025))
        new_rate = round(rate * (1 + rate_shift), 4)

        if high == float("inf"):
         adjusted.append((new_low, float("inf"), new_rate))
        else:
         new_high = round(high * (1 + inflation) ** (year - 2025))
         adjusted.append((new_low, new_high, new_rate))

    return adjusted
