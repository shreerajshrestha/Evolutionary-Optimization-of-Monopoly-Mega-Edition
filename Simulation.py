
# NOTE: In real game, player can deal in credit with other player
# In this analysis, we assume that players can only do transaction in cash
# Following this assumption, once a player is bankrupt, since he can not
# owe any other player any amount

import random
import numpy
import datetime

# Variable game parameters that can be set along with setters
############################################################
# Default properties are 4 players and 500 turns
no_of_players = 0
no_of_turns = 0
score_chart = []

# Function to set no_of_players
def set_players(num):

    global no_of_players, player_position, player_cash

    if num> 1 and num <= 8:
        no_of_players = num

        # Setting default player properties
        player_position = [0 for i in range(no_of_players)] # -1 for IN JAIL, -2 for BANKRUPT
        player_cash = [starting_cash for i in range(no_of_players)]

    else:
        print 'ERROR: 1 < no_of_players <= 8'
        print  'Value not changed and is ', no_of_players

# Function to set no_of_turns
def set_turns(num):

    global no_of_turns

    if num >= no_of_players:
        no_of_turns = num
    else:
        print 'no_of_turns < no_of_players'
        print  'Value not changed and is ', no_of_turns



# Static game properties that do not change throughout the game
####################################################################
no_of_squares = 52
starting_cash = 2500
min_cash = 200
bail_cash = 50
luxury_tax = 75
default_income_tax = 200
go_cash = 200

