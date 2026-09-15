ålder = int(input("hur gammal är du"))

if ålder == 17:
    print("du är lika gammal som de flästa i ee25")

if ålder != 43:
    print("du är inte lika gammal som per")
else:
    print("du är lika gammal som per")

if ålder <= 13:
    print("du är väldigt ung")
elif ålder < 18:
    print("du får inte ta körkort")
elif ålder < 20:
    print("du får ta körkort")
else:
    print("du får handla på systembolaget")

namn = input("vad är det namn")

if namn == "per":
    print("kung")
elif namn == "per":
    print("så stavar man inte")
else:
    print("varför heter du inte per")
    
if ålder == 43 and namn == "per":
    print("du måste vara per hagfors")