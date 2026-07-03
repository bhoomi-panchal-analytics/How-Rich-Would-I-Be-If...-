# 💰 How Rich Would I Be?

An interactive financial planning application that helps users estimate how much wealth they can accumulate through disciplined monthly investing. The application demonstrates the power of compound interest, long-term investing, and the impact of inflation using an intuitive dashboard and interactive visualizations.

---

## 📌 Overview

Most people underestimate the power of consistent investing over long periods.

**How Rich Would I Be?** allows users to experiment with different investment scenarios and instantly visualize how their money grows over time. By combining financial modelling with an interactive user interface, the project transforms complex financial calculations into an engaging and easy-to-understand experience.

---

## ✨ Features

* Calculate future value of monthly SIP investments
* Adjustable investment assumptions
* Inflation-adjusted wealth calculation
* Interactive wealth growth chart
* Investment vs. Returns comparison
* Year-wise portfolio value table
* Indian currency formatting (₹, Lakhs, Crores)
* Clean and responsive Streamlit interface

---

## 📊 Inputs

Users can customize:

* Current Age
* Retirement Age
* Monthly SIP Amount
* Expected Annual Return (%)
* Inflation Rate (%)

---

## 📈 Outputs

The application calculates:

* Future Portfolio Value
* Total Amount Invested
* Total Wealth Created
* Inflation Adjusted (Real) Wealth
* Year-by-Year Portfolio Growth

---

## 🧮 Financial Model

The application uses the Future Value of SIP formula:

[
FV = SIP \times \frac{(1+r)^n - 1}{r} \times (1+r)
]

where:

* **SIP** = Monthly Investment
* **r** = Monthly Rate of Return
* **n** = Total Number of Monthly Investments

Real wealth is calculated after adjusting for inflation.

---

## 🛠 Tech Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

---

## 📂 Project Structure

```text
How-Rich-Would-I-Be/
│
├── app.py
├── financial_model.py
├── charts.py
├── utils.py
├── requirements.txt
├── README.md
├── assets/
└── screenshots/
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/how-rich-would-i-be.git
```

Move into the project directory:

```bash
cd how-rich-would-i-be
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

* Home Dashboard
* User Inputs
* Wealth Growth Chart
* Investment vs Returns Chart
* Results Dashboard

---

## 🎯 Learning Outcomes

Through this project, I explored:

* Financial modelling concepts
* Compound interest calculations
* Inflation-adjusted wealth estimation
* Data visualization using Plotly
* Building interactive applications with Streamlit
* Creating clean and user-friendly financial dashboards

---

## 🔮 Future Improvements

* Goal-based investment planning
* Step-up SIP calculator
* Lump sum investment analysis
* Retirement planning module
* Monte Carlo simulations
* Multiple asset class comparison
* Portfolio recommendation engine
* AI-powered financial insights
* PDF report generation
* Historical market return analysis

---

## 👩‍💻 Author

**Bhoomi Panchal**

B.Sc. Data Science | Aspiring Financial Analyst

Passionate about building finance-focused applications using Python, financial modelling, and data analytics.

---

## ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub and feel free to share feedback or suggestions for future improvements.
