"""------Lab_3------"""

# Task 1
l = [i**2 for i in range(1, 11)]
print(l)

# Task 2
def squares(start, end):
    return [i**2 for i in range(start, end+1)]

print(squares(1, 10))

# Task 3
class SquareGenerator:
    def squares(start, end):
        return [i ** 2 for i in range(start, end + 1)]

print(SquareGenerator.squares(1, 10))

# Task 4
import math

l1 = squares(1, 10)
l2 = []

for num in l1:
    l2.append(math.sqrt(num))

print(l2)

