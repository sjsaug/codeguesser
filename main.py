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
    user_answer = input("What is the language of the code snippet?\n")
    if user_answer == language:
        print("You got it right!")
    else:
        print("You got it wrong")


def timer(timer):
    #start timer when displaying code block so user has limited time to read the available snippet, thus making it more challenging and difficult for the user to cheat (they can still cheat by doing stuff like taking a photo, but we can set a timer for how long they have to answer as well)
    print("You have " + str(timer) + " seconds to view the snippet\n")
    time.sleep(timer)
    os.system("cls" if sys.platform == "win32" else "clear")

def main():
    get_rand_language_path()
    print_snippet()
    timer(10)
    check_answer()

if __name__ == "__main__":
    main()
