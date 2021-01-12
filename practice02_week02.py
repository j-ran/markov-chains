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
    



    for i in range(len(words) - 1):
        while (i + 1) < len(words):
            key = (words[i], words[i + 1])
            value = words[i + 2]