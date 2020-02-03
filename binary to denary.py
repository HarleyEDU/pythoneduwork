word = int(input("Input number 'ting: "))
 
YouAreABin = []
 
while word != 0:
    if word % 2 == 0:
        word = word / 2
        YouAreABin.insert(0,0)
    else:
        word = (word - 1) / 2
        YouAreABin.insert(0,1)
 
print(YouAreABin)
