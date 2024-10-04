from simulations import *
import example_lotteries


# reward granted, depending on number of correctly guessed numbers (in PLN) (for each combination of every section)
reward_table = { 
        0: {0: 0, 1: 0, 2: 0},
        1: {0: 0, 1: 0, 2: 48},
        2: {0: 0, 1: 187, 2: 984},
        3: {0: 313, 1: 705, 2: 14124},
        4: {0: 13810, 1: 31074, 2: 621502},
        5: {0: 3107514, 1: 6991907, 2: 139838159},
    }

# format of guess, each sublist is a section in which numbers can't repeat themselfes. each guess field must be a list of possible numbers to choose from
guess_table = [
        [
            [i for i in range(1, 50 + 1)],
            [i for i in range(1, 50 + 1)],
            [i for i in range(1, 50 + 1)],
            [i for i in range(1, 50 + 1)],
            [i for i in range(1, 50 + 1)],
        ],
        [
            [i for i in range(1, 12 + 1)],
            [i for i in range(1, 12 + 1)]
        ] 
    ]

# price of each guess (in PLN)
guess_price = 12.5



player = Player()
lottery = Lottery(
    rewards=reward_table,
    guess_price=guess_price,
    guess_table=guess_table
)
simulation = Simulation(
    lottery=lottery,
    player=player,
    rounds_per_week=3
    )

player.generate_guess(lottery) # random guess
# player.set_guess([23, 13, 12, 41, 34, 32], lottery=lottery)
# player.set_guess([[25, 49, 10, 1, 48], [4, 2]], lottery=lottery)

simulation.simulate_years_until_won(log=True)