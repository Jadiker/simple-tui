# Simple TUI

A simple Python module for creating text user interfaces that can be very easily used in projects to get up and running fast.

## Overview

`simple-tui` provides a set of straightforward functions for interactive command-line applications. Perfect for prototypes, scripts, and small projects where you need user input without the complexity of full-featured TUI libraries.

## Installation

Simply download the `tui.py` file and place it in your project directory, then import it:

```python
import tui
```

Or copy the functions you need directly into your script.

## Quick Start

```python
import tui

# Display text
tui.display("Hello, world!")

# Get user input
name = tui.prompt("What's your name?")
tui.display(f"Hello, {name}!")

# Present choices to user
options = ["Option 1", "Option 2", "Option 3"]
choice = tui.choice(options, "Please select an option:")
tui.display(f"You chose: {options[choice]}")
```

## Functions

### `display(text)`

Display text on the screen.

**Parameters:**
- `text`: Any object to display (will be printed)

**Example:**
```python
tui.display("This is some text")
tui.display(42)  # Works with any type
```

### `prompt(text)`

Prompts the user for input with the given text.

**Parameters:**
- `text`: The prompt message to display

**Returns:** The user's input as a string

**Example:**
```python
name = tui.prompt("Enter your name:")
age = tui.prompt("Enter your age: ")
```

### `valid_prompt(text, validator)`

Prompts the user for input and repeats until they provide a valid response.

**Parameters:**
- `text`: The prompt message to display
- `validator`: A function that takes the input string and returns `True` if valid, or raises an exception if invalid

**Returns:** The valid user input as a string

**Example:**
```python
def is_number(value):
    int(value)  # Raises ValueError if not a number
    return True

age = tui.valid_prompt("Enter your age (number only): ", is_number)

# Or with a simple lambda
email = tui.valid_prompt("Enter email: ", lambda x: "@" in x)
```

### `multiline_prompt(text, sentinel="..")`

Prompts the user for multi-line input. The user types their input across multiple lines and ends with a sentinel value.

**Parameters:**
- `text`: The prompt message to display
- `sentinel`: The string that ends input (default: `".."`)

**Returns:** The multi-line input as a single string with newlines preserved

**Example:**
```python
story = tui.multiline_prompt("Tell me a story:")
# User types multiple lines and ends with ".."

poem = tui.multiline_prompt("Write a haiku:", "END")
# User types multiple lines and ends with "END"
```

### `choice(options, text=None)`

Display a numbered list of options and let the user pick one. Users can select by number or by typing the beginning of an option.

**Parameters:**
- `options`: A list/sequence of strings representing the choices
- `text`: Optional text to display before the options

**Returns:** The 0-based index of the selected option

**Example:**
```python
colors = ["Red", "Green", "Blue"]
selected = tui.choice(colors, "Pick a color:")
print(f"You chose: {colors[selected]}")

# User can type "1", "2", "3" or "r", "g", "b"
```

## Complete Example

Here's a complete example showing how to build a simple interactive program:

```python
import tui

def main():
    tui.display("Welcome to the Simple Survey!")
    
    # Get basic info
    name = tui.prompt("What's your name?")
    
    # Get validated input
    def is_positive_number(value):
        num = int(value)
        if num <= 0:
            raise ValueError("Must be positive")
        return True
    
    age = tui.valid_prompt("What's your age? ", is_positive_number)
    
    # Multiple choice
    colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
    fav_color_idx = tui.choice(colors, "What's your favorite color?")
    fav_color = colors[fav_color_idx]
    
    # Multi-line input
    story = tui.multiline_prompt("Tell us something interesting about yourself:")
    
    # Display results
    tui.display("\n" + "="*40)
    tui.display("Survey Results:")
    tui.display(f"Name: {name}")
    tui.display(f"Age: {age}")
    tui.display(f"Favorite Color: {fav_color}")
    tui.display(f"Story: {story}")

if __name__ == "__main__":
    main()
```

## Why Simple TUI?

- **Zero dependencies** - Just standard Python
- **Minimal learning curve** - Five functions, that's it!
- **Robust input handling** - Handles edge cases like EOF/Ctrl+C gracefully
- **Flexible** - Works for quick scripts or more complex CLI apps
- **Copy-paste friendly** - Grab just what you need

Perfect for:
- Prototypes and proof-of-concepts
- Configuration scripts
- Interactive data entry
- Simple CLI tools
- Educational projects
- Any time you need "just enough" user interaction

## License

This is a simple utility module. Use it however you like!
