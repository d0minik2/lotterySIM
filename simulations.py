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
    
    
    def set_guess(self, player_guess: list[list[int]], lottery = None):
        if lottery is not None:
            if lottery.is_guess_correct(player_guess):
                self.guess = player_guess
            else:
                raise("Player's guess is not correct")
        else: 
            self.guess = player_guess
       
        
    def spend_money(self, money: float):
        self.money_spent += money
        
        
    def grant_money(self, money: float):
        self.money_earned += money
    
    
    def generate_guess(self, lottery):
        self.guess = lottery.generate_random_guess()
        return self.get_guess
        

class Lottery:
    def __init__(self,
        rewards: dict[int, float],
        guess_price: float,
        guess_table: list[list[list[int]]]
        ):
        self.rewards = rewards
        self.guess_price = guess_price
        self.guess_table = guess_table
        
        self.correct_guess = None


    def generate_random_guess(self) -> list[list[int]]:
        guess = []
        
        for section in self.guess_table:
            correct_section = []
            
            for numbers in section:
                n = random.choice(numbers)
                
                while n in correct_section: # numbers in each section must be different
                    n = random.choice(numbers) 
                correct_section.append(n)
                
            guess.append(correct_section)

        return guess
    
    
    def generate_winning_numbers(self) -> list[list[int]]:
        self.correct_guess = self.generate_random_guess()
        return self.correct_guess
    
    
    def count_reward(self, player: Player) -> (bool, float):
        guess = player.get_guess()
        correct = []
        max_correct = []
        
        for i, section in enumerate(guess): # count how many correct answers in each section
            section_correct = len(set(section).intersection(set(self.correct_guess[i])))
            correct.append(section_correct)
            
            if section_correct == len(section):
                max_correct.append(True)
            else:
                max_correct.append(False)
        
        price = self.rewards.copy()
        for i in correct:
            price = price[i]
        
        return (all(max_correct), price)
        
    
    def play_round(self, player: Player) -> bool:
        # returns true when won the top price
        
        self.generate_winning_numbers()
        
        correct, won_money = self.count_reward(player)
        
        player.spend_money(self.guess_price)
        player.grant_money(won_money) 
        
        return correct
    
    
    def is_guess_correct(self, guess: list[int]) -> bool:
        if not isinstance(guess, (list, tuple)): # wrong formant
            return False
        
        for i, s in enumerate(guess):
            if not isinstance(s, (list, tuple)): # wrong formant
                return False
            
            if len(s) != len(self.guess_table[i]): # wrong format
                return False
            
            for j, n in enumerate(s):
                if n not in self.guess_table[i][j]: # number must be defined in guess table
                    return False
                
                if n in s[:j]: # numbers in section cant repeat
                    return False
                
        return True
    

    
class Simulation:
    def __init__(self,
        lottery: Lottery,
        player: Player = None,
        rounds_per_week: int = 1,
    ):
        self.lottery = lottery
        
        if player is not None:
            self.player = player
        else:
            self.player = Player() # create default player
        
        self.rounds_per_week = rounds_per_week
        
        self.years_passed = 0
        self.weeks_passed = 0
        self.top_price_wins = 0
    
    
    def get_balance(self) -> float:
        return self.player.get_balance()
    
    
    def simulate_week(self):
        for _ in range(self.rounds_per_week):
            if self.lottery.play_round(self.player):
                self.top_price_wins += 1
        self.weeks_passed += 1
     
      
    def simulate_year(self):
        for _ in range(52):
            self.simulate_week()
        self.years_passed += 1
    
    
    def simulate_years(self, n, log=False):
        for _ in range(n):
            self.simulate_year()
            
            if log:
                print(self.get_results())
    
    
    def simulate_years_until_won(self, n_of_wins=1, log=False):
        while self.top_price_wins < n_of_wins:
            self.simulate_year()
            
            if log:
                print(self.get_results())
        
    
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