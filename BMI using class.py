class bmi1:
    def __init__(self, bmi):
        self.bmi = int(bmi)


weight = input("Please enter your weight:")
wt1 = int(weight)
height = input("Please enter your height:")
ht1 = float(height)
bmi = wt1 / (ht1 * ht1)
bmi1 = int(bmi)
print(f"Yor BMI calculation is: {bmi1}")