square_names = ['GO', 'Mediterranean Avenue', 'Community Chest', 'Baltic Avenue', 'Arctic Avenue',
                'Income Tax', 'Reading Railroad', 'Massachusetts Avenue', 'Oriental Avenue', 'Chance',
                'Gas Company', 'Vermont Avenue', 'Connecticut Avenue', 'Jail', 'Auction', 'Maryland Avenue',
                'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenue',
                'Pennsylvania Railroad', 'St. James Place', 'Community Chest', 'Tennessee Avenue',
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

upgrade_cost = [-1, 50, -1, 50, 50, -1, 100, 50, 50, -1,
                -1, 50, 50, -1, -1, 100, 100, -1, 100, 100,
                100, 100, 100, 100, 100, 150, -1, 150, -1, 150,
                150, 150, -1, 100, 150, 150, -1, 140, 140, -1,
                150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
                -1, 200]

rent_value = [-1, 2, -1, 4, 5, -1, 25, 6, 6, -1,
               40000, 6, 8, -1, -1, 10, 10, 40000, 10, 12,
               25, 14, 14, -1, 16, 16, -1, 90, -1, 90,
               20, 20, -1, 25, 22, 22, 40000, 24, 24, -1,
               26, 26, 26, -1, 28, 25, -1, -1, 35, 35,
               -1, 50]

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

rent_value_H = [-1, 250, -1, 450, 450, -1, -1, 550, 550, -1,
               -1, 550, 600, -1, -1, 750, 750, -1, 750, 900,
               -1, 950, 950, -1, 1000, 1000, -1, 1050, -1, 1050,
               1100, 1100, -1, -1, 1150, 1150, -1, 1200, 1200, -1,
               1275, 1275, 1275, -1, 1400, -1, -1, -1, 1500, 1500,
               -1, 2000]

rent_value_S = [-1, 750, -1, 950, 950, -1, -1, 1050, 1050, -1,
               -1, 1050, 1100, -1, -1, 1250, 1250, -1, 1250, 1400,
               -1, 1450, -1, 1450, 1500, 1500, -1, 2050, -1, 2050,
               2100, 2100, -1, -1, 2150, 2150, -1, 2200, 2200, -1,
               2275, 2275, 2275, -1, 2400, -1, -1, -1, 2500, 2500,
               -1, 3000]

mortgage_value = [-1, 30, -1, 30, 40, -1, 100, 50, 50, -1,
               75, 50, 60, -1, -1, 70, 70, 75, 70, 80,
               100, 90, -1, 90, 100, 100, -1, 110, -1, 110,
               120, 120, -1, 100, 130, 130, 75, 140, 140, -1,
               150, 150, 150, -1, 160, 100, -1, -1, 175, 175,
               -1, 200]


# for chance_cards > 10000, value represents the index of destination square
# -30000 represents go back three spaces
# integer value < 10000 represents the amount of money to pay or being paid
# String values represent special cards
community_chest_cards = [-150, 100, 520000, '+50P', 10, -50, 25, 100, 45, 100, 200, 20, 'GJ', -100, 'OJ', 'REP']
chance_cards = ['REP', 'OJ', 510000, 50, 150, '-50P', 60000, -15, 520000, -30000, 'GJ', 160000, 300000, 'A2U', 'A2R', 'A2R']



# Player behaviors along with their setters
################################################
# Default behaviors include player prefers to pay out of jail and
# Pays $200 income tax
# NOTE ----------------------
# Still to factor dependence on opponent's owned properties for paying out of JAIL
# And calculating total assets for income tax
# This includes: Total cash on hand, printed price of unmortgaged properties,
# mortgage value of mortgaged properties, and printed prices of buildings owned.
# A player must decide their option before adding up their total assets.
pay_out_of_jail = 1
pay_default_income_tax = 1

# Function to set pay_out_of_jail
def set_pay_out_of_jail(bool):

    global pay_out_of_jail

    if bool == 0  or bool == 1:
        pay_out_of_jail = bool

# Function to set pay_default_income_tax
def set_pay_default_income_tax(bool):
    global pay_default_income_tax

    if bool == 0  or bool == 1:
        pay_default_income_tax = bool



# Player properties
###########################################
player_position = []
player_cash = []
player_oj_card = []
square_owner = []



# Function that returns one random perceived value for the property
# @parameter        none
# @return           a list containing perceived values for each square on the board
def generate_random_perceived_value_for(square_ix):

    if face_values[square_ix] > 0:

        # Perceived value is within 0 to 4 times the face value
        # NOTE ###############################################################################################################
        # Should be normal distribution centered at face value
        return random.randint(face_values[square_ix] * 0, face_values[square_ix] * 4)

    else:
        return face_values[square_ix]



# Function that returns a random list of perceived values
# @parameter        none
# @return           a list containing perceived values for each square on the board
def generate_perceived_value_vector():

    global no_of_squares, face_values

    perceived_value_vector = []

    for i in range(no_of_squares):

        if face_values[i] > 0:

            # Perceived value is within 0 to 4 times the face value
            # NOTE #########################################################################################################
            # Should be normal distribution centered at face value
            perceived_value_vector.append(random.randint(face_values[i] * 0, face_values[i] * 4))

        else:
            perceived_value_vector.append(face_values[i])

    return perceived_value_vector

# Function that randomizes the COMMUNITY CHEST and CHANCE cards
# @parameter        seed value for random number generator
def randomize(seed_val):

    global community_chest_cards, chance_cards

    random.seed(seed_val)

    # Randomizing the community chest cards
    temp_ix = []
    temp_list = []
    while len(temp_ix) < len(community_chest_cards):
        ix = random.randint(0, 15)
        if ix not in temp_ix:
            temp_ix.append(ix)
    temp_list = []
    for i in range(len(community_chest_cards)):
        temp_list.append(community_chest_cards[temp_ix[i]])
    community_chest_cards = temp_list

    # Randomizing the chance cards
    temp_ix = []
    temp_list = []
    while len(temp_ix) < len(chance_cards):
        ix = random.randint(0, 15)
        if ix not in temp_ix:
            temp_ix.append(ix)
    for i in range(len(chance_cards)):
        temp_list.append(chance_cards[temp_ix[i]])
    chance_cards = temp_list



# Function that prints the board
# @parameter        none
# @return           print string
def print_board():

    global no_of_squares, square_names, square_type, face_values, rent_value, mortgage_value

    for i in range(no_of_squares):
        print i, ',',square_names[i], ',',square_type[i], ',', face_values[i], ',', rent_value[i], ',', mortgage_value[i]


# Function that prints the board
# @parameter        list of scores, perceived value vector, count of iteration
# @return           none
def print_board_with_val(scores, perceived_values, iteration):

    global no_of_squares, square_names

    print 'Iteration ', iteration, '\n\n', 'Scores: ', '\n', scores, '\n\n', 'Mean: ', numpy.mean(scores), '\n',\
        'Median: ', numpy.median(scores), '\n', 'Minimum: ', min(scores), '\n', 'Maximum: ', max(scores), '\n'

    for i in range(no_of_squares):
        print i, ',',square_names[i], ',',perceived_values[i]

    print '\n'



# Function that prints the board on to a file
# @parameter        list of scores, perceived value vector, count of iteration
# @return           none
def print_board_with_val_to_file(scores, perceived_values, iteration):

    global no_of_squares, square_names

    fname = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

    with open(fname,'a') as out:

        out.write("Iteration %r\n\nScores:\n%r\n\nMean:%r\nMedian:%r\nMinimum:%r\nMaximum:%r\n\n" % \
                  (iteration, scores, numpy.mean(scores), numpy.median(scores), min(scores), max(scores)))

        out.write("Alpha sample:\n")
        for i in range(no_of_squares):
            out.write("%r, %s, %r \n" % (i,square_names[i],perceived_values[i]))

        out.write("\n")
        out.close()


# Function that process the roll for a player
# @parameter        none
# @return           doubles, triples, mr_monopoly, bus_ticket, moves_forward
def roll_dice():

    doubles, triples, mr_monopoly, bus_ticket, moves_forward = 0, 0, 0, 0, 0

    # Roll dice three times at random
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)

    # Mr. Monopoly?
    if (die3 == 4) or (die3 == 5):
        mr_monopoly = 1
        die3 = 0

    # Bus Ticket?
    if die3 == 6:
        bus_ticket = 1
        die3 = 0

    # Doubles?
    if (die1 == die2) or (die2 == die3) or (die3 == die1):
        doubles = 1

    # Triples?
    if (die1 == die2 == die3):
        triples = 1

    # Moves forward is the sum of three die
    moves_forward = die1 + die2 + die3

    return doubles, triples, mr_monopoly, bus_ticket, moves_forward




