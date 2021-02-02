def isPermutation(str1, str2):
  # Base case
  if len(str1) != len(str2) or not str1 or not str2:
    return False
  
  # Sort strings
  sort1 = "".join(sorted(str1))
  sort2 = "".join(sorted(str2))

  # Compare strings
  if sort1 != sort2:
    return False

  return True

response = "Yes, they are permutations" if isPermutation("cba", "cba") else "No, they are not permutations"
print(response)

# Creates dictionary
def dictionary(str):
  dict = {}
  for c in str:
    if c in dict:
      dict[c] += 1
    else:
      dict[c] = 1
      
  return dict



def isPermutation2(str1, str2):
  # Base case
  if len(str1) != len(str2) or not str1 or not str2:
    return False

  # Add to dictionary
  dict = dictionary(str1)

  for c in str2:
    if c in dict and dict[c] > 0:
      dict[c] -= 1
    else:
      return False
  return True
    
response2 = "Yes, they are permutations" if isPermutation2("cca", "bcc") else "No, they are not permutations"
print(response2)