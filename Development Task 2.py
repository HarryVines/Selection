#Harry Vines
#selection development excercise 2
#29-09-14

temperature = float(input("Please enter the temperature of the water in centigrades: "))
if temperature >= 100:
    print("The water is boiling")
elif temperature <= 0:
    print("The water is frozen")
else:
    print("The water is unchanged")
