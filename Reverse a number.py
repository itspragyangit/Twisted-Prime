  
def reverse_int(new_num):
  new_num_rev = 0
  # print(type(new_num))
  while (new_num > 0):
    a = new_num % 10
    new_num_rev = new_num_rev*10 + a
    new_num = new_num // 10
  return new_num_rev
reverse_int(56)
