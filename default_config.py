# --------------- rewards granted ---------------
# reward granted, depending on number of correctly guessed numbers (in PLN) (for each section)

# EUROJACKPOT
# REWARD_TABLE = {
#     0: {0: 0, 1: 0, 2: 0},
#     1: {0: 0, 1: 0, 2: 48},
#     2: {0: 0, 1: 187, 2: 984},
#     3: {0: 313, 1: 705, 2: 14124},
#     4: {0: 13810, 1: 31074, 2: 621502},
#     5: {0: 3107514, 1: 6991907, 2: 139838159},
# }

# LOTTO
REWARD_TABLE = {
    0: 0,
    1: 0,
    2: 0,
    3: 57,
    4: 1032,
    5: 52201,
    6: 13983816
}



# --------------- format of guess ---------------

# EUROJACKPOT
# GUESS_TABLE = [
#     [
#         [i for i in range(1, 50 + 1)],
#         [i for i in range(1, 50 + 1)],
#         [i for i in range(1, 50 + 1)],
#         [i for i in range(1, 50 + 1)],
#         [i for i in range(1, 50 + 1)],
#     ],
#     [
#         [i for i in range(1, 12 + 1)],
#         [i for i in range(1, 12 + 1)]
#     ] 
# ]

# LOTTO
GUESS_TABLE = [
    [
        [i for i in range(1, 49 + 1)],
        [i for i in range(1, 49 + 1)],
        [i for i in range(1, 49 + 1)],
        [i for i in range(1, 49 + 1)],
        [i for i in range(1, 49 + 1)],
        [i for i in range(1, 49 + 1)],
    ]
]


# price for every guess (in PLN)

# LOTTO
GUESS_PRICE = 3

# EUROJACKPOT
# GUESS_PRICE = 12.5

# rounds simulated every week
ROUNDS_PER_WEEK = 3