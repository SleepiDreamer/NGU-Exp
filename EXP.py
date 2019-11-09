import math


power = float(input("power? "))
cap = float(input("cap? (don't write the last 3 zeros) "))
bars = float(input("bars? "))
defratio = input("do you want to use the 1/37.5/1 ratio? (yes/no) ")

if defratio == "yes":
    ratiopow = 1
    ratiocap = 37.5
    ratiobars = 1
else:
    ratiopow = float(input("what power to cap ratio? "))
    ratiocap = float(input("what cap ratio? "))
    ratiobars = float(input("what bars to cap ratio? "))

recpow = (cap // ratiocap * ratiopow)
recbars = (cap // ratiocap * ratiobars)
powerExp = round(recpow - power, 1)
barsExp = round(recbars - bars, 1)


if powerExp != 0 and barsExp != 0:
    if powerExp < 0 or barsExp < 0:

        if powerExp < barsExp:
            morecap = abs(powerExp * ratiocap)
        else:
            morecap = abs(barsExp * ratiocap)

        print()
        if powerExp > 0:
            print(f"You should have {abs(powerExp)} more power and {abs(barsExp)} less bars which means you need to buy power first and then {morecap}k more cap")
        elif barsExp > 0:
            print(f"You should have {abs(powerExp)} less power and {abs(barsExp)} more bars which means you need to buy bars first and then {morecap}k more cap")
        else:
            print(f"You should have {abs(powerExp)} less power and {abs(barsExp)} less bars which means you need {morecap}k more cap")
    else:
        print()
        print(f"You need to have {powerExp} more power and {barsExp} more bars")
        print()
        print("EXP needed for full efficiency:")
        print(f"\tpower: {math.ceil(powerExp * 150)} EXP")
        print(f"\tbars: {math.ceil(barsExp * 80)} EXP")
        print(f"\ttotal: {math.ceil((powerExp * 150) + (barsExp * 80))} EXP")

else:
    print(f"Go ahead and buy {ratiocap} more Energy Cap!")

input()
