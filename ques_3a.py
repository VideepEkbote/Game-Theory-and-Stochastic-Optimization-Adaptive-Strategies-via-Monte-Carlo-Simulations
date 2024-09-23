import random
import time


class Alice:
    def __init__(self):
        self.past_play_styles = [1, 1]
        self.results = [1, 0]
        self.opp_play_styles = [1, 1]
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.

        Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        nA = self.points
        nB = len(self.results) - nA
        if nB / (nA + nB) > 15 / 44:
            return 0
        else:
            return 2

        pass

    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.

        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result


class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1, 1]
        self.results = [0, 1]
        self.opp_play_styles = [1, 1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        move = random.choice([0, 1, 2])
        return move

    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.

        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result


def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.

    Returns:
        None
    """
    ya = alice.play_move()
    yb = bob.play_move()
    frompayoff = payoff_matrix[ya][yb]

    outcomes = [1.0, 0.5, 0.0]
    resultofround = random.choices(outcomes, frompayoff)[0]
    alice.observe_result(ya, yb, resultofround)
    bob.observe_result(yb, ya, 1 - resultofround)
    # return alice.points, bob.points, resultofround


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.

    Returns:
        None
    """
    payoff_matrix = [[[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]],
                     [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 1 / 5]],
                     [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]

    alice = Alice()
    bob = Bob()

    for iteration in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)
        payoff_matrix[0][0] = [bob.points / (alice.points + bob.points), 0, alice.points / (alice.points + bob.points)]

    #return alice.points, bob.points, payoff_matrix


if __name__ == "__main__":
    monte_carlo(num_rounds=100000)
# Run Monte Carlo simulation with a specified number of rounds