class agecal:

    def __init__(self, age):
        self.age = int(age)
        self.age_left = 90 - self.age
        print(f"You have {self.age_left} years more left to live.")

        Days = self.age_left * 365
        Weeks = self.age_left * 52
        Months = self.age_left * 12
        print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")


your_age = input("Please enter your Age (** Average life-expectancy is 90 years**):: ")
life_exptncy = agecal(your_age)



