

__author__ = 'dmyers'

import random
import math
import Simulation

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

    # The number of buyable properties = 37
    face_values = [-1, 60, -1, 60, 80, -1, 200, 100, 100, -1, 150, 100, 120,
                   -1, -1, 140, 140, 150, 140, 160, 200, 180, -1, 180, 200, 200,
                   -1, 220, -1, 220, 240, 240, -1, 200, 260, 260, 150, 280, 280,
                   -1, 300, 300, 300, -1, 320, 200, -1, -1, 350, 350, -1, 400]

    mortgage_value = [-1, 30, -1, 30, 40, -1, 100, 50, 50, -1,
                       75, 50, 60, -1, -1, 70, 70, 75, 70, 80,
                       100, 90, -1, 90, 100, 100, -1, 110, -1, 110,
                       120, 120, -1, 100, 130, 130, 75, 140, 140, -1,
                       150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
                       -1, 200]

    rent_value = [-1, 2, -1, 4, 5, -1, 25, 6, 6, -1,
                   400, 6, 8, -1, -1, 10, 10, 400, 10, 12,
                   25, 14, -1, 14, 16, 16, -1, 18, -1, 28,
                   20, 20, -1, 25, 22, 22, 400, 24, 24, -1,
                   26, 26, 26, -1, 28, 25, -1, -1, 35, 35,
                   -1, 50]

    upgrade_cost = [-1, 50, -1, 50, 50, -1, 100, 50, 50, -1,
                    -1, 50, 50, -1, -1, 100, 100, -1, 100, 100,
                    100, 100, -1, 100, 100, 150, -1, 150, -1, 150,
                    150, 150, -1, 100, 150, 150, -1, 140, 140, -1,
                    150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
                    -1, 200]

    rent_value_1 = [-1, 10, -1, 20, 30, -1, 50, 30, 30, -1,
                    100000, 30, 40, -1, -1, 50, 50, 100000, 50, 60,
                    50, 70, -1, 70, 80, 80, -1, 100, -1, 100,
                    100, 100, -1, 50, 110, 110, 100000, 120, 120, -1,
                    130, 130, 130, -1, 150, 50, -1, -1, 175, 175,
                    -1, 200]

    rent_value_2 = [-1, 30, -1, 60, 80, -1, 100, 90, 90, -1,
                    200000, 90, 100, -1, -1, 150, 150, 200000, 150, 180,
                    100, 200, -1, 200, 220, 220, -1, 90, -1, 90,
                    100, 100, -1, 100, 330, 330, 200000, 360, 360, -1,
                    390, 390, 390, -1, 450, 100, -1, -1, 500, 500,
                    -1, 600]

    rent_value_3 = [-1, 90, -1, 180, 240, -1, 200, 270, 270, -1,
                    -1, 270, 300, -1, -1, 450, 450, -1, 450, 500,
                    200, 550, -1, 550, 600, 600, -1, 700, -1, 700,
                    750, 750, -1, 200, 800, 800, -1, 850, 850, -1,
                    900, 900, 900, -1, 1000, 200, -1, -1, 1100, 1100,
                    -1, 1400]

    rent_value_4 = [-1, 160, -1, 320, 360, -1, -1, 400, 400, -1,
                    -1, 400, 450, -1, -1, 625, 625, -1, 625, 700,
                    -1, 750, -1, 750, 800, 800, -1, 875, -1, 875,
                    925, 925, -1, -1, 975, 975, -1, 1025, 1125, -1,
                    1100, 1100, 1100, -1, 1200, -1, -1, -1, 1300, 1300,
                    -1, 1700]

    rent_value_H = [-1, 250, -1, 450, 450, -1, -1, 550, 550, -1,
               -1, 550, 600, -1, -1, 750, 750, -1, 750, 900,
               -1, 950, -1, 950, 1000, 1000, -1, 1050, -1, 1050,
               1100, 1100, -1, -1, 1150, 1150, -1, 1200, 1200, -1,
               1275, 1275, 1275, -1, 1400, -1, -1, -1, 1500, 1500,
               -1, 2000]

    rent_value_S = [-1, 750, -1, 950, 950, -1, -1, 1050, 1050, -1,
               -1, 1050, 1100, -1, -1, 1250, 1250, -1, 1250, 1400,
               -1, 1450, -1, 1450, 1500, 1500, -1, 2050, -1, 2050,
               2100, 2100, -1, -1, 2150, 2150, -1, 2200, 2200, -1,
               2275, 2275, 2275, -1, 2400, -1, -1, -1, 2500, 2500,
               -1, 3000]

    owner = []
    totalOnSide = [9,10,10,8]

    for i in range(len(face_values)):
        if face_values[i] > 0:
            owner.append(-1)
        else:
            owner.append(-2)

    maxTurns = 1600

    location = [0,0,0,0]
    money = [starting_cash for i in range(4)]
    busticket = [0,0,0,0]
    inJail = [False, False, False, False]
    stayInJail = [0,0,0,0]

    player = random.randint(0, 3)
    turn = 0
    nConsecutiveDoubles = 0

    bankrupt = []  # Order in which players have gone bankrupt

    numberOwned = [{},{},{},{}]
    for i in range(4):
        for group in ['PE', 'LB', 'DB', 'OE', 'RD', 'YW', 'GN', 'PK', 'RR', 'UY']:
            numberOwned[i][group] = 0

    upgradeLevel = [0 for i in range(len(face_values))]
    ownedProperties = [[],[],[],[]]

    all_bought = 0
    turning_point = -1

    while turn <= maxTurns:

        turning_point = turn
        if (not all_bought) and (len(ownedProperties[0]) + len(ownedProperties[1]) + len(ownedProperties[2]) + len(ownedProperties[3])) >= 37:
            all_bought = 1
            turning_point = turn

        #print player
        #print "\t", money[player]
        #print "\tBus ticket owned = ", busticket[player]
        #print "\tCash at hand = ", money[player]
        #print "\tIs player in Jail ", inJail[player]
        #print "\tOld location", square_names[location[player]]

        fromSquare = location[player]

        # If there is only one unbankrupted player, end the game
        if len(bankrupt) == 3:
            #print "\tOnly one player remains.  Done!"
            break

        # If the player has no money, continue to next player
        if money[player] <= 0:
            #print "\tPlayer is bankrupt.  Skipping."
            nConsecutiveDoubles = 0
            player = (player + 1) % 4
            continue

        justOutOfJail = False
        # If the player is in jail, the player strategies to pay out and has enough cash to bail make them pay to get out
        if square_type[location[player]] == 'JL' and inJail[player] and stayInJail[player] == 0 and money[player] >= bail_cash + min_cash:
            #print "\tPaying to get out of jail", player
            money[player] -= bail_cash
            inJail[player] = False
            justOutOfJail = True

        roll = 0

        # If the player is in jail and the player strategies to stay, roll the die for double
        if square_type[location[player]] == 'JL' and inJail[player] and stayInJail[player] > 0:

            # Roll two die and go to just visiting if doubles
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)

            #print "\tRolled", die1, die2

            if die1 == die2:
                #print "\tDoubles rolled so getting out of jail"
                inJail[player] = False
                justOutOfJail = True
                roll = die1 + die2
                location[player] = (location[player] + roll) % no_of_squares
                stayInJail[player] = 0
            else:
                #print "\tDoubles not rolled so staying in jail"
                stayInJail[player] += 1
                nConsecutiveDoubles = 0
                player = (player + 1) % 4
                turn += 1
                continue

            # If no doubles till the 3rd turn, payout
            if stayInJail[player] == 4:

                # If player does not have money to pay bail, the player is bankrupt
                if money[player] < bail_cash:
                    #print "\tPlayer in jail and cannot pay bail so bankrupt"
                    for i in range(len(owner)):
                        if owner[i] == player:
                            owner[i] = -1
                            upgradeLevel[i] = 0
                    bankrupt.append(player)
                    stayInJail[player] = 0
                    nConsecutiveDoubles = 0
                    player = (player + 1) % 4
                    turn += 1
                    continue

                else:
                    #print "\tPlayer in jail and paying bail on failure to roll doubles"
                    money[player] -= bail_cash
                    inJail[player] = False
                    justOutOfJail = True
                    stayInJail[player] = 0

        # Variables required for Bus Ticket rule
        side = location[player] / 13
        lower = side * 13
        upper = (side + 1) * 13

        ownedOnSide = 0
        for i in range(lower, upper):
            if owner[i] >= 0:
                ownedOnSide += 1

        busTicketUsed = False

        # If player just got out of jail, cannot use Bus Ticket
        if not justOutOfJail:

            sideSkipped = False

            # If there is unowned property on the player's side and player has bus tickets
            #  use bus ticket to move player to the unowned square
            if ownedOnSide < totalOnSide[side] and busticket[player] > 0 and side > 1:

                buyables = []
                buyingScore = []
                for i in range(location[player] + 1, upper):
                    if owner[i] == -1:
                        buyables.append(i)
                        buyingScore.append(numberOwned[player][square_type[i]])

                buyables = [y for (x, y) in sorted(zip(buyingScore, buyables), reverse = True)]
                buyingScore = [x for (x, y) in sorted(zip(buyingScore, buyables), reverse = True)]

                if len(buyables) > 0:

                    # Move player to the square group which the player already owns
                    if buyingScore[0] > 0:
                        location[player] = buyables[0]

                    # If no color groups are owned, choose square based on the player values
                    else:
                        max = -9999
                        maxIx = -3
                        for ix in buyables:
                            if playerValues[player][square_type[ix]] > max:
                                max = playerValues[player][square_type[ix]]
                                maxIx = ix
                        location[player] = maxIx

                    location[player] = buyables[0]
                    busticket[player] -= 1
                    busTicketUsed = True
                    #print "\tBusticket used to go to an unowned property ", square_names[location[player]]


            # If all the properties on the side (only 3rd and 4rth) of the board are owned and player has bus tickets
            # jump to the corner square
            elif ownedOnSide == totalOnSide[side] and busticket[player] > 0 and side > 1:

                if side == 3 and location[player] % 13 > 10:
                    # Do nothing
                    location[player] = location[player]
                else:
                    #print player, "at position", square_names[location[player]]
                    #print "\t", "owner vector = ", owner[lower:upper], "side =", side
                    busticket[player] -= 1
                    busTicketUsed = True
                    sideSkipped = True
                    location[player] = ((side + 1) * 13) % no_of_squares
                    #print "\tBusticket used to skip the ", side, " side to", square_names[location[player]]

            # If Bus Ticket used on the 3rd side to Go to Jail, use the Stay In Jail strategy
            if busTicketUsed and sideSkipped and side == 2:
                stayInJail[player] = 1
                #print "\tBusticket used to skip 3rd side so using Stay in Jail strategy"


            # If Bus Ticket is not used, roll the die and advance player
            isDoubles = False
            if not busTicketUsed:

                # Roll dice three times at random
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                die3 = random.randint(1, 6)
                #print "\tRolled", die1, die2, die3

                # Mr. Monopoly?
                if (die3 == 4) or (die3 == 5):
                    isMrMonopoly = True
                    die3 = 0

                # Bus Ticket?
                if die3 == 6:
                    #print "\tPlayer ", player," received a Bus Ticket (6 for die 3 is BT)."
                    if random.random() < 1.0 / 14 or sum(busticket) == 13:
                        busticket = [0, 0, 0, 0]

                    busticket[player] += 1
                    die3 = 0

                # Doubles?
                if die1 == die2 and die1 != die3:
                    #print "\tDoubles rolled"
                    isDoubles = True

                # Triples?
                if die1 == die2 == die3:
                    isTriples = True

                # Moves forward is the sum of three die
                roll = die1 + die2 + die3

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

                # Advance current player based on dice roll
                location[player] = (location[player] + roll) % no_of_squares
                #print "\tAdvancing based on dice roll to ", square_names[location[player]]

        # If the player passes GO, award $200
        if fromSquare + roll >= no_of_squares:
            #print "\t$200 for passing GO"
            money[player] += 200

        square = location[player]

        # If the player lands on Bus Ticket square, give a bus ticket
        if square_type[square] == 'BT':
            #print "\tPlayer received a Bus Ticket on landing on Bus Ticket square"
            busticket[player] += 1

        # If the player lands on go to jail, go to jail
        if square_type[square] == 'GJ':
            #print "\tGoing to JAIL from GO TO JAIL"
            location[player] = JAIL
            inJail[player] = True
            nConsecutiveDoubles = 0
            player = (player + 1) % 4
            turn += 1
            continue

        # If the player lands on community chest cards or chance cards
        if square_type[square] == 'CC' or square_type[square] == 'CE':

            rand = random.random()

            # GO TO JAIL card
            if rand < 1.0 / 16:
                #print "\tWent to JAIL from chance or community chest"
                location[player] = JAIL
                inJail[player] = True

            # ADVANCE TO GO card - player collects 200
            if rand >= 1.0 / 16 and rand < 2.0 / 16:
                #print "\tAdvanced to GO from chance or community chest"
                location[player] = 0
                money[player] += 200

            # Additional rules of CHANCE cards that move the player
            if square_type[square] == 'CE':

                # Advance to properties
                if rand >= 2.0 / 16 and rand < 7.0 / 16:
                    transition = [6, 16, 30, 51, 0][random.randint(0, 4)]
                    location[player] = transition
                    #print "\tAdvancing due to property Chance card to ", square_names[location[player]]

                # Advance to nearest utility
                if rand >= 7.0 / 16 and rand < 8.0 / 16:

                    if location[player] == 9 or location[player] == 46:
                        location[player] = 10
                    elif location[player] == 28:
                        location[player] = 36
                    #print "\tAdvancing due to Nearest Utility Chance card to ", square_names[location[player]]

                # Two cards to Advance to the nearest railroad
                if rand >= 8.0 / 16 and rand < 10.0 / 16:

                    if location[player] == 9:
                        location[player] = 20
                    elif location[player] == 28:
                        location[player] = 33
                    elif location[player] == 46:
                        location[player] = 6
                    #print "\tAdvancing due to Nearest Railroad Chance card to ", square_names[location[player]]

                # Move back three spaces
                if rand >= 10.0 / 16 and rand < 11.0/16:

                    location[player] -= 3
                    #print "\tMoving 3 spaces back for Chance card to ", square_names[location[player]]

        square = location[player]
        #print "\tNew final location", square_names[location[player]],"for owner", owner[location[player]]

        # If the player lands on an owned property, pay rent
        if owner[square] > -1 and owner[square] != player:

            #print "\tPaying rent to player", owner[square]

            payee = owner[square]
            group = square_type[square]

            # Calculate required rent for Utility
            if group == 'UY':
                if numberOwned[payee][group] == 1:
                    rent = 4 * roll
                elif numberOwned[payee][group] == 2:
                    rent = 10 * roll
                elif numberOwned[payee][group] == 3:
                    rent = 20 * roll

            # Calculate required rent for Railroad
            if group == 'RR':

                if numberOwned[payee][group] == 1:
                    rent = rent_value[square]
                elif numberOwned[payee][group] == 2:
                    rent = rent_value_1[square]
                elif numberOwned[payee][group] == 3:
                    rent = rent_value_2[square]
                elif numberOwned[payee][group] == 4:
                    rent = rent_value_3[square]

                # If a railroad is upgraded, rent is doubled
                if upgradeLevel[square] == 1:
                    rent = rent * 2


            # Calculating required rent for unimproved properties
            if (group == 'DB' or group == 'PE') and upgradeLevel[square] == 0:

                if numberOwned[payee][group] < 2:
                    rent = rent_value[square]
                elif numberOwned[payee][group] == 2:
                    rent = 2 * rent_value[square]
                elif numberOwned[payee][group] == 3:
                    rent = 3 * rent_value[square]

            if (group in ['LB', 'PK', 'OE', 'RD', 'YW', 'GN']) and upgradeLevel[square] == 0:

                if numberOwned[payee][group] < 3:
                    rent = rent_value[square]
                elif numberOwned[payee][group] == 3:
                    rent = 2 * rent_value[square]
                elif numberOwned[payee][group] == 4:
                    rent = 3 * rent_value[square]

            # Calculating rent for upgraded properties
            if (group in ['PE', 'LB', 'DB', 'OE', 'RD', 'YW', 'GN', 'PK']) and upgradeLevel[square] > 0:

                if upgradeLevel[square] == 1:
                    rent = rent_value_1[square]
                elif upgradeLevel[square] == 2:
                    rent = rent_value_2[square]
                elif upgradeLevel[square] == 3:
                    rent = rent_value_3[square]
                elif upgradeLevel[square] == 4:
                    rent = rent_value_4[square]
                elif upgradeLevel[square] == 5:
                    rent = rent_value_H[square]
                elif upgradeLevel[square] == 6:
                    rent = rent_value_S[square]

            #print "\tRent =", rent
            #print "\t", square_names[square], group
            #print "\tNumbers owned: ", numberOwned[payee][group], "Upgrade Level: ", upgradeLevel[square]

            # If the player can't pay rent, they are out of the game
            if money[player] < rent:
                #print "\tBankrupt from paying rent"
                for i in range(len(owner)):
                    if owner[i] == player:
                        owner[i] = -1
                        upgradeLevel[i] = 0

                money[player] -= rent
                bankrupt.append(player)
                nConsecutiveDoubles = 0
                player = (player + 1) % 4
                turn += 1
                continue
            else:
                #print "\tRent paid = ", rent
                money[player] -= rent
                money[owner[square]] += rent

        # If the player lands on an unowned property, decide to purchase it or not
        if owner[square] == -1 and face_values[square] > 0:

            #print "\tProperty is unowned"
            group = square_type[square]

            if busTicketUsed and money[player] - face_values[square] > min_cash:
                #print "\tPuchasing property ", square_names[square], " for ", face_values[square]
                owner[square] = player
                money[player] -= face_values[square]
                numberOwned[player][group] += 1
                ownedProperties[player].append(square)

            # Purchase the property if its face value is less than perceived value and purchasing won't go below minimum cash
            elif random.random() < playerValues[player][group] and money[player] - face_values[square] > min_cash:
                #print "\tPuchasing property ", square_names[square], " for ", face_values[square]
                owner[square] = player
                money[player] -= face_values[square]
                numberOwned[player][group] += 1
                ownedProperties[player].append(square)

        #--- Property upgrades

        makingUpgrades = True
        while (makingUpgrades and money[player] > min_cash):

            upgradeable = []
            importance = []

            # Identify all properties that could be upgraded in a list
            for prop in range(len(ownedProperties[player])):
                i = ownedProperties[player][prop]

                group = square_type[i]

                # Skip unupgradable properties
                if group not in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR']:
                    continue

                if not owner[i] == player:
                    continue

                # Need at least 2 of a property group to make improvements for DB and PE
                if (group == 'DB' or group == 'PE') and numberOwned[player][group] < 2:
                    continue

                # Need at least 3 of a property group to make improvements for DB and PE
                if (group in ['LB', 'PK', 'OE', 'RD', 'YW', 'GN']) and numberOwned[player][group] < 3:
                    continue

                # If a Train Depot is built, cannot upgrade further
                # Railroads can be upgraded even if one is owned
                if group == 'RR' and upgradeLevel[i] == 1:
                    continue

                # Other color group can be upgraded to sky scrapers
                if upgradeLevel[i] == 6:
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

            propertyToUpgrade = -3
            for i in range(len(sortedImportances)):
                cumSum += sortedImportances[i]
                if target < cumSum:
                    propertyToUpgrade = sortedUpgradeable[i]

            # Upgrade the property
            money[player] -= upgrade_cost[propertyToUpgrade]
            upgradeLevel[propertyToUpgrade] += 1

            # print "Upgrading ", square_names[propertyToUpgrade], "of color group", square_type[propertyToUpgrade]
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

    return points, turning_point


