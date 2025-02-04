import numpy as np 
import matplotlib.pyplot as plt

# Define the square wave parameters
T = 2 * np.pi  # period - given by the 2 on the angular frequency
A = 1          # amplitude
omega = 2 * np.pi / T  # fundamental angular frequency

# Time vector for one period (more periods can be plotted if desired)
t = np.linspace(-T, T, 1000)

def square_wave_fourier(t, N):
    """
    Compute the Fourier series approximation of a square wave.
    
    Parameters:
        t (np.array): Array of time values.
        N (int): Number of odd harmonics to include (e.g., N=5 sums 1st, 3rd, 5th, 7th, 9th harmonics).
        
    Returns:
        np.array: Fourier series approximation of the square wave.
    """
    f = np.zeros_like(t)
    # Use odd harmonics: 1, 3, 5, ... (2*n-1)
    for n in range(1, N + 1):
        harmonic = 2 * n - 1
        f += (1 / harmonic) * np.sin(harmonic * omega * t)
    f *= (4 * A / np.pi)
    return f

# Choose the number of harmonics for approximation
harmonics = [1, 3, 5, 10, 50]  # different approximations

plt.figure(figsize=(10, 8))

# Plot the approximations
for i, N in enumerate(harmonics, start=1):
    plt.subplot(len(harmonics), 1, i)
    y = square_wave_fourier(t, N)
    plt.plot(t, y, label=f'{N} odd harmonics')
    plt.title(f'Fourier Series Approximation of a Square Wave ({N} odd harmonics)')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.ylim(-1.5 * A, 1.5 * A)
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

# This function uses sine waves to approximate a square wave by adding up multiple waves (harmonics).
# The more harmonics we use, the closer the result gets to a sharp square wave.
# We add only the odd-numbered harmonics (1st, 3rd, 5th, etc.).
# Each harmonic is smaller and helps sharpen the edges of the wave.
# The final result is a combination of waves that looks like a square wave with smoother transitions.
# 1. Defining Parameters:
# - The period (T) is set to 2π, so the fundamental frequency is ω = 2π/T.
# - The amplitude (A) is set to 1.

# 2. Fourier Series Function:
# The `square_wave_fourier` function approximates the square wave using a finite number of odd harmonics.
# For each harmonic n, we add the term: (1 / (2n-1)) * sin((2n-1) * omega * t).

# Elinam Erika Azorliade
# McGovern Twumasi Owusu-Bekoe
# Kevin Papa Kwesi Bekoe
