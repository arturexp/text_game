MENU = """***Welcome to the Journey to Mount Qaf*** 
    
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""


def menu():
    print(MENU)
    user_choice = input().lower()
    if user_choice == 'start' or user_choice == '1':
        print("Goodbye!")
    elif user_choice == 'load' or user_choice == '2':
        print("Goodbye!")
    elif user_choice == 'quit' or user_choice == '3':
        print('Goodbye!')
        exit(0)
    else:
        print('Unknown input! Please enter a valid one.')
        menu()


menu()

