matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

flat = [n for row in matrix for n in row]
# flat2 = [n for n in row for row in matrix] # doesn't work

print(flat)

