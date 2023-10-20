def print_upper_words(words):
    """For a list of words, print out each word on a seperate line, uppercased.
    
        >>> print_upper_words(["Everything", "Is", "Awesome"])
        EVERYTHING
        IS
        AWESOME
    """

    for word in words:
        print(word.upper())

def print_upper_words_two(words):
    """Print out each word on a seperate line and uppercase words that start with e or E.
    
        >>> print_upper_words_two(["Eclipse", "Anaconda", "echo", "baseball"])
        ECLIPSE
        ECHO
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_three(words, must_start_with):
    """Print out each word on seperate line and uppercase.  Must start with given letter
    
        >>> print_upper_words_three(["hello", "hey", "goodbye", "yo", "yes"])
        ...                     must_start_with=["h", "y"]
        HELLO
        HEY
        YO
        YES
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break