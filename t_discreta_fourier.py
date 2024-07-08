from scipy.fft import fft
import numpy as np
x = np.array([1.0, 3.0, 4.0, 7.0, 3.0, 5.0, -1.0])
y = fft(x)
print(y)