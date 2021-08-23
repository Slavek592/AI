#!/bin/python
from .memory_worker import *


def main(ai_name, language, hint):
    my_message = my_answer_searcher("1\n", ai_name)[0]
    print(my_message.replace("\n", "").replace("%", "\n").replace("$", ""))
    my_index = "1\n"
    his_index = "1\n"
    while True:
        if hint:
            print(memory_reader(my_index, ai_name, False))
            print(memory_reader("0\n", ai_name, False))
        his_message = input("").lower()
        if his_message == "ewinwej":
            if language == "Czech":
                learn_something(his_index + "\n", input("napiste spravnou odpoved\n"), ai_name)
            else:
                learn_something(his_index + "\n", input("input the correct answer\n"), ai_name)
        elif his_message in ["ewin where", "ewin kde"]:
            print(my_index.replace("\n", ""))
        elif his_message in ["dobrou", "zatim", "bye", "good night"]:
            print(his_message)
            break
        else:
            his_index = his_answer_searcher(my_index, his_message, ai_name)
            if his_index == "it is not in the memory":
                if language == "Czech":
                    typo = input("je to preklep?\n")
                else:
                    typo = input("is it typo?\n")
                if typo in ["no", "ne"]:
                    if language == "Czech":
                        new = input("nova, nebo odpoved?\n")
                    else:
                        new = input("new or answer?\n")
                    if new in ["new", "nova"]:
                        learn_something("0\n", his_message, ai_name)
                    else:
                        learn_something(my_index, his_message, ai_name)
            else:
                [my_message, my_index] = my_answer_searcher(his_index, ai_name)
                print(my_message.replace("\n", "").replace("%", "\n").replace("$", ""))
