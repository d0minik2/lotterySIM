from default_config import *
from simulations import *


if __name__ == "__main__":
    player = Player()
    
    lotto = Lottery(
        rewards=REWARD_TABLE,
        guess_price=GUESS_PRICE,
        guess_table=GUESS_TABLE,
        )
     
    simulation = Simulation(
        lottery=lotto,
        player=player,
        rounds_per_week=ROUNDS_PER_WEEK
        )
    
    
    player.generate_guess(lotto) # chybił trafił
    
    # player.set_guess([23, 13, 12, 41, 34, 32], lottery=lotto)
    # player.set_guess([[25, 49, 10, 1, 48], [4, 2]], lottery=lotto)
    
    simulation.simulate_years_until_won(log=True)