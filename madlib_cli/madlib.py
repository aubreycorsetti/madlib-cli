from textwrap import dedent
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


def welcome():
    print(dedent("""
    Heyo! Welcome to the MAD world of madlib!
    To play: please follow the prompts!"""))


welcome()
# def story = ("It was a {Adjective} and {Adjective} {Noun}.")


adjective = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")
noun = input("Enter a noun: ")

story = ("It was a " + adjective + " and " + adjective2 + " " + noun)
print(story)
