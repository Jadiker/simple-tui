'''Functions for creating a Text User Interface'''

from typing import List

def _input(*args, **kwargs):
    '''
    Make sure that KeyboardInterrupts are treated as such.
    See https://stackoverflow.com/a/31131378 for more info.
    '''
    try:
        return input(*args, **kwargs)
    except EOFError as e: # pylint: disable = invalid-name
        raise KeyboardInterrupt from e


def display(text):
    '''
    Display one line of text on the screen

    text is a string
    '''
    print(text)

def prompt(text):
    '''
    Prompts the user for a value

    prompt is a string
    '''
    if not (text.endswith(" ") or text.endswith("\n") or text.endswith("\t")):
        # give space for the user's response
        text += " "
    return _input(text)

def choice(options: List[str]) -> int:
    '''
    Display a list of options of what the user can do and let the user pick one

    options is a list of strings (each one is an option the user can choose)

    Returns the index of the option that was chosen.
    '''
    print("Please choose one of the following options:")
    for index, option in enumerate(options):
        human_index = index + 1
        print("    {}. {}".format(human_index, option))
    print()

    # ask the user for choices
    number = None
    while number is None:
        try:
            user_input = _input("Type the number or the option: ")
            try:
                number = int(user_input)
            except ValueError:
                simple_user_input = user_input.strip().lower()
                for index, option in enumerate(options):
                    simple_option = option.strip().lower()
                    if simple_user_input == simple_option:
                        number = index + 1

            assert isinstance(number, int)
            number -= 1
            if number < 0 or len(options) <= number:
                raise ValueError("Invalid number")

        except Exception: # pylint: disable = broad-except
            print("Sorry, please enter a number between 1 and {} or the exact option".format(len(options)))
            number = None
    return number

if __name__ == "__main__":
    display("Hello world!")
    user_response = prompt("Testing user input: ")
    print("Got back: {}".format(user_response))
    my_options = ["The first option", "The second option"]
    user_choice = choice(my_options)
    print("The user chose to do the following: {}".format(my_options[user_choice]))
