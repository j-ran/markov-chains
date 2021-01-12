"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open the file
    # read the entire contents
    contents = open(file_path).read()

    return contents

#print(open_and_read_file('green-eggs.txt'))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """


    chains = {}
 
    # take the out put from the pre. func. (prob don't need)
    # split the words 
    words = text_string.split()
    # loop through the words
        # make tuples in our empty dict.
        
    # looping over every two word pair in the text
    for i in range(len(words) - 1):
        key = (words[i], words[i + 1])
        value = words[i + 2]

#at this moment, having an Index Error at line 57
#just an idea: while (i + 1) is < range(len(words) - 1)

        #if key is in dictionary already, 
        if key not in chains:
            chains[key] = []
        # add value to existing key
        chains[key].append(value)    

#    print(chains)

print(make_chains('green-eggs.txt'))



def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)



#question: do we need to close the  text file?
#    contents.close(file_path)