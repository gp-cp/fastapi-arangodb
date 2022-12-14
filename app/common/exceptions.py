
class DocumentNotFoundError(Exception):

    def __init__(self, key):
        self.key = key
        self.message = self.__str__()
        super().__init__(self.message)

    def __str__(self):
        return f'Document with key {self.key} not found.'


class AuthenticationError(Exception):
    def __init__(self):
        self.message = self.__str__()
        super().__init__(self.message)

    def __str__(self):
        return "Username or password is wrong."