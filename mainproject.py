#krish gurung
#samuri game
#april 8 2024
#importing all the modules
import random
import time
import re
import os
import pyinputplus as pyip
import openpyxl
#some instructions about the game
def instructions():
    print("Parrying means deflecting an attack. The boss you'll deal with will be attacking you with various attacks, and if you match the type of attack he's planning, you'll be able to retain your health.")
#function for first boss
def fightBoss1(bossHp,playerHp):
    print('Start attacking!')
    print('Boss HP:', bossHp)
    print('1 for quick attack')
    print('2 for heavy attack')
    print("\n\n")
    attackCount = 0
    #while not loop to keep running till boss is dead or hp=0
    while not bossHp <= 0:
        #restricting attacking after a while
        while not attackCount >= 3:
            #light attack
            print('Keep attacking! Quick attack or heavy attack?')
            attack = int(input())
            if attack == 1:
                bossHp -= 10
                print('Boss HP:', bossHp)
                attackCount += 1
                if bossHp <= 0:
                    print('Lesssgooooo! You defeated the boss')
                    return
            elif attack == 2:#heavy attack
                bossHp -= 30
                attackCount += 1
                if bossHp <= 0:
                    print('Lesssgooooo! You defeated the boss')
                    return
        # Only printing boss HP if it's greater than zero to avoid negative value
                elif bossHp > 0:  
                    print('Boss HP:', bossHp)
                    attackCount += 2
            else:
                print('Invalid attack')
                break
        print("\n\n")
        if bossHp > 0:
           #passing player hp to function
            playerHp = bossAttack(playerHp)
            attackCount = 0
#boss2  
def fightBoss2(bossHp,playerHp):
    print('Start attacking!')
    print('Player HP:', playerHp)
    print('Boss HP:', bossHp)
    print('1 for quick attack')
    print('2 for heavy attack')
    print("\n\n")
    #while not loop to keep running till boss is dead or hp=0
    while not bossHp <= 0:
        attackCount = 0
         # Restricting attack
        while not attackCount >= 3:
            print('Keep attacking! Quick attack or heavy attack?')
            attack = int(input())
            if attack == 1:
                #using random to genrate attacks
                bossDeflection = random.randint(1, 3)
                #non-deflectuion logic
                if bossDeflection != 1:
                    bossHp -= 10
                    if bossHp <= 0:
                        print('Lesssgooooo! You defeated the boss')
                        break
                    else:
                        print('Boss HP:', bossHp)
                        attackCount += 2
                else:
                    #deflection logic
                    print('Your attack was deflected')
                    playerHp -= 10
                    if playerHp > 0:
                        print('Player HP:', playerHp)
                    else:
                        lost()#calling lost function if hp less than zero
                    
                    attackCount += 2
            elif attack == 2:
                bossDeflection = random.randint(1, 3)
                if bossDeflection != 2:
                    bossHp -= 30
                    #exiting after boss loses
                    if bossHp <= 0:
                        print('Lesssgooooo! You defeated the boss')
                        print("\n\n")
                        break
                    else:
                        print('Boss HP:', bossHp)
                        attackCount += 2
                else:
                    print('Your attack was deflected')
                    playerHp -= 20
                    #determining player loses or win
                    if playerHp > 0:
                        print('Player HP:', playerHp)
                    else:
                        lost()
                    attackCount += 2
            else:
                print('Invalid attack')
                break
        print("\n\n")
        if bossHp > 0:
            #passing playerHp to the loop
            playerHp = bossAttack(playerHp)
            attackCount = 0
#3rd boss fight
def fightBoss3(bossHp,playerHp):
    print("\n\n")
    print('Start attacking!')
    print('Boss HP:', bossHp)
    print('Player HP:', playerHp)
    print('1 for quick attack')
    print('2 for heavy attack')
    print("\n\n")
    #while not loop to keep running till boss is dead or hp=0
    while not bossHp <= 0:
        attackCount = 0
    # Restricting attack
        while not attackCount >= 3:
            print('Keep attacking! Quick attack or heavy attack?')
            print("\n\n")
            attack = int(input())
            if attack == 1:
                #deflection with random
                #non-deflection case
                bossDeflection = random.randint(1, 3)
                if bossDeflection != 1:
                    bossHp -= 10
                    if bossHp <= 0:
                        print('Lesssgooooo! You defeated the boss')
                        break
                    elif bossHp > 0:
                        print('Boss HP:', bossHp)
                        attackCount += 2
                else:#when attack is deflected case
                    print('Your attack was deflected')
                    playerHp -= 10
                    if playerHp > 0:
                        print('Player HP:', playerHp)
                    elif playerHp <= 0:
                        lost()
                    else:
                        break
                    attackCount += 2
            elif attack == 2:#heavy attack deflection case
                #non deflect
                bossDeflection = random.randint(1, 3)
                if bossDeflection != 2:
                    bossHp -= 30
                    if bossHp <= 0:
                        print('Lesssgooooo! You defeated the boss')
                        print("\n\n") 
                        break
                    elif bossHp > 0:
                        print('Boss HP:', bossHp)
                        attackCount += 2
                else:#deflect
                    print('Your attack was deflected')
                    playerHp -= 20
                    if playerHp > 0:
                        print('Player HP:', playerHp)
                    else:
                        lost()
                    
                    print('No damage to the boss')
                    attackCount += 2
            else:
                print('Invalid attack')
                break
        print("\n\n")
        if bossHp > 0:
               #passing the value
                playerHp = bossFinalAttack(playerHp)
        
                attackCount = 0
    
