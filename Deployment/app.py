import streamlit as st
import pandas as pd
import pickle
import sys
print(sys.executable)

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="IPL Predictor", page_icon="🏏", layout="wide")

# ---------- LOAD FILES ----------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>🏏 IPL Match Winner Predictor</h1>", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.header("Match Details")

teams = [
    'Royal Challengers Bengaluru','Mumbai Indians','Chennai Super Kings',
    'Kolkata Knight Riders','Delhi Capitals','Punjab Kings',
    'Sunrisers Hyderabad','Rajasthan Royals','Lucknow Super Giants','Gujarat Titans'
]

venues = [
    'Mumbai','Delhi','Chennai','Kolkata','Hyderabad',
    'Bangalore','Jaipur','Ahmedabad','Lucknow','Mohali'
]

team1 = st.sidebar.selectbox("Select Team 1", teams)
team2 = st.sidebar.selectbox("Select Team 2", teams)
venue = st.sidebar.selectbox("Select Venue", venues)

# ---------- VALIDATION ----------
if team1 == team2:
    st.warning("⚠️ Team 1 and Team 2 must be different!")
else:
    if st.button("🔮 Predict Winner"):

        # ---------- INPUT ----------
        input_df = pd.DataFrame({
            'team1': [team1],
            'team2': [team2],
            'venue': [venue],
            'toss_winner': [team1],
            'toss_decision': [0]
        })

        # ---------- PREPROCESS ----------
        input_df = pd.get_dummies(input_df)

        # ✅ IMPORTANT FIX: match training columns
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # ✅ convert to DataFrame again after scaling (fix warning + alignment)
        input_scaled = scaler.transform(input_df)
        input_scaled = pd.DataFrame(input_scaled, columns=columns)

        # ---------- PREDICTION ----------
        prediction = model.predict(input_scaled)[0]

        # ✅ SAFER LOGIC
        winner = team1 if prediction == 1 else team2

        # ---------- OUTPUT ----------
        st.markdown("## 🏆 Predicted Winner")
        st.success(f"{winner}")