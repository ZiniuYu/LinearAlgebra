Chapter 2.5 Inverse Matrices
============================

Suppose :math:`A` is a square matrix. 
We look for an "**inverse matrix**" :math:`A^{-1}` of the same size, such that 
:math:`A^{-1}` *times* :math:`A` *equals* :math:`I`.
*But* :math:`A^{-1}` *might not exist*.

.. note::

    **DEFINITION**: The matrix :math:`A` is **invertible** if there exists a 
    matrix :math:`A^{-1}` that "inverts" :math:`A`:

    * **Two-sided inverse**: :math:`A^{-1}A = I` and :math:`AA^{-1} = I`.

**Not all matrices have inverses**:

* **Note 1**: The inverse exists if and only if elimination produces :math:`n` pivots (row exchanges are allowed).

* **Note 2**: The matrix :math:`A` cannot have two different inverses.
  Suppose :math:`BA=I` and also :math:`AC=I`.
  Then :math:`B =C`:

  .. math::
  
    B(AC) = (BA)C\ \mathrm{gives}\ BI=IC\ \mathrm{or}\ B=C.

  This shows that a *left-inverse* :math:`B` and a *right-inverse* :math:`C` must be the *same matrix*.

* **Note 3**: If :math:`A` is invertible, the one and only solution to :math:`A\x=\b` is :math:`\x=A^{-1}\b`:

.. note::

    **Multiply** :math:`A\x=\b` **by** :math:`A^{-1}`. **Then** :math:`\x = A^{-1}A\x = A^{-1}\b`.

* **Note 4**: **Suppose there is a nonzero vector** :math:`\x` **such that** :math:`A\x = \bs{0}`.
  *Then* :math:`A` *connot have an inverse*.
  no matrix can bring :math:`\bs{0}` back to :math:`\x`.

.. Tip::

    If :math:`A` is invertible, then :math:`A\x=\bs{0}` can only have the zero solution :math:`\x=A^{-1}\bs{0}=\bs{0}`.

* **Note 5**: A 2 by 2 matrix is invertible if and only if :math:`ad-bc` is not zero:

  **2 by 2 Inverse**:

  .. math::

      \bb a&d\\c&d \eb^{-1} = \frac{1}{ad-bc} \bb d&-b\\-c&a \eb.

  The number :math:`ad-bc` is the determinant of :math:`A`.
  A matrix is invertible if its determinant is not zero.

* **Note 6**: A diagonal matrix has an inverse provided no diagonal entries are zero:

  .. math::

      \mathrm{If}\ A = \bb d_1 \\ & \ddots \\ && d_n \eb \ \mathrm{then}\ 
      A^{-1} = \bb 1/d_1 \\ & \ddots \\ && 1/d_n \eb.

The Inverse of a Product :math:`AB`
-----------------------------------

The product :math:`AB` has an inverse, if and only if the two factors :math:`A` 
and :math:`B` are separately invertible (and the same size).

.. note::

    If :math:`A` and :math:`B` are invertible then so is :math:`AB`.
    The inverse of a product :math:`AB` is

    * :math:`(AB)^{-1}=B^{-1}A^{-1}`.

**Inverse of AB**:

.. math::

    (AB)^{-1}(B^{-1}A^{-1}) = AIA^{-1} = AA^{-1} = I.

**Reverse order**:

.. math::

    (ABC)^{-1} = C^{-1}B^{-1}A^{-1}.

**Inverse of an elimination matrix**:

.. math::

    E = \bb 1&0&0\\-5&1&0\\0&0&1 \eb\ \mathrm{and}\ E^{-1} = \bb 1&0&0\\5&1&0\\0&0&1 \eb.

For square matrices, an inverse on one side is automatically an inverse on the other side.

.. math::

    F = \bb 1&0&0\\0&1&0\\0&-4&1 \eb\ \mathrm{and}\ F^{-1} = \bb 1&0&0\\0&1&0\\0&4&1 \eb.

    FE = \bb 1&0&0\\-5&1&0\\20&-4&1 \eb\ \mathrm{is\ inverted\ by}\ E^{-1}F^{-1} = \bb 1&0&0\\5&1&0\\0&4&1 \eb.

* In this order :math:`FE`, row 3 feels an effect from row 1.
  
* In this order :math:`E^{-1}F^{-1}`, row 3 feels no effect from row 1.
  
.. note::

    In elimination order :math:`F` follows :math:`E`.
    In reverse order :math:`E^{-1}` follows :math:`F^{-1}`.
    :math:`\bs{E^{-1}F^{-1}}` **is quick.**
    **The multipliers 5, 4 fall into place below the diagonal of 1's.**

Calculating :math:`A^{-1}` by Gauss-Jordan Elimination
------------------------------------------------------

Each of the columns :math:`\bs{x_1}, \bs{x_2}, \bs{x_3}` of :math:`A^{-1}` is 
multiplied by :math:`A` to produce a column of :math:`I`:

.. note::

    **3 columns of** :math:`A^{-1}`: 
    :math:`AA^{-1}=A\bb \bs{x_1}&\bs{x_2}&\bs{x_3} \eb = \bb \bs{e_1}&\bs{e_2}&\bs{e_3} \eb = I`.

**The Gauss-Jordan method computes** :math:`A^{-1}` **by solving all** :math:`n` **equations together**.

Start Gauss-Jordan on :math:`K`

.. math::

    \bb K&\bs{e_1}&\bs{e_2}&\bs{e_3} \eb = \bb 2&-1&0&1&0&0 \\ -1&2&-1&0&1&0 \\ 0&-1&2&0&0&1 \eb

(:math:`\frac{1}{2}`\ row 1 + row 2)