#Attacking of boss which user will need to parry
#using regex for input validation 
def bossAttack(playerHp):
    attackType = random.randint(1, 3)
    pattern = re.compile(r'^[1-3]$')
    print('Enemy has started to make his move. How would you react? 1, 2, or 3?')
    reactionUser = None
    while reactionUser not in range(1, 4):
        userInput = input()
        if pattern.match(userInput):
            reactionUser = int(userInput)
        else:
            print('Invalid input. Please enter a number between 1 and 3.')

    if reactionUser == attackType:
        print('You successfully stopped an attack!')
    else:
        if attackType == 1:
            playerHp -= 10
            print('Unsuccessful! Enemy used a light attack!')
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)

        elif attackType == 2:
            playerHp -= 20
            print('Unsuccessful! Enemy used a medium attack!')
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)
        else:
            playerHp -= 30
            print('Unsuccessful! Enemy used a heavy attack!')
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)
    return playerHp#returning the value
#final boss attacking function
def bossFinalAttack(playerHp):
    attackType = random.randint(1, 3)
    print('Enemy has started to make his move. How would you react? 1, 2, or 3?')
    reactionUser = int(input())
    if reactionUser == attackType:
        print('You successfully stopped an attack!')
    else:#damage according to the attack
        if attackType == 1:
            playerHp -= 10
            print('Unsuccessful! Enemy used a light attack!')
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)
        elif attackType == 2:
            playerHp -= 20
            print('Unsuccessful! Enemy used a medium attack!')
            
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)
        elif attackType==3:
            playerHp -= 30
            print('Unsuccessful! Enemy used a heavy attack!')
            if playerHp <= 0:
                print('Player HP: 0')
                lost()
            else:
                print('Player HP:', playerHp)
        else:#non deflectable attack
            playerHp -= 50
            print('FireBall incoming! Enemy used a special power!')
            if playerHp <= 0:
                 lost()
            else:
                print('Player HP:', playerHp)
    return playerHp
#to read Bosses list from excell
def readSpreadSheet():
    workBook = openpyxl.load_workbook("C:\\PYTHON\\vLog.xlsx")
    sheet = workBook.active
    v1Name = sheet['A2'].value
    v1Health = sheet['B2'].value
    v1Difficulty = sheet['C2'].value
    v1SpecialAbility = sheet['D2'].value

    v2Name = sheet['A3'].value
    v2Health = sheet['B3'].value
    v2Difficulty = sheet['C3'].value
    v2SpecialAbility = sheet['D3'].value

    v3Name = sheet['A4'].value
    v3Health = sheet['B4'].value
    v3Difficulty = sheet['C4'].value
    v3SpecialAbility = sheet['D4'].value

    print("Name", "Health", "Difficulty", "Special Ability")
    print(v1Name, v1Health, v1Difficulty, v1SpecialAbility)
    print(v2Name, v2Health, v2Difficulty, v2SpecialAbility)
    print(v3Name, v3Health, v3Difficulty, v3SpecialAbility)
#reading from a txt file
def gameLogo():
    try:
        with open("c:\\PYTHON\\logo.txt", encoding="utf-8") as fileOne:
            fileContent = fileOne.read()
            print(fileContent)
    except FileNotFoundError:
        print("Logo file not found.")
#declaring hero name using string slicing
def namingOfHero():
    print("Please give us the name of your hero's first name and last name")
    namePattern = re.compile(r'^[a-zA-Z\'-]+\s[a-zA-Z\'-]+$')
    heroName=input()
    firstName="p1"
    if namePattern.match(heroName):
        firstName = heroName.split()[0]
        print("Hero's name is valid")
        print('let\'s proceed')
    else:
        print('invalid input.Please give correct input.')
        heroName=input()
    return firstName
#losing screen
def lost():
    print('You lost!do you want to try again?')
    print('y for yes')
    print('n for no')
    answer=input()
    if answer=='y':
        main()
    elif answer=='n':
        print('Thanks for your time')
#Asking to play again
def playAgain():
    print('do you want to play again?')
    print('y for yes')
    print('n for no')
    answer=input()
    if answer=='y':
        main()
    else:
        return

