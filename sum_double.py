def sum_double(a, b):
  
  #stores the sum in a local variable
  sum = a + b
  #double it if a and b are the same number and returns the sum
  if a == b:
    sum = sum * 2
    return sum
  
  # a + b if a and b are different numbers and retuns the sum
  if a != b:
    sum = a + b
    return sum
