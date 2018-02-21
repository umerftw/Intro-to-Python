#!/usr/bin/env python

"""""
The purpose of this script is to analyze a given book.
The user can find the number of total words and number of unique words in the book.

Please take no offense to the outputted sentence.
"""""

# Print a sentence using format with the total number of words and the unique number of words (hint: use a set)
words = []
for line in open('land_time_forgot.txt'):
    line = line.strip()
    words.extend(line.split(" "))

words_set = set(words)
print('This book has {} total words and {} unique words.'.format(len(words), len(words_set)))

# Calculate the word frequency using the word list, the word set, and a for loop with list.count and store it in a
# dictionary (hint: don't forget to use float)
word_dict = {}
for word in words:
    if word in words_set:
        word_dict[word] = float(words.count(word))

# Calculate the word with the maximum frequency (hint: use max)
word_max = max(word_dict, key=word_dict.get)
print('The word that shows up most frequently in this book: "{}"'.format(word_max))

# Get the minimum frequency (hint: use values)
min_freq = float(min(word_dict.values()))

# Store all of the words that have the minimum frequency in a list (hint: use a for loop and items)
min_freq_words = []
for word, count in word_dict.items():
    if count == min_freq:
        min_freq_words.append(word)

# Print a sentence of the minimum frequency and the number of words with that frequency
print('The minimum number of times a word appears in the book is {}. There are {} words with that frequency.'
      .format(min_freq, len(min_freq_words)))

# Print a sentence of the percentage of words that are unique in the book (hint: use :.1f in your format)
num_unique_words = len(words_set)
num_words = len(words)
percentage = (num_unique_words / num_words) * 100
print('The percentage of unique words in the book: %.1f' % percentage)
