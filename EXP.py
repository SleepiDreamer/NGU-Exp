import math

power = float(input("power? "))
cap = float(input("cap? (don't write the last 3 zeros) "))
bars = float(input("bars? "))
rat = float(input("what ratio? "))

rec = math.floor(cap // rat)
powerExp = rec - power
barsExp = rec - bars

if rec > 0:
    print()
    print("You need to have " + str(powerExp) + " more speed, and " + str(barsExp) + " more bars")
    print()
    print("EXP needed for full efficiency:")
    print("power: " + str(math.ceil(powerExp * 150)) + " EXP")
    print("bars: " + str(math.ceil(barsExp * 80)) + " EXP")
    print("total: " + str(math.ceil(powerExp * 150 + barsExp * 80)) + " EXP")
else:
    print("You are fully efficient!")