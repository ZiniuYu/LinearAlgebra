Chapter 2.2 The idea of Elimination
===================================

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

    **Pivot**: first nonzero in the row that does the elimination.

    **Multiplier**: (entry to eliminate) divided by (pivot).

*To solve* :math:`n` *equations we want* :math:`n` *pivots*.
**The pivots are on the diagonal of the triangle after elimination**.

Breakdown of Elimination
------------------------

* Permanet failure with no solution.

* Failure with infinitely many solutions.

* Temporary failure (zero in pivot). A row exchange produces two pivots.

**Failure**: For :math:`n` equations we do not get :math:`n` pivots.

**Elimination leads to an equation**
:math:`\bs{0} \neq \bs{0}` (no solution) or :math:`\bs{0} = \bs{0}` (many solutions)

**Success comes with** :math:`\bs{n}` **pivots.**
**But we may have to exchange the** :math:`\bs{n}` **equations.**

Three Equations in Three Unknowns
---------------------------------

.. math::

    2x + 4y - 2z &= 2

    4x + 9y - 3z &= 8

    -2x - 3y + 7z &= 10
    
**Step 1**: Subtract 2 times equation 1 from equation2.
This leaves :math:`y+z=4`.

**Step 2**: Subtract -1 times equation 1 from equation 3.
This leaves :math:`y+5z=12`.

    :math:`\x` **is eliminated**:
    :math:`\begin{matrix} 1y+1z=4 \\ 1y+5z=12 \end{matrix}`

**Step 3**: Subtract equation 2\ :sub:`new` from 3\ :sub:`new`.
The multiplier is :math:`1/1=1`.
Then :math:`4z=8`.

The original :math:`A\x = \b` has been converted into an upper triangular :math:`U\x = \bs{c}`:

.. math::

    2x + 4y - 2z &= 2
    
    1y + 1z &= 4
    
    4z &= 8

The solution is :math:`(x,y,z) = (-1,2,2)`.

Elimination from :math:`A` to :math:`U`
---------------------------------------

For a 4 by 4 problem, or an :math:`n` by :math:`n` problem, elimination proceeds in the same way.

**Column 1**: Use the first equation to create zeros below the first pivot.

**Column 2**: Use the new equation 2 to create zeros below the secod pivot.

**Column 3 to** :math:`\bs{n}`: Keep going to find all :math:`n` pivots and the upper triangular :math:`U`.

After column 2 we have :math:`\bb x&x&x&x \\ 0&x&x&x \\ 0&0&x&x \\ 0&0&x&x \eb`.
We want :math:`\bb x&x&x&x \\ &x&x&x \\ &&x&x \\ &&&x \eb`.

The result of forward elimination is an upper triangular system.
It is nonsigular if there is a full set of :math:`n` pivots.