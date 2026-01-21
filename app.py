import streamlit as st
import pandas as pd

# --- Model Parameters (original scale, from your notebook) ---
intercept = -416.85          # replace with your actual intercept_original_scale
rent_effect = 1.01      # replace with your actual rent_effect
commute_effect = 302.07     # replace with your actual commute_effect

# --- Load dataset (optional, just for reference in app) ---
df = pd.read_csv("rent_commute_data.csv")

# --- Streamlit UI ---
st.set_page_config(page_title="🏠 Rent vs Commute Predictor", layout="centered")

st.title("🏠 Rent vs Commute Cost Predictor")
st.write("Estimate your effective monthly life cost based on rent and commute time.")

# Sliders for user input
rent = st.slider("Monthly Rent (₹)", min_value=4000, max_value=25000, value=15000, step=500)
commute = st.slider("Daily Commute (minutes)", min_value=5, max_value=120, value=60, step=5)

# Calculate predicted life cost
predicted_cost = intercept + rent_effect * rent + commute_effect * commute

# Display predicted cost in a styled metric card
st.metric(label="💰 Predicted Monthly Life Cost", value=f"₹{int(predicted_cost):,}")

# Recommendation based on cost vs rent
if predicted_cost > 2 * rent:
    st.warning("⚠️ This choice might be expensive compared to rent!")
else:
    st.success("✅ This seems like a reasonable choice!")
#---
w_rent = rent_effect * rent
w_commute = commute_effect * commute

threshold = 0.15 #15% difference
diff_ratio = abs(w_rent - w_commute)/ max(w_rent, w_commute)
if diff_ratio < threshold:
    st.write("🎲Rent and commute contribute within a similar range to the predicted life cost.")
elif w_rent > w_commute:
    st.write("🏡Rent contributes nptoceably more to the predicted life cost than commute.")
else:
    st.write("🚕Commute contributes nptoceably more to the predicted life cost than rent.")



# Optional: Show sample dataset
if st.checkbox("Show sample dataset"):
    st.write(df.head())

#Optional: Show parameters
if st.checkbox("Show parameters"):
    st.write(intercept)
    st.write(rent_effect)
    st.write(commute_effect)

# Footer
st.markdown("---")
st.markdown("📊 Built with Linear Regression from scratch | Gradient Descent | Python + Streamlit")
