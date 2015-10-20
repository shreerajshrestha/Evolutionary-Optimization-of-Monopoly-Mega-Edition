# Average rent paid per turn for Bus Ticket followed by a Dice Roll

import Simulation
import datetime

N = 1000000
fname = datetime.datetime.now().strftime("BusTicketAndDiceRollAnalysis %I:%M:%S %p on %B %d, %Y")

with open(fname,'a') as out:
    out.write("Average rents paid for Bus Ticket followed by a Dice Roll on %r iterations\n"%(N))
    out.write(datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y"))
    out.write("\n\n")
out.close()

average_for_position = []

for i in range(Simulation.no_of_squares):

    start_position = i
    rents_list = []

    # If on GO TO JAIL, set rents to zero and continue
    if i == 39:
        with open(fname,'a') as out:
            out.write("%s - %r\n" % (Simulation.square_names[i], 0))
        out.close()
        continue

    # For all other squares, do N iterations of DB
    for n in range(N):

        pos = start_position
        landed_squares = []
        rents_paid = []

        # Code for Bus Ticket move to corner square

        # print "Starting position = ", Simulation.square_names[pos]
        moves_forward = 13 - (pos % 13)

        square_ix = (pos + moves_forward) % Simulation.no_of_squares
        square_name = Simulation.square_names[(pos + moves_forward) % Simulation.no_of_squares]
        square_type = Simulation.square_type[square_ix]

        if square_type == 'RR':
            rent = Simulation.rent_value_3[square_ix]

        elif square_type == 'UY':
            rent = Simulation.rent_value_2[square_ix] / 10000 * moves_forward

        else:
            rent = Simulation.rent_value_S[square_ix]

        if rent < 0:
            rent = 0

        landed_squares.append(square_name)

        if square_type == 'GJ':
            rents_paid.append(0)
            pos = -1

        else:
            rents_paid.append(rent)
            pos = (pos + moves_forward) % Simulation.no_of_squares

        # print moves_forward
        # print "Rent paid = ", rent
        # print "Current position = ", Simulation.square_names[pos], "\n"

        # Code for dice roll

        # If not IN JAIL, do a normal move
        if pos != -1:

            # print "Starting position = ", Simulation.square_names[pos]
            doubles, triples, mr_monopoly, bus_ticket, moves_forward = Simulation.roll_dice()

            square_ix = (pos + moves_forward) % Simulation.no_of_squares
            square_name = Simulation.square_names[(pos + moves_forward) % Simulation.no_of_squares]
            square_type = Simulation.square_type[square_ix]

            if square_type == 'RR':
                rent = Simulation.rent_value_3[square_ix]

            elif square_type == 'UY':
                rent = Simulation.rent_value_2[square_ix] / 10000 * moves_forward

            else:
                rent = Simulation.rent_value_S[square_ix]

            if rent < 0:
                rent = 0

            landed_squares.append(square_name)
            rents_paid.append(rent)

            pos = (pos + moves_forward) % Simulation.no_of_squares

            # print doubles, triples, mr_monopoly, bus_ticket, moves_forward
            # print "Rent paid = ", rent
            # print "Current position = ", Simulation.square_names[pos], "\n"

            if mr_monopoly:

                ix = pos
                moves_forward = 0
                found = 0

                while not found:

                    moves_forward += 1
                    ix = (ix + 1) % Simulation.no_of_squares

                    if Simulation.face_values[ix] > 0:
                        found = 1

                # print "Starting position = ", Simulation.square_names[pos]

                square_ix = (pos + moves_forward) % Simulation.no_of_squares
                square_name = Simulation.square_names[(pos + moves_forward) % Simulation.no_of_squares]
                square_type = Simulation.square_type[square_ix]

                if square_type == 'RR':
                    rent = Simulation.rent_value_3[square_ix]

                elif square_type == 'UY':
                    rent = Simulation.rent_value_2[square_ix] / 10000 * moves_forward

                else:
                    rent = Simulation.rent_value_S[square_ix]

                if rent < 0:
                    rent = 0

                landed_squares.append(square_name)
                rents_paid.append(rent)

                pos = (pos + moves_forward) % Simulation.no_of_squares

                # print "Mr. Monopoly"
                # print "Rent paid = ", rent
                # print "Current position = ", Simulation.square_names[pos], '\n'
                # If IN JAIL, stay IN JAIL if doubles are not rolled

        else:
            # print "Starting position = ", Simulation.square_names[pos]

            doubles, triples, mr_monopoly, bus_ticket, moves_forward = Simulation.roll_dice()

            if doubles:
                landed_squares.append("Just Visiting")
                rents_paid.append(0)
                pos = 13
            else:
                landed_squares.append("In Jail")
                rents_paid.append(0)
                pos = -1

        # print landed_squares
        # print rents_paid

        this_avg = sum(rents_paid)
        rents_list.append(this_avg)
        # print this_avg, '\n'

        # avg = sum(rents_list)/float(len(rents_list))
        # print avg

    avg = sum(rents_list)/float(len(rents_list))
    average_for_position.append(avg)
    # print avg

    with open(fname,'a') as out:
        out.write("%s - %r\n" % (Simulation.square_names[i], avg))
    out.close()

with open(fname,'a') as out:
    out.write("\nDump as list:\n")
    out.write("%r" % average_for_position)
out.close()

# for p in range(Simulation.no_of_squares):
#    print Simulation.square_names[p], Simulation.rent_value_S[p]




