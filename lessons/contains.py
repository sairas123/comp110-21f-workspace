"""Example of writing a function to process a list."""

# Define a function
# Name 'contains'
# Two prameters (needle (str), haystack (list[str]))
# Return True if needle is found in the haystack
# Move through each item in list until needle is found
        # Use a counter variable to process each index of the loop
        # one-by-one
 # As soon as needle is found return True
    #If all items have been checked, return False

def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in the haystack, False otherwise."""
    # Move through each item in list until needle is found
    i: int = 0 
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    
    return False

    
def main() -> None:
    """Entrypoint of program."""
    names: list[str]= ["Kris", "Kaki"]
    print(contains("Kevin", names))


if __name__ == "__main__":
    main ()