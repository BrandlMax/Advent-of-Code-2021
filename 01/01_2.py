# READ FILE
with open('input.txt') as f:
    input = f.readlines()
inputINTUngrouped = [int(numeric_string) for numeric_string in input]

# Group
inputINT = []
i = 0
while i < len(inputINTUngrouped):
    if i + 2 < len(inputINTUngrouped):
        inputINT.append(inputINTUngrouped[i] +
                        inputINTUngrouped[i+1] + inputINTUngrouped[i+2])
    i += 1

# Count Increase
increaseCount = 0
prevNumber = inputINT[0]
for x in inputINT:
    if prevNumber < x:
        increaseCount = increaseCount + 1
    prevNumber = x
print("RESULT")
print(increaseCount)
