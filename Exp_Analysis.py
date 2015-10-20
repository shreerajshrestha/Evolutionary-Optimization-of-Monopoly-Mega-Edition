
import Simulation

pos = 13

count = [0 for i in range(Simulation.no_of_squares)]

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if k > 3: k = 0
            count[i+j+k] += 1

prob = [count[i]/(6.0*6*6) for i in range(len(count))]

print count
print prob
print sum(prob)
print

exp_bus = []
for i in range(pos + 1, 13 * (pos/13 + 1) + 1):

    if Simulation.rent_value_S[i % Simulation.no_of_squares] < 0:
        weight = 0
    else:
        weight = Simulation.rent_value_S[i % Simulation.no_of_squares]

    exp_bus.append(weight)

    print Simulation.square_names[i % len(Simulation.square_names)],\
        weight

min_bus = 999999
for i in range(len(exp_bus)):
    if exp_bus[i] < min_bus and exp_bus[i] > 0:
        min_bus = exp_bus[i]

print "Min Bus", min_bus
print "Max Bus", max(exp_bus)
print





exp_dice = []
for i in range(Simulation.no_of_squares):

    if Simulation.rent_value_S[(pos + i) % Simulation.no_of_squares] < 0:
        weight = 0
    else:
        weight = Simulation.rent_value_S[(pos + i) % Simulation.no_of_squares]

    exp_dice.append(prob[i] * weight)
    print Simulation.square_names[(pos + i) % Simulation.no_of_squares], prob[i] * weight

min_dice = 999999
for i in range(len(exp_dice)):
    if exp_dice[i] < min_dice and exp_dice[i] > 0:
        min_dice = exp_dice[i]

print "Expected rent paid on dice roll = ", sum(exp_dice)
