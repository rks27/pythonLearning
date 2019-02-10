pl1_score = []
pl2_score = []
for i in range (5):
    win = int(input("1 win 2 lose for pl1:"))
    if win == 1:
        if i == 1:
            pl1_score.append(15)
        if i == 2:
            pl1_score[0] == (30)
        if i == 2:
            pl1_score[0] == (40)
        if i == 3:
            pl1_score[0] == ("Win")
        if i == 4:
            pl1_score[0] == ("Already won")
    if win == 2:
        if i == 1:
            pl2_score.append(15)
        if i == 2:
            pl2_score[0] == (30)
        if i == 2:
            pl2_score[0] == (40)
        if i == 3:
            pl2_score[0] == ("Win")
        if i == 4:
            pl2_score[0] == ("Already won")
    else:
        print("Error")
    print(pl1_score)
    print(pl2_score)
    if pl1_score == "Win" or pl1_score == "Already won":
        print("1 win")
    if pl2_score == "Win" or pl2_score == "Already won":
        print("2 win")

        
        
