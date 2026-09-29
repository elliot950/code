


# datorn ska fråga oss hur högt vi släpper bollen ifrån

höjd=float(input('hur högt släptes bollen ifrån i metrar:'))

studsar=0

while höjd >= 0.01:
    höjd = höjd*0.7
    studsar+=1
print (studsar)