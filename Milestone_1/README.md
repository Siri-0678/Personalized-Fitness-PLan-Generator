# FitPlan AI – Personalized Fitness Plan Generator  
## Milestone 1 Submission

---

## Objective of the Milestone

The objective of this milestone is to develop a Streamlit-based web application that calculates the Body Mass Index (BMI) of a user based on given inputs and displays the health classification result.

The application ensures proper input validation and is successfully deployed on Hugging Face Spaces.

---

## BMI Formula Explanation

Body Mass Index (BMI) is calculated using the formula:

BMI = Weight (kg) / (Height (m))²

Since the user provides height in centimeters, it is first converted to meters:

Height (m) = Height (cm) / 100

Then the BMI value is calculated using the standard formula.

---

## Steps Performed

1. Designed a user input form using Streamlit.
2. Collected the following inputs:
   - Name
   - Age
   - Gender
   - Height (in cm)
   - Weight (in kg)
3. Implemented proper input validation:
   - No empty required fields.
   - No zero or negative values.
4. Converted height from centimeters to meters.
5. Calculated BMI using the standard formula.
6. Classified BMI into categories:
   - Underweight
   - Normal weight
   - Overweight
   - Obese
7. Displayed the BMI result clearly with proper formatting.
8. Successfully deployed the application on Hugging Face Spaces.

---

## Technologies Used

- Python
- Streamlit
- Hugging Face Spaces
- GitHub

---

## Hugging Face Deployment Link

Add your Hugging Face Space link here:

https://huggingface.co/spaces/SiriGayathri06/AI_Fitness_Planner

---

## Screenshots of the Running Application

### Input Form
![Input Screenshot](screenshots/form.png)

### Output with BMI Result
![Output Screenshot](screenshots/output.png)

---

## Milestone Status

Milestone 1 completed successfully with proper input validation, BMI calculation logic, and successful deployment.
