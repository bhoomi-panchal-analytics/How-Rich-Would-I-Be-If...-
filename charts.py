"""
charts.py

All Plotly visualizations for the
How Rich Would I Be? application.
"""

import plotly.graph_objects as go
import plotly.express as px


def portfolio_growth_chart(df):
    """
    Portfolio value over time.
    """

    fig = px.line(
        df,
        x="Year",
        y="Portfolio Value",
        markers=True,
        title="📈 Portfolio Growth"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="Years",
        yaxis_title="Portfolio Value (₹)",
        hovermode="x unified"
    )

    return fig


def investment_vs_returns_chart(df):
    """
    Investment vs Returns Area Chart
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Investment"],
            mode="lines",
            stackgroup="one",
            name="Investment"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Year"],
            y=df["Returns"],
            mode="lines",
            stackgroup="one",
            name="Returns"
        )
    )

    fig.update_layout(
        title="💰 Investment vs Wealth Created",
        template="plotly_white",
        height=500,
        xaxis_title="Years",
        yaxis_title="Amount (₹)"
    )

    return fig


def wealth_breakdown_chart(total_investment, wealth_created):
    """
    Pie Chart
    """

    fig = px.pie(
        values=[total_investment, wealth_created],
        names=["Investment", "Returns"],
        title="Portfolio Breakdown"
    )

    fig.update_layout(
        height=450
    )

    return fig
