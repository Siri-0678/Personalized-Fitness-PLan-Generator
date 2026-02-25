import streamlit as st
import os
from huggingface_hub import InferenceClient
from prompt_builder import build_prompt


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="FitPlan AI", page_icon="💪", layout="centered")


# ---------------- MODEL FUNCTION ----------------
def query_model(prompt):
    try:
        HF_TOKEN = os.getenv("HF_SECRET")

        if not HF_TOKEN:
            return "❌ HF_SECRET not found. Please set your HuggingFace token."

        client = InferenceClient(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            token=HF_TOKEN
        )

        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are a certified professional fitness trainer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=22000,   # Safe limit
            temperature=0.7
        )

        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Model Error: {str(e)}"


# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "landing"

if "result" not in st.session_state:
    st.session_state.result = None


# ---------------- GLOBAL STYLING ----------------
st.markdown("""
<style>
/* Gradient Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #b57edc, #e573a9);
    background-attachment: fixed;
}
.block-container {
    padding-top: 0rem;
}
/* Center Layout */
.main-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
}
.main-card h1 {
    text-align: center;
    font-weight: 700;
    color: #333;
    margin-bottom: 10px;
}
.main-card h3 {
    text-align: center;
    font-weight: 500;
    color: #666;
    margin-bottom: 25px;
}
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    border-radius: 4px !important;
}
.stButton > button {
    display: block;
    margin: 25px auto 0 auto;
    background-color: #333;
    color: white;
    border-radius: 20px;
    padding: 10px 28px;
    border: none;
    font-weight: 500;
}
.stButton > button:hover {
    background-color: #111;
}
.result-box {
    background: #fafafa;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid #eee;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- LANDING PAGE ----------------
if st.session_state.page == "landing":

    st.markdown('<div class="main-wrapper"><div class="main-card">', unsafe_allow_html=True)

    st.markdown("<h1>💪 Welcome to FitPlan AI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>AI-Generated Workout Designed For YOU</h3>", unsafe_allow_html=True)

    st.write("Fill your profile and get a scientifically tailored 5-day fitness plan.")

    if st.button("🚀 Get Started"):
        st.session_state.page = "main"
        st.rerun()

    st.markdown('</div></div>', unsafe_allow_html=True)


# ---------------- MAIN PAGE ----------------
elif st.session_state.page == "main":

    st.markdown('<div class="main-wrapper"><div class="main-card">', unsafe_allow_html=True)

    st.markdown("<h1>💪 FitPlan AI</h1>", unsafe_allow_html=True)
    

    # ---------------- INPUTS ----------------
    name = st.text_input("Name *")
    age = st.number_input("Age *", min_value=0, step=1)
    gender = st.selectbox("Gender *", ["", "Male", "Female", "Other"])
    height_cm = st.number_input("Height (cm) *", min_value=0.0)
    weight_kg = st.number_input("Weight (kg) *", min_value=0.0)

    goal = st.selectbox(
        "Fitness Goal *",
        ["", "Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
    )

    equipment = st.multiselect(
        "Equipment *",
        ["Dumbbells", "Resistance Band", "Yoga Mat", "Inclined bench",
         "Cycle", "Treadmill", "Skipping rope", "Pullups bar",
         "Weight plates", "Hula hoop ring"]
    )

    fitness_level = st.radio(
        "Fitness Level *",
        ["Beginner", "Intermediate", "Advanced"]
    )

    # ---------------- SUBMIT ----------------
    if st.button("Submit Profile"):

        if not name:
            st.error("This field is compulsory: Name")

        elif age <= 0:
            st.error("This field is compulsory: Age")

        elif not gender:
            st.error("This field is compulsory: Gender")

        elif height_cm <= 0:
            st.error("This field is compulsory: Height")

        elif weight_kg <= 0:
            st.error("This field is compulsory: Weight")

        elif not goal:
            st.error("This field is compulsory: Fitness Goal")

        elif not equipment:
            st.error("This field is compulsory: Equipment")

        else:
            st.success("Profile Submitted Successfully!")

            prompt, bmi, bmi_status = build_prompt(
                name,
                gender,
                height_cm,
                weight_kg,
                goal,
                fitness_level,
                equipment
            )

            enhanced_prompt = f"""
{prompt}
User Age: {age}
Act as an experienced strength & conditioning coach.
Analyze:
• Age
• BMI status
• Fitness level
• Goal
• Equipment access
Design a personalized 5-day weekly training program.
Each day must include:
• Training Focus
• Warm-up
• Main Workout (Sets × Reps)
• Rest Period
• Cool Down
After Day 5 include:
• Weekly Coaching Tips
• Nutrition Guidance
• Recovery Strategy
• Safety Notes
Do NOT create a generic template.
Make it professional and realistic.
"""

            with st.spinner("Generating Workout Plan..."):
                st.session_state.result = query_model(enhanced_prompt)

            st.info(f"BMI: {bmi:.2f} ({bmi_status})")

    # ---------------- DISPLAY RESULT ----------------
    if st.session_state.result:
        st.subheader("🏋️ Your Personalized Workout Plan")

        st.markdown(f"""
        <div class="result-box">
        {st.session_state.result}
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            label="📄 Download Plan",
            data=st.session_state.result,
            file_name="fitplan_workout.txt",
            mime="text/plain"
        )

    st.markdown('</div></div>', unsafe_allow_html=True)
