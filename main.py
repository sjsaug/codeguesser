# refer to planning.txt
import random
import time
import os
import sys
import configparser
from colorama import Fore, Style
from cryptography.fernet import Fernet

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
    global text_color #make unbound false flag in certain editors go away
    print("What language is the code snippet below written in?\n")
    code_lines = get_snippet(path)
    match snippet_color:
        case "yellow":
            text_color = Fore.YELLOW
        case "blue":
            text_color = Fore.BLUE
        case "green":
            text_color = Fore.GREEN
        case "red":
            text_color = Fore.RED
        case "cyan":
            text_color = Fore.CYAN
        case "magenta":
            text_color = Fore.MAGENTA
        case "black":
            text_color = Fore.BLACK
        case "white":
            text_color = Fore.WHITE

    for elem in code_lines:
        print(text_color + elem)
    print(Style.RESET_ALL)
    #print(*code_lines, sep='\n') #alternative method to above but compatability issues with printing colored text

def check_answer():
    global pts_gained
    pts_gained = 0
    user_answer = input("What language was that code snippet written in? (options : python | cpp | js | react | css | rust | c# | go | lua | php)\n")
    if user_answer == language:
        pts_gained+=5
        print("Correct, %s was the correct language!" % language)
    else:
        pts_gained-=3
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
    settings_options = dict(configParser.items('Settings'))

    #FIXES
    global is_iterm2
    is_iterm2 = fixes_options['is_iterm2']

    #DEV
    global enable_debugging
    enable_debugging = dev_options['enable_debugging']

    #SETTINGS
    global viewing_lenght
    viewing_lenght = settings_options['viewing_timer_lenght']

    global num_turns
    num_turns = settings_options['number_of_turns']

    global snippet_color
    snippet_color = settings_options['snippet_text_color']


def encrypt(key):
    global encrypted_data

    f = Fernet(key)

    #opening file to encrypt
    with open('points.txt', 'rb') as pts_file:
        unencrypted_data = pts_file.read()
    
    #encrypting and writing encrypted data
    encrypted_data = f.encrypt(unencrypted_data)
    with open('points.txt', 'wb') as pts_file:
        pts_file.write(encrypted_data)

def decrypt(key):
    global encrypted_data
    f = Fernet(key)
    #open file again to retrieve encrypted data
    with open('points.txt', 'rb') as pts_file:
        encrypted_data = pts_file.read()

    #decrypting and writing decrypted data
    decrypted_data = f.decrypt(encrypted_data)
    with open('points.txt', 'wb') as pts_file:
        pts_file.write(decrypted_data)
    

def points_system():
    key = Fernet.generate_key()
    
    with open('points.txt', 'r+') as pts_file:
        total_pts = pts_file.read()


    #decrypt pts
    #if total_pts == 0 or "0":
        #encrypt(key)
    #decrypt(key)

    #writing pts to txt
    global pts_gained    
    total_pts_int = int(total_pts)
    total_pts_int+=pts_gained
        
    with open('points.txt', 'w+') as pts_file:
        pts_file.write(str(total_pts_int))

    #encrypting pts
    #encrypt(key)
    


def main():
    read_config()
    fix_mac()
    get_rand_language_path()
    print_snippet()
    if viewing_lenght != "infinite": #we can just check if it's a str but doing this to make it easier to understand what this code does
        timer(int(viewing_lenght))
    check_answer()
    points_system()


def startup():
    read_config()
    global num_turns
    num_curr_turns = 0
    if num_turns == "infinite":
        while True:
            if __name__ == "__main__":
                main()
    if num_turns != "infinite":
        while num_curr_turns < int(num_turns):
            if __name__ == "__main__":
                num_curr_turns += 1
                main()


startup()
