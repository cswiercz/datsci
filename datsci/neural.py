r"""Neural Networks
===============

Simple implementation of some neural network stuff from [ESL]_.

Given a collection of nonlinear functions

.. math::

    g_m(\omega_m^T X), \; m=1,\ldots,M,

find parameters $\omega_m$ such that the error

.. math::

    \sum_{i=1}^N \left(y_i - \sum_{m=1}^M g_m(\omega_m^T x_i) \right)^2

is minimized given training data $(x_i, y_i), \; i=1,\ldots,N$. Sometimes, we
choose to minimize over functions $g_m$ as well.

References
----------

[ESL] - Elements of Statistical Learning
"""


