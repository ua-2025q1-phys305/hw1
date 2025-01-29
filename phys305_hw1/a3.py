#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 3: Rewriting the Coupled Harmonic Oscillator (2 points)
#
# Objective: Take the coupled harmonic oscillator problem we solved in
# the lab and rewrite it using a well-structured Python class.
#
# Details:
# * Your implementation should encapsulate the behavior and parameters
#   of the system in an object*oriented design.
# * Ensure your class includes methods to compute the system's
#   dynamics.
# * The description of the assignment and the solution template can be
#   found in phys305_hw1/a3.py.

# From lab 3, we solve systems of coupled harmonic oscillators
# semi-analytically by numerically solving eigenvalue problems.
# However, the code structure was not very clean, making the code hard
# to reuse.  Although numerical analysis in general does not require
# object-oriented programming, it is sometime useful to package
# stateful caluation into classes.  For this assignment, we will
# provide a template class.  Your responsibility to implement the
# methods in the class.

import numpy as np

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for plotting
import matplotlib.pyplot as plt


class CoupledOscillators:
    """A class to model and simulate a system of coupled harmonic
    oscillators.

    Attributes:
        Omega (np.ndarray): Array of angular frequencies of the normal modes.
        V (np.ndarray): Matrix of eigenvectors representing normal modes.
        M0 (np.ndarray): Initial amplitudes of the normal modes.

    """

    def __init__(self, X0=[-0.5, 0, 0.5], m=1.0, k=1.0):
        """Initialize the coupled harmonic oscillator system.

        Args:
            X0 (list or np.ndarray): Initial displacements of the oscillators.
            m (float): Mass of each oscillator (assumed identical).
            k (float): Spring constant (assumed identical for all springs).

        """
        # TODO: Construct the stiffness matrix K

        # TODO: Solve the eigenvalue problem for K to find normal modes

        # TODO: Store angular frequencies and eigenvectors

        # TODO: Compute initial modal amplitudes M0 (normal mode decomposition)

    def __call__(self, t):
        """Calculate the displacements of the oscillators at time t.

        Args:
            t (float): Time at which to compute the displacements.

        Returns:
            np.ndarray: Displacements of the oscillators at time t.

        """
        # TODO: Reconstruct the displacements from normal modes


if __name__ == "__main__":
    # Define the time array for simulation
    T = np.linspace(0, 10, num=101)

    # Initialize the coupled oscillator system with default parameters
    co = CoupledOscillators()

    # Print displacements of the oscillators at each time step
    print("Time(s)  Displacements")
    print("----------------------")
    for t in T:
        X = co(t)  # Compute displacements at time t

        print(f"{t:.2f}", X)  # Print values for reference
