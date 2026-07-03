"""
utils.py

Utility functions for the
How Rich Would I Be? application.
"""

import pandas as pd


def format_currency(amount):
    """
    Format currency in Indian numbering system.

    Example:
    54327910 -> ₹5,43,27,910
    """

    amount = round(float(amount))

    num = str(abs(amount))

    if len(num) <= 3:
        result = num
    else:
        result = num[-3:]
        num = num[:-3]

        while len(num) > 2:
            result = num[-2:] + "," + result
            num = num[:-2]

        if num:
            result = num + "," + result

    if amount < 0:
        return f"-₹{result}"

    return f"₹{result}"


def format_large_number(amount):
    """
    Convert number into Lakhs / Crores.

    Example:
    2500000 -> ₹25.00 Lakhs
    """

    amount = float(amount)

    if amount >= 1e7:
        return f"₹{amount/1e7:.2f} Crore"

    elif amount >= 1e5:
        return f"₹{amount/1e5:.2f} Lakhs"

    else:
        return format_currency(amount)


def download_dataframe(df: pd.DataFrame):
    """
    Convert dataframe to CSV bytes.
    """

    return df.to_csv(index=False).encode("utf-8")


def calculate_cagr(initial, final, years):
    """
    Calculate CAGR.
    """

    if initial <= 0 or years <= 0:
        return 0

    return ((final / initial) ** (1 / years) - 1) * 100


def percentage_return(investment, portfolio):
    """
    Percentage gain.
    """

    if investment == 0:
        return 0

    return ((portfolio - investment) / investment) * 100


def years_remaining(current_age, retirement_age):
    """
    Remaining investment years.
    """

    return retirement_age - current_age
