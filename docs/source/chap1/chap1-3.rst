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

**The matrix** :math:`A` **acts on the vector** :math:`\x`. 
The output :math:`A\x` is a **combination** :math:`\b` **of the columns of** :math:`A`.

.. math::
    
    A\x = \bb 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb \bb x_1 \\ x_2 \\ x_3 \eb
    = \bb \bs{x_1} \\ \bs{x_2} - \bs{x_1} \\ \bs{x_3} - \bs{x_2} \eb
    = \bb b_1 \\ b_2 \\ b_3 \eb = \b

This :math:`A` is a "**difference matrix**" because :math:`\b` combinations difference of the input vector :math:`\x`.

:math:`A\x` is also **dot products with rows**:

.. math::

    A\x = \bb 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb \bb x_1 \\ x_2 \\ x_3 \eb
    = \bb (1,0,0)\cd(x_1,x_2,x_3) \\ (-1,1,0)\cd(x_1,x_2,x_3) \\ (0,-1,1)\cd(x_1,x_2,x_3) \eb.

Linear combinations are the key to linear algebra, and the output :math:`A\x` is
a linear combination of the **columns** of :math:`A`.

Linear Equations
----------------

**Now we think of** :math:`\b` **as known and we look for** :math:`\x`.

    *Old question*: Compute the linear combination :math:`x_1\u + x_2\v + x_3\w` to find :math:`\b`.

    *New question*: Which combination of :math:`\u, \v, \w` produces a particular vector :math:`\b`?

.. note::

    **Equations** :math:`A\x = \b`:
    :math:`\begin{matrix} x_1 = b_1 \\ -x_1+x_2=b_2 \\ -x_2+x_3=b_3 \end{matrix}`.
    **Solution** :math:`\x = A^{-1}\b`:
    :math:`\begin{matrix} x_1 = b_1 \\ x_2=b_1+b_2 \\ x_3=b_1+b_2+b_3 \end{matrix}`.
    
*The equations can be solved in order (top to bottom) because* :math:`A` *is a triangular matrix*.

This matrix :math:`A` is "**invertible**". 
From :math:`\b` we can recover :math:`\x`. 
We write :math:`\x` as :math:`A^{-1}\b`.

The Inverse Matrix
------------------

:math:`A\x = \b` is solved by 

.. math::
    
    \bb x_1 \\ x_2 \\ x_3 \eb
    = \bb b_1 \\ b_1 + b_2 \\ b_1 + b_2 + b_3 \eb
    = \bb 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \eb \bb b_1 \\ b_2 \\ b_3 \eb.

#. For every :math:`\b` there is one solution to :math:`A\x = \b`.
#. The matrix :math:`A^{-1}` produces :math:`\x = A^{-1}\b`.

*Note on calculus*. The vector :math:`\x` changes to a function :math:`x(t)`.
The differences :math:`A\x` become the *derivative* :math:`dx/dt = b(t)`.
The sums :math:`A^{-1}\b` become the *integral* of :math:`b(t)`.
**Sums of differences are like integrals of derivatives**.

    Fundamental Theorem of Calculus: integration is the inverse of differentiation.
    
    :math:`\bs{Ax=b} \ ` and :math:`\ \bs{x=A^{-1}b} \quad`
    :math:`\dp \frac{dx}{dt}=b \ \mathrm{and}\  x(t) = \int_{0}^{t}b\ dt`.

    **Centered difference of** :math:`\bs{x(t)=t^2}`
    :math:`\quad \dp \frac{(t+1)^2 - (t-1)^2}{2} = 2t`.

Cyclic Differences
------------------

Keeps the same columns :math:`\u` and :math:`\v` but changes :math:`\w` to a new vector :math:`\w^*`:

.. math::

    \u = \bb 1 \\ -1 \\ 0 \eb \quad
    \v = \bb 0 \\ 1 \\ -1 \eb \quad
    \w^* = \bb -1 \\ 0 \\ 1 \eb

The linear combinations of :math:`\u, \v, \w^*` lead to a **cyclic difference matrix** :math:`C`:

.. note::

    **Cyclic**: :math:`C\x = \bb 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \eb
    \bb x_1 \\ x_2 \\ x_3 \eb = \bb x_1 - x_3 \\ x_2 - x_1 \\ x_3 - x_2 \eb
    = \b`

The three equations either have **infinitely many solutions** (sometimes) or else **no solutions** (usually).

**All linear combinations** :math:`x_1\u + x_2\v + x_3\w^*`
**lie on the plane given by** :math:`b_1 + b_2 + b_3 = 0`.

Independence and Dependence
---------------------------

**The key question is whether the third vector is in that plane**:

    **Independence**: :math:`\w` is not in the plane of :math:`\u` and :math:`\v`.
    
    **Dependence**: :math:`\w` is not in the plane of :math:`\u` and :math:`\v`.
    
:math:`\u, \v, \w` are **independent**.
No combination except :math:`0\u + 0\v + 0\w = \bs{0}` gives :math:`\b = \bs{0}`.

:math:`\u, \v, \w^*` are **dependent**.
Other combinations like :math:`\u + \v + \w^*` give :math:`\b = \bs{0}`.

The vectors go into the columns of an :math:`n` by :math:`n` matrix:

    Independent columns: :math:`A\x = \bs{0}` has one solution.
    :math:`A` is an **invertible matrix**.

    Dependent columns: :math:`C\x = \bs{0}` has many solutions.
    :math:`C` is a **singular matrix**.