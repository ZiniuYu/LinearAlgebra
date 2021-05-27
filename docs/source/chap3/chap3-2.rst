Chapter 3.2 The Nullspace of :math:`A`: Solving :math:`Ax = 0` and :math:`Rx=0`
=================================================================================

For a :math:`m` by :math:`n` matrix, one immediate solution to :math:`A\x=\bs{0}` is :math:`\x=\bs{0}`.
For invertible matrices this is the only solution.
For other non-invertible matrices, there are nonzero solutions to :math:`A\x=\bs{0}`.
*Each solution* :math:`\x` *belongs to the nullspace of* :math:`A`.

.. note::

    The nullspace :math:`N(A)` consists of all solutions to :math:`A\x=\bs{0}`.
    These vectors :math:`\x` are in :math:`\R^n`.

The solution vectors :math:`\x` have :math:`n` components.
They are vectors in :math:`\R^n`, so *the nullspace is a subspace of* :math:`\R^n`.
The column space :math:`\bs{C}(A)` is a subspace of :math:`\R^m`.

.. note::

    **Special solution** :math:`A\bs{s}=\bs{0}`: The nullspace of 
    :math:`A=\bb 1&2\\3&6 \eb` contains all multiples of 
    :math:`\bs{s} = \bb -2\\1 \eb`.

This is the best way to describe the nullspace, by computing special solutions to :math:`A\x=\bs{0}`.
**The solution is special because we set the free variable to** :math:`\bs{x_2=1}`.

.. Tip::

    The nullspace of :math:`A` consists of all combinations of the special solutions to :math:`A\x=\bs{0}`.

.. math::

    \bb 1&2&3 \eb\bb x\\y\\z \eb = 0 \mathrm{\ has\ two\ special\ solutions\ }
    \bs{s}_1 = \bb -2\\1\\0 \eb \mathrm{\ and\ } \bs{s}_2 = \bb -3\\0\\1 \eb.

*The last two components of* :math:`\bs{s}_1` *and* :math:`\bs{s}_2` 
*are "free" and we choose them specially as* 1,0 *and* 0,1.
Then the first components -2 and -3 are determined by the equation :math:`A\x=\bs{0}`.

Pivot Columns and Free columns
------------------------------

The first column of :math:`A=\bb 1&2&3 \eb` contains the only pivot, so the first component of :math:`\x` is *not free*.
**The free components correspond to columns with no pivots**.
The special choice (one or zero) is only for the free variables in the special solutions.

The Reduced Row Echelon Form :math:`R`
--------------------------------------


The Rank of a Matrix
--------------------


Rank One
--------