def getRatesBinary(input, gamma: str, epsilon: str):
    column = 0
    row = 0
    while column < len(input[0]):
        zeroes = 0
        ones = 0
        while row < len(input):
            if input[row][column] == "1":
                ones+=1
            else:
                zeroes+=1 
            row+=1 
        gamma += '1' if ones > zeroes else '0'
        epsilon += '1' if ones <= zeroes else '0'
        column += 1
        row = 0
    return int(gamma,2) * int(epsilon,2)

def lifeSupportRating(input):
    row = 0
    oxygenGenerator, co2Scrubber = [], []
    ones, zeroes = 0, 0
    while row < len(input):
        if input[row][0] == "1":
            ones+=1
        else:
            zeroes+=1
        row+=1
    row = 0
    while row < len(input):
        if (input[row][0] == "1" and ones > zeroes) or (input[row][0] == "0" and zeroes > ones):
            oxygenGenerator.append(input[row])
        else:
            co2Scrubber.append(input[row])
        row+=1
    return getValidRating(oxygenGenerator, "oxy", 0, 1) * getValidRating(co2Scrubber, "co2", 0, 1)        


def getValidRating(rating, ratingType, row, column):
    ratingLength = len(rating)
    validRatings = []
    if len(rating) == 1:
        return int(rating[0],2)
    ones, zeroes = 0, 0
    while row < ratingLength:
        if rating[row][column] == "1":
            ones+=1
        else:
            zeroes+=1
        row+=1
    row = 0
    if ratingType == "oxy":
        while row < ratingLength:
            if rating[row][column] == "1" and ones >= zeroes:
                validRatings.append(rating[row])
            elif rating[row][column] == "0" and zeroes > ones:
                validRatings.append(rating[row])                
            row+=1
    elif ratingType == "co2":
        while row < ratingLength:
            if rating[row][column] == "0" and ones >= zeroes:
                validRatings.append(rating[row])
            elif rating[row][column] == "1" and zeroes > ones:
                validRatings.append(rating[row])                
            row+=1 
    print(validRatings)                       
    return getValidRating(validRatings, ratingType, 0, column+ 1)             

diagReport = []

with open("input.txt") as f:
    diagReport = [line.rstrip() for line in f]

test = ["00100", 
        "11110", 
        "10110", 
        "10111", 
        "10101", 
        "01111",
        "00111", 
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"]
print(getRatesBinary(diagReport, "", ""))
print(lifeSupportRating(diagReport))