Chapter 2.6 Elimination = Factorization: :math:`A = LU`
=======================================================

**The factors** :math:`L` **and** :math:`U` **are triangular matrices**.
**The factorization that comes from elimination is** :math:`\bs{A=LU}`.

:math:`U` is the upper triangular matrix with the pivots on its diagonal from elimination.

:math:`L` is the lower triangular matrix whose entries are exactly the 
multipliers :math:`l_{ij}`--which multiplied the pivot row :math:`j` when it was 
subtracted from row :math:`i`.

Forward from :math:`A` to :math:`U`:

.. math::

    E_{21}A = \bb 1&0\\-3&1 \eb \bb 2&1\\6&8 \eb = \bb 2&1\\0&5 \eb = U.

Back from :math:`U` to :math:`A`:

.. math::

    E_{21}^{-1}A = \bb 1&0\\3&1 \eb \bb 2&1\\0&5 \eb = \bb 2&1\\6&8 \eb = A = LU.

For larger matrices with many :math:`E`'s, :math:`L` will include all their inverses.

.. note::

    :math:`(E_{32}E_{31}E_{21})A=U` becomes :math:`A=(E_{21}^{-1}E_{31}^{-1}E_{32}^{-1})U` which is :math:`A=LU`.

Explanation and Examples
------------------------

*First point*: Every inverse matrix :math:`E^{-1}` is *lower triangular*.
Its off-diagonal entry is :math:`l_{ij}`, to undo the subtraction produced by :math:`-l_{ij}`.
The main diagonals of :math:`E` and :math:`E^{-1}` contain 1's.

*Second point*: **This lower triangular product of inverses is** :math:`\bs{L}`.

*Third point*: Each multiplier :math:`l_{ij}` goes directly into its :math:`i,j` 
position *unchanged* in the product of inverses which is :math:`L`.
:math:`L` also has 1's down its diagonal.

.. note::

    :math:`\bs{A=LU}`: **This is elimination without row exchanges**.
    The upper triangular :math:`U` has the pivots on its diagonal.
    The lower triangular :math:`L` has all 1's on its diagonal.
    **The multipliers** :math:`l_{ij}` **are below the diagonal of** :math:`L`.

.. Tip::

    * When a row of :math:`A` starts with zeros, so does that row of :math:`L`.
    * When a column of :math:`A` starts with zeros, so does that column of :math:`U`.

**The key reason why** :math:`A` equals :math:`LU`:

.. math::

    \mathrm{Row\ 3\ of\ }U=(\mathrm{Row\ 3\ of\ } A)-l_{31}(\mathrm{Row\ 1\ of\ } U)-l_{32}(\mathrm{Row\ 2\ of\ } U)

Rewrite this equation to see that the row :math:`\bb l_{31} & l_{32} 1 \eb` is multiplying the matrix :math:`U`:

.. note::

    :math:`\mathrm{Row\ 3\ of\ }A=1(\mathrm{Row\ 3\ of\ } U)+l_{31}(\mathrm{Row\ 1\ of\ } U)+l_{32}(\mathrm{Row\ 2\ of\ } U)`

**Better balance from LDU**: **Divide** :math:`U` **by a diagonal matrix** :math:`D` **that contains the pivots**.
That leaves a new triangular matrix with 1's on the diagonal:

.. math::

    \mathrm{Split\ } U \mathrm{\ into\ } \bb d_1\\&d2\\&&\ddots\\&&&d_n \eb
    \bb 1&u_{12}/d_1&u_{13}/d_1&\cd\\&1&u_{23}/d_2&\cd\\&&\ddots&\vdots\\&&&1 \eb.

.. note::

    **The triangular factorization can be written** :math:`\bs{A=LU}` or :math:`\bs{A=LDU}`.

One Square System = Two Triangular Systems
------------------------------------------

.. note::

    **1 Factor** (into :math:`L` and :math:`U`, by elimination on the left side matrix :math:`A`).

    **2 Solve** (forward elimination on :math:`\b` using :math:`L`, then back substitution for :math:`\x` using :math:`U`.

.. note::

    **Forward and backward**: Solve :math:`L\bs{c} = \b` and then solve :math:`U\x = \bs{c}`.

:math:`LU\x = L\bs{c}` is just :math:`A\x=\b`.

The Cost of Elimination
-----------------------

.. note::

    **Elimination on** :math:`A` **requires about** :math:`\frac{1}{3}n^3` 
    **multiplications and** :math:`\frac{1}{3}n^3` **subtractions**.

.. note::

    **Solve**: **Each right side needs** :math:`n^2` **multiplications and** :math:`n^2` **subtractions**.

A **band matrix** :math:`B` has only :math:`w` nonzero diagonals below and above its main diagonal.
The zero entries outside the band stay zero in elimination (they are zero in :math:`L` and :math:`U`).

.. note::

    **Band matrix**: :math:`\bs{A}` **to** :math:`\bs{U}`: :math:`\frac{1}{3}n^3` 
    reduces to :math:`nw^2\quad` **Solve**: :math:`n^2` reduces to :math:`2nw`.