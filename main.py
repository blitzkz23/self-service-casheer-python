from src.module.display import *
from src.entity.user import User

def main():
    welcome_menu()
    newUser = User(name='Joni')
    print(newUser.welcome_user())


if __name__ == '__main__':
    main()