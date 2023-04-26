# refer to planning.txt
import random
import time
import os
import sys

def get_rand_language_path():
    possible_languages = ['python', 'cpp', 'js']
    global language
    global path
    language = random.choice(possible_languages)
    match language:
        case "python":
            path = './python_snippet.txt'
        case "cpp":
            path = './cpp_snippet.txt'
        case "js":
            path = './js_snippet.txt'

    return path


def get_snippet(path):
    code_lines = []
    with open(path, "r") as f:
        for line in f.readlines():
            code_lines.append(line)
        
    return code_lines


def print_snippet():
    print("What language is the snippet below written in?\n")
    code_lines = get_snippet(path)
    print(*code_lines, sep='\n')

def check_answer():
    user_answer = input("What language was that code snippet written in? (options : python | cpp | js)\n")
    if user_answer == language:
        print("Correct, %s was the correct language!" % language)
    else:
        print("You got it wrong. The correct answer was %s" % language)


def timer(timer):
    #start timer when displaying code block so user has limited time to read the available snippet, thus making it more challenging and difficult for the user to cheat (they can still cheat by doing stuff like taking a photo, but we can set a timer for how long they have to answer as well)
    while 0 < timer:
        sys.stdout.write("\rYou have %d seconds left to view the snippet" % timer)
        sys.stdout.flush()
        timer -= 1
        time.sleep(1)

    os.system("cls" if sys.platform == "win32" else "clear")

def main():
    get_rand_language_path()
    print_snippet()
    timer(5) #in future we can create a select system where either the user selects a preset time or sets a custom one
    check_answer()

if __name__ == "__main__":
    main()
