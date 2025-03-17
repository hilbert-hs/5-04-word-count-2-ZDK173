def text_to_wordlist(filename):
    # read the text from filename into a string
    with open(filename) as f:
        example_paragraph = f.read()

    # make all letters lowercase
    ex_par_lowered = example_paragraph.lower()

    #remove all periods (you'll want to repeat this for any other punctuation in your paragraph)
    ex_par_lower_no_punc = ex_par_lowered.replace(".", "").replace(",", "")

    # convert the paragraph into a list of individual strings
    ex_word_list = ex_par_lower_no_punc.split(" ")

def count_frequencies(lst):
    words = {}

    for word in lst:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words


