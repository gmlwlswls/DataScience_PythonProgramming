# 3. Print Stars

# Make a function that print stars as below.

# (1) `star_flag(n)` (n is a positive number)

# (2) `star_Z(n) (n>2)`


# 1-1.
def star_flag(n) :
  for i in range(2*n - 1) :
    if i < n :
      print('*' * (i+1))
    else :
      print('*' * (2*n -1 - i))

star_flag(3)
print()
star_flag(5)

# 1-2.
def star_Z(n) : #(n>2)
  print('*' * n)
  for i in range(n - 2) :
    print(' ' * (n - 2 - i), '*')
  print('*' * n)

star_z(4)
star_z(5)
    