#main program
def main():
    gameLogo()#displaying logo at the top
    #welcome messages
    print('Welcome to "The Samurai" game!')
    instructions()
    print('For parrying: press 1, 2, or 3. If you match the attack type, you won\'t deal any damage.')
    #declaring global variables
    global bossHp, playerHp
    bossHp = 100#fixing the values
    playerHp = 100#fixing the values
    villainList=['King','Devil Jin','Lee']#using list for storing villan names
    print("\n\n")#spaces
    print('Details of Bosses you have to deal with')
    readSpreadSheet()#callling excell
    print("\n\n")#sapces
    hero=namingOfHero()#assigning hero name
    #choosing a game mode
    print('Choose a game mode:')
    print('1. Classic league')
    print('2. Quick Game')
    try:
    # Input validation using pyinputplus
        gameMode = pyip.inputNum(prompt="Choose '1' or '2'", min=1, max=2, limit=1)
        print("\n\n")
    except:
        main()
    #classic mode
    if gameMode == 1:
        startTime=time.time()#starting time
        print(hero,'Are you ready?')
        print(villainList[0], ' Appeared') 
        fightBoss1(100,100)#calling function
        endTime = time.time()#ending time
        timeTaken = endTime - startTime#total time taken
        print('Time taken to fight the bosses:', timeTaken, 'seconds')
    
        print('You defeated Boss 1. Next Round!!!')
        print("\n\n")

        #   boss2 fight
        print(hero,'Are you ready?')
        print(villainList[1], ' Appeared') 
        startTime = time.time()#starting time
        fightBoss2(100,100)  # calling boss2
        endTime = time.time()#ending time
        timeTaken = endTime - startTime#total time taken
        print('Time taken to fight Boss 2:', timeTaken, 'seconds')

        #boss3 fight
        print(hero,'Are you ready?')
        print(villainList[2], ' Appeared') 
        startTime = time.time()#starting time
        fightBoss3(bossHp,100)
        endTime = time.time()#ending time
        timeTaken = endTime - startTime#total time taken
        print('Time taken to fight Boss 3:', timeTaken, 'seconds')
        print('Congratulations! You Won')
        print('Thanks for playing!')
        playAgain()#playing again fucntion

    elif gameMode == 2:
        print('Quick Game Mode')  # Implement quick game mode logic here
        print('choose the boss you wanna playwith')
#for i in loop to print out levels
        for i in range(1, 4):
            print(str(i) + ". level " + str(i) + " boss")
        print('4. Random Boss')
        #try and exceptions for decisions
        try:
            decision = int(input())
            if decision == 1:
                startTime = time.time()
                print(hero,'Are you ready?')
                print(villainList[0], ' Appeared') 
                fightBoss1(100,100)
                print('Thanks for playing quick mode')
                endTime = time.time()
                timeTaken = endTime - startTime
                print('Time taken to fight Boss 2:', timeTaken, 'seconds')
                playAgain()
            elif decision == 2:
                startTime = time.time()
                print(villainList[1], ' Appeared') 
                fightBoss2(100,100)
                print('Thanks for playing quick mode')
                endTime = time.time()
                timeTaken = endTime - startTime
                print('Time taken to fight Boss 2:', timeTaken, 'seconds')
                playAgain()
            elif decision == 3:
                startTime = time.time()
                print(villainList[2], ' Appeared') 
                fightBoss3(100,100)
                endTime = time.time()
                timeTaken = endTime - startTime
                print('Time taken to fight Boss 2:', timeTaken, 'seconds')
                print('Thanks for playing quick mode')
                playAgain()
            elif decision == 4:
                startTime = time.time()
                randomNo = random.randint(1, 3)
                if randomNo == 1:
                    print(villainList[0], ' Appeared') 
                    fightBoss1(100,100)
                    endTime = time.time()
                    timeTaken = endTime - startTime
                    print('Time taken to fight Boss 2:', timeTaken, 'seconds')
                    print('Thanks for playing quick mode')
                    playAgain()
                elif randomNo == 2:
                    print(villainList[1], ' Appeared') 
                    fightBoss2(100,100)
                    endTime = time.time()
                    timeTaken = endTime - startTime
                    print('Time taken to fight Boss 2:', timeTaken, 'seconds')
                    print('Thanks for playing quick mode')
                    playAgain()
                    
                else:
                    print(villainList[2], ' Appeared') 
                    fightBoss3(100,100)
                    endTime = time.time()
                    timeTaken = endTime - startTime
                    print('Time taken to fight Boss 3:', timeTaken, 'seconds')
                    playAgain()
                    print('Thanks for playing quick mode')
                  
        except ValueError:
            print('Invalid input')
            main()
    print('The End!')
main()
#calling main function
