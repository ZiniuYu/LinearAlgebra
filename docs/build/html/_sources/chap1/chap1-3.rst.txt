Chapter 1.3 Matrices
====================

The linear combinations of the three vectors 
:math:`\u = (1, -1, 0)`, :math:`\v = (0, 1, -1)`, :math:`\w = (0, 0, 1)`
are :math:`x_1\u + x_2\v + x_3\w`:

.. math::

    x_1 \bb 1 \\ -1 \\ 0 \eb + x_2 \bb 0 \\ 1 \\ -1 \eb + x_3 \bb 0 \\ 0 \\ 1 \eb
    = \bb x_1 \\ x_2 - x_1 \\ x_3 - x_2 \eb.

Rewrite that combination using a matrix:

.. note::

    **Matrix times vector**, **Combination of columns**:

    * :math:`A\x = \bb 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb \bb x_1 \\ x_2 \\ x_3 \eb = \bb x_1 \\ x_2 - x_1 \\ x_3 - x_2 \eb`

**The matrix** :math:`A` **acts on the vector** :math:`\x`. The output
:math:`A\x` is a **combination** :math:`\b` **of the columns of**
:math:`A`.

.. math::
    
    A\x = \bb 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb \bb x_1 \\ x_2 \\ x_3 \eb
    = \bb \bs{x_1} \\ \bs{x_2} - \bs{x_1} \\ \bs{x_3} - \bs{x_2} \eb
    = \bb b_1 \\ b_2 \\ b_3 \eb = \b

This :math:`A` is a "**difference matrix**" because :math:`\b` combinations
difference of the input vector :math:`\x`.

:math:`A\x` is also **dot products with rows**:

.. math::

    A\x = \bb 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb \bb x_1 \\ x_2 \\ x_3 \eb
    = \bb (1,0,0)\cd(x_1,x_2,x_3) \\ (-1,1,0)\cd(x_1,x_2,x_3) \\ (0,-1,1)\cd(x_1,x_2,x_3) \eb.

Linear combinations are the key to linear algebra, and the output :math:`A\x` is
a linear combination of the **columns** of :math:`A`.

Linear Equations
----------------

**Now we think of** :math:`\b` **as known and we look for** :math:`\x`.

    *Old question*: Compute the linear combination :math:`x_1\u + x_2\v + x_3\w`
    to find :math:`\b`.

    *New question*: Which combination of :math:`\u, \v, \w` produces a particular
    vector :math:`\b`?

.. note::

    **Equations** :math:`A\x = \b`:
    :math:`\begin{matrix} x_1 = b_1 \\ -x_1+x_2=b_2 \\ -x_2+x_3=b_3 \end{matrix}`.
    **Solution** :math:`\x = A^{-1}\b`:
    :math:`\begin{matrix} x_1 = b_1 \\ x_2=b_1+b_2 \\ x_3=b_1+b_2+b_3 \end{matrix}`.
    
*The equations can be solved in order (top to bottom) because* :math:`A` *is a
triangular matrix*.

This matrix :math:`A` is "**invertible**". From :math:`\b` we can recover
:math:`\x`. We write :math:`\x` as :math:`A^{-1}\b`.

The Inverse Matrix
------------------


Cyclic Differences
------------------


Independence and Dependence
---------------------------

