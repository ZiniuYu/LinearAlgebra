Chapter 3.4 Independece, Basis and Dimension
============================================

There are :math:`n` columns in an :math:`m` by :math:`n` matrix.
But the true "dimension" of the column space is not necessarily :math:`n`.
The dimension is measured by counting **independent columns**.
*The true dimension of the column space is the rank* :math:`r`.

The goal is to understand a **basis**: **independent vectors that "span the space"**.

.. Tip::

    **Every vector in the space is a unique combination of the basis vectors**.

.. note::

    #. **Independent vectors**: no extra vectors.

    #. **Spanning a space**: enough vectors to produce the rest.

    #. **Basis for a space**: not too many or too few.

    #. **Dimension of a space**: the number of vectors in a basis.

Linear Independece
------------------

.. note::

    **DEFINITION**: The columns of :math:`A` are *linearly independent* when the 
    only solution to :math:`A\x=\0` is :math:`\x=\0`.
    **No other combination** :math:`A\x` **of the columns gives the zero vector**.

The columns are independent when the nullspace :math:`\bs{N}(A)` contains only
the zero vector.

.. note::

    **DEFINITION**: The sequence of vectors :math:`\v_1,\cds,\v_n` is 
    **linearly independent** if the only combination that gives the zero vector
    is :math:`0\v_1+0\v_2+\cds+0\v_n`.

    * :math:`x_1\v_1+x_2\v_2+\cds+x_n\v_n=\0` only happens when all :math:`x`'s are zero.

If a combination gives :math:`\0`, when the :math:`x`'s are not all zero, the vectors are *dependent*.

.. note::

    **Full column rank**: The columns of :math:`A` are independent exactly when the rank is :math:`r=n`.
    There are :math:`n` pivots and no free variables.
    Only :math:`\x=\0` is in the nullspace.

.. note::

    Any set of :math:`n` vectors in :math:`\R^m` must be linearly dependent if :math:`n>m`.

The columns might be dependent or might be independent if :math:`n\leq m`.
Elimination will reveal the :math:`r` pivot columns.
*It is those* :math:`r` *pivot columns that are independent*.

Vectors that Span a Subspace
----------------------------

*The column space consists of all combinations* :math:`A\x` *of the columns*.

.. note::

    **DEFINITION**: A set of vectors **spans** a space if their linear combinations fill the space.

.. tip::

    The columns of a matrix span its column space.
    They might be dependent.

**The combinations of the rows produce the "row space"**.

.. note::

    **DEFINITION**: The **row space** of a matrix is the subspace of :math:`\R^n` spannede by the rows.
    **The row space of** :math:`A` **is** :math:`\bs{C}(A^T)`.
    **It is the column space of** :math:`A^T`.

A Basis for a Vector Space
--------------------------

We want **enough independent vectors to span the space** (and not more).

.. note::

    **DEFINITION**: A **basis** for a vector space is a sequence of vectors with two properties:

    * **The basis vectors are linearly independent and they span the space**.

.. tip::

    **There is one and only one way to write** :math:`\v` **as a combination of the basis vectors**.

Suppose :math:`\v=a_1\v_1+\cds+a_n\v_n` and also :math:`\v=b_1\v_1+\cds+b_n\v_n`.
By subtraction :math:`(a_1-b_1)\v_1+\cds+(a_n-b_n)\v_n` is the zero vector.
From the independence of the :math:`\v`'s, each :math:`a_i-b_i=0`.
Hence :math:`a_i=b_i`, and there are not two ways to produce :math:`\v`.

The columns of the :math:`n` by :math:`n` identity matrix give the "**standard basis**" for :math:`\R^n`.

The columns of *every invertible* :math:`n` *by* :math:`n` *matrix* give a basis for :math:`\R^n`:

* **Invertible matrix**: Independent columns; Column space is :math:`\R^3`:

    .. math::

        A=\bb 1&0&0\\1&1&0\\1&1&1 \eb.

* **Singular matrix**: Dependent columns; Column space :math:`\neq \R^3`:

    .. math::
    
        B=\bb 1&0&1\\1&1&2\\1&1&2 \eb.

The only solution to :math:`A\x=\0` is :math:`\x=A^{-1}\0=\0`.
The columns are independent.
They spsan the whole space :math:`\R^n`--because every vector :math:`\b` is a combination of the columns.
:math:`A\x=\b` can always be solved by :math:`\x=A^{-1}\b`.

.. note::

    The vectors :math:`\v_1,\cds,\v_n` are a **basis for** :math:`\R^n` exactly
    when they are **the columns of an** :math:`n` **by** :math:`n`
    **invertible matrix**.
    Thus :math:`\R^n` has infinitely many different bases.

When the columns are dependent. we keep only the *pivot columns*--the first two
columns of :math:`B` above, with its two pivots.
They are independent and they span the column space.

.. note::

    **The pivot columns of** :math:`A` **are a basis for its column space**.
    The pivot rows of :math:`A` are a basis for its row space.
    So are the pivot rows of its echelon form :math:`R`.
            



Dimension of a Vector Space
---------------------------




Bases for Matrix Spaces and Function Spaces
-------------------------------------------