# Function that takes 2 strings and determines if they're 1 or 0 edits away (Add, Delete, Replace)
def oneAway(str1, str2):
  # Base case: Return False if length arent equal or there is a length difference larger than 1
  if len(str1) != len(str2) and abs(len(str1) - len(str2)) != 1:
    return False

  # First case, equal length strings. Must be replace or exactly the same strings.
  if len(str1) == len(str2):
    replacedOnce = False
    for i in range(len(str1)):
      # If character at index not equal, it is replaced at least once.
      if str1[i] != str2[i]:
        if replacedOnce != True:
          replacedOnce = True
        else:
          return False
  else:
    # Second case, unequal strings by exactly 1 character.
    # Set min and max string
    minStr = str1 if len(str1) < len(str2) else str2
    maxStr = str2 if len(str1) < len(str2) else str1
    addOne = False

    # Loop through lower string.
    for i in range(len(minStr)):
      # Increment to check against next index for larger string when they don't match
      if addOne != True:
        if minStr[i] != maxStr[i]:
          addOne = True
      else:
        if minStr[i] != maxStr[i + 1]:
          return False

  return True

response = "Is one away" if oneAway("abe", "ab") else "Is NOT one away"
print(response)

# Time Complexity: 