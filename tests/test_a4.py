# This is a pytest script to test the HeatSolver class from Assignment 4.
# The HeatSolver class should be imported from the solution file.

import numpy as np
from phys305_hw1.a4 import HeatSolver

def test_Solver():
    """Test the HeatSolver class for correctness of the computed
    temperature profile at a fixed time (t=1).

    The test checks:
    1. That the HeatSolver correctly initializes with the given
       parameters.
    2. That the computed temperature profile at t=1 closely matches
       the expected values.

    The expected solution is precomputed for a Gaussian initial
    condition.

    Test Procedure:
    * Define a spatial grid for the problem.
    * Set an initial Gaussian temperature profile.
    * Initialize the HeatSolver instance.
    * Compute the temperature profile at t=1.
    * Compare the computed results with expected values using np.allclose().

    """
    # Define simulation parameters
    X  = np.linspace(-0.5, 0.5, num=65) # Spatial grid
    U0 = np.exp(-0.5 * X**2 / 0.01)     # Initial Gaussian temperature profile

    # Initialize the heat solver with periodic boundary conditions
    hs = HeatSolver(U0, L=X[-1] - X[0], alpha=0.1)

    # Initialize the heat solver with periodic boundary conditions
    hs = HeatSolver(U0, L=X[-1] - X[0], alpha=0.1)

    # Compute temperature profile at t=1
    U1 = hs(1)

    # Reference solution at t=1 (precomputed values)
    U1_ref = [
        0.23894964,0.23902299,0.23916902,0.23938635,0.23967296,0.24002618,
        0.2404427 ,0.24091863,0.24144954,0.24203046,0.24265597,0.24332024,
        0.24401705,0.24473991,0.24548206,0.24623658,0.24699642,0.24775449,
        0.24850371,0.24923708,0.24994775,0.2506291 ,0.25127475,0.25187869,
        0.25243526,0.25293928,0.25338604,0.25377137,0.25409166,0.25434394,
        0.25452584,0.25463566,0.25467238,0.25463566,0.25452584,0.25434394,
        0.25409166,0.25377137,0.25338604,0.25293928,0.25243526,0.25187869,
        0.25127475,0.2506291 ,0.24994775,0.24923708,0.24850371,0.24775449,
        0.24699642,0.24623658,0.24548206,0.24473991,0.24401705,0.24332024,
        0.24265597,0.24203046,0.24144954,0.24091863,0.2404427 ,0.24002618,
        0.23967296,0.23938635,0.23916902,0.23902299,0.23894964]

    # Validate the computed results
    assert np.allclose(U1, U1_ref), (
        "HeatSolver failed: computed temperature profile does not match reference values."
    )
