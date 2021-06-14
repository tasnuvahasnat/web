import random
import matplotlib.pyplot as graph
import turtle
################################## remember to add writing on the map displaying how many free troops there are + troops per province

troopsInProvince ={}
troopsInProvince[5] = 2
provincesClaimed ={}
provincesClaimed['playername'] = [5]
provincesClaimed['enemy1'] = [4]
provincesClaimed['enemy2'] = [15]

endGame = False
startGame= True
events = False

neighbors = []

turnCounter = 0 #what turn is it

########### variables for player #############

age = 18
freeTroops = 2
morale = 70
wealth = 11
age = 18
numTroops = 3
size = 4
personalHappiness = 50
wealth_list = []
turn_list =[]
morale_list =[]
troops_list =[]
dead = False
name = 0
empire = 0

########### variables for computer #############

morale1 = 70
morale2 = 70
wealth1 = 10
wealth2 = 10
numTroops1 = 3
numTroops2 = 3
troopsInProvince1 = {}
troopsInProvince1[4] =2

troopsInProvince2 = {}
troopsInProvince2[15] =2
freeTroops1 = 2
freeTroops2 = 2
war1 = False
war2 = False
trade1 = False
trade2 = False
contact1 = False
contact2 = False

##################################################################
##################################################################
######################COMPUTER SHENANIGANS########################
##################################################################
##################################################################

def computerClaim():
    global neighbors
    global provincesClaimed
    global troopsInProvince1
    global troopsInProvince2
    global freeTroops1
    global freeTroops2
    global morale1
    global morale2
    if freeTroops1 >1:
        enemy1values = provincesClaimed['enemy1']
        print(enemy1values)
        prov_1 = random.choice(enemy1values)
        print(prov_1)
        enemy1neighbors = province_neighbors(prov_1, enemy1values, 'enemy1')
        print('neighbors' ,enemy1neighbors)
        newClaim_1 = random.choice(enemy1neighbors)
        provincesClaimed['enemy1'].append(newClaim_1)
        move1 = random.randint(2,freeTroops1)
        freeTroops1 = freeTroops1 - move1
        troopsInProvince1[newClaim_1] = move1
    else:
        computerMilitary()
    if freeTroops2 > 1:
        enemy2values = provincesClaimed['enemy2']
        prov_2 = random.choice(enemy2values)
        enemy2neighbors = province_neighbors(prov_2, enemy2values, 'enemy2')
        newClaim_2 = random.choice(enemy2neighbors)
        provincesClaimed['enemy2'].append(newClaim_2)
        move2 = random.randint(2,freeTroops2)
        freeTroops2 = freeTroops2 - move2
        troopsInProvince2[newClaim_2] = move2
    else:
        computerMilitary()
    
def computer_filtered_military(s):
    global provincesClaimed
    global troopsInProvince1
    values = provincesClaimed['enemy1']
    for item in values:
        border = province_neighbors(item, values, 'enemy1')
        if len(border) == 0:
            if troopsInProvince1[item] > 0:
                return False
            else:
                return True
        else:
            return True
        
def computer_filtered_military_2(s):
    global provincesClaimed
    global troopsInProvince1
    values = provincesClaimed['enemy2']
    for item in values:
        border = province_neighbors(item, values, 'enemy2')
        if len(border) == 0:
            if troopsInProvince1[item] > 0:
                return False
            else:
                return True
        else:
            return True
def same_lists_1 (a):
    global provincesClaimed
    player = provincesClaimed['playername']
    for item in player:
        if item == a:
            return True
    return False
        
        
    
def computerMilitary():
    global numTroops1
    global numTroops2
    global troopsInProvince1
    global troopsInProvince2
    global wealth1
    global wealth2
    global provincesClaimed
    global freeTroops1
    global freeTroops2
    
    if wealth1 > 10:
        training = random.randint(2, wealth1)
        numTroops1 +=training
        freeTroops1+= training
    if wealth2 > 10:
        training2 = random.randint(2,wealth2)
        numTroops2+=training2
        freeTroops2+=training2
    enemy1provinces = provincesClaimed['enemy1']
    counter = 0
    print('enemy provinces', enemy1provinces)
    while counter < len(enemy1provinces):
        which = enemy1provinces[counter]
        print('choice' ,which)
        border = province_neighbors(which, enemy1provinces, 'enemy1')
        if len(border) == 0 and freeTroops1 > 1:
            
            x = random.randint(0, freeTroops1)
            freeTroops1 = freeTroops1-x
            troopsInProvince1[which] = troopsInProvince1[which] + x
            counter+=1
            
        elif len(border) == 0 and freeTroops1 < 2:
            filtered = list(filter(computer_filtered_military,enemy1provinces))
            d = random.choice(filtered)
            number = random.randint(1, d)
            troopsInProvince1[counter]+=number
            troopsInProvince[d] = troopsInProvince - number
            counter+=1
        counter+=1
        
    counter = 0
    enemy2provinces = provincesClaimed['enemy2']
    
    while counter < len(enemy2provinces):
        which = enemy2provinces[counter]
        border = province_neighbors(which, enemy2provinces, 'enemy2')
        if len(border) == 0 and freeTroops2 > 1:
            
            x = random.randint(0, freeTroops2)
            freeTroops2 = freeTroops2-x
            troopsInProvince2[which]+=x
            counter+=1
            
        elif len(border) == 0 and freeTroops2 < 2:
            filtered = list(filter(computer_filtered_military_2, enemy2provinces))
            d = random.choice(filtered)
            number = random.randint(1, d)
            troopsInProvince1[counter]+=number
            troopsInProvince[d] = troopsInProvince - number
            counter+=1
        counter+=1
        

