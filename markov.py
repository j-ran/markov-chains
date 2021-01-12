"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open the file
    # read the entire contents
    file_text = open(file_path)
    contents = file_text.read()
    file_text.close()
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

    # to set a stop point    
    words.append(None)

    # loop through the words
    # make tuples in our empty dict.
    # looping over every two word pair in the text
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        #if key is in dictionary already, 
        if key not in chains:
            chains[key] = []
        # add value to existing key
        chains[key].append(value)    

#   print(chains)
    return chains

# make_chains('green-eggs.txt')



def make_text(chains):
    """Return text from chains."""

    # Make a new key out of the second word in the first key 
    # and the random word you pulled out from the list of words that followed it.
    # Look up that new key in the dictionary, 
    # and pull a new random word out of the new list.
    # Keep doing that until your program raises a KeyError.


    
    key = choice(list(chains.keys()))
    words = [key[0], key[1]] # keys from the dict.
    word = choice(chains[key])

# make a new key from the last item of the previous key
# and stop when one of the keys is None
    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

# return the result as a string of words
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