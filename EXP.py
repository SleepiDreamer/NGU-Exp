import math

power = float(input("power? "))
cap = float(input("cap? "))
bars = float(input("bars? "))

rec = math.floor(cap // 37.5)
powerExp = rec - power
barsExp = rec - bars

if rec > 0:
    print()
    print("You need to have " + str(powerExp) + " more speed, and " + str(barsExp) + " more bars")
    print()
    print("EXP needed for full efficiency:")
    print("power: " + str(powerExp * 150) + " EXP")
    print("bars: " + str(barsExp * 80) + " EXP")
    print("total: " + str(powerExp * 150 + barsExp * 80) + " EXP")
else:
    print("You are fully efficient!")