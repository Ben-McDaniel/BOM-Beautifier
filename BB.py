import os
import sys

def beautify(inputPath):
    inputFile = open(inputPath, 'r')
    data = inputFile.readlines()
    parsed_data = []
    component_types = set()

    for line in data:
        parsed_data.append(line.split('|'))
    
    for line in parsed_data:
        this_type = line[4]
        component_types.add(''.join([char for char in line[4] if char.isalpha()]))


    for component in component_types:
        outputFile = open(component+".csv", "w")
        outputFile.write("Part Number, Ref Des\n")

        #identify all entries that are type component
        for line in parsed_data:
            if component == ''.join([char for char in line[4] if char.isalpha()]):
                #calculate which ref des numbers the entry contains
                rds = ''.join([char for char in line[4] if not char.isalpha()]).split(',')
                allNums = []
                for numRange in rds:
                    if '-' in numRange:
                        bothNums = numRange.split('-')
                        for i in range(int(bothNums[0]), int(bothNums[1]) + 1):
                            allNums.append(i)
                    else: 
                        allNums.append(int(numRange))

                #write that part number, ref des
                for num in allNums:
                    outputFile.write(line[1] + "," + str(component) + str(num) + "\n")

        outputFile.close()

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] is None:
        print("You must give an input file")
        sys.exit()
    beautify(sys.argv[1])

    