import pickle
import pandas as pd
import streamlit as st

# Load trained pipeline
pipe = pickle.load(open("StudentMentalHealthScore.pkl", "rb"))

# Streamlit UI
st.title("🧠 Student Mental Health Score Prediction")

# Inputs
age = st.text_input("Age (Numeric e.g: 20)")
gender = st.selectbox("Gender", ["Select", "Male", "Female"])
AL = st.selectbox("Academic Level", ["Select", "Undergraduate", "Graduate", "High School"])
ADU = st.text_input("Average Daily Usage Hours (e.g: 2, 4.5)")
MUP = st.selectbox("Most Used Platform", ["Select", "Instagram", "TikTok", "Facebook", "WhatsApp", 
                                          "Twitter", "LinkedIn", "WeChat", "Snapchat", 
                                          "VKontakte", "LINE", "KakaoTalk", "YouTube"])
AAP = st.selectbox("Affects Academic Performance", ["Select", "Yes", "No"])
Shpn = st.text_input("Sleep Hours per Night (e.g: 5, 7.5)")
RS = st.selectbox("Relationship Status", ["Select", "Single", "In Relationship", "Complicated"])

# Predict Button
if st.button("Predict Mental Health Score"):
    if (gender == "Select" or AL == "Select" or MUP == "Select" or AAP == "Select" or RS == "Select" or
        age == "" or ADU == "" or Shpn == ""):
        st.warning("⚠️ Please fill all inputs correctly.")
    else:
        try:
            # Prepare input as a DataFrame with correct column names
            input_df = pd.DataFrame({
                'Age': [float(age)],
                'Gender': [gender],
                'Academic_Level': [AL],
                'Avg_Daily_Usage_Hours': [float(ADU)],
                'Most_Used_Platform': [MUP],
                'Affects_Academic_Performance': [AAP],
                'Sleep_Hours_Per_Night': [float(Shpn)],
                'Relationship_Status': [RS]
            })

            # Predict
            prediction = pipe.predict(input_df)[0]
            st.success(f"🎯 Predicted Mental Health Score: {round(prediction, 2)} / 10")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
