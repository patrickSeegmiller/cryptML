from whole_number_operations import fast_powering_algorithm, integer_sqrt, is_square, integer_nthrt, find_modular_inverse, greatest_common_divisor, absolute_value
from rational_number_operations import get_cf_convergents, cf_expansion

def continued_fraction_factorization(e, N):
    """
    TODO: Docstring
    """

    convergents = get_cf_convergents(cf_expansion(e, N))

    for num, denom in convergents:
        if num == 0:
            continue
        p, q = integer_quadratic_formula(1, ((e*denom - 1) // num) - N - 1, N)
        if (p != None) and (q!= None):
            if (p * q) == N:
                return [p, q]

    return None

def fermat_factorization(n: int) -> list[int]:
    '''
        Performs Fermat's method for factoring an odd number `n`.
    
        Fermat's method relies on the fact that any odd number can be expressed 
        as a difference of squares. It checks numbers near the square root of `n` 
        for ways in which `n` can be written as a difference of perfect squares. 
        If `n = b^2 - a^2`, it factors as `n = (b-a)(b+a)`.

    Args:
        n (int): The number to be factored.

    Returns:
        list[int]: A list containing the two factors of `n`.

    Raises:
        ValueError: If `n` is not an odd number greater than 1.

    '''

    # We first check that n is an odd number greater than 1.
    if not isinstance(n, int) or n <= 1 or n % 2 == 0: 
        raise ValueError("n should be an odd number greater than 1.")
    
    # Next we check whether n is a perfect square.
    if is_square(n):
        return [integer_sqrt(n), integer_sqrt(n)]

    # Now we perform Fermat's method, starting with a = sqrt(n) + 1.
    # We check whether a^2 - n is a perfect square. If not, we increment a by 1 and repeat.
    try:
        a = integer_sqrt(n-1) + 1
        b_squared = a*a - n
        while not is_square(b_squared):
            a = a + 1
            b_squared = a*a - n
    except KeyboardInterrupt:
        print("Fermat's method was interrupted by the user.")
        return None

    # We return the factors of n.
    return [a - integer_sqrt(b_squared), a + integer_sqrt(b_squared)]

def known_decryption_key_factorization(decryption_key, public_exponent, modulus):
    """
    TODO: Docstring
    """
    k = d*e - 1
    factors_of_two = 0
    while k % 2 == 0:
        factors_of_two += 1
        k = k // 2

def pollard_p_minus_one_factorization(N):
    """
    TODO: Docstring
    """
    UPPER_BOUND = 1000000

    a = 2 #Other choices of 'a' can be used here.
    for i in range(2, UPPER_BOUND):
        a = fast_powering_algorithm(a, i, N)
        d = greatest_common_divisor(a - 1, N)
        if 1 < d and d < N:
            print(f"Pollard's p - 1 Factorization Algorithm factored {N}: ", end="")
            return [d, N // d]

    print(f"Pollard's p - 1 Factorization Algorithm did not succeed in finding a non trivial factor of {N} with an upper bound of {UPPER_BOUND}.")
    return None

def pollard_rho_factorization(N):
    """
    TODO: Docstring
    """
    MAX_ITERATIONS = 1000000
    
    x = 1 #Other choices of 'x' and 'y' can be used here.
    y = 2
    g = greatest_common_divisor(absolute_value(y - x), N)
    for i in range(MAX_ITERATIONS):
        x = (x**2 + 1) % N
        y = (y**2 + 1) % N
        y = (y**2 + 1) % N
        g = greatest_common_divisor(absolute_value(y - x), N)
        if g > 1 and g < N:
            return [g, N // g] 
            
    print(f"The maximum number of iterations has been reached without finding any nontrivial factors of {N}.") 
  