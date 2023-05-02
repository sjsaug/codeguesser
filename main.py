# refer to planning.txt
import random
import time
import os
import sys
import configparser

def get_rand_language_path():
    possible_languages = ['python', 'cpp', 'js', 'react', 'css', 'rust', 'c#', 'go', 'lua', 'php']
    global language
    global path
    language = random.choice(possible_languages)
    if enable_debugging == "True":
        print("Chosen language : " + language)

    match language:
        case "python":
            path = './snippets/python_snippet.txt'
        case "cpp":
            path = './snippets/cpp_snippet.txt'
        case "js":
            path = './snippets/js_snippet.txt'
        case "react":
            path = './snippets/react_snippet.txt'
        case "css":
            path = './snippets/css_snippet.txt'
        case "rust":
            path = './snippets/rust_snippet.txt'
        case "c#":
            path = './snippets/c#_snippet.txt'
        case "go":
            path = './snippets/golang_snippet.txt'
        case "lua":
            path = './snippets/lua_snippet.txt'
        case "php":
            path = './snippets/php_snippet.txt'
    
    return path


def get_snippet(path):
    code_lines = []
    with open(path, "r") as f:
        for line in f.readlines():
            code_lines.append(line)
        
    return code_lines


def print_snippet():
    print("What language is the code snippet below written in?\n")
    code_lines = get_snippet(path)
    print(*code_lines, sep='\n')

def check_answer():
    user_answer = input("What language was that code snippet written in? (options : python | cpp | js | react | css | rust | c# | go | lua | php)\n")
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

def fix_mac():
    if sys.platform == "darwin" and is_iterm2 == "True":
        os.system('stty erase "^H"')
        if enable_debugging == "True":
            print("stty erase has been run")

def read_config():
    configParser = configparser.RawConfigParser()
    configFilePath = r'./codeguesser.cfg'
    configParser.read(configFilePath)
    fixes_options = dict(configParser.items('Fixes'))
    dev_options = dict(configParser.items('Dev'))

    global is_iterm2
    is_iterm2 = fixes_options['is_iterm2']

    global enable_debugging
    enable_debugging = dev_options['enable_debugging']

def main():
    read_config()
    fix_mac()
    get_rand_language_path()
    print_snippet()
    timer(10) #in future we can create a select system where either the user selects a preset time or sets a custom one
    check_answer()

if __name__ == "__main__":
    main()
