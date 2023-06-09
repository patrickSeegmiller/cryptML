
def horners_polynomial_evaluation(polynomial_coefficients: list[float or int], input_value: (float or int)) -> float:
    """
    Evaluates a polynomial using Horner's method given its coefficients and an input value.

    Args:
        polynomial_coefficients (list[float]): The coefficients of the polynomial in descending order of degree.
        input_value (float): The value at which the polynomial is evaluated.

    Returns:
        float: The result of evaluating the polynomial at the given input value.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that polynomial_coefficients is a list of integers or floats
    # and that input_value is an integer or float.
    if not isinstance(polynomial_coefficients, list) or not all(isinstance(coeff, (int, float)) for coeff in polynomial_coefficients):
        raise ValueError("Polynomial coefficients must be a list of integers or floats.")
    if not isinstance(input_value, (int, float)):
        raise ValueError("Input value must be an integer or float.")
    
    # Evaluate the polynomial using Horner's method
    for coefficient in polynomial_coefficients:
        result = result * input_value + coefficient

    # Return the result
    return result

def synthetic_division(polynomial_coefficients: list[float], constant_term: float) -> list[float]:
    """
    Performs synthetic division on a polynomial given its coefficients and a constant term.

    Args:
        polynomial_coefficients (list[float]): The coefficients of the polynomial in descending order of degree.
        constant_term (float): The constant term used in synthetic division.

    Returns:
        list[float]: The coefficients of the resulting polynomial after synthetic division.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that polynomial_coefficients is a list of integers.
    if not isinstance(polynomial_coefficients, list) or not all(isinstance(coeff, int) for coeff in polynomial_coefficients):
        raise ValueError("Polynomial coefficients must be a list of integers or floats.")
    if not isinstance(constant_term, int):
        raise ValueError("Constant term must be an integer or float.")
    
    # Perform synthetic division
    remainder = 0
    resultant_coefficients = []
    for coefficient in polynomial_coefficients:
        resultant_coefficients.append(coefficient + remainder * constant_term)

    # Return the coefficients of the resulting polynomial
    return resultant_coefficients

def polynomial_long_division(dividend: list[float], divisor: list[float]) -> list[tuple[float, int]]:
    """
    Performs polynomial long division on a dividend and divisor given their coefficients, producing a list of tuples containing 
    the nonzero coefficients of the quotient and remainder of the polynomial long division, both in descending order of degree, paired
    with their respective degrees.

    Args:
        dividend (list[float]): The coefficients of the dividend in descending order of degree.
        divisor (list[float]): The coefficients of the divisor in descending order of degree.

    Returns:
        tuple[list[float], list[float]]: A tuple containing the coefficients of the quotient and remainder of the
        polynomial long division, both in descending order of degree.

    Raises:
        ValueError: If the input parameters are not in the expected format.
    """

    # First, check that the input is valid by checking that dividend and divisor are lists of integers.
    if not isinstance(dividend, list) or not all(isinstance(coeff, int) for coeff in dividend):
        raise ValueError("Dividend coefficients must be a list of integers or floats.")
    if not isinstance(divisor, list) or not all(isinstance(coeff, int) for coeff in divisor):
        raise ValueError("Divisor coefficients must be a list of integers or floats.")
    
    #TODO: Check this function for correctness and test it

    # Perform polynomial long division
    quotient = []
    remainder = dividend
    while len(remainder) >= len(divisor):
        # Determine the degree of the next term of the quotient
        quotient_degree = len(remainder) - len(divisor)
        
        # Determine the coefficient of the next term of the quotient
        quotient_coefficient = remainder[0] / divisor[0]

        # Add the next term of the quotient to the quotient list
        quotient.append((quotient_coefficient, quotient_degree))

        # Subtract the next term of the quotient multiplied by the divisor from the remainder
        remainder = [remainder[i] - quotient_coefficient * divisor[i] for i in range(len(divisor))] + remainder[len(divisor):]

    # Return the quotient and remainder
    return (quotient, remainder)

def infinite_polynomial_long_division(dividend: list[float], divisor: list[float], num_terms: int) -> list[tuple[float, int]]:
    """
    A functiont that produces the first num_terms terms of the quotient of a polynomial long division. For use
    in quotients involving infinite series.

    Args:
        dividend (list[float]): The coefficients of the dividend in descending order of degree.
        divisor (list[float]): The coefficients of the divisor in descending order of degree.
        num_terms (int): The maximum degree of the quotient to be produced.

    Returns:
        tuple[list[float], list[float]]: A tuple containing the coefficients of the quotient and remainder of the
        polynomial long division, both in descending order of degree.

    Raises:
        ValueError: If dividend or divisor are not lists of floats or integers.
        ValueError: If num_terms is not an integer.
    
    """

    # First, check that the input is valid by checking that dividend and divisor are lists of integers.
    if not isinstance(dividend, list) or not all(isinstance(coeff, (int, float)) for coeff in dividend):
        raise ValueError("Dividend coefficients must be a list of integers or floats.")
    if not isinstance(divisor, list) or not all(isinstance(coeff, (int, float)) for coeff in divisor):
        raise ValueError("Divisor coefficients must be a list of integers or floats.")
    if not isinstance(num_terms, int):
        raise ValueError("Number of terms must be an integer.")
    

    #TODO Check this function for correctness and test it

    # Perform polynomial long division
    quotient = []
    remainder = dividend
    for i in range(num_terms):
        # Determine the degree of the next term of the quotient
        quotient_degree = len(remainder) - len(divisor)
        
        # Determine the coefficient of the next term of the quotient
        quotient_coefficient = remainder[0] / divisor[0]

        # Add the next term of the quotient to the quotient list
        quotient.append((quotient_coefficient, quotient_degree))

        # Subtract the next term of the quotient multiplied by the divisor from the remainder
        remainder = [remainder[i] - quotient_coefficient * divisor[i] for i in range(len(divisor))] + remainder[len(divisor):]

    # Return the quotient and remainder
    return (quotient, remainder)

