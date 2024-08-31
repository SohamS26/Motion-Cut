import os

def count_words(text):
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The text to count words from.
    
    Returns:
        int: The number of words in the text.
    """
    # Split text by spaces to extract words
    words = text.split()
    return len(words)

def get_input():
    """
    Prompt the user to input a sentence or paragraph.
    
    Returns:
        str: The user input text.
    """
    while True:
        print("\n" + "=" * 50)
        text = input("Enter a sentence or paragraph: ").strip()
        print("=" * 50)
        
        if text:
            return text
        else:
            print("\n[ERROR] Input cannot be empty. Please try again.")

def display_result(word_count):
    """
    Display the word count result in a formatted manner.
    
    Args:
        word_count (int): The number of words in the input text.
    """
    print("\n" + "=" * 50)
    print(f"The number of words in the given text is: {word_count}")
    print("=" * 50)

def clear_screen():
    """
    Clear the console screen for better readability.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """
    The main function to run the Word Counter program.
    """
    clear_screen()
    print("=" * 50)
    print("Welcome to the Word Counter Program!".center(50))
    print("=" * 50)

    # Get input from the user
    user_text = get_input()

    # Count words in the input text
    word_count = count_words(user_text)

    # Display the result
    display_result(word_count)

    print("\nThank you for using the Word Counter Program!".center(50))
    print("=" * 50)

if __name__ == "__main__":
    main()
