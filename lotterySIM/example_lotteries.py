from .simulations import Lottery


class Lotto(Lottery):
    def __init__(self):
        reward_table = {
            0: 0,
            1: 0,
            2: 0,
            3: 57,
            4: 1032,
            5: 52201,
            6: 13983816
        }
        
        guess_table = [
            [
                [i for i in range(1, 49 + 1)],
                [i for i in range(1, 49 + 1)],
                [i for i in range(1, 49 + 1)],
                [i for i in range(1, 49 + 1)],
                [i for i in range(1, 49 + 1)],
                [i for i in range(1, 49 + 1)]
            ]
        ]
        
        guess_price = 3
        
        
        Lottery.__init__(self, 
            rewards=reward_table,
            guess_price=guess_price,
            guess_table=guess_table
        )
        
        

class EuroJackpot(Lottery):
    def __init__(self):
        reward_table = {
            0: {0: 0, 1: 0, 2: 0},
            1: {0: 0, 1: 0, 2: 48},
            2: {0: 0, 1: 187, 2: 984},
            3: {0: 313, 1: 705, 2: 14124},
            4: {0: 13810, 1: 31074, 2: 621502},
            5: {0: 3107514, 1: 6991907, 2: 139838159},
        }

        
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
        
        guess_price = 12.5
  
        Lottery.__init__(self, 
            rewards=reward_table,
            guess_price=guess_price,
            guess_table=guess_table
        )