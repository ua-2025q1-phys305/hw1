#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 4: Solving the Heat Equation and Visualizing Results (2 points)
#
# Objective: Solve the 1D heat equation semi-analytically and create a
# visualization of the solution.
#
# Details:
# * You should put the solver in a class, which can be based on
#   assignment 3.
# * Given an arbitrary initial temperature profile, your solver should
#   return a semi-analytical solution of the temperature at arbitrary
#   time.
# * The description of the assignment and the solution template are
#   available in `phys305_hw1/a4.py`.

# From Lecture 4, we learned that the Fourier transform was first
# developed to solve the heat equation. A "Fourier mode" in the
# solution of a heat equation corresponds to a "normal mode" in our
# coupled oscillator equation in lab 3. Instead of oscillating, each
# Fourier mode decays exponentially. This similarity allows us to
# reuse code from `phys305_hw1/a3.py` and modify it to create a heat
# equation solver.

import numpy as np

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for plotting
import matplotlib.pyplot as plt


class HeatSolver:
    """A class to compute the semi-analytical solution of the 1D heat equation
    using the Fourier transform method.

    The heat equation:

        ∂U/∂t = α ∂²U/∂x²

    can be solved by expanding U(x, t) in terms of Fourier modes,
    which decay exponentially over time.  The Fourier coefficients
    evolve as:

        C_k(t) = C_k(0) * exp(-λ_k * t)

    where λ_k = α k² represents the decay rate of each mode and k is
    the wavenumber.

    Attributes:
        C0 (np.ndarray): Initial Fourier coefficients of U(x,0).
        lambd (np.ndarray): Decay rates for each Fourier mode.

    """

    def __init__(self, U0, L=1, alpha=1):
        """Initialize the heat equation solver.

        Args:
            U0 (list or np.ndarray): Initial temperature profile.
            L (float): Length of the computational domain.
            alpha (float): Diffusion coefficient (thermal diffusivity).

        Notes:
        * Assumes **periodic boundary conditions**.
        * The Fourier Transform is used to decompose U0 into modes.

        """
        # TODO: Compute the wave numbers for periodic boundary conditions

        # TODO: Store the initial Fourier transform of U0

        # TODO: Compute decay rates for each Fourier mode

    def __call__(self, t):
        """Compute the temperature profile U(x, t) at a given time t.

        Args:
            t (float): Time at which to compute the temperature profile.

        Returns:
            np.ndarray: The temperature profile U(x, t) at time t.

        """
        # TODO: Compute time evolution of Fourier coefficients

        # TODO: Transform back to real space


if __name__ == "__main__":
    # Define simulation parameters
    T = np.linspace(0, 1, num=101)      # Time grid
    X = np.linspace(-0.5, 0.5, num=65)  # Spatial grid
    U0 = np.exp(-0.5 * X**2 / 0.01)     # Initial Gaussian temperature profile

    # Initialize the heat solver with periodic boundary conditions
    hs = HeatSolver(U0, L=X[-1] - X[0], alpha=0.1)

    # Print temperature profile at each time step and save plots
    print("Time(s)  Temperature Profile")
    print("----------------------------")

    for i, t in enumerate(T):
        U = hs(t)  # Compute temperature profile at time t

        print(f"{t:.2f}", U)  # Print values for reference

        # Plot the temperature profile
        plt.plot(X, U)
        plt.ylim(-0.1, 1.1)
        plt.xlabel("Position $x$")
        plt.ylabel("Temperature $U(x,t)$")
        plt.title(f"Heat Diffusion at $t={t:.2f}$")

        # Save the figure
        plt.savefig(f"{i:04d}.png")
        plt.close()
