"""
message.property

Contains the message class to handle messages from the files
"""
class Message:
    """
    Contains a message the can be printed out to the screen
    """
    def __init__(self, message_string):
        """
        Creates an instance of messsage

        Arguments:

        message_string: string containing the message
                        to be displayed

        Returns:

        instance of message
        """
        self.message_string = message_string

    def print_message(self):
        """
        Prints the message to stdout
        """
        print("This is the class message {}".format(self.message_string))

    def __str__(self):
        """
        Overrides the str operator to print a pretty string
        """
        return "This is overriding the str class of the fuction: {}".format(self.message_string)

    def __add__(self, msg):
        """
        Overrides the add operator to either add a Message or string

        Arguments:
            msg - A Message instance or string that is to be added

        Returns:
            New Message instance with msg added to the message_string
        """
        if isinstance(msg, str):
            r_msg = Message(self.message_string + msg)
        elif isinstance(msg, Message):
            r_msg = Message(self.message_string + msg.message_string)
        else:
            raise TypeError("Class Message does not know how to add" +
                            "a variable of type {}".format(type(msg)))
        return r_msg
