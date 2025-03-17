###########################################################
###   Copy and paste your word frequency code here      ###
###   into two new functions:                           ###
###      text_to_word_list()                            ###
###      count_frequencies()                            ###
###   OR add your word frequency code to thie repo as   ###
###   a separate file and import it                     ###
###########################################################
import frequency
# remove these if you are going to import your frequency module
# def text_to_word_list():
#   pass

# def count_frequencies():
#   pass

word_list = frequency.text_to_wordlist('sample.txt')
word_freq_dict = frequency.count_frequencies(word_list)
###########################################################
###   Write your new functions here:                    ###
###      find_max_valued_key()                          ###
###########################################################

def find_max_valued_key(dict):
   max = 0
   word = ''
   for key in dict:
      if dict[key] > max:
        max = dict[key]
        word = key
        dict[key] = 0
   return[word ,max ]

###########################################################
###   Write your loop to find the top                   ###
###   five most frequent words                          ###
###########################################################

for i in range(5):
   biggest = (find_max_valued_key(word_freq_dict))
   print(f"{biggest[0]} appears {biggest[1]} times.")
   word_freq_dict.pop(biggest[0])



