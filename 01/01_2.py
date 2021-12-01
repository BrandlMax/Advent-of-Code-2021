# READ FILE
with open('input.txt') as f:
    input = f.readlines()

# INPUT AS NUMBERS
inputINTUngrouped = [int(numeric_string) for numeric_string in input]
# print(inputINT)

# Group Array
inputINT = []
i = 0
while i < len(inputINTUngrouped):
    if i + 2 < len(inputINTUngrouped):
        inputINT.append(inputINTUngrouped[i] +
                        inputINTUngrouped[i+1] + inputINTUngrouped[i+2])
    i += 1

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
print("RESULT")
print(increaseCount)
