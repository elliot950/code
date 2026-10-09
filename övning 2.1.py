mätarställning=int(input("mätarställning idag?"))
mätarställning_årsen=int(input("mätarställning för ett år sedan?"))

körda_mil = mätarställning - mätarställning_årsen
print ("antal körda mil: ",  körda_mil)

Liter_bensin=int(input("Antal liter bensin?"))
förbrukning_per_mil = Liter_bensin / körda_mil
print("förbrukning per mil är ", förbrukning_per_mil)