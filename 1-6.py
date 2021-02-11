# Function that compresses a string "aabcccccaaa" becomes "a2b1c5a3", if converted
def compressString(str):
  # Inits
  result = ""
  lastChar = str[0]
  count = 1

  # Loop through string
  for i, c in enumerate(str):
    # Base case is skip first letter
    if i != 0:
      # Check if current character is equal to the last character, increment count.
      if c == lastChar:
        count += 1
      # Else, add last character and count to result, reset
      else:
        result += f"{lastChar}{count}"
        lastChar = c
        count = 1

  # Add to final result
  result += f"{lastChar}{count}"
  return result if len(result) < len(str) else str

response = compressString("aabcccccaaa")
print(f"Response of compressString is: {response}")

# Time Complexity: O(N)