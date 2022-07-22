# Import libraries
import numpy as np

def cosine(x, x1, x2):
    """Returns cosine value (y) for given time step (x) in one period (T) based on the interval between x1 and x2.

    Args:
        x (float): time step
        x1 (float): period start (y=1)
        x2 (float): period end (y=1)

    Returns:
        val (float): cosine value
    """
    from math import cos, pi
    T = x2-x1
    val = 0.5 * cos(2.0 * pi * (x - x1) / T)
    return val

def rpeaks_cosine_interpolation(rpeaks_idx, length):
    """Returns a cosine interpolation with varying frequency for successive events (rpeaks_idx) of a binary time series.

    Args:
        rpeaks_idx (array): index of r-peaks in the time series
        length (int): length of the time series

    Returns:
        rpeaks_cip : cosine interpolation of rpeaks
    """
    import numpy as np
    num_rpeaks = len(rpeaks_idx)
    
    # Interpolation
    rpeaks_cip = [np.nan]*(rpeaks_idx[0])

    for i in range(num_rpeaks):
        if i == num_rpeaks-1:
            break
        x1 = rpeaks_idx[i]
        x2 = rpeaks_idx[i+1]
        T = x2-x1
        f = lambda x: cosine(x, x1, x2)
        # span interval with corresponding number of time steps
        x = np.linspace(x1, x2, T)
        y = [f(x) for x in x]
        rpeaks_cip = rpeaks_cip + y

    rpeaks_cip = rpeaks_cip + [np.nan]*(length-rpeaks_idx[-1])
    # keep in mind: there are nans at the start and end

    return rpeaks_cip