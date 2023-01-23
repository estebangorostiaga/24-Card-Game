import numpy as np

def sumFunc(combinations):
    sum_list = []
    for i in combinations:
        if(sum(i) == 24):
            sum_list.append(i)
    return sum_list

def subtFunc():
    
    return

def multFunc(combinations):
    mult_list = []
    for i in combinations:
        if(np.prod(i) == 24):
            mult_list.append(i)
    return mult_list

def divFunc():
    
    return

def combListFunc(cardList):
    
    handNum = 4 # Number of cards in each hand
    currentHand = [1] * handNum  # Combination of cards we have in our current hand
    combinations = list() #currentHand
    possibleCombs = pow(len(cardList), handNum) # possibleCombs is a variable for all possible ways to combine the 4 numbers for each hand
    count = 0
    index = 0 # index of cards in hand 0-3 (4 cards)
    count2 = 0

    while True:
        # Changes the number for each card is it parses through the 4 cards    from [13,1,1,1] to [1,2,1,1] and then [2,2,1,1]. index 3 will be the last one to change
        indx2 = index

        if(currentHand[index] < len(cardList)):
            count2 += 1
            count += 1
            currentHand[index] = count
            if(currentHand not in combinations):   # Adds or ignores the current hand's combination to Combination List         
                combinations.append(currentHand[:])
        else:
            currentHand[indx2] = 1

            while True:
                indx2 += 1
                if(indx2 > 3):
                    break
                if(currentHand[indx2] < len(cardList)):
                    currentHand[indx2] += 1
                    break
                else:
                    currentHand[indx2] = 1
            
            if(currentHand[index]):    
                count = 0
        if(indx2 > 3):
            break

    return combinations

def main():
    cardList = list(range(1,14)) # Number of cards in each suit
    combinationList = combListFunc(cardList)  # combListFunc will return all possile combinations for the entire Card List e.g (1,5,8, 13) and (13,1,8,5)
    combTot = len(combinationList)
    
    sumList = sumFunc(combinationList)  # All possible combinations of 24 by just sum
    combinationList = [x for x in combinationList if x not in sumList]

    multList = multFunc(combinationList)  # All possible combinations of 24 by just sum
    combinationList = [x for x in combinationList if x not in multList]

if __name__ == "__main__":
    main()