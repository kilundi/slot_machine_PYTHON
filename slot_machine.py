import random

MAX_LINES = 3
MAX_BET= 100
MIN_BET=10

ROWS = 3
COLS =3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items( ):
        for _ in range(symbol_count) :
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column =[]

        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)
        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end= "")
        print()

def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a valid number.")
    # print(amount)
    return amount


def get_bet():
    while True:
        amount=input("Enter amount you would like to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be greater than ${MIN_BET} and less than ${MAX_BET}")
        else:
            print("Please enter a valid number.")
    # print(amount)
    return amount

def get_number_of_lines():
    while True:
        lines=input(f"Enter the amount of lines your would like to bet on [1 - {str(MAX_LINES)}] ?: ")
        if lines.isdigit():
            lines=int(lines)
            if 0  < lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines should be between 1 to {MAX_LINES}")
        else:
            print("Please enter a valid number.")

    return lines

def spin_fun(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough amount to bet ${total_bet}, your current balance is: ${balance }")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_value)

    print(f"Your winning amount is ${winnings}.\nCongratulations!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance: ${balance}\n")
        spin = input("Press enter to play (q to quit).").lower()
        if spin == "q":
            break
        balance += spin_fun(balance)

    print(f"You are left with $ {balance}. Thanks for playing!\n")

main()