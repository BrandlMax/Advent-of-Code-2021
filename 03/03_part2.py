import numpy as np
# READ FILE
with open('input.txt') as f:
    input = f.read().splitlines()


def countBitsumOfIndex(input, index):
    bitSum = np.zeros(len(input[0]), dtype=int)
    for reportLine in input:
        i = 0
        while i < len(bitSum):
            bitSum[i] = bitSum[i] + int(reportLine[i])
            i += 1

    oxygenGeneratorRatingCommon = np.zeros(len(input[0]), dtype=int)
    coTwoScrubberRatingCommon = np.zeros(len(input[0]), dtype=int)
    i = 0
    while i < len(bitSum):
        if bitSum[i] >= float(len(input)/float(2)):
            oxygenGeneratorRatingCommon[i] = 1
            coTwoScrubberRatingCommon[i] = 0
        else:
            oxygenGeneratorRatingCommon[i] = 0
            coTwoScrubberRatingCommon[i] = 1
        i += 1
    return [oxygenGeneratorRatingCommon[index], coTwoScrubberRatingCommon[index]]


def filterRatings(input, checkIndexPos, toBeValue):
    inputLine = 0
    while inputLine < len(input):
        if int(input[inputLine][checkIndexPos]) != int(toBeValue):
            input[inputLine] = ""
        inputLine += 1
    return filter(None, input)


# THE LOOP
oxygenGeneratorRating = np.array(input)
coTwoScrubberRating = np.array(input)
i = 0
while i < len(input[0]):

    if len(coTwoScrubberRating) > 1:
        coTwoScrubberRating = filterRatings(
            coTwoScrubberRating, i, countBitsumOfIndex(coTwoScrubberRating, i)[1])

    if len(oxygenGeneratorRating) > 1:
        oxygenGeneratorRating = filterRatings(
            oxygenGeneratorRating, i, countBitsumOfIndex(oxygenGeneratorRating, i)[0])

    i += 1

# BIN TO DEC
oxygenGeneratorRating = int("".join(str(bit)
                            for bit in oxygenGeneratorRating), 2)
coTwoScrubberRating = int("".join(str(bit) for bit in coTwoScrubberRating), 2)

print("RESULT")
print(oxygenGeneratorRating * coTwoScrubberRating)
