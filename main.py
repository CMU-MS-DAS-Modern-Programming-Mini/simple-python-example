import os

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

if __name__ == "__main__":
    main()
