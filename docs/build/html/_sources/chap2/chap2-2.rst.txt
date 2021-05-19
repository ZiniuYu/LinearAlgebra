Chapter2.2 The idea of Elimination
==================================

For 2 by 2 equations, before elimination, :math:`x` and :math:`y` appear in both equations. 
After elimination, the first unknown :math:`x` has disappeared from the second equation.

**Before**:

.. math::

    x - 2y &= 1

    3x + 2y &= 11

**After** (multiply equation 1 by 3, subtract to eliminate :math:`3x`):

.. math::
    
    x - 2y &= 1

    8y &= 8

The goal of elimination: produces an **upper triangular system**. 
The system is solved from the bottom upwards.
This process is called **back substitution**. 
It is used for upper triangular systems of any size, after elimination gives a triangle.

If the first equation is changed to :math:`4x - 8y = 4`, the multiplier changes to :math:`l = \frac{3}{4}`.
*To find the multiplier, divide the coefficient 3 to be eliminated by the pivot 4*:

.. math::

    \bs{4}x - 8y &= 4

    \bs{3}x + 2y &= 11

**Multiply eqution 1 by 3/4 and subtract from equation 2**:

.. math::
    
    4x - 8y &= 4

    8y &= 8

.. note::

    **Pivot**: first nonzero in the row that does the elimination

    **Multiplier**: (entry to eliminate) divided by (pivot)

*To solve n equations we want n pivots*.
**The pivots are on the diagonal of the triangle after elimination**.

Breakdown of Elimination
------------------------

Three Equations in Three Unknowns
---------------------------------

Elimination from :math:`A` to :math:`U`
---------------------------------------