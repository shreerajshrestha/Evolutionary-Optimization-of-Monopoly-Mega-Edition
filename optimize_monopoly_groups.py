__author__ = 'dmyers'

import random;
import math


def playGame(p0, p1, p2, p3):

    playerValues = [p0, p1, p2, p3]

    no_of_squares = 52
    starting_cash = 2500
    min_cash = 200
    bail_cash = 50
    luxury_tax = 75
    default_income_tax = 200
    go_cash = 200
    JAIL = 13

    square_names = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Arctic Avenue',
                    'Income Tax', 'Reading Railroad', 'Massachusetts Avenue', 'Oriental Avenue', 'Chance',
                    'Gas Company', 'Vermont Avenue', 'Connecticut Avenue', 'Jail', 'Auction', 'Maryland Avenue',
                    'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue',
                    'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Aveune',
                    'New York Avenue', 'New Jersey Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance',
                    'Indiana Avenue', 'Illinois Avenue', 'Michigan Avenue', 'Bus Ticket', 'B. & O. Railroad',
                    'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'California Avenue',
                    'Go to Jail', 'Pacific Avenue', 'South Carolina Avenue', 'North Carolina Avenue',
                    'Community Chest', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Birthday Gift',
                    'Florida Avenue', 'Park Place', 'Luxury Tax', 'Boardwalk']

    square_type = ['GO', 'PE', 'CC', 'PE', 'PE', 'IT', 'RR', 'LB', 'LB', 'CE',
                    'UY', 'LB', 'LB', 'JL', 'AN', 'PK', 'PK', 'UY', 'PK', 'PK',
                    'RR', 'OE', 'CC', 'OE', 'OE', 'OE', 'FP', 'RD', 'CE', 'RD',
                    'RD', 'RD', 'BT', 'RR', 'YW', 'YW', 'UY', 'YW', 'YW', 'GJ',
                    'GN', 'GN', 'GN', 'CC', 'GN', 'RR', 'CE', 'BG', 'DB', 'DB',
                    'LT', 'DB']

    face_values = [-1, 60, -1, 60, 80, -1, 200, 100, 100, -1,
                   150, 100, 120, -1, -1, 140, 140, 150, 140, 160,
                   200, 180, -1, 180, 200, 200, -1, 220, -1, 220,
                   240, 240, -1, 200, 260, 260, 150, 280, 280, -1,
                   300, 300, 300, -1, 320, 200, -1, -1, 350, 350,
                   -1, 400]

    mortgage_value = [-1, 30, -1, 30, 40, -1, 100, 50, 50, -1,
                       75, 50, 60, -1, -1, 70, 70, 75, 70, 80,
                       100, 90, -1, 90, 100, 100, -1, 110, -1, 110,
                       120, 120, -1, 100, 130, 130, 75, 140, 140, -1,
                       150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
                       -1, 200]

    rent_value = [-1, 2, -1, 4, 5, -1, 25, 6, 6, -1,
                   400, 6, 8, -1, -1, 10, 10, 400, 10, 12,
                   25, 14, 14, -1, 16, 16, -1, 18, -1, 28,
                   20, 20, -1, 25, 22, 22, 400, 24, 24, -1,
                   26, 26, 26, -1, 28, 25, -1, -1, 35, 35,
                   -1, 50]

    upgrade_cost = [-1, 50, -1, 50, 50, -1, 100, 50, 50, -1,
                    -1, 50, 50, -1, -1, 100, 100, -1, 100, 100,
                    100, 100, 100, 100, 100, 150, -1, 150, -1, 150,
                    150, 150, -1, 100, 150, 150, -1, 140, 140, -1,
                    150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
                    -1, 200]

    rent_value_1 = [-1, 10, -1, 20, 30, -1, 50, 30, 30, -1,
                    100000, 30, 40, -1, -1, 50, 50, 100000, 50, 60,
                    50, 70, 70, -1, 80, 80, -1, 100, -1, 100,
                    100, 100, -1, 50, 110, 110, 100000, 120, 120, -1,
                    130, 130, 130, -1, 150, 50, -1, -1, 175, 175,
                    -1, 200]

    rent_value_2 = [-1, 30, -1, 60, 80, -1, 100, 90, 90, -1,
                    200000, 90, 100, -1, -1, 150, 150, 200000, 150, 180,
                    100, 200, 200, -1, 220, 220, -1, 90, -1, 90,
                    100, 100, -1, 100, 330, 330, 200000, 360, 360, -1,
                    390, 390, 390, -1, 450, 100, -1, -1, 500, 500,
                    -1, 600]

    rent_value_3 = [-1, 90, -1, 180, 240, -1, 200, 270, 270, -1,
                    -1, 270, 300, -1, -1, 450, 450, -1, 450, 500,
                    200, 550, 550, -1, 600, 600, -1, 700, -1, 700,
                    750, 750, -1, 200, 800, 800, -1, 850, 850, -1,
                    900, 900, 900, -1, 1000, 200, -1, -1, 1100, 1100,
                    -1, 1400]

    rent_value_4 = [-1, 160, -1, 320, 360, -1, -1, 400, 400, -1,
                    -1, 400, 450, -1, -1, 625, 625, -1, 625, 700,
                    -1, 750, 750, -1, 800, 800, -1, 875, -1, 875,
                    925, 925, -1, -1, 975, 975, -1, 1025, 1125, -1,
                    1100, 1100, 1100, -1, 1200, -1, -1, -1, 1300, 1300,
                    -1, 1700]

    owner = []
    for i in range(len(face_values)):
        if face_values[i] > 0:
            owner.append(-1)
        else:
            owner.append(-2)

    maxTurns = 1600
    numSquares = 52

    location = [0,0,0,0]
    money = [starting_cash for i in range(4)]
    inJail = [False, False, False, False]

    player = random.randint(0, 3)
    turn = 0
    nConsecutiveDoubles = 0

    bankrupt = []  # Order in which players have gone bankrupt

    numberOwned = [{},{},{},{}]
    for i in range(4):
        for group in ['PE', 'LB', 'DB', 'OE', 'RD', 'YW', 'GN', 'PK', 'RR', 'UY']:
            numberOwned[i][group] = 0

    numberOfHouses = [0 for i in range(len(face_values))]
    ownedProperties = [[],[],[],[]]


    while turn <= maxTurns:
        #print player

        # If there is only one unbankrupted player, end the game
        if len(bankrupt) == 3:
            #print "\tOnly one player remains.  Done!"
            break

        # If the player has no money, continue to next player
        if money[player] <= 0:
            #print "\tPlayer is bankrupt.  Skipping."
            player = (player + 1) % 4
            continue

        # If the player is in jail, just make them pay to get out
        if square_type[location[player]] == 'JL' and inJail[player]:
            #print "\tPaying to get out of jail"
            money[player] -= bail_cash
            inJail[player] = False
            if money[player] <= 0:
                #print "\tPLayer went bankrupt from paying bail."
                # Return all properties to unowned status
                for i in range(len(owner)):
                    if owner[i] == player:
                        owner[i] = -1
                        numberOfHouses[i] = 0

                bankrupt.append(player)
                player = (player + 1) % 4
                turn += 1
                continue


        # Roll dice
        die1  = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = die1 + die2
        #print "\tRolled", roll

        if die1 == die2:
            isDoubles = True
        else:
            isDoubles = False

        # If this is the player's third consecutive double roll, go to jail and end turn
        if isDoubles and nConsecutiveDoubles == 2:
            #print "\tGoing to jail for rolling 3 consecutive doubles"
            location[player] = JAIL
            inJail[player] = True
            nConsecutiveDoubles = 0
            player = (player + 1) % 4
            turn += 1
            continue
        else:
            nConsecutiveDoubles += 1

        #print "\tOld location", location[player]

        # If the player passes GO, award $200
        if location[player] + roll >= no_of_squares:
            #print "\t$200 for passing GO"
            money[player] += 200

        # Advance current player based on dice roll
        location[player] = (location[player] + roll) % no_of_squares
        square = location[player]

        #print "\tNew location", square

        # If the player lands on an owned property, pay rent
        if owner[square] > -1 and owner[square] != player and face_values[square] > -1:

            #print "\tPaying rent to player", owner[square]

            payee = owner[square]
            group = square_type[square]
            rent = rent_value[square]

            # Calculate required rent
            if group == 'UY' and numberOwned[payee][group] == 1:
                rent = 4 * roll
            if group == 'UY' and numberOwned[payee][group] > 1:
                rent = 10 * roll
            if (group == 'DB' or group == 'PE') and numberOwned[payee][group] == 3:
                if numberOfHouses[square] == 0:
                    rent = 3 * rent_value[square]
                elif numberOfHouses[square] == 1:
                    rent = rent_value_1[square]
                elif numberOfHouses[square] == 2:
                    rent = rent_value_2[square]
                elif numberOfHouses[square] == 3:
                    rent = rent_value_3[square]
                elif numberOfHouses[square] == 4:
                    rent = rent_value_4[square]
            if (group in ['LB', 'PK', 'OE', 'RD', 'YW', 'GN']) and numberOwned[payee][group] == 4:
                if numberOfHouses[square] == 0:
                    rent = 3 * rent_value[square]
                elif numberOfHouses[square] == 1:
                    rent = rent_value_1[square]
                elif numberOfHouses[square] == 2:
                    rent = rent_value_2[square]
                elif numberOfHouses[square] == 3:
                    rent = rent_value_3[square]
                elif numberOfHouses[square] == 4:
                    rent = rent_value_4[square]

            # Calculate required rent
            if group == 'UY' and numberOwned[payee][group] == 1:
                rent = 4 * roll
            if group == 'UY' and numberOwned[payee][group] > 1:
                rent = 10 * roll
            if (group == 'DB' or group == 'PE') and numberOwned[payee][group] == 3:
                rent = 3 * rent_value[square]
            if (group in ['LB', 'PK', 'OE', 'RD', 'YW', 'GN']) and numberOwned[payee][group] == 4:
                rent = 3 * rent_value[square]

            #print "\t", rent

            # If the player can't pay rent, they are out of the game
            if money[player] < rent:
                #print "\tBankrupt from paying rent"
                for i in range(len(owner)):
                    if owner[i] == player:
                        owner[i] = -1
                        numberOfHouses[i] = 0

                money[player] -= rent
                bankrupt.append(player)
                player = (player + 1) % 4
                turn += 1
                continue
            else:
                money[player] -= rent
                money[owner[square]] += rent

        # If the player lands on an unowned property, decide to purchase it or not
        if owner[square] == -1 and face_values[square] > 0:

            #print "\tProperty is unowned"
            group = square_type[square]

            # Purchase the property if its face value is less than perceived value and purchasing won't go below minimum cash
            if random.random() < playerValues[player][group] and money[player] - face_values[square] > min_cash:
                #print "\tPuchasing property"
                owner[square] = player
                money[player] -= face_values[square]
                numberOwned[player][group] += 1
                ownedProperties[player].append(square)

        # If the player lands on chance or community chest, probabilisitcally go to jail
        if square_type[square] == 'CC' or square_type[square] == 'CE':

            if random.random() < 1.0 / 16:
                #print "\tWent to JAIL from chance or community chest"
                location[player] = JAIL
                inJail[player] = True
                nConsecutiveDoubles = 0
                player = (player + 1) % 4
                turn += 1
                continue

        # If the player lands on go to jail, go to jail
        if square_type[square] == 'GJ':
            #print "\tGoing to JAIL from GO TO JAIL"
            location[player] = JAIL
            inJail[player] = True
            nConsecutiveDoubles = 0
            player = (player + 1) % 4
            turn += 1
            continue


        #--- Property upgrades

        makingUpgrades = True
        while (makingUpgrades and money[player] > min_cash):

            upgradeable = []
            importance = []

            # Identify all properties that could be upgraded in a list
            for prop in range(len(ownedProperties[player])):
                i = ownedProperties[player][prop]

                group = square_type[i]

                # Skip unownable properties
                if group not in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB']:
                    continue

                if not owner[i] == player:
                    continue

                # Need at least 3 of a property group to make improvemets
                if numberOwned[player][group] < 3:
                    continue

                if numberOfHouses[i] == 4:
                    continue

                if money[player] < upgrade_cost[i] + min_cash:
                    continue


                upgradeable.append(i)
                importance.append(playerValues[player][group + '_up'])

            if len(upgradeable) == 0:
                makingUpgrades = False
                break

            # Sort based on importances
            sortedUpgradeable = [upgr for (imp, upgr) in sorted(zip(importance, upgradeable), reverse = True)]
            sortedImportances = [imp for (imp, upgr) in sorted(zip(importance, upgradeable), reverse = True)]

            # Choose a property based on importance
            total = sum(importance)
            target = random.random() * total
            cumSum = 0.0

            for i in range(len(sortedImportances)):
                cumSum += sortedImportances[i]
                if target < cumSum:
                    propertyToUpgrade = sortedUpgradeable[i]

            # Purchase a house for the property
            money[player] -= upgrade_cost[propertyToUpgrade]
            numberOfHouses[propertyToUpgrade] += 1

            #print "Upgrading ", square_names[propertyToUpgrade]
            #print "Money remaining", money[player]


        # If the player did not roll doubles, switch to the next player
        if not isDoubles:
            nConsecutiveDoubles = 0
            player = (player + 1) % 4
            turn += 1

    # If there are unbankrupted players remaining, order them based on money and value of properties
    totalAssets = []
    for i in range(4):
        if i in bankrupt:
            index = bankrupt.index(i)
            totalAssets.append((4 - index) * -1000000)
        else:
            assets = money[i]
            for j in range(len(owner)):
                if owner[j] == i:
                    assets += face_values[j]
            totalAssets.append(assets)

    ranking = [0, 1, 2, 3]
    ranking = [r for (x,r) in sorted(zip(totalAssets, ranking), reverse = True)]

    # Assign points based on ordering
    points = [0,0,0,0]
    points[ranking[0]] = 4
    points[ranking[1]] = 2
    points[ranking[2]] = 1
    points[ranking[3]] = 0

    return points



