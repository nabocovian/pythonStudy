"""
This program checks if a given square matrix meets certain conditions.

The program takes an integer 'n' as input, followed by 'n' lines of space-separated integers representing the matrix elements.

The program calculates the sum of the main diagonal, the sum of the anti-diagonal, the sum of each row, and the sum of each column.
It also generates a sorted list of numbers from 1 to n^2.

Finally, the program checks if the sum of the main diagonal, the anti-diagonal, each row, and each column is equal,
and if the sorted list of matrix elements is equal to the generated list of numbers.

If all conditions are met, it prints 'YES'; otherwise, it prints 'NO'.
"""

n = int(input())  # Input the size of the matrix

mult = [[int(i) for i in input().split()] for _ in range(n)]  # Input the matrix elements

s_main = 0
s_add = 0
s_row = 0
s_cowl = 0

# Calculate the sum of the main diagonal, the anti-diagonal, each row, and each column
for i in range(n):
    for y in range(n):
        s_main += mult[i][i]
        s_add += mult[i][n - i - 1]
        s_row += mult[y][i]
        s_cowl += mult[i][y]
        break

count = 1
total = []

# Generate a list of numbers from 1 to n^2
while count != n ** 2 + 1:
    total.append(str(count))
    count += 1

total_mult = []

# Flatten the matrix into a single list
for i in range(n):
    for y in range(n):
        total_mult.append(str(mult[i][y]))
total_mult.sort()
total.sort()

# Check if all conditions are met
if (
    s_main == s_add
    and s_main == s_row
    and s_main == s_cowl
    and total_mult == total
):
    print("YES")
else:
    print("NO")
