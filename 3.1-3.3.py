minuter = int(input("hur många minuter ringer du i månaden"))
if minuter < 33:
    print("du bör välja kontant")
elif minuter < 66:
    print("du bör välja normal")
else:
    print("du bör välja plus")
