Chapter 3.5 Dimensions of the Four Subspaces
============================================

The **rank** of a matrix is the number of pivots.
The **dimension** of a subspace is the number of vectors in a basis.
*The rank of* :math:`A` *reveals the dimensions of all four fundamental subspaces*.

Two subspaces come directly from :math:`A`, and the other two from :math:`A^T`:

.. note::

    **Four Fundamental Subspaces**:

    #. The **row space** is :math:`\bs{C}(A^T)`, a subspace of :math:`\R^n`.

    #. The **column space** is :math:`\bs{C}(A^T)`, a subspace of :math:`\R^n`.

    #. The **nullspace** is :math:`\bs{C}(A^T)`, a subspace of :math:`\R^n`.

    #. The **left nullspace** is :math:`\bs{C}(A^T)`, a subspace of :math:`\R^n`.

*The row space of* :math:`A` *is the column space of* :math:`A^T`.

Four the left nullspace we solve :math:`A^T\y=\0`--that system is :math:`n` by :math:`m`.
*This is the nullspace of* :math:`A^T`.

Part 1 of the Fundamental Theorem finds the dimensions of the four subspaces.
**The row space and column space have the same dimension** :math:`r`.
This number :math:`r` is the **rank** of the matrix.

:math:`\bs{N}(A)` **and** :math:`\bs{N}(A^T)` **have dimensions** :math:`n-r`
**and** :math:`m-r`, **to make up the full** :math:`n` **and** :math:`m`.

Part 2 of the Fundamental Theorem will describe how the four subspaces fit together.

The Four Subspaces for :math:`R`
--------------------------------

Suppose :math:`A` is reduced to its row echelon form :math:`R`.
The main point is that *the four dimensions are the smae for* :math:`A` *and* :math:`R`.

As a specific 3 by 5 example, look at the four subspaces for this echelon matrix :math:`R`:

.. math::

    R = \bb 1&3&5&0&7\\0&0&0&1&2\\0&0&0&0&0 \eb.

The rank of this matrix is :math:`r=2` (*two pivots*).

.. note::

    **1.** The **row space** of :math:`R` has dimension 2, matching the rank.

The first two rows are a basis.
Rows 1 and 2 span the row space :math:`\bs{C}(R^T)`.

The pivot rows 1 and 2 are independent.
If we look only at the pivot columns, we see the :math:`r` by :math:`r` identity matrix.
So the :math:`r` pivot rows are a basis for the row space.

.. tip::

    **The dimension of the row space is the rank** :math:`r`.
    **The nonzero rows of** :math:`R` **form a basis**.

.. note::

    **2.** The **column space** of :math:`R` also has dimension :math:`r=2`.

The pivot columns 1 and 4 form a basis for :math:`\bs{C}(R)`.
They are independent because they start with the :math:`r` by :math:`r` identity matrix.
Every other (free) column is a combination of the pivot columns.

    Column 2 is 3 (column 1). The special solution is :math:`(-3,1,0,0,0)`.

    Column 3 is 5 (column 1). The special solution is :math:`(-5,0,1,0,0)`.

    Column 5 is 7 (column 1) + 2 (column 4). The special solution is :math:`(-7,0,0,-2,1)`.

.. tip::

    **The dimension of the column space is the rank** :math:`r`.
    **The pivot columns form a basis**.

.. note::

    **3.** The **nullspace** of :math:`R` has dimension :math:`n-r=5-2`.
    There are :math:`n-r=3` free variables.
    Here :math:`x_2,x_3,x_5` are free (no pivots in those columns).
    They yield the three special solutions to :math:`R\x=\0`.
    Set a free variable to 1, and solve for :math:`x_1` and :math:`x_4`.

.. math::

    \bs{s}_2 = \bb -3\\1\\0\\0\\0 \eb \quad
    \bs{s}_3 = \bb -5\\0\\1\\0\\0 \eb \quad
    \bs{s}_5 = \bb -7\\0\\0\\-2\\1 \eb \quad

With :math:`n` variables and :math:`r` pivots, that leaves :math:`n-r` free variables and special solutions.
The special solutions are independent, because they contain the identity matrix in rows 2, 3, 5.
So :math:`\bs{N}(R)` has dimension :math:`n-r`.

.. tip::

    **The nullspace has dimension** :math:`n-r`.
    **The special solutions form a basis**.

.. note::

    **4.** The **nullspace of** :math:`R^T` (**left nullspace of** :math:`R`) has dimension :math:`m-r=3-2`.

