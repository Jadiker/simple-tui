'''Functions for creating a Text User Interface'''

from typing import Any, Callable, Collection, Optional, Sequence

TAB = "    "

def _input(prompt: str = "") -> str:
    '''
    Make sure that KeyboardInterrupts are treated as such.
    See https://stackoverflow.com/a/31131378 for more info.
    '''
    try:
        return input(prompt)
    except EOFError as e: # pylint: disable = invalid-name
        raise KeyboardInterrupt from e

def display(text: Any) -> None:
    '''Display text on the screen'''
    print(text)

def prompt(text: str) -> str:
    '''Prompts the user for a value'''
    if not (text.endswith(" ") or text.endswith("\n") or text.endswith("\t")):
        # give space for the user's response
        text += " "
    return _input(text)

def valid_prompt(text: str, validator: Callable[[str], bool]) -> str:
    '''
    Prompts the user for a value and repeats the prompt until they put a valid response.
    
    The validator can either return false or raise an exception in order to not accept an input.
    '''
    while True:
        user_response = prompt(text)
        try:
            validator(user_response)
            valid = True
        except Exception:
            valid = False
        if valid:
            return user_response
        else:
            display("That was not a valid response.")


def multiline_prompt(text: str, sentinel: str = "..") -> str:
    '''
    Prompts the user for a value that can span multiple lines.
    Will notify the user of what the sentinel is.
    When the last line is the sentinel value, the prompting ends and the other text is returned.
    '''
    if not text.endswith("\n"):
        # give space for the user's response
        text += "\n"
    if sentinel:
        end_help_text = f"(To finish, type '{sentinel}' on a line by itself and press enter.)\n"
    else:
        end_help_text = f"(To finish, press enter twice.)\n"

    text += end_help_text

    ans = ""
    line = _input(text)
    while line != sentinel:
        ans += line
        ans += "\n"
        line = _input()

    # take off the trailing newline
    return ans[:-1]

def choice(options: Sequence[str], text: Optional[str]=None) -> int:
    '''
    Display a list of options of what the user can do and let the user pick one.
    Displays the text before presenting the options.

    Each string in `options` is an option the user can choose

    Returns the (0-indexed) index of the option that was chosen.
    '''
    if len(options) == 0:
        raise ValueError("No options were given.")
        
    if text:
        display(text)
    display("Please choose one of the following options:")
    for index, option in enumerate(options):
        human_index = index + 1
        if "\n" in option:
            # the option has multiple lines
            # add an extra indent to all of the lines after the first line
            option_lines = option.split("\n")
            multiline_option_str = f"{TAB}{human_index}. {option_lines[0]}\n" + "\n".join([f"{TAB}{TAB}{line}" for line in option_lines[1:]])
            display(multiline_option_str)
        else:
            # just a single line - no need to add extra indentation
            display(f"{TAB}{human_index}. {option}")
    display("") # blank line for the user to respond afterwards

    if len(options) == 1:
        display(f"There is only one option (1. {options[0]}), so it has been automatically chosen.")
        return 0

    # ask the user for choices
    number: Optional[int] = None
    while number is None:
        try:
            user_input = _input("Type the number or the option: ")
            try:
                number = int(user_input)
            except ValueError:
                simple_user_input = user_input.strip().lower()
                possible_options = [index + 1 for index, option in enumerate(options) if option.strip().lower().startswith(simple_user_input)]
                if len(possible_options) == 0:
                    display(f"There are no options that begin with '{simple_user_input}'.")
                    raise ValueError("Invalid start of option")
                elif len(possible_options) == 1:
                    number = possible_options[0]
                else:
                    display(f"There are {len(possible_options)} options that start with '{simple_user_input}':")
                    for index in possible_options:
                        computer_index = index - 1
                        display(f"{TAB}{index}. {options[computer_index]}")
                    display("Please be more specific.")
                    raise ValueError("Unspecific option")

            assert isinstance(number, int)
            number -= 1 # adjust from human index to computer index
            if number < 0 or len(options) <= number:
                raise ValueError("Invalid number")

        except (ValueError, AssertionError) as e:
            display(f"Sorry, please enter a number between 1 and {len(options)} or the start of a specific option.")
            number = None

    return number

if __name__ == "__main__":
    user_response = multiline_prompt("Tell me something interesting")
    print(f"Got back:\n{user_response}")
    display("Hello world!")
    user_response = prompt("Testing user input: ")
    print(f"Got back: {user_response}")
    my_options = ["The first option", "The second option"]
    user_choice = choice(my_options, "Here are a few options.")
    print("The user chose to do the following: {}".format(my_options[user_choice]))
