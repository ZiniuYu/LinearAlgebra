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
            
.. note::

    **Question**: Given five vectors in :math:`\R^7`, **how do you find a basis for the space they span**?

*First answer*: Make them the rows of :math:`A`, and eliminate to find the nonzero rows of :math:`R`.

*Second answer*: Put the five vectors into the columns of :math:`A`.
Eliminate to find the pivot columns (of :math:`A` not :math:`R`).
Those pivot columns are a basis for the column space.

**All bases for a vector space contain the same number of vectors**.

.. tip::

    **The number of vectors, in any and every basis, is the "dimnesion" of the space**.

Dimension of a Vector Space
---------------------------

.. note::

    If :math:`\v_1,\cds,\v_m` and :math:`\w_1,\cds,\w_n` are both bases for the same vector space, then :math:`m=n`.

**Proof**: Suppose that there are more :math:`\w`'s than :math:`\v`'s.
From :math:`n>m` we want to reach a contradiction.
The :math:`\v`'s are a basis, so :math:`\w_1` must be a combination of the :math:`\v`'s.
If :math:`\w_1` equals :math:`a_{11}\v_1+\cds+a_{m1}\v_m`, this is the first 
column of a matrix multiplication :math:`VA`:

    **Each** :math:`\w` **is a combination of the** :math:`\v`\ **'s**:

    .. math::

        W=\bb &&&\\\w_1&\w_2&\cds&\w_n\\&&& \eb=\bb &&\\\v_1&\cds&\v_m\\&& \eb
        \bb a_{11}&&a_{1n}\\\vdots&&\vdots\\a_{m1}&&a_{mn} \eb=VA.

    We don't know each :math:`a_{ij}`, but we know the shape of :math:`A` (it is :math:`m` by :math:`n`).
    The second vector :math:`\w_2` is also a combination of the :math:`\v`'s.
    The coefficients in that combination fill the second column of :math:`A`.
    The key is that :math:`A` has a row for every :math:`\v` and a column for every :math:`\w`.
    :math:`A` is a shrot wide matrix, since we assumed :math:`n>m`.
    So :math:`A\x=\0` **has a nonzero solution**.

    :math:`A\x=\0` gives :math:`VA\x=\0` which is :math:`W\x=\0`.
    *A combination of the* :math:`\w`\ *'s gives zero*!
    Then the :math:`\w`could not be a basis--ou assumption :math:`n>m` is **not possible** for two bases.

    If :math:`m>n` we exchange the :math:`\v`'s and :math:`\w`'s and repeat the same steps.
    The only way to avoid a contradiction is to have :math:`m=n`.
    This completes the proof that :math:`m=n`.

The number of basis vectors depends on the space--not on a particular basis.
The number is the same for every basis, and it counts the "degrees of freedom" in the space.
The dimension of the space :math:`\R^n` is :math:`n`.

.. note::

    **DEFINITION**: The **dimension of a space** is the **number of vectors** in every basis.

Bases for Matrix Spaces and Function Spaces
-------------------------------------------

**Matrix spaces**: The vector space :math:`\bs{M}` contains all 2 by 2 matrices.
Its dimension is 4.

    **One basis is**:

    .. math::

        A_1,A_2,A_3,A_4=\bb 1&0\\0&0 \eb,\bb 0&1\\0&0 \eb,\bb 0&0\\1&0 \eb,\bb 0&0\\0&1 \eb.

    Those matrices are linearly independent.
    We are not looking at their columns, but at the whole matrix.
    Combinations of those four matrices can produce any matrix in :math:`\bs{M}`, so they space the space:

    **Every** :math:`A` **combines the basis matrices**:

    .. math::

        c_1A_1+c_2A_2+c_3A_3+c_4A_4=\bb c_1&c_2\\c_3&c_4 \eb=A.

    :math:`A` is zero only if the :math:`c`'s are all zero--this proves independece of :math:`A_1,A_2,A_3,A_4`.

    The three matrices :math:`A_1,A_2,A_4` are a basis for a subspace--the upper triangular matrices.
    Its dimension is 3.
    :math:`A_1` and :math:`A_4` are a basis for the diagonal matrices.

    To push this further, think about the space of all :math:`n` by :math:`n` matrices.
    One possible basis uses matrices that have only a single nonzero entry (that entry is 1).
    There are :math:`n^2` positions for that 1, so there are :math:`n^2` basis matrices:

        * **The dimension of the whole** :math:`n` **by** :math:`n` **matrix space is** :math:`n^2`.

        * **The dimension of the subspace of** *upper triangular* **matrices is** :math:`\frac{1}{2}n^2+\frac{1}{2}n`.

        * **The dimension of the subspace of** *diagonal* **matrices is** :math:`n`.

        * **The dimension of the subspace of** *symmetric* **matrices is** :math:`\frac{1}{2}n^2+\frac{1}{2}n`.

**Function spaces**: The equations :math:`d^2y/dx^2=0` and :math:`d^2y/dx^2=-y` 
and :math:`d^2y/dx^2=y` involve the second derivative.
In calculus we solve to find the functions :math:`y(x)`:

    * :math:`y\ppr=0` is solved by any linear function :math:`y=cx+d`.

    * :math:`y\ppr=-y` is solved by any combination :math:`y=c\sin x+d\cos x`.

    * :math:`y\ppr=y` is solved by any combination :math:`y=ce^x+de^{-x}`.

    That solution space for :math:`y\ppr=-y` has two basis functions: :math:`\sin x` and :math:`\cos x`.
    The space for :math:`y\ppr=0` has :math:`x` and 1.
    It is the "nullspace" of the second derivative!
    The dimension is 2 ineach case (these are second-order equations).

The dimension of the space :math:`\bs{\rm{Z}}` is *zero*.
**The empty set** (containing no vectors) **is a basis for** :math:`\bs{\rm{Z}}`.
We can never allow the zero vector into a basis, because then linear independence is lost.