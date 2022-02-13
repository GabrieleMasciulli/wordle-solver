import json
from math import log2


def countWordsLeftFromPattern(word, pattern):
    count = 0

    return

# in wordle a pattern is an assignment for each letter in the word of either the color green, yellow or grey,
# respectively meaning that the letter was in the right position, it occured at least once in the word but in the wrong position
# and it wasn't at all in the word.


def computePatterns():
    colors = ['black', 'yellow', 'green']

    patterns = []

    for l_1 in range(3):
        for l_2 in range(3):
            for l_3 in range(3):
                for l_4 in range(3):
                    for l_5 in range(3):
                        pattern = (colors[l_1], colors[l_2],
                                   colors[l_3], colors[l_4], colors[l_5])
                        patterns.append(pattern)

    # less verbose way to create the pattern array
    # patterns = [(a, b, c, d, e)
    #             for a in colors for b in colors for c in colors for d in colors for e in colors]  # all possible patterns for a 5-letter word
    return patterns


def main():
    word = "trews"
    patterns = computePatterns()

    # array mapping the number of words left for each pattern related to a given word
    words_left = []

    for p in patterns:
        words_left.append(
            {'pattern': p, 'value': countWordsLeftFromPattern(word, p)})

    print(words_left)


main()
