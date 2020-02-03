import time
ducks=10
while ducks >1:
    song=("little ducks went swimming one day, over the hills and far away, one stupid duck fell down a bridge. YAY. It died. Now there are less....")
    endsong=("NOW ONLY 1 DUCK REMAINS, KILLED HIMSELF FROM ALL THE PAIN. REST IN PIECE DUCKS. REST IN PIECE. LAY IN THE WATER DEAD.")
    print(ducks, song)
    if ducks == 10:
        print("no ducks dead yet")
        ducks=ducks-1
        time.sleep(5)
    else:
        print(10-ducks, "have already died lol")
        time.sleep(6)
        ducks=ducks-1
print(endsong)


