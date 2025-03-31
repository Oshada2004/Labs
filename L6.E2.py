#L6.E2

#Dictionary wich stores the count of people of particular year
yearCount = {} 


#performs the calculation related to last 3 digits
def subOrder(year):
    yearCount[year] = yearCount.get(year, 0) + 1
    return yearCount[year]


#performs the calculation related to the 3 digits after 1st four digits
def calculateDayCount(year, month, day):
    monthlyDays = [31, 29 if year % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(monthlyDays[:month - 1]) + day


#returns the last 6 digits of the NIC after formatting
def calculateNic(year, month, day, gender):
    totalDays = calculateDayCount(year, month, day)
    numGroup2 = str(500 + totalDays) if gender == 'F' else f'{totalDays:03d}'
    numGroup3 = f'{subOrder(year):03d}'
    return numGroup2, numGroup3


#opens the files of input and output
with open('inputFile.txt', 'r') as inputFile, open('outputFile.txt', 'w') as outputFile:

    #iterates for all lines in input file
    for line in inputFile:
        name, bday, gender = line.split()
        year, month, day = map(int, bday.split('-'))
        grp2, grp3 = calculateNic(year, month, day, gender)
        #print NIC to the output file 
        outputFile.write(f'{name} {year}{grp2}{grp3}\n')
