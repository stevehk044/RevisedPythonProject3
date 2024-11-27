def calculate_bmi(weight, height):
   bmi = weight / (height ** 2)
   return bmi


def bmi_category(bmi):
   if bmi < 18.5:
      return "Underweight"
   elif 18.5 <= bmi < 24.9:
      return "Normal weight"
   elif 25 <= bmi < 29.9:
      return "Overweight"
   else:
      return "Obese"


def main():
   try:
      weight = float(input("Enter your weight in kilograms: "))
      height = float(input("Enter your height in meters: "))

      bmi = calculate_bmi(weight, height)
      category = bmi_category(bmi)

      print(f"Your BMI is {bmi:.2f}")
      print(f"Category: {category}")

      if category == "Underweight":
         print("Consider a balanced diet to reach a healthier weight.")
      elif category == "Normal weight":
         print("Great job! Keep maintaining your healthy lifestyle.")
      elif category == "Overweight":
         print("Consider a balanced diet and regular exercise to reach a healthier weight.")
      else:
         print("Consult with a healthcare provider for guidance on achieving a healthier weight.")

   except ValueError:
      print("Invalid input. Please enter numerical values for weight and height.")


if __name__ == "__main__":
   main()

