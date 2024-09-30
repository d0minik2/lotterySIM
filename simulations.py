import typing
from random import randint

# TODO czy podane liczby maja zmieniać się co rundę?


class Player:
    def __init__(self):
        self.balance = 0
        self.money_spent = 0
        self.money_won = 0
        # TODO player guess?
    
    def get_guess(self) -> list[int]:
        pass
    
    def get_balance(self) -> float:
        pass
    
    def set_guess(self, player_guess: list[int], lottery = None):
        pass
    
    def generate_guess(self, lottery):
        pass
        


class Lottery:
    def __init__(self,
        rewards: dict[int, float],
        guess_price: float,
        no_guesses: int,
        numbers: list[int]
        ):
        pass
    
    def is_guess_correct(self, guess) -> bool:
        pass
    
    def generate_winning_numbers(self) -> list[int]:
        pass
    
    def play_round(self, player: Player) -> bool:
        # returns true when won the top price
        pass
    

    
class Simulation:
    def __init__(self,
        lottery: Lottery,
        player: Player,
        rounds_per_week: int,
    ):
        self.years_passed = 0
        self.weeks_passed = 0
        pass
    
    def get_balance(self) -> float:
        pass
    
    def simulate_week(self):
        pass
      
    def simulate_year(self):
        pass
    
    def get_results(self) -> str:
        # simulated {} years
        # 
        # money spent: {}
        # money won: {}
        # total balance: {}
        # 
        # won the top price {} times
        pass
    
    def __str__(self):
        return self.get_results()