def testAgainstRandom(p):

    state = random.getstate()

    score = 0

    #random.seed(0)

    for iter in range(100):
        population = []
        nIndividuals = 3
        for n in range(nIndividuals):

            newIndividual = {}
            for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY',
                      'PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:
                #newIndividual[i] = random.random()
                #newIndividual[i] = 1.0

                if random.random() > .5:
                    newIndividual[i] = random.random()
                else:
                    newIndividual[i] = random.random()

            population.append(newIndividual)
        points = playGame(p, population[0], population[1], population[2])
        score += points[0]

    random.setstate(state)
    return score


def findRandomMember(fitness):

    totalFitness = sum(fitness)
    target = totalFitness * random.random()

    cumFitness = 0
    for i in range(len(fitness)):
        cumFitness += fitness[i]

        if target < cumFitness:
            return i


#--- Main

square_names = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Arctic Avenue',
                'Income Tax', 'Reading Railroad', 'Massachusetts Avenue', 'Oriental Avenue', 'Chance',
                'Gas Company', 'Vermont Avenue', 'Connecticut Avenue', 'Jail', 'Auction', 'Maryland Avenue',
                'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue',
                'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Aveune',
                'New York Avenue', 'New Jersey Avenue', 'Free Parking', 'Kentucky Avenue', 'Chance',
                'Indiana Avenue', 'Illinois Avenue', 'Michigan Avenue', 'Bus Ticket', 'B. & O. Railroad',
                'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'California Avenue',
                'Go to Jail', 'Pacific Avenue', 'South Carolina Avenue', 'North Carolina Avenue',
                'Community Chest', 'Pennsylvania Avenue', 'Short Line', 'Chance', 'Birthday Gift',
                'Florida Avenue', 'Park Place', 'Luxury Tax', 'Boardwalk']

