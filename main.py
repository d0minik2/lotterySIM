from default_config import *
from simulations import *


if __name__ == "__main__":
    player = Player()
    
    lotto = Lottery(
        rewards=REWARD_TABLE,
        guess_price=GUESS_PRICE,
        no_guesses=NO_GUESSES,
        numbers=NUMBERS
        )
    
    simulation = Simulation(
        lottery=lotto,
        player=player,
        rounds_per_week=ROUNDS_PER_WEEK
        )
    
    
    player.generate_guess(lotto) # chybił trafił
    
    # player.set_guess([23, 13, 12, 41, 34, 32], lottery=lotto)
    
    for _ in range(100000):
        simulation.simulate_year()
        print(simulation.get_results())
    