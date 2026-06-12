import re


# 1. BMI Calculator
def calculate_bmi(question):

    numbers = re.findall(r"\d+\.?\d*", question)

    if len(numbers) >= 2:
        weight = float(numbers[0])
        height = float(numbers[1])

        bmi = weight / (height ** 2)

        return f"BMI = {bmi:.2f}"

    return None


# 2. Blood Pressure Classifier
def classify_bp(question):

    numbers = re.findall(r"\d+", question)

    if len(numbers) >= 2:

        systolic = int(numbers[0])
        diastolic = int(numbers[1])

        if systolic < 120 and diastolic < 80:
            return "Blood Pressure: Normal"

        elif systolic < 130:
            return "Blood Pressure: Elevated"

        elif systolic < 140:
            return "Blood Pressure: Hypertension Stage 1"

        else:
            return "Blood Pressure: Hypertension Stage 2"

    return None


# 3. Diabetes Risk Tool
def diabetes_risk(question):

    if "diabetes risk" in question.lower():

        return """
Risk Factors:
• Obesity
• Family history
• Lack of exercise
• High blood pressure
"""

    return None


# 4. Symptom Checker
def symptom_checker(question):

    q = question.lower()

    if "fever" in q and "cough" in q:

        return """
Possible Conditions:
• Common Cold
• Flu
• COVID-19
"""

    return None


# 5. Drug Information
def drug_info(question):

    q = question.lower()

    medicines = {

        "paracetamol":
        "Paracetamol helps reduce fever and pain.",

        "ibuprofen":
        "Ibuprofen is used for inflammation and pain.",

        "metformin":
        "Metformin is used for Type-2 Diabetes."
    }

    for drug, info in medicines.items():

        if drug in q:
            return info

    return None


# 6. Heart Rate Tool
def heart_rate(question):

    numbers = re.findall(r"\d+", question)

    if "heart rate" in question.lower() and numbers:

        hr = int(numbers[0])

        if 60 <= hr <= 100:
            return "Heart Rate: Normal"

        elif hr < 60:
            return "Heart Rate: Low"

        else:
            return "Heart Rate: High"

    return None


# 7. Daily Water Intake
def water_intake(question):

    if "water intake" in question.lower():

        return """
Recommended Daily Water Intake:
• Women: 2.7 liters/day
• Men: 3.7 liters/day
"""

    return None


# 8. Calorie Calculator
def calorie_info(question):

    if "calories" in question.lower():

        return """
Average Daily Calories:
• Women: 1800-2200 kcal
• Men: 2200-2800 kcal
"""

    return None


# 9. Pregnancy BMI Advice
def pregnancy_bmi(question):

    if "pregnancy bmi" in question.lower():

        return """
Pregnant women should consult their doctor
for personalized BMI recommendations.
"""

    return None


# 10. Body Temperature Checker
def temperature_checker(question):

    numbers = re.findall(r"\d+\.?\d*", question)

    if "temperature" in question.lower() and numbers:

        temp = float(numbers[0])

        if temp < 37.5:
            return "Body Temperature: Normal"

        else:
            return "Body Temperature: Fever Detected"

    return None


# Master Router
def check_medical_tools(question):

    tools = [

        calculate_bmi,
        classify_bp,
        diabetes_risk,
        symptom_checker,
        drug_info,
        heart_rate,
        water_intake,
        calorie_info,
        pregnancy_bmi,
        temperature_checker

    ]

    for tool in tools:

        result = tool(question)

        if result:
            return result

    return None