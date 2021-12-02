# READ FILE
with open('input.txt') as f:
    input = f.read().splitlines()

horizontal = 0
depth = 0

for command in input:
    if "forward" in command:
        horizontal = horizontal + int(command[-1])
    elif "up" in command:
        depth = depth - int(command[-1])
    elif "down" in command:
        depth = depth + int(command[-1])

print("RESULT")
print(horizontal*depth)
