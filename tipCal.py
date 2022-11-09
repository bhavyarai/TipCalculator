# Tip Calculator
# The program prints value to amount a person should pay when the bill is split.
print("Welcome to the Tip Calculator!")
total_bil = float(input("What was your total Bill? $"))
n_people = int(input("How many people to split the bill? "))
tip_perc = int(input("What percentage of tip would you like to give? 10, 12 or 15?"))

amnt = round((total_bil + total_bil * tip_perc / 100) / n_people, 2)

print(f"Each person should pay ${amnt}")
