def is_pangram(s):

    # First of all we will convert our sentence in a sentence with each letter in lower case, it will be simpler
    s = s.lower()

    # Later we generate a list with all letters in the alphabet, in this case we use a range between the
    # letter 'a' and the letter 'z' that previously we converted in an ASCII value with 'ord()'
    # in order to be able to convert it into a character again.
    alph = [chr(i) for i in range(
        ord('a'), ord('z')+1)]

    # Here we start to apply the conditionals.

    # In the first case we improve the time execution if we apply the lenght conditional because if
    # the sentence contains less letters than alphabet it's obvious the return will be 'False'.
    if len(s) < len(alph):

        return False

    # In this second condition, first we generate a list where we eliminate the characters which are not letters
    # and we only obtain the letters. Later we check if 'alph' is a subset of the other list thus proving
    # the sentence contains at least one time each letter from the alphabet.
    elif set(alph) <= set([i for i in s if i.isalpha() == True]):

        return True

    # The rest will be 'False'.
    else:

        return False
