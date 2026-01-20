# rent-vs-commute-cost-predictor
A real life Linear Regression project using Gradient Descent from scratch to analyze rent vs  commute trade-offs.

# Rent vs Commute Cost Predictor

## Problem Statement
Choosing a house based only on rent ignores hidden costs like commute time.
This project predicts the effective monthly life cost using Linear Regression.

## Approach
- Created a synthetic dataset based on realistic cost assumptions
- Implemented Linear Regression using Gradient Descent from scratch
- Analyzed feature impact and model limitations
- Built an interactive UI (Streamlit)

## Tech Stack
- Python
- NumPy, Pandas, Matplotlib
- Streamlit
- Figma (UI Design)

## Status
🚧 In Progress — Dataset creation

Each minute of daily commute has an estimated cost of Rs. 10 due to time, energy and transport. 
Hence: life_cost = rent + (commute_minutes * 30 * 10) + noise
