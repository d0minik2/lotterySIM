# reward granted, depending on number of correctly guessed numbers (in PLN)
REWARD_TABLE = {
    0: 0,
    1: 0,
    2: 0,
    3: 57,
    4: 1032,
    5: 52201,
    6: 13983816
}

# numbers to guess from
NUMBERS = [i for i in range(1, 49 + 1)]

# how many numbers you can guess per lottery
NO_GUESSES = 6

# price for every guess (in PLN)
GUESS_PRICE = 3

# rounds simulated every week
ROUNDS_PER_WEEK = 3