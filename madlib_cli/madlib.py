import re


def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    pieces = tuple(re.findall(r"{([^{}]*)}", string))
    for x in pieces:
        string = string.replace(x, "")
    return string, pieces


def merge(stripped, inputs):
    return stripped.format(*inputs)


welcome = """
Heyo! Welcome to the MAD world of madlib!
To play: please follow the prompts!
"""


def main():
    print(welcome)
    file_path = input(" Enter File Path or hit 'Enter' for the default > ")
    if file_path == "":
        file_path = "assets/madlib.txt"
    try:
        script = read_template(file_path)
        empty_string, parts = parse_template(script)
        filled_list = []
        for i in parts:
            user_input = input(f"  Enter {i} > ")
            filled_list.append(user_input)
        result = merge(empty_string, filled_list)
        print(f"\nHere is your Madlib:\n\n" + result)
        with open('assets/result.txt', 'w') as writer:
            writer.write(result)
    except:
        print('An error occurred')


if __name__ == '__main__':
    main()