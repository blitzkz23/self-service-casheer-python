'''
This file contain Class for User to store email, name, and password.
'''

class User:
    def __init__(self, email='', name='', password=''):
        self.email = email
        self.name = name
        self.password = password

    def welcome_user(self):
        return f'Hello, {self.name} what would you like to do?'
    