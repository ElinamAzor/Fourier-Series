import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 2 * np.pi  # Period of the square wave
N = 10  # Number of harmonics
x = np.linspace(0, T, 1000)  # Time domain

# Define square wave using Fourier series
def square_wave(x, harmonics):
    wave = np.zeros_like(x)
    for n in range(1, harmonics * 2, 2):  # Only odd harmonics
        wave += (4 / (np.pi * n)) * np.sin(n * x)
    return wave

# Plot the transformation
plt.figure(figsize=(10, 6))
for i in range(1, N + 1):
    y = square_wave(x, i)
    plt.plot(x, y, label=f'{i} Harmonic(s)')

# Adding labels and legend
plt.title('Transformation of Square Wave to Sinusoidal Wave')
plt.xlabel('x (radians)')
plt.ylabel('Amplitude')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(alpha=0.4)
plt.legend(loc='upper right', fontsize='small')

plt.show()