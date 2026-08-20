import pandas as pd

def display_value(value, fallback="_"):
    if value is None or pd.isna(value):
        return fallback
    return str(value)