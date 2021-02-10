# Write function that determines if a string a palindrome off of any permutation
def palinPerm(str):
  # Create empty set
  charSet = set()

  # Loop through string, if character does not exist in set, add it. If it does, remove it.
  for c in str:
    if c not in charSet:
      charSet.add(c)
    else:
      charSet.remove(c)

  # The final set should either have 1 element or none
  return len(charSet) == 1 or len(charSet) == 0


response = "It is a palinPerm" if palinPerm("dadadad") else "No, not a palinPerm"
print(response)

# Time Complexity: O(N)