import streamlit as st

st.set_page_config(
    page_title="FitPlan AI",
    page_icon="💪",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dff6ff, #f8fbff);
}


.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 10px;
}

.stButton>button {
    width: 100%;
    background-color: #007bff;
    color: white;
    font-weight: 600;
    padding: 12px;
    border-radius: 10px;
    border: none;
}

.stButton>button:hover {
    background-color: #0056b3;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; margin-bottom:30px;'>💪 FitPlan AI</h1>", unsafe_allow_html=True)

st.markdown('<div class="section-title">👤 Personal Information</div>', unsafe_allow_html=True)

name = st.text_input("Name")
height_cm = st.number_input("Height (in centimeters)", min_value=0.0, step=0.1)
weight_kg = st.number_input("Weight (in kilograms)", min_value=0.0, step=0.1)

st.markdown('<div class="section-title">🏋 Fitness Details</div>', unsafe_allow_html=True)

goal = st.selectbox(
    "Fitness Goal",
    [
        "Flexible",
        "Weight Loss",
        "Build Muscle",
        "Strength Gaining",
        "Abs Building"
    ]
)

st.markdown("### Available Equipment")

col1, col2, col3 = st.columns(3)

with col1:
    dumbbells = st.checkbox("Dumbbells")
    yoga_mat = st.checkbox("Yoga mat")
    inclined_bench = st.checkbox("Inclined bench")
    cycle = st.checkbox("Cycle")
    hand_gripper = st.checkbox("Hand gripper")

with col2:
    bands = st.checkbox("Resistance Band")
    no_equipment = st.checkbox("No Equipment")
    treadmill = st.checkbox("Tread mill")
    skipping_rope = st.checkbox("Skipping rope")
    pullups_bar = st.checkbox("Pullups bar")

with col3:
    weight_plates = st.checkbox("Weight plates")
    hula_hoop = st.checkbox("Hula hoop ring")
    bosu_ball = st.checkbox("Bosu ball")

st.markdown("### Fitness Level")

fitness_level = st.radio(
    "",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

generate = st.button("🚀 Generate Personalised Plan")

if generate:

    equipment_selected = any([
        dumbbells, yoga_mat, inclined_bench, cycle, hand_gripper,
        bands, no_equipment, treadmill, skipping_rope, pullups_bar,
        weight_plates, hula_hoop, bosu_ball
    ])

    if not name.strip():
        st.error("Name is required.")
    elif height_cm <= 0:
        st.error("Height must be greater than 0.")
    elif weight_kg <= 0:
        st.error("Weight must be greater than 0.")
    elif not equipment_selected:
        st.error("Please select at least one equipment option.")
    elif not goal:
        st.error("Please select a fitness goal.")
    elif not fitness_level:
        st.error("Please select your fitness level.")
    else:
        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        st.success("Fitness profile submitted successfully!")

        st.markdown(f"""
        <div style="
            margin-top:20px;
            padding:20px;
            border-radius:15px;
            background-color:#f4f9ff;
            font-family: 'Segoe UI', sans-serif;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.05);
        ">
            <h3 style="color:#007bff; margin-bottom:15px;">
                📋 Your Fitness Summary
            </h3>
            <p style="font-size:18px; font-weight:500;">
                <strong>Name:</strong> {name}
            </p>
            <p style="font-size:18px; font-weight:500;">
                <strong>BMI:</strong> {bmi}
            </p>
            <p style="font-size:18px; font-weight:500;">
                <strong>Category:</strong> {category}
            </p>
            <p style="font-size:18px; font-weight:500;">
                <strong>Goal:</strong> {goal}
            </p>
            <p style="font-size:18px; font-weight:500;">
                <strong>Fitness Level:</strong> {fitness_level}
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
