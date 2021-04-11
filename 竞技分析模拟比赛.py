import random
def printinfo():
    print("This project simulates the competition between Candidator A and Candidator B in certain sport")
    print("you need to input the competence of A and B(as the decimal between 0 and 1)")

def getInput():
    a = eval(input("Please input the competence of A（0-1）:"))
    b = eval(input("Please input the competence of B（0-1）:"))
    n = eval(input("Please input the number of simulating competition:"))
    return a, b, n

def printSummary(winsA,winsB):
    n = winsA +winsB
    print("Simulating competition is beginning, it has been simulated {} competition".format(n))
    print("Candidator A has won {} competition, which is {:0.1%}".format(winsA,winsA/n))
    print("Candidator A has won {} competition, which is {:0.1%}".format(winsB,winsB/n))

def simNGames(n,probA,probB):
    winsA,winsB = 0 , 0
    for i in range (n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB +=1
    return winsA,winsB

def simOneGame(probA,probB):
    scoreA,scoreB =0,0
    serving = "A"
    while not GameOver(scoreA, scoreB):
        if serving == "A":
            if random.random()<probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random.random()<probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def GameOver(scoreA,scoreB):
    return scoreA == 15 or scoreB ==15
                
def main():
    printinfo()
    probA, probB, n =getInput()
    winsA , winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

main()