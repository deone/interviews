def palindrome_chain_length(n):
    # parameter n is a positive integer
    # your function should return the number of steps
    count = 0
    if str(n) == str(n)[::-1]:
        return count
    else:
        while str(n) != str(n)[::-1]:
            n = n + int(str(n)[::-1])
            count += 1
        return count

print(palindrome_chain_length(87))

def palindrome_chain_length_2(n):
  # parameter n is a positive integer
  # your function should return the number of steps
  counter = 0
  while True:
    p = int(str(n)) + int(str(n)[::-1])
    counter += 1
    if str(p) == str(p)[::-1]:
      break
    else:
      n = p
  return counter