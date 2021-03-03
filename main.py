import os

MENU = """***Welcome to the Journey to Mount Qaf*** 

1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""


class Character:
    difficulty = {'1': 'Easy', '2': 'Medium', '3': 'Hard'}
    LIVES = {'1': 5, '2': 3, '3': 1}

    def __init__(self, user_name, char_name, char_species, char_gender,
                 char_snack, char_weapon, char_tool, game_difficulty):
        self.user_name = user_name.capitalize()
        self.char_name = char_name.capitalize()
        self.char_species = char_species.capitalize()
        self.char_gender = char_gender.capitalize()
        self.char_snack = char_snack.capitalize()
        self.char_weapon = char_weapon.capitalize()
        self.char_tool = char_tool.capitalize()
        self.game_difficulty = game_difficulty
        self.lives = Character.LIVES[game_difficulty]

    def __str__(self):
        p1 = f'Your character: {self.user_name}, {self.char_species}, {self.char_gender}'
        p2 = f'Your inventory: {self.char_snack}, {self.char_weapon}, {self.char_tool}'
        diff = f'Difficulty: {Character.difficulty[self.game_difficulty]}'
        return '\n'.join([p1, p2, diff])

    def __repr__(self):
        return str({'user_name': self.user_name, 'char_name': self.char_name, 'char_species': self.char_species,
                    'char_gender': self.char_gender, 'char_snack': self.char_snack, 'char_weapon': self.char_weapon,
                    'char_tool': self.char_tool, 'game_difficulty': self.game_difficulty, 'lives': self.lives})


def create_new_character(name):
    print('Create your character:')
    char_name = input('1- Name ')
    char_species = input('2- Species ')
    char_gender = input('3- Gender ')

    print('Pack your bag for the journey:')
    char_snack = input('1- Favourite Snack ')
    char_weapon = input('2- A weapon for the journey ')
    char_tool = input('3- A traversal tool ')

    print('Choose your difficulty:\n1- Easy\n2- Medium\n3- Hard')
    game_difficulty = input()
    if game_difficulty == '1' or game_difficulty.lower() == 'easy':
        game_difficulty = '1'
    elif game_difficulty == '2' or game_difficulty.lower() == 'medium':
        game_difficulty = '2'
    elif game_difficulty == '3' or game_difficulty.lower() == 'hard':
        game_difficulty = '3'

    print('Good luck on your journey!')
    return Character(name, char_name, char_species, char_gender, char_snack, char_weapon, char_tool, game_difficulty)


def save_progress(char):
    current_path = os.getcwd()
    try:
        os.mkdir('saves')
    except FileExistsError:
        pass

    os.chdir(current_path + '\\saves')

    if os.path.exists(char.user_name):
        os.remove(char.user_name)

    with open(char.user_name + '.txt', 'w') as file:
        file.write(repr(char))


def start_new_game():
    user_name = input("Enter a user name to save your progress or type '/b' to go back ")
    if user_name == '/b':
        print('Going back to menu...\n')
        menu()
    else:
        new_char = create_new_character(user_name)
        save_progress(new_char)
        return new_char


def menu():
    print(MENU)
    user_choice = input().lower()
    if user_choice == 'start' or user_choice == '1':
        print("Starting a new game...")
        print(start_new_game())
    elif user_choice == 'load' or user_choice == '2':
        print("Goodbye!")
    elif user_choice == 'quit' or user_choice == '3':
        print('Goodbye!')
        exit(0)
    else:
        print('Unknown input! Please enter a valid one.')
        menu()


menu()
