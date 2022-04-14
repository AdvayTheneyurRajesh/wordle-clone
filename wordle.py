seimport random

words = ['MAJOR','REBUT','REPAY','EXIST','WORDS','BLUSH','FOCAL','RIGHT','WRONG',
         'LUCKY','HEATH','DWARF','MODEL','CLEAN','STINK','GRADE','QUIET','BENCH',
         'CHEFS','FEIGN','CIGAR','DEATH','FRESH','CRUST','CHAIN','PHONE','REACT']

print("""Instructions:
1. X means the letter doesn't exist in the word,
   _ means the letter exists but it is not in the right position and 
   O means that you have guessed the position and the letter correct
2. You have 6 lives. Good luck!\n""")

answer=words[random.randint(0, len(words)-1)] 
i,lives=0,5
correctltr,wrongltr=[],[]
clue=['-','-','-','-','-'] 
for i in range(lives,-1,-1):    #range(0,5) gives output as 0 1 2 3 4
                                #range(5,0,-1) gives output as 5 4 3 2 1
                                #range(5,-1,-1) gives output 5 4 3 2 1 0
    inputword=input("Enter your 5 letter word guess: \n").upper()
    for index in range(len(inputword)):
        
        if inputword[index]==answer[index]:
            clue[index]='O'
            correctltr.append(inputword[index])
        elif inputword[index] in answer:
            clue[index]='_'
            correctltr.append(inputword[index])
        else:
            clue[index]='X'
            wrongltr.append(inputword[index])

    correctltr.sort()
    wrongltr.sort()
    print(''.join(clue),'\t\tLetters in the word: ',''.join(set(correctltr)),
          '\t\tLetters not in the word: ',''.join(set(wrongltr)),
          '\t\tLives remaining: ',i)
    print()
    if ''.join(clue) == 'OOOOO':
        break

print("Your score: ",i*100+100)

    
    



