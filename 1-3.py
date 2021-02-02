# Write function that replaces all spaces in a string with %20
def replace(str):
    print("Replacing all spaces with %20 in: '{}'".format(str))

    # Base case

    # Declare empty string for result
    result = ""

    # Loop through string
    for c in str:
        # Check for spaces
        if " " in c:
            result += "%20"
        else:
            result += c
    return result

print(replace("this is a string"))

# Time Complexity: O(N)