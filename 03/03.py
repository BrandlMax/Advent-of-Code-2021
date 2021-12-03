import numpy as np
# READ FILE
with open('input.txt') as f:
    input = f.read().splitlines()

bitSum = np.zeros(len(input[0]), dtype=int)
gammaRate = np.zeros(len(input[0]), dtype=int)
epsilonRate = np.zeros(len(input[0]), dtype=int)

# COUNT BITSUM
for reportLine in input:
    i = 0
    while i < len(bitSum):
        bitSum[i] = bitSum[i] + int(reportLine[i])
        i += 1

# GET GAMMA & EPSILON
i = 0
while i < len(bitSum):
    if bitSum[i] > len(input) / 2:
        gammaRate[i] = 1
        epsilonRate[i] = 0
    else:
        gammaRate[i] = 0
        epsilonRate[i] = 1
    i += 1

# BIN TO DEC
gammaRate = int("".join(str(bit) for bit in gammaRate), 2)
epsilonRate = int("".join(str(bit) for bit in epsilonRate), 2)

print("RESULT")
print(gammaRate * epsilonRate)
