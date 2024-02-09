### Introduction

This Python script is a simple slot machine game that allows users to simulate playing a slot machine. The game is run in the console and involves making bets on different lines to win credits. The symbols and their respective counts and values are customizable, providing flexibility to tailor the game to specific preferences.

### Features

1. **Customizable Symbols:**

   - The `symbol_count` dictionary defines the count of each symbol in the slot machine.
   - The `symbol_value` dictionary assigns a value to each symbol.

2. **Game Rules:**

   - Users can set the maximum and minimum bet values (`MAX_BET` and `MIN_BET`).
   - The number of lines to bet on can be adjusted, with a maximum number defined by `MAX_LINES`.

3. **Random Symbol Generation:**

   - The `get_slot_machine_spin` function generates random symbols for each column in the slot machine based on the specified counts.

4. **Winnings Calculation:**

   - The `check_winnings` function determines the winnings based on the alignment of symbols in the columns.

5. **User Interaction:**

   - The game prompts users to deposit an initial amount, choose the number of lines to bet on, and enter the bet amount for each line.

6. **Balance Management:**
   - The user's balance is updated after each spin, and the game continues until the user decides to quit.

### How to Play

1. Run the script in a Python environment.
2. Deposit an initial amount when prompted.
3. Press Enter to play or 'q' to quit.
4. Choose the number of lines and bet amount for each line.
5. View the slot machine display and check for winnings.
6. The game continues until the user decides to quit.

### Customization

- Adjust the `symbol_count` and `symbol_value` dictionaries to customize the symbols and their characteristics.
- Modify `MAX_BET`, `MIN_BET`, and `MAX_LINES` to change the betting limits and the maximum number of lines.

### Requirements

- This script requires a Python environment to run.

### Example

```python
# Customize symbols and their counts/values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Run the game
main()
```
