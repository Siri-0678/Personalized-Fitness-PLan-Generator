

# FitPlan AI

## Objective of the Milestone

The objective of this milestone is to design and deploy an AI-powered fitness planning application that generates a fully personalized 5-day workout program based on user-specific inputs.

The application collects user details such as name, age, gender, height, weight, fitness goal, fitness level, and available equipment. Using this information, it calculates BMI and generates a structured, professional workout plan through a large language model.

The goal is to demonstrate:

* Effective prompt engineering
* Integration of a Large Language Model (LLM) using Hugging Face Inference API
* Streamlit-based user interface development
* Real-time AI inference
* Deployment using Hugging Face Spaces

---

## Model Name Used

**Model:** mistralai/Mistral-7B-Instruct-v0.2
**Provider:** Hugging Face
**Access Method:** Hugging Face InferenceClient (API-based inference)

This instruction-tuned model is optimized for structured conversational responses, making it suitable for generating detailed, formatted fitness programs.

---

## Prompt Design Explanation

The prompt is carefully structured to avoid generic outputs and ensure professional-quality results.

### Key Prompt Design Elements:

1. Role Definition
   The model is instructed to act as:

   > "A certified professional fitness trainer"
   > and
   > "An experienced strength & conditioning coach"

2. User-Specific Context
   The prompt includes:

   * Name
   * Age
   * Gender
   * BMI and BMI status
   * Fitness goal
   * Fitness level
   * Equipment availability

3. Structured Output Requirements
   The model is explicitly instructed to generate:

   For each of the 5 days:

   * Training Focus
   * Warm-up
   * Main Workout (Sets × Reps)
   * Rest Period
   * Cool Down

   After Day 5:

   * Weekly Coaching Tips
   * Nutrition Guidance
   * Recovery Strategy
   * Safety Notes

4. Anti-Generic Constraint
   The prompt includes:

   > "Do NOT create a generic template. Make it professional and realistic."

This ensures the model produces customized and high-quality output rather than a standard template.

---

## Steps Performed

### 1. Model Loading

* Hugging Face API token is retrieved from environment variable `HF_SECRET`.
* The `InferenceClient` is initialized with:

  * Model: mistralai/Mistral-7B-Instruct-v0.2
  * Token authentication
* Chat completion API is used for inference.

### 2. Prompt Creation

* User inputs are collected via Streamlit form.
* BMI is calculated inside `prompt_builder.py`.
* A structured prompt is dynamically generated using:

  * User data
  * BMI and BMI status
  * Coaching instructions
  * 5-day training structure requirements

### 3. Inference Testing

* The prompt is passed to the model using:

  * `chat_completion()`
  * Controlled temperature (0.7)
  * Max token limit
* The generated output is:

  * Displayed in a styled result container
  * Available for download as a text file

### 4. Frontend Implementation

* Developed using Streamlit
* Session state handling for navigation
* Custom CSS styling
* Structured input validation
* Download functionality for generated plan

### 5. Deployment

* Application deployed using Hugging Face Spaces
* Environment variables securely configured
* Fully functional web-based AI fitness planner

---

## Sample Generated Output (Example)

Below is a shortened example of a generated workout plan:

### Day 1 – Upper Body Strength

Training Focus: Chest and Triceps
Warm-up: 5 minutes light cardio + dynamic shoulder mobility
Main Workout:

* Dumbbell Bench Press – 4 × 8
* Incline Dumbbell Press – 3 × 10
* Tricep Dips – 3 × 12
  Rest Period: 60–90 seconds
  Cool Down: Static chest and triceps stretching

### Day 2 – Lower Body Strength

Training Focus: Quadriceps and Glutes
Warm-up: Bodyweight squats and lunges
Main Workout:

* Goblet Squats – 4 × 10
* Romanian Deadlifts – 3 × 8
* Walking Lunges – 3 × 12
  Rest Period: 60–90 seconds
  Cool Down: Hamstring and hip flexor stretches

(Continues for Day 3, Day 4, Day 5)

After Day 5:

* Weekly Coaching Tips
* Nutrition Guidance
* Recovery Strategy
* Safety Notes

---

## Hugging Face Space Deployment Link

Add your deployed Hugging Face Space link below:

https://huggingface.co/spaces/SiriGayathri06/FitPlan_AI


---

## Conclusion

FitPlan AI demonstrates the integration of modern LLM capabilities with prompt engineering and frontend deployment to create a practical, AI-powered fitness planning system.

This milestone validates the ability to:

* Design structured AI prompts
* Generate personalized outputs
* Integrate APIs securely
* Deploy production-ready AI applications

---
