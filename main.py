import os
from message import Message

def print_message_from_file(filename):
    with open(filename, "r") as f_to_read:
        message = f_to_read.read()
        print("This is the message")
        print("{}".format(message))

def print_separator(num_chars=45):
    print("{}".format("".join(["-" for x in range(0, num_chars)])))

def main():
    for i in range(0, 10):
        print("Hello World!#{}".format(i))

    sample_list = [0, 1, 2, 3, 4,
                   5, 6, 7, 8, 9]

    print_separator()

    for i in sample_list:
        print("Hello List!#{}".format(i))

    print_separator()

    sample_list_comp = [x for x in range(0, 1)]

    for i in sample_list_comp:
        print("Hello Comprehension!#{}".format(i))

    print_separator()

    sample_dictionary = {"english": "hat",
                         "french": "chapeau"}

    for k, val in sample_dictionary.items():
        print("The word in {} is {}".format(k, val))

    print_separator()

    filename = os.path.join(os.getcwd(), "message.txt")
    print("The File is at {}".format(filename))

    print_message_from_file(filename)

    print_separator()

    msg = Message("... this is in class.")
    msg.print_message()

    print_separator()

    print("{}".format(msg))

    print_separator()

    msg_add = msg + " | adding a string"
    msg_add.print_message()

    print_separator()

    msg2 = Message("... adding a message class")
    msg_add = msg + msg2
    msg_add.print_message()

    print_separator()
    try:
        num = 6.003432
        msg_add = msg + num
    except Exception as e_msg:
        print("There was an exception {}".format(str(e_msg)))

if __name__ == "__main__":
    main()
