def reader(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines


def lines_to_words(list_of_lines):
        word_list = []
        for line in list_of_lines:
            word_list.extend(line.split(" "))
        return word_list


 word_set = set(word_list)
 print("There are {} words in the book and {} of them are unique".format(len(word_list), len(word_set)))

def list_to_count(word_list):
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1
    return word_freq

def min(frequency):
    min_word_freq = min(frequency.values())
    min_words = []
    for word, fr in frequency.items():
        if fr == min_word_freq:
            min_words.append(word)
    return min_word_freq, min_words

print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))

 if __name__ == '__main__':
    my_lines = reader(land_time_forgot.txt)
    my_list = lines_to_words(my_lines)
    word_set = set(word_list)
    print("There are {} words in the book and {} of them are unique".format(len(word_list), len(word_set)))

    my_freq = list_to_count(my_list)
    max_word = max(my_freq, key=my_freq.get)
    print("Most frequent word is '{}' at {} with frequency {}".format(max_word, my_freq[max_word],
                                                                           my_freq[max_word]))
    min_word = min(word_freq)
    print("The lowest word_frequency is {} and there are {} words in the book with that word_frequency".format(min_word_freq, len(min_words)))
