class insured:
    def __init__(self, mar_stats):
        self.mar_stats = mar_stats
        if ((self.mar_stats == "True")):
            print(f"You are insured")
        elif ((self.mar_stats == "False") and (sex == "Male") and (age >= 30)):
            print(f"You are insured")
        elif ((self.mar_stats == "False") and (sex == "Female") and (age >= 25)):
            print(f"You are insured")
        else:
            print(f"You are NOT insured")

mar_stats = input("Please enter your marital status as True or False: ")
sex = input("Please enter your sex as Male or Female: ")
age = int(input("Please enter your age: "))
insur = insured(mar_stats)