def testAgainstRandom(p):

    #state = random.getstate()
    #random.seed(0)

    score = 0
    for iter in range(100):
        population = []
        nIndividuals = 3
        for n in range(nIndividuals):

            newIndividual = {}
            for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY',
                      'PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:
                #newIndividual[i] = random.random()

                # For Aggresive tournament opponents
                newIndividual[i] = 1.0

                #if random.random() > .5:
                #    newIndividual[i] = random.random() * .20
                #else:
                #    newIndividual[i] = random.random() * .20 + .80

            population.append(newIndividual)

        points, turning_point = playGame(p, population[0], population[1], population[2])
        score += points[0]

        turning_points.append(turning_point)

    #random.setstate(state)
    return score


def findRandomMember(fitness):

    totalFitness = sum(fitness)
    target = totalFitness * random.random()

    cumFitness = 0
    for i in range(len(fitness)):
        cumFitness += fitness[i]

        if target < cumFitness:
            return i

def findMeanAndMedian(player):

    scores = []
    for i in range(21):
        scores.append(testAgainstRandom(player))

    scores = sorted(scores)

    #print scores
    return sum(scores)/len(scores), scores[11]

def runGeneticAlgorithm():

    # Initialize the starting population
    population = []
    nIndividuals = 1000
    for n in range(nIndividuals):
        newIndividual = {}
        for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY',
                  'PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:

            #Generate probabilistic property value randomly
            if random.random() > .5:
                newIndividual[i] = random.random() * .20
            else:
                newIndividual[i] = random.random() * .20 + .80

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
            #print i, fitness[i]
            if i % 100 == 0:
                print i, fitness[i]

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
        print "(Mean, Median) = ", findMeanAndMedian(population[0])
        print "Average Turning Point = ",sum(turning_points)/len(turning_points)
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

            newIndividual1 = {}
            newIndividual2 = {}

            #Split

            '''
            keys = population[0].keys()
            split = random.randint(0,len(keys))

            for i in range(split):
                newIndividual1[keys[i]] = firstIndividual[keys[i]]
                newIndividual2[keys[i]] = secondIndividual[keys[i]]

            for i in range(split, len(keys)):
                newIndividual1[keys[i]] = secondIndividual[keys[i]]
                newIndividual2[keys[i]] = firstIndividual[keys[i]]
            '''

            count = 0
            r = random.randint(0,9)
            for i in ['PE', 'LB', 'PK', 'OE', 'RD', 'YW', 'GN', 'DB', 'RR', 'UY']:
                if count <= r:
                    newIndividual1[i] = firstIndividual[i]
                    newIndividual2[i] = secondIndividual[i]
                else:
                    newIndividual1[i] = secondIndividual[i]
                    newIndividual2[i] = firstIndividual[i]
                count += 1

            r = random.randint(10,19)
            for i in ['PE_up', 'LB_up', 'PK_up', 'OE_up', 'RD_up', 'YW_up', 'GN_up', 'DB_up', 'RR_up', 'UY_up']:
                if count <= r:
                    newIndividual1[i] = firstIndividual[i]
                    newIndividual2[i] = secondIndividual[i]
                else:
                    newIndividual1[i] = secondIndividual[i]
                    newIndividual2[i] = firstIndividual[i]
                count += 1

            #print len(newIndividual1) == len(newIndividual2) == len(firstIndividual) == len(secondIndividual)

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


#--- Main
turning_points = []
runGeneticAlgorithm()