# Function that initializes the score chart
# @parameter number of players in the match
# @return none
def initialize_score_chart():

    global score_chart, no_of_players

    # Score chart is varied exponentially to the power of 2, and starting at 0
    # NOTE ####################################################################################################################
    # Score chart needs to be updated to support higher number of players in matches
    # If player in match is 8, the range of score is too high

    for i in range(no_of_players):
        score = pow(2, no_of_players - i - 2)
        if score < 1: score = 0
        score_chart.append(score)

    '''
    # Code to check if the scoring system is working properly
    print 'Score Chart: ', score_chart
    print 'Player Cash: ', player_cash
    print 'Rank: ', rank
    print 'Score: ', score
    '''


# Function that returns the rank of the players
# @parameter        a list of perceived_values
# @parameter        number of players in a match
# @parameter        maximum number of turns per players in a match
# @return           rank of players in the match
def play_match(perceived_values, players_in_match, turns_in_match):

    global no_of_squares, starting_cash, min_cash, bail_cash, luxury_tax, default_income_tax, go_cash
    global player_position, player_cash, square_owner
    global pay_out_of_jail, pay_default_income_tax
    global score_chart

    # Setting variable game parameters
    set_players(players_in_match)
    set_turns(turns_in_match)

    # Some validation routines to make sure the size of perceived values is the same as
    # the number of players in the match
    if len(perceived_values) != no_of_players:
        return 'The perceived values must contain as many lists as the number of players.'

    # Also make sure that all the perceived values have size equal to the number of squares on the board
    for i in range(len(perceived_values)):
        if len(perceived_values[i]) != no_of_squares:
            return 'The lists in perceived values must be equal in length to the no of squares on the board.'

    # Loop control variables
    count_turn = 0
    count_doubles = 0
    count_in_jail = 0
    playing = 0


    # Setting default player properties
    player_position = [0 for i in range(no_of_players)] # -1 for IN JAIL, -2 for BANKRUPT
    player_cash = [starting_cash for i in range(no_of_players)]
    player_oj_card = [0 for i in range(no_of_players)]

    # -2 for properties of bankrupt
    # -1 for not owned
    # and if owned player no. of the owner who owns it, i.e 0, 1, 2 ... no_of_players
    square_owner = [-1 for i in range(no_of_squares)]


    # Main Program loop
    while count_turn < no_of_turns * no_of_players:

        from_chance = 0

        # If player is bankrupt, skip
        if player_position[playing] == -2:
            playing = (playing + 1) % no_of_players
            count_turn += 1
            count_doubles = 0
            continue

        # If the player has negative money,
        # Declare bankrupt and seize all properties if not yet done
        # Skip the player's roll
        if player_cash[playing] < 0:

            # Send player to BANKRUPT position and set cash to negative
            # such that the negative value represents the rank in ascending order
            player_position[playing] = -2
            player_cash[playing] = 0
            player_cash[playing] = min(player_cash) - 1

            # Seize all the properties that the player owns
            # and set it as unowned
            # NOTE ################################################################################################################
            # When mortgaging and Auction is implemented the value should be set to -2, i.e Bank
            for i in range(no_of_squares):
                if square_owner[i] == playing:
                    square_owner[i] = -1

            playing = (playing + 1) % no_of_players
            count_turn += 1
            count_doubles = 0
            continue

        # Roll the dice
        doubles, triples, mr_monopoly, bus_ticket, moves_forward = roll_dice()

        # If the player is IN JAIL
        if player_position[playing] == -1:

            # Player prefers and can afford to bail out
            if pay_out_of_jail and player_cash[playing] > bail_cash + min_cash:

                player_cash[playing] -= 50
                player_position[playing] = 13
                count_in_jail = 0

                # Increment the turn and current player
                playing = (playing + 1) % no_of_players
                count_turn += 1
                count_doubles = 0
                continue

            # If the player prefers to roll the dice instead
            else:

                # If doubles rolled, from JAIL to JUST VISITING
                if doubles:
                    count_in_jail = 0
                    player_position[playing] = 13

                # If doubles not rolled
                elif doubles != 1:
                    count_in_jail += 1

                    # If third time double not rolled, pay out of jail
                    if count_in_jail >= 3:
                        player_cash[playing] -= 50
                        player_position[playing] = 13
                        count_in_jail = 0

                    # Else increment the turn and current player
                    else:
                        playing = (playing + 1) % no_of_players
                        count_turn += 1
                        count_doubles = 0
                        continue

            # Doubles on coming out of jail are ignored
            count_doubles = 0
            doubles = 0

        # Increment double count if doubles are rolled
        count_doubles += doubles

        # If three doubles are rolled consecutively send the player to JAIL square
        # advance the player and turn, then break
        if count_doubles >= 3:
            player_position[playing] = -1
            playing = (playing + 1) % no_of_players
            count_turn += 1
            count_doubles = 0
            continue

        # NOTE ###################################################################################################################
        # These cases will be handled later on
        if triples:
            moves_forward = moves_forward
        elif mr_monopoly:
            moves_forward = moves_forward
        elif bus_ticket:
            moves_forward = moves_forward

        # Calculate the destination square
        destination_square = (player_position[playing] + moves_forward) % no_of_squares

        # It is important to deal with rules that make the player change his position first
        # Since transactions do not occur until the player's is stationary
        #
        # We deal with Chance square first and Community Chest square second because
        # One of the Chance card can lead the player to Community Chest square
        # And for the fact that these squares can potentially move the player to another square


        # Dealing with CHANCE squares
        if square_type[destination_square] == 'CE':

            from_chance = 1
            ix = random.randint(0, len(chance_cards) - 1)

            # If chance card is an integer
            if isinstance(chance_cards[ix], int):

                # GO BACK THREE SPACES
                if chance_cards[ix] == -30000:
                    if destination_square - 3 >= 0:
                        destination_square -= 3
                        moves_forward -= 3
                    else:
                        destination_square = (destination_square - 3 + no_of_squares) % no_of_squares
                        moves_forward -= 3

                # Cards that move the player to a specific position
                elif chance_cards[ix] >= 10000:

                    new_destination_square = chance_cards[ix]/10000

                    # If the new destination is ahead current destination
                    if new_destination_square >= destination_square:
                        moves_forward += (new_destination_square - destination_square)
                    # If the new destination is behind current destination
                    else:
                        moves_forward += (new_destination_square - destination_square + no_of_squares)
                    destination_square = new_destination_square % no_of_squares

                # For cards that deal with cash
                else:
                    player_cash[playing] += chance_cards[ix]

            # If chance card is a string
            else:

                # ADVANCE TO NEAREST RAILROAD STATION
                if chance_cards[ix] == 'A2R':

                    new_destination_square = 0
                    if destination_square == 9:
                        new_destination_square = 20
                    elif destination_square == 28:
                        new_destination_square = 33
                    elif destination_square == 46:
                        new_destination_square = 6

                    # If the new destination is ahead current destination
                    if new_destination_square >= destination_square:
                        moves_forward += (new_destination_square - destination_square)
                    # If the new destination is behind current destination
                    else:
                        moves_forward += (new_destination_square - destination_square + no_of_squares)
                    destination_square = new_destination_square % no_of_squares

                # ADVANCE TO NEAREST UTILITY
                elif chance_cards[ix] == 'A2U':

                    new_destination_square = 0
                    if destination_square == 9 or destination_square == 46:
                        new_destination_square = 10
                    elif destination_square == 28:
                        new_destination_square = 36

                    # If the new destination is ahead current destination
                    if new_destination_square >= destination_square:
                        moves_forward += (new_destination_square - destination_square)
                    # If the new destination is behind current destination
                    else:
                        moves_forward += (new_destination_square - destination_square + no_of_squares)
                    destination_square = new_destination_square % no_of_squares

                # ELECTED CHAIRMAN card, pay $50 to each player
                elif chance_cards[ix] == '-50P':
                    for i in range(no_of_players):
                        if i != playing and player_position[i] != -2:
                            player_cash[playing] -= 50
                            player_cash[i] += 50

                # MAKE GENERAL REPAIRS CARD
                # NOTE ##########################################################################################################
                # Still to implement the repairs for hotel, skyscrapers, and train depots
                elif chance_cards[ix] == 'REP':
                    paying_factor = 0
                    for i in range(len(square_owner)):
                        if square_owner[i] == playing:
                            paying_factor += 1
                    player_cash[playing] -= paying_factor * 25

                # GET OUT OF JAIL FREE CARD
                # NOTE ############################################################################################################
                # Still to implement the rules for using this card
                elif chance_cards[ix] == 'OJ':
                    player_oj_card[playing] += 1

                # GO DIRECTLY TO JAIL Card
                elif chance_cards[ix] == 'GJ':
                    player_position[playing] = -1
                    playing = (playing + 1) % no_of_players
                    count_turn += 1
                    count_doubles = 0
                    continue

        # Dealing with COOMMUNITY CHEST squares
        if square_type[destination_square] == 'CC':

            ix = random.randint(0, len(community_chest_cards) - 1)

            # If the community chest card is an integer
            if isinstance(community_chest_cards[ix], int):

                # Cards that move the player to a specific position
                if community_chest_cards[ix] >= 10000:

                    new_destination_square = community_chest_cards[ix]/10000

                    # If the new destination is ahead current destination
                    if new_destination_square >= destination_square:
                        moves_forward += (new_destination_square - destination_square)
                    # If the new destination is behind current destination
                    else:
                        moves_forward += (new_destination_square - destination_square + no_of_squares)
                    destination_square = new_destination_square % no_of_squares

                # For cards that deal with cash
                else:
                    player_cash[playing] += community_chest_cards[ix]

            # If the community chest card is a string
            else:

                # MAKE GENERAL REPAIRS CARD
                # NOTE ##########################################################################################################
                # Still to implement the repairs for hotel, skyscrapers, and train depots
                if community_chest_cards[ix] == 'REP':
                    paying_factor = 0
                    for i in range(len(square_owner)):
                        if square_owner[i] == playing:
                            paying_factor += 1
                    player_cash[playing] -= paying_factor * 40

                # GRAND OPERA OPENING card, collect $50 from each player
                elif community_chest_cards[ix] == '+50P':
                    for i in range(no_of_players):
                        if i != playing and player_position[i] != -2:
                            player_cash[playing] += 50
                            player_cash[i] -= 50

                # GET OUT OF JAIL FREE CARD
                # NOTE ############################################################################################################
                # Still to implement the rules for using this card
                elif community_chest_cards[ix] == 'OJ':
                    player_oj_card[playing] += 1

                # GO DIRECTLY TO JAIL Card
                elif community_chest_cards[ix] == 'GJ':
                    player_position[playing] = -1
                    playing = (playing + 1) % no_of_players
                    count_turn += 1
                    count_doubles = 0
                    continue


        # If GO TO JAIL square, send player to JAIL
        elif square_type[destination_square] == 'GJ':
            player_position[playing] = -1
            playing = (playing + 1) % no_of_players
            count_turn += 1
            count_doubles = 0
            continue

        # If player did not end up IN JAIL
        # and will pass by the GO square, give $200 to the player
        if player_position >= 0 and player_position[playing] + moves_forward >= no_of_squares:
            count_crossed_go = (player_position[playing] + moves_forward) / no_of_squares
            player_cash[playing] += go_cash * count_crossed_go

        # Move the player to the destination square
        if player_position >= 0:
            player_position[playing] = destination_square

        # NOTE:
        # After dealing with "moving" rules, we now process financial transactions
        # This might get tricky once we include the rules for triples, Mr. Monopoly and Bus Ticket

        # Dealing with Luxury Tax
        if square_type[destination_square] == 'LT':

            if pay_default_income_tax:
                player_cash[playing] -= luxury_tax
            else:
                print "Calculate total asset and pay"


        # Dealing with purchasing unowned properties
        elif (square_owner[destination_square] == -1
            and face_values[destination_square] > 0
            and perceived_values[playing][destination_square] >= face_values[destination_square]
            and player_cash[playing] >= face_values[destination_square] + min_cash):

            player_cash[playing] -= face_values[destination_square]
            square_owner[destination_square] = playing

        # Dealing with paying rent
        elif (square_owner[destination_square] >= 0
            and face_values[destination_square] > 0
            and square_owner[destination_square] != playing):

            owner = square_owner[destination_square]

            # Calculate rent to be paid
            # For UTILITY, rent is 400 percent the sum of dice roll
            rent_amount = 0
            if square_type[destination_square] == 'UY':
                rent_amount = rent_value[destination_square]
            else:
                rent_amount = rent_value[destination_square] * moves_forward / 10000

            # If here from Chance card
            if from_chance:
                # Pay double rent for Railroad
                if square_type[destination_square] == 'RR':
                    rent_amount = rent_value[destination_square] * 2

                #Pay 10 times of a random throw of dice
                elif square_type[destination_square] == 'UY':
                    doubles, triples, mr_monopoly, bus_ticket, amount_thrown = roll_dice()
                    rent_amount = amount_thrown * 10

            # Deducting cash from player
            cash_in_hand = player_cash[playing]
            player_cash[playing] -= rent_amount

            # If the player ends up with negative cash, he is bankrupt
            # and cannot pay the owner of the square in cash, so rent = 0
            #
            '''NOTE ------------------------------------
            # For now, transfer all property of the bankrupt to the bank and mark them unowned
            # But once mortgaging, upgrades and houses are taken into account
            # Player has the option to use these to generate cash'''
            if player_cash[playing] < 0:
                ''' Skipped this section since properties of bankrupt player are marked unowned, i.e -1 above
                for i in range(no_of_squares):
                    if square_owner[i] == playing:
                        square_owner[i] = -2
                '''
                player_cash[playing] = -9999
                player_cash[owner] += cash_in_hand
            else:
                player_cash[owner] += rent_amount

        # Increment turn count and player number if no doubles rolled
        # If not, increment double count
        if not doubles:
            playing = (playing + 1) % no_of_players
            count_turn += 1
            count_doubles = 0

    sorted_player_cash = sorted(player_cash)
    rank = [no_of_players - sorted_player_cash.index(player_cash[k]) for k in range(len(player_cash))]
    score = [score_chart[rank[k] - 1] for k in range(len(rank))]

    return score, rank

# print_board()