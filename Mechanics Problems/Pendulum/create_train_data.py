import numpy as np
import pandas as pd
from math import sin, pi

g = 9.81

# Differential equation for the pendulum
def pendulum_equation(theta, omega, l):
    return omega, -(g / l) * sin(theta)

# Runge-Kutta 4th Order Method
def runge_kutta4(y0, t0, tf, dt, length, f):
    times = np.arange(t0, tf, dt)
    y = np.zeros((len(times), len(y0)))
    y[0] = y0

    for i in range(1, len(times)):
        k1 = np.array(f(*y[i - 1], length)) * dt
        k2 = np.array(f(*(y[i - 1] + k1 / 2), length)) * dt
        k3 = np.array(f(*(y[i - 1] + k2 / 2), length)) * dt
        k4 = np.array(f(*(y[i - 1] + k3), length)) * dt
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return times, y

# Generate data
data = []
max_rows = 5000
num_simulations = 10
rows_per_simulation = max_rows // num_simulations

# Define ranges for theta0 and omega0
theta0_range = np.linspace(0, 2 * pi, 20)
omega0_range = np.linspace(-10, 10, 20)

for i in range(num_simulations):
    theta0 = np.random.choice(theta0_range)
    omega0 = np.random.choice(omega0_range)
    length = np.random.uniform(0.1,2)  # Random length

    t, sol = runge_kutta4([theta0, omega0], 0, 120, 0.5, length, pendulum_equation)
    x = length * np.sin(sol[:, 0]) + np.random.uniform(-0.1, 0.1, len(sol))  # Adding noise
    y = -length * np.cos(sol[:, 0]) + np.random.uniform(-0.1, 0.1, len(sol))  # Adding noise
    data.append(pd.DataFrame({'Time': t[:rows_per_simulation], 'X': x[:rows_per_simulation], 'Y': y[:rows_per_simulation], 'Theta0': theta0, 'Omega0': omega0, 'Length': length}))

combined_data = pd.concat(data)
combined_data.to_csv('pendulum_data.csv', index=False)