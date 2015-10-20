with open("Stats/optimization_stats.txt", "r") as fs1:

    with open("Stats/optimization_stats.csv", "w") as fs2:

        fs2.write("Generation, Best Fitness, Purple, Light Blue, Pink, Orange, Red, Yellow, Green, Dark Blue, Railroad, Utility, Purple Upgrade, Light Blue Upgrade, Pink Upgrade, Orange Upgrade, Red Upgrade, Yellow Upgrade, Green Upgrade, Dark Blue Upgrade, Railroad Upgrade, Utility Upgrade, Mean Fitness, Median Fitness \n")
        count = 1
        line_no = 0
        for line in fs1:
            line_no = count%25
            if line_no == 1:
                line_array = line.split(" = ")
                fs2.write(line_array[1].strip())
                fs2.write(",")
            elif line_no == 2:
                line_array = line.split(" = ")
                fs2.write(line_array[1].strip())
                fs2.write(",")
            elif line_no > 2 and line_no < 23:
                line_array = line.split(" ")
                fs2.write(line_array[1].strip())
                fs2.write(",")
            elif line_no == 24:
                line = line.replace("(","")
                line = line.replace(")","")
                line = line.replace("=",",")
                line = line.replace(" ","")
                line_array = line.split(",")
                fs2.write(line_array[2].strip())
                fs2.write(",")
                fs2.write(line_array[3].strip())
                fs2.write("\n")
            count = count + 1

    fs2.close()
fs1.close()