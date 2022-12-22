import re


def read_template(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    words = tuple(re.findall(r"{([^{}]*)}", string))
    for x in words:
        string = string.replace(x, "")
        return string, words


def merge(stripped, inputs):
    return stripped.format(*inputs)


welcome = """
    Heyo! Welcome to the MAD world of madlib!
    To play: please follow the prompts!"""


def main():
    print(welcome)
    file_path = input("Enter file path or hit Enter/Return")
    if file_path == "":
        file_path == "assets/madlib.txt"
    try:
        message = read_template(file_path)
        empty_string, parts = parse_template(message)
        filled_list = []
        for i in parts:
            user_input = input(f" Enter {i} > ")
            filled_list.append(user_input)
        result = merge(empty_string, filled_list)
        print(f"\nWas that fun? Here are your results:\n\n" + result)
        with open('assets/result.txt', 'w') as author:
            author.write(result)
    except:
        print('Oops! An error occurred.')


if __name__ == '__main__':
    main()
