# READ FILE
with open('test.txt') as f:
    input = f.readlines()

# INPUT AS NUMBERS
inputINTUngrouped = [int(numeric_string) for numeric_string in input]

print(len(inputINTUngrouped))
print(len(inputINTUngrouped) - len(inputINTUngrouped) % 3)
