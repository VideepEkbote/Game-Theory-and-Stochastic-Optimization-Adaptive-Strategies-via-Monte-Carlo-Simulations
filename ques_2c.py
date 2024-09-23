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
        Decide Alice's play style for the current round.

        Returns:
            0 : attack
            1 : balanced
            2 : defence

        """
        n = len(self.results)
        nA = self.points
        nB = n - self.points
        if self.results[-1] == 1:
            if (nB) / (nB + nA) > 6 / 11:
                return 0
            else:
                return 2
        elif self.results[-1] == 0.5:
            return 0
        else:
            return 1
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
        pass


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
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:
            return 0

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
    frompayoff = payoff_matrix[ya][yb]  # probabilty 3 tuple from payoffmatrix

    outcomes = [1.0, 0.5, 0.0]
    resultofround = random.choices(outcomes, frompayoff)[0]  # weighted choice
    alice.observe_result(ya, yb, resultofround)
    bob.observe_result(yb, ya, 1 - resultofround)
    # return alice.points, bob.points, resultofround


def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    num_rounds = 1000
    payoff_matrix = [[[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]],
                     [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 1 / 5]],
                     [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]

    expected = 0

    for iteration in range(num_rounds):
        mat = payoff_matrix
        wins = 1
        alice = Alice()
        bob = Bob()
        curexpected = 0
        while wins <= T:
            simulate_round(alice, bob, payoff_matrix)
            mat[0][0] = [bob.points / (alice.points + bob.points), 0, alice.points / (alice.points + bob.points)]
            if alice.results[-1] == 1:
                wins += 1
            curexpected += 1
        expected += curexpected
    return expected / num_rounds



