def isUnique(str):
  # Create empty set
  charSet = set()

  # Loop through str
  for c in str:
    # Check if char in set
    if c in charSet:
      return False
    else:
      charSet.add(c)
  return True
  
unique = "String is unique" if isUnique("abc") else "String is not unique"
print(unique)

# Time Complexity: O(N)