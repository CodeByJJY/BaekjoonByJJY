# Squares  # 6887

tiles = int(input())
length = 1

while (length**2) <= tiles:
    length += 1

print(f"The largest square has side length {length-1}.")