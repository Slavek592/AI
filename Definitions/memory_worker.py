#!/bin/python
from random import randint


def memory_reader(index, ai_name, my):
    file = open("Data/" + ai_name + "_memory.txt", "r")
    possibilities = []
    found = 0
    for read_line in file:
        if found == 1:
            if read_line == "\n":
                pass
            elif read_line.startswith("#") & my:
                found = 0
            elif read_line.startswith("$") & (not my):
                found = 0
            else:
                possibilities.append([read_line])
                found = 2
        elif found == 2:
            possibilities[len(possibilities) - 1].append(read_line)
            found = 0
        else:
            if read_line == "#" + str(index):
                found = 1
    return possibilities


def my_answer_searcher(index, ai_name):
    possibilities = memory_reader(index, ai_name, True)
    if not possibilities:
        possibilities = memory_reader("0\n", ai_name, True)
    if len(possibilities) > 1:
        return possibilities[randint(0, len(possibilities) - 1)]
    else:
        return possibilities[0]


def his_answer_searcher(index, his_answer, ai_name):
    possibilities = memory_reader(index, ai_name, False)
    for read_message in possibilities:
        if read_message[0] in [his_answer + "\n", "#" + his_answer + "\n"]:
            return read_message[1]
    possibilities = memory_reader("0\n", ai_name, False)
    for read_message in possibilities:
        if read_message[0] in [his_answer + "\n", "#" + his_answer + "\n"]:
            return read_message[1]
    return "it is not in the memory"


def learn_something(index, message, ai_name):
    memory = open("Data/" + ai_name + "_memory.txt", "a")
    number_of_messages = open("Data/" + ai_name + "_number_of_messages.txt", "r")
    number = 0
    for read_number in number_of_messages:
        number = int(read_number) + 1
    memory.write("\n#" + str(index))
    memory.write(str(message))
    memory.write("\n" + str(number))
    number_of_messages = open("Data/" + ai_name + "_number_of_messages.txt", "w")
    number_of_messages.write(str(number))
