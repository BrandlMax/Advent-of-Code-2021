from collections import Counter
# READ FILE
with open('input.txt') as f:
    input = f.read().splitlines()

# Format Vectors -> vectors
vectorsStrings = []
for vector in input:
    vectorsStrings.append(vector.split(" -> "))

vectors = []
for vector in vectorsStrings:
    choordsArray = []
    for choords in vector:
        choordsArray.append(map(int, choords.split(",")))
    vectors.append(choordsArray)

# Only consider horizontal and vertical lines
horizontalAndVerticalVectors = []

for vector in vectors:
    isHorizontal = vector[0][0] == vector[1][0]
    isVertical = vector[0][1] == vector[1][1]
    if isHorizontal:
        vector.append("isHorizontal")
        horizontalAndVerticalVectors.append(vector)
    elif isVertical:
        vector.append("isVertical")
        horizontalAndVerticalVectors.append(vector)

# Check Overlapping


def drawLine(choordSystem, vector):
    # print(vector)
    if vector[2] == "isHorizontal":
        start = vector[0][1] if vector[0][1] < vector[1][1] else vector[1][1]
        end = vector[0][1] if vector[0][1] > vector[1][1] else vector[1][1]
        for yChoords in range(start, end+1):
            # print("({}|{})".format(vector[0][0], yChoords))
            choordSystem.append("({}|{})".format(vector[0][0], yChoords))

    elif vector[2] == "isVertical":
        start = vector[0][0] if vector[0][0] < vector[1][0] else vector[1][0]
        end = vector[0][0] if vector[0][0] > vector[1][0] else vector[1][0]
        for xChoords in range(start, end+1):
            # print("({}|{})".format(xChoords, vector[0][1]))
            choordSystem.append("({}|{})".format(xChoords, vector[0][1]))

    return choordSystem


# drawLines in choordSystem
choordSystem = []
for vector in horizontalAndVerticalVectors:
    choordSystem = drawLine(choordSystem, vector)

# Count Intersections
intersections = 0
for amount in Counter(choordSystem).values():
    if amount > 1:
        intersections += 1

print("RESULT")
print(intersections)
