"""A module to keep track of a plaintext."""

import math


class Message:

    """An instance of a plaintext.

    This is a wrapper class for a plaintext, which consists
    of one polynomial.

    Attributes:
        poly (Polynomial): Plaintext polynomial.
        scaling_factor (float): Scaling factor.
    """

    def __init__(self, message: list = None):
        """
        Set Message.
        """
        # Spread the message into a list
        self.__message = [*message]
        self.message = [*message]
        self.padding = []
        _length = len(self.__message)
        self.length = _length

    def __str__(self):
        """Represents plaintext as a readable string.

        Returns:
            A string which represents the Plaintext.
        """
        return str(self)

    def add_dynamic_padding(self) -> list:
        """Adds padding to the message to be a multiple of 2.

        Returns:
            The padded message.
        """
        # Get the length of the original message
        oringinal_message_lenght = len(self.__message)

        # Set the length of the message after padding
        # Set to the length of the message at the initial state
        length = len(self.__message)

        # Go through the message and update the length to be a power of 2
        while self.is_message_length_power_of_2(length) != True:
            length += 1

        if length > oringinal_message_lenght:
            # Add padding to the message
            for i in range(length - oringinal_message_lenght):
                # add padding to the front of the message
                self.__message.insert(0, 0)
                self.padding.insert(0, 0)

        _length = len(self.message)
        self.length = _length
        return self.__message

    def is_power_of_2(self, length) -> bool:
        # Check if the length is a power of 2
        return length > 0 and math.log2(length).is_integer()

    def is_message_length_power_of_2(self, length: int) -> bool:
        """Checks if the length of the given message is a power of 2.

        Args:
            message: The message to check.

        Returns:
            True if the length of the message is a power of 2, False otherwise.
        """

        if length == 0:
            return False
        if length == 1:
            return True

        while length > 1:
            if length % 2 != 0:
                return False
            length //= 2

        return True

    def remove_padding(self, message: list) -> list:
        """Removes the padding from the message.

        Args:
            message: The message to remove the padding from.

        Returns:
            The message without padding.
        """
        # Remove the padding
        for i in range(len(self.padding)):
            # Remove the padding from the front of the message
            message.pop(0)
            

        return message

    def get_padded_message(self) -> list:
        """Gets the Padded message.

        Returns:
            The message.
        """
        return self.__message
    
    def length(self) -> int:
        """Gets the length of the message.

        Returns:
            The length of the message.
        """
        return len(self.__message)

    @staticmethod
    def get_least_padding(messages: list) -> list:
        """Gets the Padded message.

        Returns:
            The message.
        """

        # Get the index if the message with the biggest length
        max_index = 0
        for i in range(len(messages)):

            if  messages[i].length > messages[max_index].length:
                max_index = i

        # Get the padding of the message with the biggest length
        padding = messages[max_index].padding

        return padding

    @staticmethod
    def remove_padding_from_message(message: list, padding: list) -> list:
        """Removes the padding from the message.

        Args:
            message: The message to remove the padding from.

        Returns:
            The message without padding.
        """
        # Remove the padding
        for i in range(len(padding)):
            message.pop(0)

        return message
    
    @staticmethod
    def trancate_padding(vector_message, paddings) -> list:
        """Removes the padding from the message.

        Args:
            message: The message to remove the padding from.

        Returns:
            The message without padding.
        """

        _vector_message = [*vector_message]
        # Get the padding of the message with the biggest length
        padding = Message.get_least_padding(paddings)

        trimmed_message = Message.remove_padding_from_message(_vector_message, padding)

        return trimmed_message