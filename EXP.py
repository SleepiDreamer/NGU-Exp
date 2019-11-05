import math


power = float(input("power? "))
cap = float(input("cap? (don't write the last 3 zeros) "))
bars = float(input("bars? "))
ratiopow = float(input("what power to cap ratio? (e.g. -->1<--/37.5/1) "))
ratiocap = float(input("what cap ratio? (e.g. 1/-->37.5<--/1) "))
ratiobars = float(input("what bars to cap ratio? (e.g. 1/37.5/-->1<--) "))

recpow = math.floor(cap // ratiocap * ratiopow)
recbars = math.floor(cap // ratiocap * ratiobars)
powerExp = recpow - power
barsExp = recbars - bars

print(recpow)
print(recbars)
print(power)

if recpow != 0 and recbars != 0:
    print()
    print("You need to have " + str(powerExp) + " more speed, and " + str(barsExp) + " more bars")
    print()
    print("EXP needed for full efficiency:")
    print("power: " + str(math.ceil(powerExp * 150)) + " EXP")
    print("bars: " + str(math.ceil(barsExp * 80)) + " EXP")
    print("total: " + str(math.ceil(powerExp * 150 + barsExp * 80)) + " EXP")
else:
    print("You are fully efficient!")

while True:
    pass