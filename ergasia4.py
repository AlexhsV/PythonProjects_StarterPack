import random

print("Fair game stats:")
p1_wins = 0
p2_wins = 0
draws = 0
for i in range(100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        #print("P2 wins!")
        p2_wins+=1
    else:

        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            p1_wins+=1
        elif sum2>sum1:
            #print("P2 wins!")
            p2_wins+=1
        else:
            #print("draw!")
            draws+=1

print("P1 wins out of 100 fair games: " + str(p1_wins))
print("P2 wins out of 100 fair games: " + str(p2_wins))
print("Draws out of 100 fair games: " + str(draws))


print("---------------------------------------------------------")
print("Unfair game stats:")

p1_wins = 0
p2_wins = 0
draws = 0
for i in range(100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    start = 1
    while sum1<16:
        sum1=0
        if start == 1:  #if its the first card ,search in the list xartia backwards until you find 10 or J or Q or K ,so that is the starting card
            plith = len(xartia)
            for cards in reversed(xartia):
                plith = plith -1
                if cards[0] == 10 or cards[0] == "J" or cards[0] == "Q" or cards[0] == "K":
                    player1.append(xartia.pop(plith))
                    start-=1
                    break
        else:
            player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        #print("P2 wins!")
        p2_wins+=1
    else:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        start = 1
        while sum2<16:
            sum2=0
            if start == 1: #if its the first card ,search in the list xartia backwards until you find not10 or notJ or notQ or notK ,so that is the starting card
                plith = len(xartia)
                for cards in reversed(xartia):
                    plith = plith -1
                    if cards[0] == 1 or cards[0] == 2 or cards[0] == 3 or cards[0] == 4 or cards[0] == 5 or cards[0] == 6 or cards[0] == 7 or cards[0] == 8 or cards[0] == 9:
                        player2.append(xartia.pop(plith))
                        start-=1
                        break
            else:
                player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
            #print("P1 wins!")
            p1_wins+=1
        elif sum2>sum1:
            #print("P2 wins!")
            p2_wins+=1
        else:
            #print("draw!")
            draws+=1

print("P1 wins out of 100 games: " + str(p1_wins))
print("P2 wins out of 100 games: " + str(p2_wins))
print("Draws out of 100 games: " + str(draws))
