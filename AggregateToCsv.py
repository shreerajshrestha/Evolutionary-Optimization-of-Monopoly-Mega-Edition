
import Simulation

with open("Logs/aggregate.txt", "r") as fs1:

    with open("Logs/aggregate2.csv", "w") as fs2:

        for line in fs1:

            line_array = line.split(",")

            for i in range(len(line_array)):

                fs2.write("%s \n" % (line_array[i]))

        for i in range(len(Simulation.square_names)):
            fs2.write("%s \n" % Simulation.square_names[i])

    fs2.close()
fs1.close()




