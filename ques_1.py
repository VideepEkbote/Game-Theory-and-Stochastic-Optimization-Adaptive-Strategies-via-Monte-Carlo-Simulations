"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M = 1000000007



def mod_add(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a + b) % M


def mod_multiply(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return (a * b) % M


def mod_divide(a, b):
    a = (a % M + M) % M
    b = (b % M + M) % M
    return mod_multiply(a, pow(b, M - 2, M))


# Problem 1a
def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """

    def f(x, t):
        if x == 0 and t == 2: return 0
        if x == 1 and t == 2: return 1
        if x == 2 and t == 2: return 0
        if dp[x][t] != -1: return dp[x][t]
        if x == 1:
            dp[x][t] = mod_multiply(mod_divide(x, t - 1), f(x, t - 1))
            return dp[x][t]
        if x == t - 1:
            dp[x][t] = mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1))
            return dp[x][t]
        dp[x][t] = mod_add(mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1)),
                           mod_multiply(mod_divide(x, t - 1), f(x, t - 1)))
        # mod_multiply(mod_divide(x ,t - 1) ,(f(x, t - 1))

        return dp[x][t]

    t = alice_wins + bob_wins
    dp = [[-1 for i in range(t + 1)] for j in range(t + 1)]

    dp[0][2] = 0
    dp[1][2] = 1
    dp[2][2] = 0

    return f(alice_wins, t)


# Problem 1b (Expectation)
def calc_expectation(t):
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """

    def f(x, t):
        if x == 0 and t == 2: return 0
        if x == 1 and t == 2: return 1
        if x == 2 and t == 2: return 0
        if dp[x][t] != -1: return dp[x][t]
        if x == 1:
            dp[x][t] = mod_multiply(mod_divide(x, t - 1), f(x, t - 1))
            return dp[x][t]
        if x == t - 1:
            dp[x][t] = mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1))
            return dp[x][t]
        dp[x][t] = mod_add(mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1)),
                           mod_multiply(mod_divide(x, t - 1), f(x, t - 1)))
        # mod_multiply(mod_divide(x ,t - 1) ,(f(x, t - 1))

        return dp[x][t]

    dp = [[-1 for i in range(t + 1)] for j in range(t + 1)]

    dp[0][2] = 0
    dp[1][2] = 1
    dp[2][2] = 0
    s = 0

    for i in range(-(t - 2), t - 1):

        if (i + t) % 2 == 0:
            s = mod_add(s, mod_multiply(i, f((i + t) // 2, t)))
    return s


# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """

    def f(x, t):
        if x == 0 and t == 2: return 0
        if x == 1 and t == 2: return 1
        if x == 2 and t == 2: return 0
        if dp[x][t] != -1: return dp[x][t]
        if x == 1:
            dp[x][t] = mod_multiply(mod_divide(x, t - 1), f(x, t - 1))
            return dp[x][t]
        if x == t - 1:
            dp[x][t] = mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1))
            return dp[x][t]
        dp[x][t] = mod_add(mod_multiply(f(x - 1, t - 1), mod_divide(t - x, t - 1)),
                           mod_multiply(mod_divide(x, t - 1), f(x, t - 1)))
        # mod_multiply(mod_divide(x ,t - 1) ,(f(x, t - 1))

        return dp[x][t]

    dp = [[-1 for i in range(t + 1)] for j in range(t + 1)]

    dp[0][2] = 0
    dp[1][2] = 1
    dp[2][2] = 0
    v = 0

    for i in range(-(t - 2), t - 1):

        if (i + t) % 2 == 0:
            v = mod_add(v, mod_multiply(mod_multiply(i, i), f((i + t) // 2, t)))
    return v
