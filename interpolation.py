def lagrange_interpolate(X, Y):
    """
    Lagrange interpolation
    :param X: X values
    :param Y: Y values
    :return: interpolation polynomial function
    """
        
    def P(x):
        """
        Interpolation polynomial
        :param x: x value
        :return: y value
        """
        y = 0
        for j in range(len(X)):
            p = 1
            for i in range(len(X)):
                if i != j:
                    p *= (x - X[i]) / (X[j] - X[i])
            y += Y[j] * p
        return y

    return P
