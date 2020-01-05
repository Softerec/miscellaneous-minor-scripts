# -*- coding: utf-8 -*-
"""
Gets rid of multiple spaces in the provided multiline text input.

"""


def replace_multiple_chars_from_string(multiple_char, input_string):
    '''Replace multiple instances of multiplec_char from the input_string.
    In the returned string there is only one instance of multiple_car 
    in place of cain of multiple_char-s existing in input_string.
    Returns string with removed multiple chars cains from the input_string.
    '''
    text_wo_substring = input_string.replace(multiple_char+multiple_char, multiple_char)
    while multiple_char+multiple_char in text_wo_substring:
        text_wo_substring = replace_multiple_chars_from_string(multiple_char, text_wo_substring)
                
    return text_wo_substring


def get_multiple_lines_input():
    '''Asks for input (line or multiline) text can be placed.
    Returns multiline string.
    '''

    print("Please type/paste multiple or single line of text.\n"
            "To end editing Press Crtl+z on Windows on Ctrl+d on Linux/Mac.")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    lines = "\n".join(lines)

    return lines


def main():

    text_for_space_cleanup = ''

    while text_for_space_cleanup != 'exit':
        print('To quit: write exit, press Enter and end text editing.\n')
        text_for_space_cleanup = get_multiple_lines_input()

        if text_for_space_cleanup != 'exit':

            if '  ' in text_for_space_cleanup:
                multiple_char = ' '
                input_string = text_for_space_cleanup
                text_wo_multispaces = replace_multiple_chars_from_string(multiple_char, input_string)
                print('Press enter to display cleaned text (without multiple spaces):\n','-'*40)
                input()
                print(text_wo_multispaces)
                return text_wo_multispaces

            else:
                print('Provided text does not contain multiple spaces.')
                
        else:
            break

    print('Exit.')


if __name__ == "__main__":
    main()
