import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    gx = np.polyval(g_coeffs, x)
    hx = np.polyval(h_coeffs, x)
    
    if hx == 0.0:
        return 0.0

    g_prime_coeffs= np.arange(len(g_coeffs)-1, 0, -1)*g_coeffs[:-1]
    h_prime_coeffs = np.arange(len(h_coeffs)-1, 0,-1)*h_coeffs[:-1]

    g_prime = np.polyval(g_prime_coeffs, x)
    h_prime = np.polyval(h_prime_coeffs, x)

    derivative= ((g_prime * hx ) - (gx * h_prime ))/(hx**2 )

    return derivative 

    pass