def computerDiplomacy():
    global war1
    global war2
    global trade1
    global trade2
    global morale
    global numTroops
    global contact1
    global contact2
    animosity = 0 #out of 4
    
    
    enemy1provinces = provincesClaimed['enemy1']
    counter = 0
    if contact1 == False:
        while counter < len(enemy1provinces):
            which = enemy1provinces[counter]
            border = province_neighbors(which, enemy1provinces, 'enemy1')
            if len(border) == 0:
                counter+=1
            else:
                for item in border:
                    x =same_lists_1(item)
                    if x == True:
                        contact1 == True
            counter+=1
            
    counter = 0
    enemy2provinces = provincesClaimed['enemy2']
    if contact2 == False:
        while counter < len(enemy2provinces):
            which = enemy2provinces[counter]
            border = province_neighbors(which, enemy2provinces, 'enemy2')
            if len(border) == 0:
                counter+=1
            else:
                for item in border:
                    x =same_lists_1(item)
                    if x == True:
                        contact2 == True
            counter+=1
    if contact1 == True or contact2 == True:
        if morale > 90 and numTroops < 20:
            animosity = 0
        elif morale > 90 and numTroops > 20:
            animosity = 1
        elif morale > 70 and morale < 90 and numTroops < 20:
            animosity = 2
        elif morale > 70 and morale < 90 and numTroops > 20:
            animosity = 3
        elif morale > 50 and morale < 70 and numTroops < 20:
            animosity = 4
        elif morale > 50 and morale < 70 and numTroops > 20:
            war1 = True
            war2 = True
    if contact1==True: 
        if animosity == 0:
            rand1 = random.randint(0,20)
            if rand1 == 1:
                war1 = True
                trade1 = False

            if rand1 > 10:
                trade1 = True
           
        if animosity == 1:
            rand1 = random.randint(0,18)
           
            if rand1 == 1:
                war1 = True
                trade1 = False
            
            if rand1 > 10:
                trade1 = True
            
        if animosity == 2:
            rand1 = random.randint(0,14)
           
            if rand1 == 1:
                war1 = True
                trade1 = False
            
            if rand1 > 10:
                trade1 = True
            
        if animosity == 3:
            rand1 = random.randint(0,8)
            
            if rand1 == 1:
                war1 = True
                trade1 = False
           
                trade2 = False
            if rand1 > 7:
                trade1 = True
       
        if animosity == 4:
            rand1 = random.randint(0,2)
            
            if rand1 == 1:
                war1 = True
                trade1 = False
    elif contact2 == True:
        if animosity == 0:
            rand2 = random.randint(0,20)
            if rand2 == 1:
                war2 = True
                trade2 = False
            
                trade2 = False
            if rand1 > 10:
                trade1 = True
           
        if animosity == 1:
            rand2 = random.randint(0,18)
           
            if rand2 == 1:
                war2 = True
                trade2 = False
            
            if rand2 > 10:
                trade2 = True
            
        if animosity == 2:
     
            rand2 = random.randint(0,14)
            if rand1 == 1:
                war1 = True
                trade1 = False
            
            if rand1 > 10:
                trade1 = True
            
        if animosity == 3:
            
            rand2 = random.randint(0,8)
            if rand2 == 1:
                war2 = True
                trade2 = False
           
                trade2 = False
            if rand2 > 7:
                trade2 = True
       
        if animosity == 4:
            rand2 = random.randint(0,2)
            if rand2 == 1:
                war2 = True
                trade2 = False
    
                
def border_provinces_3(s):
    global provincesClaimed
    x = provincesClaimed['playername']
    if s in x:
        return True
    else:
        return False
    
