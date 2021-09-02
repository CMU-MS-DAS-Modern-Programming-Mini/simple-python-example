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
