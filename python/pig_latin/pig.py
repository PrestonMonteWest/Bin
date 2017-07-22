#!/usr/bin/env python3

import sys, re

def pigify(string):
    """Return the string translated into pig latin."""

    # private helper functions
    def get_words(string):
        return (x.group(0) for x in re.finditer("[A-z]+([A-z']+[A-z])?", string))

    def get_space(word, string):
        index = string.find(word)
        space = string[:index]
        string = string[index + len(word):]

        return (space, string)

    # word generator
    words = get_words(string)

    temp = ''

    for word in words:
        first_char = word[0].lower()
        space, string = get_space(word, string)

        # pig logic
        if first_char in "aeiou":
            word = word + "yay"
        else:
            start = word[1:]
            end = first_char + "ay"

            if word.istitle():
                word = start.title() + end
            else:
                word = start + end

        temp = temp + space + word
    else:
        temp = temp + string

    return temp

def main():
    if len(sys.argv) == 1: # no CL args
        files = [sys.stdin]
    else:
        filenames = sys.argv[1:]
        files = []

        try:
            for filename in filenames:
                files.append(open(filename, 'r'))
        except IOError:
            print("IOError: {0} not found.".format(filename))

    num_files = len(files)

    for file in enumerate(files):
        if num_files > 1:
            print(file[1].name + ":")

        with file[1] as text:
            for line in text:
                print(pigify(line), end='')

        if (file[0] + 1) != num_files:
            print()

if __name__ == "__main__":
    main()
