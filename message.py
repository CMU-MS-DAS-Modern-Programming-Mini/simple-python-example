class Message:
    def __init__(self, message_string):
        self.message_string = message_string

    def print_message(self):
        print("This is the class message {}".format(self.message_string))

    def __str__(self):
        return "This is overriding the str class of the fuction: {}".format(self.message_string)

    def __add__(self, msg):
        if isinstance(msg, str):
            r_msg = Message(self.message_string + msg)
        elif isinstance(msg, Message):
            r_msg = Message(self.message_string + msg.message_string)
        else:
            raise TypeError("Class Message does not know how to add" +
                            "a variable of type {}".format(type(msg)))
        return r_msg