square_type = ['GO', 'PE', 'CC', 'PE', 'PE', 'IT', 'RR', 'LB', 'LB', 'CE',
                'UY', 'LB', 'LB', 'JL', 'AN', 'PK', 'PK', 'UY', 'PK', 'PK',
                'RR', 'OE', 'CC', 'OE', 'OE', 'OE', 'FP', 'RD', 'CE', 'RD',
                'RD', 'RD', 'BT', 'RR', 'YW', 'YW', 'UY', 'YW', 'YW', 'GJ',
                'GN', 'GN', 'GN', 'CC', 'GN', 'RR', 'CE', 'BG', 'DB', 'DB',
                'LT', 'DB']

face_values = [-1, 60, -1, 60, 80, -1, 200, 100, 100, -1,
               150, 100, 120, -1, -1, 140, 140, 150, 140, 160,
               200, 180, -1, 180, 200, 200, -1, 220, -1, 220,
               240, 240, -1, 200, 260, 260, 150, 280, 280, -1,
               300, 300, 300, -1, 320, 200, -1, -1, 350, 350,
               -1, 400]


# Initialize the starting population
population = []
nIndividuals = 1000
for n in range(nIndividuals):
    newIndividual = {}
    for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY',
              'PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:
        if random.random() > .5:
            newIndividual[i] = random.random()
        else:
            newIndividual[i] = random.random()

    population.append(newIndividual)

