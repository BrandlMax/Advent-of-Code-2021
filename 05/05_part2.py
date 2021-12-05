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
categorizedVectors = []

for vector in vectors:
    isHorizontal = vector[0][0] == vector[1][0]
    isVertical = vector[0][1] == vector[1][1]
    if isHorizontal:
        vector.append("isHorizontal")
        categorizedVectors.append(vector)
    elif isVertical:
        vector.append("isVertical")
        categorizedVectors.append(vector)
    else:
        vector.append("isDiagonal")
        categorizedVectors.append(vector)


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
    else:
        x1 = vector[0][0]
        y1 = vector[0][1]
        x2 = vector[1][0]
        y2 = vector[1][1]

        xDir = 1
        if x1 > x2:
            xDir = -1

        i = 0
        if y1 < y2:
            while y1 + i <= y2:
                # print("({}|{})".format(x1+i*xDir, y1+i))
                choordSystem.append("({}|{})".format(x1+i*xDir, y1+i))
                i += 1
        else:
            while y1 - i >= y2:
                # print("({}|{})".format(x1+i*xDir, y1-i))
                choordSystem.append("({}|{})".format(x1+i*xDir, y1-i))
                i += 1

    return choordSystem


# drawLines in choordSystem
choordSystem = []
for vector in categorizedVectors:
    choordSystem = drawLine(choordSystem, vector)

# Count Intersections
intersections = 0
for amount in Counter(choordSystem).values():
    if amount > 1:
        intersections += 1

print("RESULT")
print(intersections)
