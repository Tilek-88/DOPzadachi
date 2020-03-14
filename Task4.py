
chet1 = 0
chet2 = 0
while (chet1 != 3 and chet2 < 3) or (chet2 != 3 and chet1 < 3):
    igrok1 = input("igrok noj kamen bumaga: ").strip()
    igrok2 = input("igrok noj kamen bumaga: ").strip()
    if igrok1 == "noj" and igrok2 == "bumaga":
        chet1 += 1
    elif igrok1 == "bumaga" and igrok2 == "kamen":
        chet1 += 1
    elif igrok1 == "kamen" and igrok2 == "noj":
        chet1 += 1
    elif igrok2 == "noj" and igrok1 == "bumaga":
        chet2 += 1
    elif igrok2 == "bumaga" and igrok1 == "kamen":
        chet2 += 1
    elif igrok2 == "kamen" and igrok1 == "noj":
        chet2 += 1
    elif igrok1 == igrok2:
        continue        

print(chet1, chet2)      


