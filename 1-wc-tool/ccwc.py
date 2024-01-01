#!/usr/bin/env python3

import argparse
import os


# counting bytes
def count_bytes(text: str) -> int:
    utf8_bytes = text.encode('utf-8')
    return len(utf8_bytes)

def count_bytes_in_file(file_path: str) -> int:
    bytes_count = 0
    with open(file_path, 'r') as file:
        newline_byte = 1 # newline consumes 1 byte
        for line in file:
            bytes_count = bytes_count + count_bytes(line) + newline_byte

    return bytes_count


# counting lines
def count_lines(text: str) -> int:
    lines = text.split('\n')
    return len(lines)

def count_lines_in_file(file_path: str) -> int:
    lines_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            lines_count = lines_count + 1

    return lines_count


#counting words
def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_words_in_file(file_path: str) -> int:
    words_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words_count = words_count + count_words(line)

    return words_count


#counting characters
def count_chars(text: str) -> int:
    return len(text)

def count_chars_in_file(file_path: str) -> int:
    char_count = 0
    with open(file_path, 'r') as file:
        newline_byte = 1 # newline consumes 1 char
        for line in file:
            char_count = char_count + count_chars(line) + newline_byte

    return char_count


# main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to the input file")
    parser.add_argument("--bytes", "-c", action="store_true", help="Count number of bytes")
    parser.add_argument("--lines", "-l", action="store_true", help="Count number of lines")
    parser.add_argument("--words", "-w", action="store_true", help="Count number of words")
    parser.add_argument("--chars", "-m", action="store_true", help="Count number of chars")
    
    args = parser.parse_args()
    if not (args.bytes or args.lines or args.words or args.chars): # if no param passed, then enable -wlc
        args.bytes = True
        args.lines = True
        args.words = True

    output = ""

    if os.path.isfile(args.input):
        file_path = args.input
        if args.bytes:
            bytes_count = count_bytes_in_file(file_path)
            output = output + str(bytes_count) + " "
        if args.lines:
            lines_count = count_lines_in_file(file_path)
            output = output + str(lines_count) + " "
        if args.words:
            words_count = count_words_in_file(file_path)
            output = output + str(words_count) + " "
        if args.chars:
            chars_count = count_chars_in_file(file_path)
            output = output + str(chars_count) + " "
    else:
        text = args.input
        if args.bytes:
            bytes_count = count_bytes(text)
            output = output + str(bytes_count) + " "
        if args.lines:
            lines_count = count_lines(text)
            output = output + str(lines_count) + " "
        if args.words:
            words_count = count_words(text)
            output = output + str(words_count) + " "
        if args.chars:
            chars_count = count_chars(text)
            output = output + str(chars_count) + " "

    print (output)

# program runs from here
main()