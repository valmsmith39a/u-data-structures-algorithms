def string_reverser(our_string):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    
    # TODO: DONE: Write your solution here
    # Solution 1
    new_string = ""
    
    for i in range(len(our_string)):
        new_string += our_string[(len(our_string) - 1) - i]
    return new_string

def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    
    # TODO: DONE: Write your solution here
    return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: DONE: Write your solution here
    word_list = our_string.split(' ')
    new_list = []
    for i in word_list:
        new_list.append(i[::-1])
    
    return ' '.join(new_list)

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: DONE: Write your solution here
    if len(str1) == len(str2):
        hamming_distance = 0
        for idx in range(len(str1)):
            if str1[idx] != str2[idx]:
                hamming_distance += 1 
        return hamming_distance
    return None
    
