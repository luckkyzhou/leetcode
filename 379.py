class PhoneDirectory(object):

    def __init__ (self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.phone = set(range(maxNumbers))

    def get (self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.phone: return -1
        else: return self.phone.pop()

    def check (self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.phone

    def release (self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number not in self.phone: self.phone.add(number)