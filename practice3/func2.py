def myfunc(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(myfunc(1, 2, 3))
print(myfunc(10, 20, 30, 40))
print(myfunc(5))