def computerWar():
    global war1
    global war2
    global numTroops1
    global numTroops1
    global numTroops
    global troopsInProvince1
    global troopsInProvince2
    global troopsInProvince
    global provincesClaimed
    
    if war1 == True:
        counter = 0
        the_list_1 = []
        p =provincesClaimed['enemy1']
        while counter < len(p):
            s = province_neighbors(p[counter], p, 'enemy1')
            border = list(filter(border_provinces_3, s))
            if len(border) > 0:
                the_list_1.append(s)
                counter+=1
            else:
                counter+=1
        counter = 0
     
        the_list_1_new = []
        a = the_list_1
        choice1 = random.choice(the_list_1)
        neighbors_list =[]
        neighbors_list = province_neighbors(choice1, a, 'enemy1')
        for item in provincesClaimed['playername']:
            counter = 0
            while counter < len(neighbors_list):
                if neighbors_list[counter] == item:
                    the_list_1_new.append(item)
                counter+=1
        choice2 = random.choice(the_list_1_new)
        troop = troopsInProvince1[choice1]
        troopDraw = random.randint(troop//2, troop)
        troopsInProvince1[choice1] = troopsInProvince1[choice1] - troopDraw
        if troopDraw > troopsInProvince[choice2]:
            provincesClaimed['enemy1'].append(choice2)
            numTroops = numTroops- troopsInProvince1[choice2]
            troopsInProvince.pop(choice2)
            keys_list = list(troopsInProvince.keys())
            provincesClaimed['playername'] = keys_list
            print('you lost province', choice2, 'to Empire 1')
        elif troopDraw == troopsInProvince[choice2]:
            troopDraw//2
            numTroops1 = numTroops1 - troopDraw
            e = troopsInProvince[choice2]
            e = e//2
            troopsInProvince[choice2] = troopsInProvince[choice2]- e
        else:
            numTroops1 = numTroops1 - troopDraw
            print('you successfully defended province', choice2, 'from Empire 1')
        
    elif war2 == True:
        counter = 0
        the_list_2 = []
        p =provincesClaimed['enemy2']
        while counter < len(p):
            s = province_neighbors(p[counter], p, 'enemy2')
            border = list(filter(border_provinces_3, s))
            if len(border) > 0:
                the_list_2.append(s)
                counter+=1
            else:
                counter+=1
        counter = 0
        counter2 = 0
        the_list_2_new = []
        a = the_list_2
        choice1 = random.choice(the_list_2)
        neighbors_list =[]
        neighbors_list = province_neighbors(choice1, a, 'enemy2')
        for item in provincesClaimed['playername']:
            counter = 0
            while counter < len(neighbors_list):
                if neighbors_list[counter] == item:
                    the_list_2_new.append(item)
                counter+=1
        choice2 = random.choice(the_list_2_new)
        troop = troopsInProvince2[choice1]
        troopDraw = random.randint(troop//2, troop)
        troopsInProvince2[choice1] = troopsInProvince2[choice1] - troopDraw
        if troopDraw > troopsInProvince[choice2]:
            provincesClaimed['enemy2'].append(choice2)
            numTroops = numTroops- troopsInProvince2[choice2]
            troopsInProvince.pop(choice2)
            keys_list = list(troopsInProvince.keys())
            provincesClaimed['playername'] = keys_list
            print('you lost province', choice2, 'to Empire 2')
        elif troopDraw == troopsInProvince[choice2]:
            troopDraw//2
            numTroops2 = numTroops2 - troopDraw
            e = troopsInProvince[choice2]
            e = e//2
            troopsInProvince[choice2] = troopsInProvince[choice2]- e
        else:
            numTroops2 = numTroops2 - troopDraw
            print('you successfully defended province', choice2, 'from Empire 2')
            
def computerMain():
    computerClaim()
    computerMilitary()
    computerWar()
    computerDiplomacy()
    
##################################################################
##################################################################
####### M E N U  I N T E R F A C E / P L A Y E R  S T U F F#######
##################################################################
##################################################################
def beginnings():
    global name
    global empire
    print('Welcome to Monarchy Madness')
    name = input('Please input your name: ')
    print('Hello', name, '!')
    empire = input('Please input the name of your empire: ')
    print('Hello', name, ', ruler of', empire)
    return name, empire
def backtoMenu( where):
    if where == 'military':
        whereTo = input('Press x to return to mainMenu, press y to return to the military menu. ')
        if whereTo == 'x':
            main(6)
        elif whereTo == 'y':
            main(1)
        else:
            print('Not a valid input. Automatically returning you to the main menu.')
            main(6)
    elif where == 'province':
        whereTo = input('Press x to return to mainMenu, press y to return to the province menu. ')
        if whereTo == 'x':
            main(6)
        elif whereTo == 'y':
            main(2)
        else:
            print('Not a valid input. Automatically returning you to the main menu.')
            main(6)
    elif where == 'warMenu':
        whereTo = input('Press x to return to mainMenu, press y to return to war menu')
        if whereTo == 'x':
            main(6)
        elif whereTo == 'y':
            main(5) #CHANGED THIS FROM MAIN(6)
        else:
            print('Not a valid input. Automatically returning you to the main menu.')
            main(6)
            
def declareWar():
    global contact1
    global contact2
    global war1
    global war2
    
    if contact1 == True and contact2 == False and war1==False:
        print('Some of your advisors are suggesting that you spread the glory of your empire to other nations. You only have contact with one nation, Empire 1. Do you follow your advisors recommendations and declare war on Empire 1? If you declare war, you will morale will go down by 20. ')
        userInput = int(input('input 1 to declar war, input 2 to stay at peace: '))
        if userInput == 1:
            war1 == True
            morale = morale - 20
        elif userInput == 2:
            print('You have kept peace. ')
            main(6)
        else:
            print('That is not a valid input. Redirecting to main menu...')
    elif contact2 == True and contact1 ==False and war2==False:
        print('Some of your advisors are suggesting that you spread the glory of your empire to other nations. You only have contact with one nation, Empire 2. Do you follow your advisors recommendations and declare war on Empire 2? If you declare war, you will morale will go down by 20 ')
        userInput = input('input 1 to declar war, input 2 to stay at peace: ')
        if userInput == 1:
            war2 == True
            morale = morale - 20
        elif userInput == 2:
            print('You have kept peace. ')
            main(6)
        else:
            print('That is not a valid input. Redirecting to main menu...')
    elif contact2 == True and contact1 == True and war1==False and war2==False:
        print('You only have contact with two nations, Empire 1 and Empire 2. If you declare war, you will morale will go down by 20 ')
        userInput = input('If you want to declare war on empire 1, INPUT 1. If you want to declare war on empire 2, INPUT 2. If you want to keep the peace, INPUT 3')
        if userInput == 1:
            war1 == True
            morale = morale - 20
        elif userInput == 2:
            war2 == True
            morale = morale-20
        elif userInput == 3:
            print('You have kept peace. ')
            main(6)
        else:
            print('That is not a valid input. Jumping to main menu...')
            main(6)
    else:
        if war1 == True and war2 == True:
            print('You are already at war with everyone.')
            main(6)
        else:
            print('You cannot declare war until you have established contact with the said nation. To do that, expand your empire until you share a border with them.')
            main(6)
            
def border_provinces_1(s):
    global provincesClaimed
    print(s)
    x = provincesClaimed['enemy1']
    if s in x:
        return True
    else:
        return False
def border_provinces_2(s):
    global provincesClaimed
    print(s)
    x = provincesClaimed['enemy2']
    if s in x:
        return True
    else:
        return False

def warMenu():
    global war1
    global war2
    global troopsInProvince1
    global troopsInProvince2
    global troopsInProvince
    global provincesClaimed
    global numTroops
    global freeTroops
    global numTroops1
    global numTroops2
    
    attackforce = 0 
    print('=' * 10 + 'WAR MENU' + '='*10  + '\n' + 'Press 1 to declare war on nations' + '\n' + 'Press 2 to access combat menu' + '\n' + 'Press 3 if you want to go back to the main menu')
    warEdit = int(input('What would you like to do?: '))
    if warEdit == 1:
        declareWar()
    elif warEdit == 2:
        the_list_1 = []
        if war1 == True:
            print('you are at war with Empire 1.')
            maps = int(input('would you like to see the current map? input 1 for yes, 2 for no.'))
            if maps == 1:
                x = turtles()
                grid(x, 2, 100)
                allColor(provincesClaimed)
                turtle.clear()
            
            counter = 0
            p =provincesClaimed['playername']
            while counter < len(p):
                s = province_neighbors(p[counter], p, 'enemy1')
                border = list(filter(border_provinces_1, s))
                if len(border) > 0:
                    the_list_1.append(s)
                    counter+=1
                else:
                    coutner+=1
                
            print('here are your provinces that border empire 1:' , the_list_1, 'When you assemble an attack force, you can only draw troops from these border provinces')
            print('here are the troops in each of your provinces:' , troopsInProvince)
            whereTo = int(input('would you like to move troops before attacking? Input 1 for yes, iunput 2 for no'))
            if whereTo == 1:
                militaryMenus()
            elif whereTo ==2:
                print('you can now choose which province to draw troops from. If you have more than 0 freetroops you will have an option to add on any freetroops to the attack force later.')
                provinceChoice = int(input('which province do you choose?'))
                inList = provinceChoice in the_list_1
                if inList == False:
                    print('you did not choose a border province.')
                    backToMenu('warMenu')
                else:
                    print('here are the troops in this province:', troopsInProvince[provinceChoice])
                    troopsDraw = int(input(' How many troops do you want to take out?'))
                    troopsInProvince[provinceChoice] = troopsInProvince[provinceChoice] - troopsDraw
                    attackforce = troopsDraw
                    if freeTroops > 0:
                        print('here are the number of freetroops you have, which arent assigned to any province', freeTroops)
                        freeTroopsDraw = int(input('input the number of freeTroops you would like to use. You can input 0 if you want to'))
                        attackforce+=freeTroopsDraw
                    theNeighbors = province_neighbors(provinceChoice, provincesClaimed['player'], 'playername')
                    print('you can now send this atackforce to an enemy province. Here are the enemy provinces you can attack')
                    enemyProvince = int(input('which province would you like to select?'))
                    inEnemy = enemyProvince in provincesClaimed['enemy1']
                    inNeighbors = enemyprovince in theNeighbors
                    if inEnemy== True and inNeighbors == True:
                        print('scouts have reported that this province has', troopsInProvince1[enemyProvince], 'troops.')
                        attackConf = int(input('do you still wish to attack? input 1 for yes, input 2 for no. If you do not attack, you will have to reassemble an attack force'))
                        if attackConf == 1:
                            if attackforce > troopsInProvince1[enemyProvince]:
                                provincesClaimed['playername'].append(enemyProvince)
                                numTroops1 = numTroops1- troopsInProvince1[enemyProvince]
                                troopsInProvince1.pop(enemyProvince)
                                keys_list = list(troopsInProvince1.keys())
                                provincesClaimed['enemy1'] = keys_list
                                print('your glorious soldiers have won the battle! The enemy troops have perished or fled the scene')
                                backtoMenu('warMenu')
                                
                            elif attackforce == troopsInProvince1[enemyProvince]:
                                print('the armies were evenly matched on the battlefield. No progress was made, but both sides faced heavy casualties.')
                                attackforce//2
                                numTroops = numTroops - attackforce
                                gg = troopsInProvince1[enemyProvince]
                                gg = gg//2
                                troopsInProvince1[enemyProvince] = troopsInProvince1[enemyProvince] - gg
                                numTroops1 = numTroops1 - gg
                                backtoMenu('warMenu')
                            else:
                                print('your troops lost the battle, and none of them survived. There were little to no casualties inflicted on the enemy')
                                numTroops = numTroops - attackforce
                                backToMenu('warMenu')
                        elif attackConf == 2:
                            backtoMenu('warMenu')
                        else:
                            print('that was not a valid input')
                            backToMenu('warMenu')
        elif war2 == True:
            the_list_2 = []
            print('you are at war with Empire 2.')
            maps = int(input('would you like to see the current map? input 1 for yes, 2 for no.'))
            if maps == 1:
                x = turtles()
                grid(x, 2, 100)
                allColor(provincesClaimed)
                turtle.exitonclick()
            
            counter = 0
            p =provincesClaimed['playername']
            while counter < len(p):
                s = province_neighbors(p[counter], p, 'enemy2')
                border = list(filter(border_provinces_2, s))
                if len(border) > 0:
                    the_list_2.append(s)
                    counter+=1
                else:
                    counter+=1
                
            print('here are your provinces that border empire 2:' , the_list_2, 'When you assemble an attack force, you can only draw troops from these border provinces')
            print('here are the troops in each of your provinces:' , troopsInProvince)
            whereTo = int(input('would you like to move troops before attacking? Input 1 for yes, iunput 2 for no'))
            if whereTo == 1:
                militaryMenus()
            elif whereTo ==2:
                print('you can now choose which province to draw troops from. If you have more than 0 freetroops you will have an option to add on any freetroops to the attack force later.')
                provinceChoice = int(input('which province do you choose?'))
                inList = provinceChoice in the_list_2
                if inList == False:
                    print('you did not choose a border province.')
                    backToMenu('warMenu')
                else:
                    print('here are the troops in this province:', troopsInProvince[provinceChoice])
                    troopsDraw = int(input(' How many troops do you want to take out?'))
                    troopsInProvince[provinceChoice] = troopsInProvince[provinceChoice] - troopsDraw
                    attackforce = troopsDraw
                    if freeTroops > 0:
                        print('here are the number of freetroops you have, which arent assigned to any province', freeTroops)
                        freeTroopsDraw = int(input('input the number of freeTroops you would like to use. You can input 0 if you want to'))
                        attackforce+=freeTroopsDraw
                    theNeighbors = province_neighbors(provinceChoice, provincesClaimed['player'], 'playername')
                    print('you can now send this atackforce to an enemy province. Here are the enemy provinces you can attack')
                    enemyProvince = int(input('which province would you like to select?'))
                    inEnemy = enemyProvince in provincesClaimed['enemy2']
                    inNeighbors = enemyProvince in theNeighbors
                    if inEnemy== True and inNeighbors == True:
                        print('scouts have reported that this province has', troopsInProvince2[enemyProvince], 'troops.')
                        attackConf = int(input('do you still wish to attack? input 1 for yes, input 2 for no. If you do not attack, you will have to reassemble an attack force'))
                        if attackConf == 1:
                            if attackforce > troopsInProvince2[enemyProvince]:
                                provincesClaimed['playername'].append(enemyProvince)
                                numTroops2 = numTroops2- troopsInProvince2[enemyProvince]
                                troopsInProvince2.pop(enemyProvince)
                                keys_list = list(troopsInProvince2.keys())
                                provincesClaimed['enemy2'] = keys_list
                                print('your glorious soldiers have won the battle! The enemy troops have perished or fled the scene')
                                backtoMenu('warMenu')
                                
                            elif attackforce == troopsInProvince2[enemyProvince]:
                                print('the armies were evenly matched on the battlefield. No progress was made, but both sides faced heavy casualties.')
                                attackforce//2
                                numTroops = numTroops - attackforce
                                gg = troopsInProvince2[enemyProvince]
                                gg = gg//2
                                troopsInProvince2[enemyProvince] = troopsInProvince2[enemyProvince] - gg
                                numTroops2 = numTroops2 - gg
                                backtoMenu('warMenu')
                            else:
                                print('your troops lost the battle, and none of them survived. There were little to no casualties inflicted on the enemy')
                                numTroops = numTroops - attackforce
                                backToMenu('warMenu')
                        elif attackConf == 2:
                            backtoMenu('warMenu')
                        else:
                            print('that was not a valid input')
                            backToMenu('warMenu')
        else:
            print('You do not have any ongoing wars. Returning to main menu..')
            main(6)
                            
                    
        
    elif warEdit == 3:
        print('returning to main menu...')
        main(6)

# s is any province from province claiming menu
# if s is owned by player, return false
def filterfunc(s):
    global provincesClaimed
    x = provincesClaimed['playername']
    if s in x:
        return False
    else:
        return True

# if s is not owned by enemy, return true
def filterfunc_1(s):
    global provincesClaimed
    print(s)
    x = provincesClaimed['enemy1']
    if s in x:
        return False
    else:
        return True

# if s is owned by an enemy, return false
def filterfunc_2(s):
    global provincesClaimed
    x = provincesClaimed['enemy1']
    if s in x:
        return False
    else:
        return True

def province_neighbors (provinceSelect, provincesowned, who):
    #for player
    global neighbors
    x = provinceSelect
    if x%4 == 0:
        column = x/4
        row = 4
    else:
        column = x//4
        column = column +1
        row = x % 4
    print('column:', column)
    print('row:', row)
    if column == 1:
        if row == 1:
            neighbors = [provinceSelect+1, provinceSelect+4]
        elif row == 4:
            neighbors = [provinceSelect-1, provinceSelect+4]
        else:
            neighbors = [provinceSelect-1, provinceSelect+1, provinceSelect+4]
        print(neighbors)
    elif column == 4:
        if row == 1:
            neighbors = [provinceSelect-4, provinceSelect+1]
        elif row == 4:
            neighbors = [provinceSelect-1, provinceSelect-4]
        else:
            neighbors = [provinceSelect-4, provinceSelect-1, provinceSelect+1]
    else:
        if row == 1:
            neighbors = [provinceSelect-4, provinceSelect+1, provinceSelect+4]
        elif row == 4:
            neighbors = [provinceSelect-4, provinceSelect-1, provinceSelect+4]
        else:
            neighbors = [provinceSelect-4, provinceSelect-1, provinceSelect+1, provinceSelect+4]
    if who == 'playername':
        filtered = list(filter(filterfunc, neighbors))
    elif who == 'enemy1':
        filtered = list(filter(filterfunc_1, neighbors))
        print(filtered)
    elif who == 'enemy2':
        filtered = list(filter(filterfunc_2, neighbors))
    return filtered
    
def militaryMenus():
    global numTroops
    global freeTroops
    global provincesClaimed
    global troopsInProvince
    global wealth
    #minimum of 2 troops per province (garrison), and to claim a province you have to have enough free troops available.
    print('=' * 10 + 'MILITARY MENU' + '='*10  + '\n' + 'Press 1 to conscript troops' + '\n' + 'Press 2 to move troops from province to province' + '\n' + 'Press 3 if you want to go back to the main menu')
    militaryEdit = int(input('What would you like to do?: '))
    if militaryEdit == 1:
        print('your wealth:' , wealth, 'coins. remember that one troops costs one coin to train, and each troop has an upkeep of one coin')
        troopConscription = int(input('How many troops do you want to conscript? '))
        if troopConscription*3 > wealth:
            print('You do not have enough money to hire this many troops!')
            backtoMenu('military')
            
        else:
            numTroops+=troopConscription
            freeTroops+=troopConscription
            print('Your army now has' , freeTroops, 'troops')
            wealth = wealth - troopConscription
            backtoMenu('military')
    elif militaryEdit == 2:
        print(troopsInProvince)
        provinceorigin = int(input('Which province do you want to draw troops from? '))
        r = provinceorigin in provincesClaimed['playername']
        if r == False:
            print('Not a province you own. ')
            backToMenu('military')
        else:
            if troopsInProvince[provinceorigin] > 0:
                print('You have', troopsInProvince, 'troops in this province.')
                
                values = provincesClaimed['playername']
                if len(values) <2:
                    print('You do not have any provinces to move troops to. ')
                    backtoMenu('military')
                else:
                    movement = int(input('How many troops do you want to move? '))
                    if movement > troopsInProvince[provinceorigin]:
                        print('You do not have enough troops in this province.')
                        backtoMenu('military')
                    else:
                        provinceDestination = int(input('Where do you want these troops to go? '))
                        VALUES = provincesClaimed['playername']
                        yesNo = provinceDestination not in VALUES
                        if yesNo == True:
                            print('You cannot move troops there. Please go to the province menu if you want to claim it. ')
                            backtoMenu('military')
                        else:
                            troopsInProvince[provinceDestination] = troopsInProvince[provinceDestination] + (movement)
                            troopsInProvince[provinceorigin] = troopsInProvince[provinceorigin] - movement
                            print('You have moved', movement, 'troops to province' , provinceDestination)
                            backtoMenu('military')
                
            else:
                print('You do not have any troops to move.')
                backtoMenu('military')
    elif militaryEdit == 3:
        main(6)
    else:
        print('that input was not valid')
        backToMenu('military')
def provinceMenu():
    global freeTroops
    global provincesClaimed
    global troopsInProvince
#     a = province_neighbors(neighbor_choice, provincesClaimed['playername'], 'playername')
    print('=' * 10 + 'PROVINCE MENU' + '='*10  + '\n' + 'Press 1 to open the province claiming menu' + '\n' + 'Press 2 to open the individual interaction menu' + '\n' + 'Press 3 to go back to main menu')
    provinceSelect = int(input('What would you like to do? '))
    if provinceSelect ==1:
        print('Please select a province to see its neighbors. Here are the provinces you have:' ,provincesClaimed['playername'])
        neighbor_choice = int(input('Please indicate your choice here: '))
        if neighbor_choice in provincesClaimed['playername']:
            
            a = province_neighbors(neighbor_choice, provincesClaimed['playername'], 'playername')
            print('Here is a list of provinces you can claim:', a)
            print('Here are the number of free troops you can use to claim: ', freeTroops)
            if freeTroops > 1:
            
                provinceClaim = int(input('Which province do you want to claim? '))
                
                variable = provinceClaim in a
                #if a == False:
                if variable == False:
                    print('Sorry, but that province is too far away to claim. Please try a different province.')
                    backtoMenu('province')
                else: 
                    claim = int(input('How many troops would you like to use to claim the province you have selected? '))
                    if claim < 2:
                        print('To occupy this province you must send 2 or more troops. ')
                        backtoMenu('province')
                    elif claim < freeTroops: 
                        freeTroops = freeTroops - claim
                        troopsInProvince[provinceClaim] = claim
                        print(troopsInProvince)
                        provincesClaimed['playername'].append(provinceClaim)
                    
                        print('You have claimed province' , provinceClaim)
                        backtoMenu('province')
                    elif claim > freeTroops:
                        print('You have tried to claim a province using more troops than you actually have. Please go back.')
                        backtoMenu('province')
            else:
                print('You do not have enough free troops to claim any provinces. Train more troops to get more troops. ')
                backtoMenu('province')
        else:
            print('You must select a province that you own.')
            backtoMenu('province')
            
    elif provinceSelect == 2:
        print('Here are the provinces you own:' , provincesClaimed['playername'])
        provinceSelect2 = int(input('Which province do you want to view? '))
        print('troops in province:', troopsInProvince[provinceSelect2], '\n')
        backtoMenu('province')
    elif provinceSelect == 3:
        main(6)
boolean = False

##################################################################
##################################################################
############### P R O V I N C E  S Y S T E M #####################
##################################################################
##################################################################

##########################################COLORING##########################################
def turtle_color():
    
    return provinceColor
def color (values, color): #INPUT THE PROVINCECLAIMED HERE, AND PROVINCECOLOR
    turtles = turtle.Turtle()
    turtles.speed(0)
    turtles.penup()
    turtles.setx(-200)
    turtles.sety(200)
    turtles.pendown()
    counter = 0 
    while counter < len(values):
        x = values[ counter ]
        if x%4 == 0:
            column = x/4
            row = 4
        else:
            column = x//4
            column = column +1
            row = x % 4
        turtles.fillcolor(color)
        
        turtles.fd(100 * column)
        turtles.rt(90)
        turtles.fd(100 * row)
        turtles.begin_fill()
        turtles.rt(90)
        turtles.fd(100)
        turtles.rt(90)
        turtles.fd(100)
        turtles.rt(90)
        turtles.fd(100)
        turtles.end_fill()
        turtles.penup()
        turtles.setx(-200)
        turtles.sety(200)
        turtles.pendown()
        counter+=1

def allColor():
    global provincesClaimed
    
    playervalues = provincesClaimed['playername']
    
    color(playervalues, 'blue')
    enemy1values = provincesClaimed['enemy1']
    
    color(enemy1values, 'green')
    enemy2values = provincesClaimed['enemy2']
    
    color(enemy2values, 'red')

######################## END COLOR #########################
def turtles():
    provinceDraw = turtle.Turtle()
    provinceDraw.speed(0)
    provinceDraw.penup()
    provinceDraw.setx(-200)
    provinceDraw.sety(100)
    provinceDraw.pendown()
    return provinceDraw

def grid (jerry, depth, length):
    counter = 0 
    if depth == 0:
        jerry.fd(length)
    elif depth == 1 :
        jerry.fd(length)
        jerry.lt(90)
        jerry.fd(length)
        jerry.lt(90)
        jerry.fd(length)
        jerry.lt(90)
        jerry.fd(length)
        jerry.fd(length)
    else:
        while counter < depth:
            grid(jerry, depth-1, length)
            jerry.lt(90)
            grid(jerry, depth-1, length)
            jerry.lt(90)
            grid(jerry, depth-1, length)
            jerry.lt(90)
            jerry.fd(length)
            jerry.lt(90)
            jerry.fd(length*3)
            jerry.rt(90)
            counter+=0.5

def map_making():
    x = turtles()
    grid(x, 2, 100)
    allColor()
    turtle.clear()


def turn():
    global events
    global turnCounter
    global turn_list
    global provincesClaimed
    global wealth
    global wealth1
    global wealth2
    global numTroops
    global morale
    global trade1
    global trade2
    global war1
    global war2
    global troopsInProvince1
    print('Here are a list of your provinces:' , provincesClaimed['playername'])
    print(' this is the wealth you had last turn: ', wealth, 'coins')
    computerMain()
    print('troopsinprovince1;',troopsInProvince1)
    wealth1 = wealth1 + 3 * len(provincesClaimed['enemy1']) 
    wealth2 = wealth2 + 3 * len(provincesClaimed['enemy2']) 
    if trade1 == True or trade2 == True:
        print('An empire you have contacted has agreed to trade wit you. Wealth generation recieves a 1.5X boost')
        wealthGain 3 * len(provincesClaimed['playername']) * morale/100 *1.5
        print('this is how many coins you made last turn:', wealthGain)
        wealth+=wealthGain
        print('Your total current wealth in coins is:' , wealth)
    elif trade1 == True and trade2 == True:
        print('You have set up a trading system with the leaders from the two empires you have contacted. Wealth generation gets a 2X boost')
        wealthGain = 3 * len(provincesClaimed['playername']) * morale/100 *2
        print('this is how many coins you made last turn:', wealthGain)
        wealth+=wealthGain
        print('Your total current wealth in coins is:' , wealth)
    else:
        wealthGain = 3 * len(provincesClaimed['playername']) * morale/100
        print('this is how many coins you made last turn:', wealthGain)
        wealth+=wealthGain
        print('Your total current wealth in coins is:' , wealth)
    if war1 or war2 == True:
        if war1 == True:
            print('NOTICE: YOU ARE AT WAR WITH EMPIRE 1')
        if war2 == True:
            print('NOTICE: YOU ARE AT WAR WITH EMPIRE 2')
    elif war1 == True and war2 == True:
        print('You are at war with every nation on the map. Act accordingly')
    else:
        print('your nation is at peace with its neighbors.')
   
    
    if wealth < 0:
        print('Your country is in debt. There will now be a morale penalty every turn')
        morale = morale - 10
    morale+=2
    
    wealth = wealth - numTroops
    print('Your troops demand payment. After payment, you wealth is now:' , wealth)
    events = True
    if events == True and dead == False:
        event()
    events = False
    
    turnCounter+=1
    turn_list.append(turnCounter)
  
    main(6)

#     #perhaps set a boolean to true, so that it triggers gavin's functions

a = 'A man approaches you and offers his army of trained mercenaries for a wagon of gold. Do you accept the trade?'
A = 'The number of troops you have increased by 25. \n Your wealth decreased by 5'
AA = 'Some of your troops left with the man. \n Number of troops decreased by 2.'

b = 'Your son murdered one of your citizns. People are demanding an execution. Do you respect their wishes?'
B = 'Your son is executed. \n Morale increases by 5. \n Number of troops decreased by 1. \n Personal happiness decreased by 20.'
BB = 'Your son lives. He took some gold off the dead man. \n Wealth increases by 2. \n Morale decreases by 10. \n Personal happiness increases by 10.'

c = 'An architect offers to build more homes and other buildings for your citizens for gold. Will you accept their offer?'
C = 'New homes and buildings are built. \n Morale increases by 15. \n Wealth decreases by 10.'
CC = 'Nothing is built. People are disappointed. \n Morale decreases by 3.'

d = 'A foreign leader offers his child to you in exhange for an alliance. Do you accept?'
D = 'You marry his child. \n Your number of troops increases by 30. \n Your wealth increases by 30. \n You do not love his child and neither do your people. \n Your personal happiness decreases by 10. \n Morale decreases by 10.'
DD = 'You do not marry his daughter. You current spouse is very happy with you. \n Your personal happiness increases 10.'

e = 'Your spouse suggests going to the local theatre. It is quite expensive. Will you go?'
E = ' You go. \n Wealth decreases by 5. \n Morale increases by 5 because people see you acting just like them. \n Perosnal happiness increases by 2.'
EE = 'You do not go. \n No status change.'

f = 'A noble you did not like is found dead under suspicious circumstances. Do you investigate?'
F = 'You investigate. The noble died a noble death and is hailed a hero.\n Morale increases by 3. \n Personal happiness decreases by 3.'
FF = 'You turn a blind eye. \n Morale decreases by 4. \n Personal happiness increases by 4.'

g = 'A popular author criticizes your decisions very publicly. Do you punish him?'
G = 'You send him to prison. \n Morale decreases by 6. \n Personal happiness increases by 6.'
GG = 'You ignore him. Personal happiness decreases by 10.'

h = 'Your people want more artwork in your empire. Will you commission more artwork?'
H = 'You commission many statues and paintings. \n Wealth decreases by 10. \n Morale increases by 5.'
HH = 'You ignore your people. \n Morale decreases by 6.'

i = 'Your oldest son wishes to marry someone. If they marry, you will have to pay a large dowry and pay for an expensive wedding. Do you allow it?'
I = 'You bless the wedding.\n Wealth decreases by 10. \n Personal happiness increases by 5.\n Morale increases by 3.'
II = 'You do not bless the wedding. \n Personal happiness decreases by 5.'

j = 'A respected soldier died a hero. Your people are demanding a large funeral. Will you hold the funeral?'
J = 'You organize a funeral.\n Wealth decreases by 5.\n Morale increases 5.'
JJ = 'You do not hold a funeral. \n Morale decreases by 5.'

k = 'Your new head chef makes you a delicious looking stew. He smiles at you strangely. Do you try the stew?'
K = 'You try the stew. \n You die.'
KK = 'You have someone else try the stew. They die. You execute the chef.\n Personal happiness decreases by 3.'

l = 'You see a stray puppy. Will you adopt the puppy?'
L = 'You adopt the stray puppy.\n Personal happiness increases by 15.'
LL = 'You do not adopt the stray puppy. \n Shame increases by 1000. Shame on you.'

m = 'A traveling jester offers to perform in your capital for some gold. Do you accept his offer?'
M = 'You pay the jester to perform.\n Wealth decreases by 2.\n Morale increases by 5. '
MM = 'You refuse to pay.\n No status effect.'

n = 'You find a pile of gold on the ground. Do you take it?'
N = 'You take it. It belonged to an orphanage.\n Wealth increases by 5.\n Morale decreases by 5.'
NN = 'You leave it.\n No status change.'

o = 'You need to pick a religion to become the standard religion of your empire. Most of your people are Protestant. The pope offers you a large sum of gold to become Catholic. Input 0 to become Protestant and input 1 to become Catholic.'
O = 'You choose to become Protestant. \n Morale increases by 6.'
OO = 'You choose to become Catholic.\n Weatlh increases by 7. \n Morale decreases by 4.'

p = 'Your citizens are protesting for more money. They want to all receive more gold. You were planning on raising taxes. Do you give them more gold? '
P = 'You hand over gold.\n Wealth decreases by 20.\n Morale increases by 25.'
PP = 'You raise taxes in response.\n Wealth increases by 15. \n Morale decreases by 25.'

q = 'A terrible disease spreads through your empire. Your people are demanding something be done. Input 0 to go scientific route and input 1 to go religious route.'
Q = 'You blame rats and pay for mass extermination of rats.\n Wealth decreases by 8.\n Morale increases by 6.'
QQ = 'You pray to your god that this plague ends.\n Morale increases by 3.'

r = 'Literacy rates are very low. People are asking for better education. Do you improve education?'
R = 'You spend money to improve education.\n Wealth decreases by 8. \n Morale increases by 6.'
RR = 'You do nothing.\n Morale decreases by 5.'

s = 'Your head guard tells you that your security is not good enough. Do you listen to him and improve security?'
S = 'You improve security.\n Wealth decreases by 10. \n Morale increases by 3. \n Personal happiness increases by 5.'
SS = 'You do nothing. You are robbed in the middle of the night.\n Wealth decreases by 30.'

t = 'You see a cute looking raccoon. Do you adopt the raccoon?'
T = 'You adopt the raccoon. He scratches and bites you and runs away.\n Personal happiness decreases by 5.'
TT = 'You give the raccoon space as it is a wild animal and should not be approached.\n No status change.'

u = 'You can import either food or silk from a foreign nation. Input 0 to import food and input 1 to import silk.'
U = 'You import food for your people.\n Morale increases by 10.'
UU = 'You import silk for yourself.\n Personal happiness increases by 5.'

v = 'You see a clown in a sewer drain. Will you speak to the clown?'
V = 'You approach the clown. He eats your soul and disappears. \n Personal happiness decreases by 30.'
VV = 'You get the heck out of there. \n No status change.'

w = 'You meet someone who claims to be a time traveler. He tells you he can transport you to anywhere. Do you listen to him?'
W = 'You accept and go into his machine. You wake up and nothing has changed. The man robbed you.\n Wealth decreases by 15.'
WW = 'You execute the heathen.\n No status changes. '

x = 'You find a machine with a tag attached saying money printer. Input 0 to print money and input 1 to sell the printer.'
X = 'You use the machine. Inflation occurs.\n Morale decreases by 10.'
XX = 'You sell the machine to some poor shmuck from outside the empire.\n Wealth increases by 10.'

y = 'You find a cool hat. Input 0 to wear the hat and input 1 to sell the hat.'
Y = 'You put on the cool hat.\n Personal happiness increases by 15.\n Swagger increases by 50.'
YY = 'You sell the cool hat.\n Wealth increases by 7.'

z = 'You and your hunting party kill lots of game. Input 0 to share with nobles and input 1 to share with everyone.'
Z = 'You, your family, and the nobles eat it.\n Personal happiness increases by 10.'
ZZ = 'You share it with your people.\n Morale increases by 10.'

eventList = [a, b, c, d, e, f, g, h, i , j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
eventDict = {a:[A,AA], b:[B,BB], c:[C,CC], d:[D,DD], e:[E,EE], f:[F,FF], g:[G,GG], h:[h,HH], i:[I,II], j:[J,JJ], k:[K,KK], l:[L,LL], m:[M,MM], n:[N,NN], o:[O,OO], p:[P,PP], q:[Q,QQ], r:[R,RR], s:[S,SS], t:[T,TT], u:[U,UU], v:[V,VV], w:[W,WW], x:[X,XX], y:[Y,YY], z:[Z,ZZ]} 

#so the code should be this: this resets the values each time
def statChange(mrl, wlth, nt, ph):
    global morale
    global wealth
    global numTroops
    global personalHappiness

    global troops_list
    global wealth_list
    global morale_list
    
    morale += mrl
    wealth += wlth

        
    numTroops += nt
    personalHappiness += ph
    morale_list.append(morale)
    troops_list.append(numTroops)
    wealth_list.append(wealth)
    
def gameOver():
    global endGame
    global dead
    endGame = True
    dead = True
    print ('Game Over.')

def death():
    global age
    global morale
    global wealth
    global dead
    global empire
    global name
    if morale < 5:
        print('Unfortunately, your people were not happy with your management. You have been overthrown, literally.\n Your people threw you into the ocean and you drowned. ')
        print('You lived to', age)
        gameOver()
    elif wealth <= -20:
        print('You have gone bankrupt and cannot pay your workers. The empire has collapsed.\n ', empire, ' will go down as the worst empire in decades of empires. ')
        print('You lived to', age)
        gameOver()
    elif dead == True:
        print('One flawed decision has cost you your life. R.I.P ', name)
        print('You lived to', age)
        gameOver()
    elif personalHappiness <= 0:
        print('You have been very upset lately. This morning your people found out you jumped over a cliff. R.I.P', name)
    elif age == 96:
        print('You win!')
        gameOver()
    
def statOutcome(outcome):
    global dead
    if outcome == A:
        statChange(0,-5,25,0)
        death()
    elif outcome == AA:
        statChange(0,0,-2,0)
        death()
    elif outcome == B:
        statChange(5,0,-1,-20)
        death()
    elif outcome == BB:
        statChange(-10,2,0,+10)
        death()
    elif outcome == C:
        statChange(+15,-10,0,0)
        death()
    elif outcome == CC:
        statChange(-3,0,0,0)
        death()
    elif outcome == D:
        statChange(-10,30,30,-10)
        death()
    elif outcome == DD:
        statChange(0,0,0,10)
        death()
    elif outcome == E:
        statChange(5,-5,0,2)
        death()
    elif outcome == EE:
        statChange(0,0,0,0)
        death()
    elif outcome == F:
        statChange(3,0,0,-3)
        death()
    elif outcome == FF:
        statChange(-4,0,0,4)
        death()
    elif outcome == G:
        statChange(-6,0,0,6)
        death()
    elif outcome == GG:
        statChange(0,0,0,-10)
        death()
    elif outcome == H:
        statChange(5,-10,0,0)
        death()
    elif outcome == HH:
        statChange(-6,0,0,0)
        death()
    elif outcome == I:
        statChange(3,-10,0,5)
        death()
    elif outcome == II:
        statChange(0,0,0,-5)
        death()
    elif outcome == J:
        statChange(5,-5,0,0)
        death()
    elif outcome == JJ:
        statChange(-5,0,0,0)
        death()
    elif outcome == K:
        dead = True
        death()
    elif outcome == KK:
        statChange(0,0,0,-3)
        death()
    elif outcome == L:
        statChange(0,0,0,15)
        death()
    elif outcome == LL:
        statChange(0,0,0,0)
        death()
    elif outcome == M:
        statChange(5,-2,0,0)
        death()
    elif outcome == MM:
        statChange(0,0,0,0)
        death()
    elif outcome == N:
        statChange(-5,5,0,0)
        death()
    elif outcome == NN:
        statChange(0,0,0,0)
        death()
    elif outcome == O:
        statChange(6,0,0,0)
        death()
    elif outcome == OO:
        statChange(-4,7,0,0)
        death()
    elif outcome == P:
        statChange(25,-20,0,0)
        death()
    elif outcome == PP:
        statChange(-20,15,0,0)
        death()
    elif outcome == Q:
        statChange(6,-8,0,0)
        death()
    elif outcome == QQ:
        statChange(3,0,0,0)
        death()
    elif outcome == R:
        statChange(6,-8,0,0)
        death()
    elif outcome == RR:
        statChange(-5,0,0,0)
        death()
    elif outcome == S:
        statChange(0,-10,0,0)
        death()
    elif outcome == SS:
        statChange(3,-20,0,5)
        death()
    elif outcome == T:
        statChange(0,0,0,-5)
        death()
    elif outcome == TT:
        statChange(0,0,0,0)
        death()
    elif outcome == U:
        statChange(10,0,0,0)
        death()
    elif outcome == UU:
        statChange(0,0,0,5)
        death()
    elif outcome == V:
        statChange(0,0,0,-30)
        death()
    elif outcome == VV:
        statChange(0,0,0,0)
        death()
    elif outcome == W:
        statChange(0,-15,0,0)
        death()
    elif outcome == WW:
        statChange(0,0,0,0)
        death()
    elif outcome == X:
        statChange(-10,0,0,0)
        death()
    elif outcome == XX:
        statChange(0,10,0,0)
        death()
    elif outcome == Y:
        statChange(0,0,0,15)
        death()
    elif outcome == YY:
        statChange(7,0,0,0)
        death()
    elif outcome == Z:
        statChange(10,0,0,0)
        death()
    elif outcome == ZZ:
        statChange(0,10,0,0)
        death()

def event():
    global eventList
    global age
    age += 3
    if age == 96:
        print("You have died of old age at the age of 96.")
        death()
    currentEvent = random.choice(eventList)
    newEventList = []
    for event in eventList:
        if event != currentEvent:
            newEventList.append(event)
    eventList = newEventList
    print(currentEvent)
    choice = (input('Unless the prompt says otherwise, input 0 to say yes and input 1 to say no: '))
    if choice != '0' and choice != '1':
        print('Not a valid input. Try again. If you fail to give a valid input again, you will recieve errors and the game will end.')
        choice = (input('Unless the prompt says otherwise, input 0 to say yes and input 1 to say no: '))
    outcome = eventDict[currentEvent][int(choice)]
    print(outcome)
    statOutcome(outcome)

def graphs():
    global troops_list
    global wealth_list
    global turn_list
    global morale_list
    
    graph.bar(turn_list, morale_list)
    graph.xlabel('Turns')
    graph.ylabel('Average Morale')
    graph.title('Morale Graph')
    graph.show()
    
    graph.bar(turn_list, wealth_list)
    graph.ylabel('Wealth of the Empire')
    graph.title('Wealth Graph')
    graph.show()
    
    graph.bar(turn_list, troops_list)
    graph.title('Army Size')
    graph.ylabel('Army Size')
    graph.show()
    main(6)

def mainMenu ():
    global startGame
    global contact1
    global contact2
    
    if startGame== True:
        beginnings()
        startGame = False
        print('=' * 10 + 'MAIN MENU'+ '='*10 + '\n'+ 'Press 1 to open military menu'+ '\n' + 'Press 2 to open province management'+ '\n' + 'Press 3 to see graphs' + '\n' + 'Press 4 to end turn and see your annual dilemma' + '\n' + 'Press 5 to open the war menu')
        userInput = int(input('What would you like to do?: '))
        return userInput
    else:
        print('=' * 10 + 'MAIN MENU'+ '='*10 + '\n'+ 'Press 1 to open military menu'+ '\n' + 'Press 2 to open province management'+ '\n' + 'Press 3 to see graphs' + '\n' + 'Press 4 to end turn and see your annual dilemma''\n' + 'Press 5 to open the war menu')
        userInput = int(input('What would you like to do?: '))
        return userInput
userInput = mainMenu()

def main(a):
    global endGame
    while endGame == False:
        
        if a ==1:
            militaryMenus()
        elif a == 2:
            provinceMenu()
        elif a ==3:
            graphs()
        elif a == 4 :
            x = turtles()
            map_making()
            
            turn()
            #     x = turtles()
#     map_making()
        elif a == 5:
            warMenu()
            #a = mainMenu()
        elif a == 6:
            a = mainMenu()
            #warMenu()
            
        else:
            print('That is not a valid input. Redirecting to main menu...')
            mainMenu()
main(userInput)
turtle.exitonclick()