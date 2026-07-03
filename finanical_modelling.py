"""
financial_model.py

Core financial calculations for the
'How Rich Would I Be?' Streamlit application.
"""

import pandas as pd


def calculate_sip(
    monthly_investment: float,
    annual_return: float,
    years: int
):
    """
    Calculates SIP growth month-by-month.

    Parameters
    ----------
    monthly_investment : float
        Monthly SIP amount.

    annual_return : float
        Expected annual return (%).

    years : int
        Investment duration.

    Returns
    -------
    dict
    """

    monthly_rate = annual_return / 100 / 12
    months = years * 12

    total_investment = 0
    portfolio_value = 0

    yearly_data = []

    for month in range(1, months + 1):

        # Existing portfolio grows
        portfolio_value *= (1 + monthly_rate)

        # New SIP invested
        portfolio_value += monthly_investment

        total_investment += monthly_investment

        # Store data every 12 months
        if month % 12 == 0:

            year = month // 12

            yearly_data.append(
                {
                    "Year": year,
                    "Investment": round(total_investment, 2),
                    "Portfolio Value": round(portfolio_value, 2),
                    "Returns": round(
                        portfolio_value - total_investment,
                        2
                    )
                }
            )

    future_value = portfolio_value

    wealth_created = future_value - total_investment

    return {
        "future_value": future_value,
        "total_investment": total_investment,
        "wealth_created": wealth_created,
        "yearly_data": pd.DataFrame(yearly_data)
    }


def adjust_for_inflation(
    future_value: float,
    inflation_rate: float,
    years: int
):
    """
    Calculates inflation-adjusted future value.
    """

    real_value = future_value / ((1 + inflation_rate / 100) ** years)

    return real_value


def calculate_all(
    current_age: int,
    retirement_age: int,
    monthly_investment: float,
    annual_return: float,
    inflation_rate: float
):
    """
    Main wrapper function.
    """

    years = retirement_age - current_age

    result = calculate_sip(
        monthly_investment,
        annual_return,
        years
    )

    real_value = adjust_for_inflation(
        result["future_value"],
        inflation_rate,
        years
    )

    result["real_value"] = real_value
    result["years"] = years

    return result
