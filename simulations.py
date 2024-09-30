import typing
import random



class Player:
    def __init__(self, guess=[]):
        self.money_spent = 0
        self.money_earned = 0
        self.balance = 0

        self.set_guess(guess)
    
    def get_guess(self) -> list[int]:
        return self.guess
    
    def get_balance(self) -> float:
        self.balance = self.money_earned - self.money_spent
        return self.balance
    
    def set_guess(self, player_guess: list[int], lottery = None):
        if lottery is not None:
            if lottery.is_guess_correct(player_guess):
                self.guess = player_guess
        self.guess = player_guess #TODO temporary
        
    def spend_money(self, money: float):
        self.money_spent += money
        
    def grant_money(self, money: float):
        self.money_earned += money
    
    def generate_guess(self, lottery):
        self.guess = []
        
        for i in range(lottery.no_guesses):
            n = random.choice(lottery.numbers) 
            
            while n in self.guess:
                n = random.choice(self.guess) 
            self.guess.append(n)

        

class Lottery:
    def __init__(self,
        rewards: dict[int, float],
        guess_price: float,
        no_guesses: int,
        numbers: list[int]
        ):
        self.rewards = rewards
        self.guess_price = guess_price
        self.no_guesses = no_guesses
        self.numbers = numbers
        
        self.correct_numbers = []

    def generate_winning_numbers(self) -> list[int]:
        self.correct_numbers = []
        
        for i in range(self.no_guesses):
            n = random.choice(self.numbers) 
            while n in self.correct_numbers:
                n = random.choice(self.numbers) 
            self.correct_numbers.append(n)
    
    def play_round(self, player: Player) -> bool:
        # returns true when won the top price
        
        self.generate_winning_numbers()
        
        # count how many numbers are the same
        correct = len(set(player.get_guess()).intersection(set(self.correct_numbers)))
        won_money = self.rewards[correct]
        player.spend_money(self.guess_price)
        player.grant_money(won_money) 
        
        if correct == self.no_guesses:
            return True
        return False
    
    def is_guess_correct(self, guess: list[int]) -> bool:
        if not isinstance(guess, (list, tuple)):
            raise(f"Guess should be a list of numbers")
        
        for i, n in enumerate(guess):
            if n not in self.numbers:
                raise(f"Guess not correct, {n} is not a correct guess")
                # return False
            if n in guess[:i]:
                raise(f"Guess not correct, numbers can't repeat")
                # return False
                
        if len(guess) != self.no_guesses:
            raise(f"Guess not correct, there should be {self.no_guesses} numbers, not {len(guess)}")
            # return False
            
        return True
    

    
class Simulation:
    def __init__(self,
        lottery: Lottery,
        player: Player,
        rounds_per_week: int,
    ):
        self.lottery = lottery
        self.player = player
        
        self.rounds_per_week = rounds_per_week
        
        self.years_passed = 0
        self.weeks_passed = 0
        self.top_price_wins = 0
    
    def get_balance(self) -> float:
        return self.player.get_balance()
    
    def simulate_week(self):
        for i in range(self.rounds_per_week):
            if self.lottery.play_round(self.player):
                self.top_price_wins += 1
        self.weeks_passed += 1
      
    def simulate_year(self):
        for i in range(52):
            self.simulate_week()
        self.years_passed += 1
    
    def get_results(self) -> str: 
        result = (
            f"simulated {self.years_passed} years\n"
            f"money spent: {self.player.money_spent}\n"
            f"money won: {self.player.money_earned}\n"
            f"total balance: {self.get_balance()}\n"
            f"won the top price {self.top_price_wins} times\n\n"
        )
        return result
    
    def __str__(self):
        return self.get_results()