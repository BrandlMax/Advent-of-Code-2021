# READ FILE
with open('input.txt') as f:
    input = f.readlines()

# INPUT AS NUMBERS
inputINT = [int(numeric_string) for numeric_string in input]
print(inputINT)

# Count Increase
increaseCount = 0
prevNumber = inputINT[0]
for x in inputINT:
    if prevNumber < x:
        increaseCount = increaseCount + 1
        prevNumber = x
    else:
        prevNumber = x
print(increaseCount)