.. math::

    \rightarrow \bb 2&-1&0&1&0&0 \\ 0&\frac{3}{2}&-1&\frac{1}{2}&1&0 \\ 0&-1&2&0&0&1 \eb

(:math:`\frac{2}{3}`\ row 2 + row 3)

.. math::

    \rightarrow \bb 2&-1&0&1&0&0 \\ 0&\frac{3}{2}&-1&\frac{1}{2}&1&0 \\ 0&0&\frac{4}{3}&\frac{1}{3}&\frac{2}{3}&1 \eb

The matrix in the first three columns is :math:`U` (upper triangular).
Jordan goes all the way to the **reduced echelon form** :math:`\bs{R=I}`.
Rows are added to rows above them, to produce **zeros above the pivots**

(Zero above third pivot) (:math:`\frac{3}{4}`\ row 3 + row 2)

.. math::

    \rightarrow \bb 2&-1&0&1&0&0 \\ 
    0&\frac{3}{2}&0&\frac{3}{4}&\frac{3}{2}&\frac{3}{4} \\ 
    0&0&\frac{4}{3}&\frac{1}{3}&\frac{2}{3}&1 \eb

(Zero above second pivot) (:math:`\frac{2}{3}`\ row 2 + row 1)

.. math::

    \rightarrow \bb 2&0&0&\frac{3}{2}&1&\frac{1}{2} \\ 
    0&\frac{3}{2}&0&\frac{3}{4}&\frac{3}{2}&\frac{3}{4} \\ 
    0&0&\frac{4}{3}&\frac{1}{3}&\frac{2}{3}&1 \eb

**The three columns of** :math:`K^{-1}` **are in the second half of** :math:`\bb I & K^{-1} \eb`:

.. math::
    
    \begin{matrix}
    (\mathrm{divide\ by\ }2) \\
    (\mathrm{divide\ by\ }\frac{3}{2}) \\
    (\mathrm{divide\ by\ }\frac{4}{3})
    \end{matrix}\quad
    \bb 1&0&0&\frac{3}{4}&\frac{1}{2}&\frac{1}{4} \\
    0&1&0&\frac{1}{2}&1&\frac{1}{2} \\
    0&0&1&\frac{1}{4}&\frac{1}{2}&\frac{3}{4} \eb
    = \bb I&\bs{x_1}&\bs{x_2}&\bs{x_3} \eb = \bb I & K^{-1} \eb.

.. note::

    **Gauss-Jordan**: 
    Multiply :math:`\bb \bs{A}&\bs{I} \eb` by :math:`\bs{A^{-1}}` to get :math:`\bb \bs{I}&\bs{A^{-1}} \eb`.

Observations about :math:`K^{-1}`:

#. :math:`K` is **symmetric** across its main diagonal. Then :math:`K^{-1}` is also symmetric.

#. :math:`K` is **tridiagonal** (only three nonzero diagonals). But :math:`K^{-1}` is a dense matrix with no zeros. The inverse of a band matrix is generally a dense matrix.

#. The *product of pivots* is :math:`2(\frac{3}{2})(\frac{4}{3})=4`. This number 4 is the **determinant** of :math:`K`.

:math:`\bs{K^{-1}}` **involves division by the determinant of** :math:`\bs{K}`:

.. math::

    K^{-1} = \frac{1}{4} \bb 3&2&1 \\ 2&4&2 \\ 1&2&3 \eb.

.. Tip::

    This is why an invertible matrix cannot have a zero determinant: we need to divide.

**If** :math:`A` **is invertible and upper triangular, so is** :math:`A^{-1}`.

The total cost for :math:`A^{-1}` using Gauss-Jordan elimination is :math:`n^3` multiplications and subtractions.

.. Tip::

    To solve :math:`Ax=b` without :math:`A^{-1}`, we deal with one column :math:`b` to find one column :math:`x`.

Singular versus Invertible
--------------------------

:math:`\bs{A^{-1}}` **exists exactly when** :math:`\bs{A}` **has a full set of** :math:`\bs{n}` **pivots**.
(Row exhange are allowed)
Prove by Gauss-Jordan elimination:

#. With :math:`n` pivots, elimination solves all the equations :math:`A\x_i=\bs{e}_i`. The columns :math:`\x_i` go into :math:`A^{-1}`. Then :math:`AA^{-1}=I` and :math:`A^{-1}` is at least a **right-inverse**.

#. Elimination is really a sequence of multiplication by :math:`E`'s and :math:`P`'s and :math:`D^{-1}`:

**Left-inverse** :math:`C`:

.. math::

    CA = (D^{-1}\cds E \cds P \cds E)A = I.

:math:`D^{-1}` divides by the pivots.
The matrices :math:`E` produce zeros below and above the pivots.
:math:`P` exchanges rows if needed.

:math:`A` **must have** :math:`n` **pivots if** :math:`AC=I`:

#. If :math:`A` doesn't have :math:`n` pivots, elimination will lead to a *zero row*.

#. Those elimination steps are taken by an invertible :math:`M`. So a row of :math:`MA` is zero.

#. If :math:`AC=I` had been possible, then :math:`MAC=M`. The zero row of :math:`MA`, times :math:`C`, gives a zero row of :math:`M` itself.

#. An invertible matrix :math:`M` can't have a zero row! :math:`A` *must* have :math:`n` pivots if :math:`AC=I`.

.. note::

    Elimination gives a complete test for invertibility of a square matrix.
    :math:`\bs{A^{-1}}` **exists when** :math:`A` **has** :math:`n` **pivots.
    The argument above shows more:

    * If :math:`AC=I` then :math:`CA=I` and :math:`C=A^{-1}`.

.. Tip::

    A triangular matrix is invertible if and only if no diagonal entries are zero.

Recognizing an Invertible Matrix
--------------------------------