# Run the genetic algorithm

nGenerations = 500

fitnessAgainstRandom = []

for generation in range(nGenerations):

    # Find fitness of each individual
    #fitness = []
    #for n in range(nIndividuals):
    #    fitness.append(fitnessFunction(population[n]))

    #--- Find fitness of each individual through competitive simulation
    # Run for 100 trials
    # On each trial, play 250 games of Monopoly
    # Each game chooses four random participants, without replacement, from the population
    # Participants play simulated game and receive points based on outcome
    # First place = 3 points, second place = 2 points, etc.
    # Individual's fitness is the total points it accumulates out of the 100 games it plays
    fitness = [0 for i in range(nIndividuals)]

    #for trial in range(100):

    #    # Generate random permutation of individuals for match groupings
    #    order = range(nIndividuals)
    #    random.shuffle(order)

    #    for match in range(nIndividuals / 4):

    #        p1 = order[match * 4]
    #        p2 = order[match * 4 + 1]
    #        p3 = order[match * 4 + 2]
    #        p4 = order[match * 4 + 3]

    #        points = playGame(population[p1], population[p2], population[p3], population[p4])

    #        fitness[p1] += points[0]
    #        fitness[p2] += points[1]
    #        fitness[p3] += points[2]
    #        fitness[p4] += points[3]

    for i in range(nIndividuals):
        fitness[i] = testAgainstRandom(population[i])

    # Sort based on fitness
    sortedFitness = [f for (f,p) in sorted(zip(fitness, population), reverse = True)]
    sortedPopulation = [p for (f,p) in sorted(zip(fitness, population), reverse = True)]

    fitness = sortedFitness
    population = sortedPopulation

    # Print the best member
    print "Generation = ", generation
    print "Best fitness = ", fitness[0]
    #print "Best individual = ", population[0]
    for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY',
              'PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:

        print i, population[0][i]

    fitnessAgainstRandom.append(testAgainstRandom(population[0]))
    print "Fitness against random = ", fitnessAgainstRandom
    print

    # Generate the next new population
    nextPopulation = []

    # Top 1% of members survive by right
    nSurvivors = int(nIndividuals * .01)
    for i in range(nSurvivors):
      nextPopulation.append(population[i])

    # Remainder are filled by combinations
    for i in range((nIndividuals - nSurvivors) / 2):

        # Pick two random members of the population, weighted by fitness scores
        index = findRandomMember(fitness)
        firstIndividual = population[index]

        index = findRandomMember(fitness)
        secondIndividual = population[index]

        #Split

        newIndividual1 = {}
        newIndividual2 = {}

        keys = population[0].keys()
        split = random.randint(0,len(keys))

        for i in range(split):
            newIndividual1[keys[i]] = firstIndividual[keys[i]]
            newIndividual2[keys[i]] = secondIndividual[keys[i]]

        for i in range(split, len(keys)):
            newIndividual1[keys[i]] = secondIndividual[keys[i]]
            newIndividual2[keys[i]] = firstIndividual[keys[i]]

        nextPopulation.append(newIndividual1)
        nextPopulation.append(newIndividual2)

    nextPopulation = nextPopulation[0:nIndividuals]

    # Mutation
    for n in range(nSurvivors + 1, nIndividuals):
        for i in population[0]:
            if random.random() < .01:
                if random.random() > .5:
                    nextPopulation[n][i] = random.random()
                else:
                    nextPopulation[n][i] = random.random()

    population = nextPopulation
