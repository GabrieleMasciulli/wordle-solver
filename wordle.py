POSSIBLE_WORDS_FILE = './data/possible_words.txt'
ALLOWED_WORDS_FILE = './data/allowed_words.txt'


def get_word_list(all):  # returns a list of strings
    result = []

    # loading either the allowed or possible words
    file = ALLOWED_WORDS_FILE if all else POSSIBLE_WORDS_FILE
    with open(file):
        result.extend([word.strip() for word in open(file).readlines()])

    return result


def word_has_letter_n_times(word, letter, occurences):
    return word.count(letter) == occurences

# returns true if the word passed as a parameter matches the given patter, false otherwise


def matches_pattern(word, possible_word, pattern):
    match = False

    for i, color in enumerate(pattern):
        if color == 'black':
            match = possible_word.find(word[i]) == -1
        elif color == 'green':
            # letter at index i MUST correspond
            match = possible_word[i] == word[i]
        elif color == 'yellow':
            ''

        if not match:
            break

    return match


def count_words_left_from_pattern(word, pattern, possible_words):
    count = 0

    # print(pattern)

    for possible_word in possible_words:
        if matches_pattern(word, possible_word, pattern):
            count += 1
            # print(f'Word: {word}, Possible word: {possible_word}')

    return count

# in wordle a pattern is an assignment for each letter in the word of either the color green,
# yellow or grey, respectively meaning that the letter was in the right position, it occured
# at least once in the word but in the wrong position and it wasn't at all in the word.


def compute_patterns():  # returns a list of tuples (each tuple represents a specific pattern)
    colors = ['black', 'yellow', 'green']

    patterns = []

    # less verbose way to create the pattern array
    patterns = [(a, b, c, d, e)
                for a in colors for b in colors for c in colors for d in colors for e in colors]  # all possible patterns for a 5-letter word
    return patterns


def main():
    word = "never"
    patterns = compute_patterns()
    possible_words = get_word_list(all=False)

    # array mapping the number of words left for each pattern related to a given word
    # words_left = []

    # for pattern in patterns:
    #     words_left.append(
    #         {'pattern': pattern, 'value': count_words_left_from_pattern(word, pattern, possible_words)})

    for pattern in patterns:
        words_left_count = count_words_left_from_pattern(
            word, pattern, possible_words)
        print(f'Pattern: {pattern}, Words left: {words_left_count}')


main()
