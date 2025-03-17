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

    return(ex_word_list)

def count_frequencies(word_list):
    dictionary = {

    }
    words = word_list

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary