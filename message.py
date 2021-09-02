class Message:
    def __init__(self, message_string):
        self.message_string = message_string

    def print_message(self):
        print("This is the class message {}".format(self.message_string))
