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
ADU = st.text_input("Average Daily Usage Hours of social media (e.g: 2, 4.5)")
MUP = st.selectbox("Most Used Platform", ["Select", "Instagram", "TikTok", "Facebook", "WhatsApp", 
                                          "Twitter", "LinkedIn", "WeChat", "Snapchat", 
                                          "VKontakte", "LINE", "KakaoTalk", "YouTube"])
AAP = st.selectbox("Affects Academic Performance", ["Select", "Yes", "No"])
Shpn = st.text_input("Sleep Hours per Night (e.g: 5, 7.5)")
RS = st.selectbox("Relationship Status", ["Select", "Single", "In Relationship", "Complicated"])

# Predict Button
if st.button("Predict Mental Health Score"):
    if "Select" in [gender, AL, MUP, AAP, RS] or "" in [age, ADU, Shpn]:
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

            # Predict and show result
            result = pipe.predict(input_df)[0]
            score = round(result, 2)

            # Show result with emotion label
            if score < 4:
                st.error(f"😟 Low Mental Health Score: {score}")
            elif score < 7:
                st.warning(f"😐 Moderate Mental Health Score: {score}")
            else:
                st.success(f"😄 Good Mental Health Score: {score}")

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 Rajhans Bagri | All Rights Reserved"
    "</div>",
    unsafe_allow_html=True
)


