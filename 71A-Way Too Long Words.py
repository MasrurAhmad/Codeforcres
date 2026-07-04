def abbreviate_words():
    # Read the number of words
    try:
        n = int(input())
    except EOFError:
        return
 
    for _ in range(n):
        word = input().strip()
        
        # Check if the word length is greater than 10
        if len(word) > 10:
            # Create abbreviation: first char + length of middle part + last char
            abbreviation = f"{word[0]}{len(word) - 2}{word[-1]}"
            print(abbreviation)
        else:
            # Print the original word if it's not "too long"
            print(word)
 
if __name__ == "__main__":
    abbreviate_words()