The equation :math:`R^T\y=\0` looks for combinations of the columns of 
:math:`R^T` (*the rows of* :math:`R`) that produce zero.
**The nullspace of** :math:`R^T` **contains all vectors** :math:`\y=(0,0,y_3)`.

.. tip::

    **If** :math:`A` **is** :math:`m` **by** :math:`n` **of rank** :math:`r`, 
    **its left nullsapce has dimension** :math:`m-r`.

.. note::

    **In** :math:`\R^n` **the row space and nullspace have dimensions** :math:`r` and :math:`n-r` (adding to :math:`n`).

    **In** :math:`\R^m` **the column space and left nullspace have dimensions**
    :math:`r` and :math:`m-r` (total :math:`m`).

The Four Subspaces for :math:`A`
--------------------------------

**The subspace dimensions for** :math:`A` **are the same as for** :math:`R`.

**This** :math:`A` **reduces to** :math:`R` (Notice :math:`\bs{C}(A)\neq\bs{C}(R)`!):

.. math::

    A=\bb 1&3&5&0&7\\0&0&0&1&2\\1&3&5&1&9 \eb

**1.** :math:`A` **has the same row space as** :math:`R`.
**Same dimension** :math:`r` **and same basis**.

    Every row of :math:`A` is a combination of the rows of :math:`R` and vice versa.
    Elimination changes rows, but not row *spaces*.
    The good :math:`r` rows of :math:`A` are the ones that end up as pivot rows in :math:`R`.

**2.** **The column space of** :math:`A` **has dimension** :math:`r`.
**The column rank equals the row rank**.

.. tip::

    **Rank Theorem**: **The number of independent columns = the number of independent rows**.

The **same** combinations of the columns are zero (or nonzero) for :math:`A` and :math:`R`.
Dependent in :math:`A \Leftrightarrow` depedent in :math:`R`.
:math:`A\x=\0` *exactly when* :math:`R\x=\0`.
The column spaces are different, but their *dimensions* are the same--equal to :math:`r`.

The :math:`r` pivot columns of :math:`A` are a basis for *its* column space :math:`\bs{C}(A)`.

**3.** :math:`A` **has the same nullsapce as** :math:`R`.
**Same dimension** :math:`n-r` **and same basis**.

The elimination steps don't change the soluions.
The special solutions are a basis for this nullspace (As we always knew).
There are :math:`n-r` free variables, so the dimension of the nullsapce is :math:`n-r`.
This is the **Counting Theorem**: :math:`r+(n-r)=n`.

.. note::

    (**dimension of column space**) + (**dimension of nullspace**) = **dimension of** :math:`\R^n`.

**4.** **The left nullspace of** :math:`A` (the nullspace of :math:`A^T`) **has dimension** :math:`m-r`.

.. note::

    **Fundamental Theorem of Linear Algebra, Part 1**:

    * **The column space and row space both have dimension** :math:`r`.

    * **The nullspaces have dimensions** :math:`n-r` **and** :math:`m-r`.

Graph are *the most important model in discrete applied mathematics*.

Rank One Matrics (Review)
-------------------------

.. note::

    **Every rank one matrix is one column times one row** :math:`A=\u\v^T`.

Rank Two Matrices = Rank One plus Rank One
------------------------------------------

Some elimination matrix :math:`E` simplifies :math:`A` to :math:`\bs{EA=R}`.
Then the inverse matrix :math:`C=E^{-1}` connects :math:`R` back to :math:`\bs{A+CR}`.

:math:`R` **has the same row space as** :math:`A`:

.. math::

    A=\bb 1&0&3\\1&1&7\\4&2&20 \eb=\bb 1&0&0\\1&1&0\\4&2&1 \eb\bb 1&0&3\\0&1&4\\0&0&0 \eb=CR.

**Matrix** :math:`A` **rank two**:

.. math::

    A=\bb &&\\\u_1&\u_2&\u_3\\&& \eb\bb &\v_1^T&\\&\v_2^T&\\&\rm{zero\ row}&\eb 
    =\u_1\v_1^T+\u_2\v_2^T=(\rm{rank\ }1)+(\rm{rank\ }1)

*Every rank* :math:`r` *matrix is a sum of* :math:`r` *rank one matrices*:
Pivot columns of :math:`A` times nonzero rows of :math:`R`.
The row :math:`\bb 0&0&0 \eb` simply disappeared.


