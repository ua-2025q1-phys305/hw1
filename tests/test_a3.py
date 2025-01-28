# This is a pytest script to test the CoupledOscillators class from
# assignment 3.  This class should be imported from the solution file.

import pytest
import numpy as np

from phys305_hw1.a3 import CoupledOscillators

@pytest.mark.parametrize('params', [
    {'N':2,  'X1':[0.17521471,0.09493644]},
    {'N':4,  'X1':[0.00060096,0.01698677,0.1758158 ,0.09494753]},
    {'N':8,  'X1':[5.36460880e-12,9.66325041e-10,1.25763949e-07,1.10888098e-05,
                   6.01088717e-04,1.69867701e-02,1.75815800e-01,9.49475297e-02]},
    {'N':16, 'X1':[1.32933324e-16,-3.11747666e-17,-4.10060005e-17,-4.85503047e-17,
                   8.74352901e-17, 5.24443263e-18, 1.21991521e-16, 2.24148784e-14,
                   5.36485433e-12, 9.66324942e-10, 1.25763949e-07, 1.10888098e-05,
                   6.01088717e-04, 1.69867701e-02, 1.75815800e-01, 9.49475297e-02]},
])
def test_Oscillators(params):
    X0 = np.zeros(params['N'])
    X0[-1] = 0.5

    co = CoupledOscillators(X0)
    X1 = co(1)

    assert np.allclose(X1, params['X1'])
