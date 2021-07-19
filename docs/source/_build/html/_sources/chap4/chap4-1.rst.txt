Chapter 4.1 Orthogonality of the Four Subspaces
===============================================

Two vectors are orthogonal when their dot product is zero: :math:`\v\cd\w=\v^T\w=0`.
This chapter moves to **orthogonal subspaces** and **orthogonal bases** and **orthogonal matrices**.
Thank of :math:`a^2+b^2=c^2` for a *right triangle* with sides :math:`\v` and :math:`\w`.

.. note::

    **Orthogonal vectors**: :math:`\v^T\w=0` and :math:`\lv\v\rv^2+\lv\w\rv^2=\lv\v+\w\rv^2`.

The right side is :math:`(\v+\w)^T(\v+\w)`.
This equals :math:`\v^T\v+\w^T\w` when :math:`\v^T\w=\w^T\v=0`.

**The row space is perpendicular to the nullsapce**.
Every row of :math:`A` is perpendicular to every solution of :math:`A\x=\0`.
This perpendicularity of subspaces is Part2 of the Fundamental Theorem of Linear Algebra.

**The column space is perpendicular to the nullspace of** :math:`A^T`.
When :math:`\b` is outside the column space--when we want to solve :math:`A\x=\b` 
and con't do it--then this nullspace of :math:`A^T` comes into its own.
It contains the error :math:`\e=\b-A\x` in the "least-squares" solution.
Least squares is the key application of linear algebra in this chapter.

**The row space and nullspace are orthogonal subspaces inside** :math:`\R^n`.

**DEFINITION**: Two subspaces :math:`\bs{V}` and :math:`\bs{W}` of a vector 
space are **orthogonal** if every vector :math:`\v` in :math:`\bs{V}` is
perpendicular to every vector :math:`\w` in :math:`\bs{W}`:

.. note::

    **Orthogonal subspaces**: :math:`\v^T\w=0` for all :math:`\v` in :math:`\bs{V}` and all :math:`\w` in :math:`\bs{W}`.

.. note::

    Every vector :math:`\x` in the nullspace is perpendicular to every row of :math:`A`, because :math:`A\x=\0`.
    **The nullspace** :math:`\bs{N}(A)` **and the row space** :math:`\bs{C}(A^T)` 
    **are orthogonal subspaces of** :math:`\R^n`.

Look at :math:`A\x=\0`.
Each row multiplies :math:`\x`:

.. math::

    A\x=\bb &\rm{row\ }1&\\&\vdots&\\&\rm{row\ }m& \eb\bb \\ \x \\ \ \eb
    =\bb 0\\\vdots\\0 \eb \quad
    \begin{matrix} \leftarrow \\ \\ \leftarrow \end{matrix} \quad
    \begin{matrix} (\rm{row\ }1)\cd\x \rm{\ is\ zero} \\ \\ 
    (\rm{row\ }m)\cd\x \rm{\ is\ zero} \end{matrix}

The first equation says that row 1 is perpendicular to :math:`\x`.
The last equation says that row :math:`m` is perpendicular to :math:`\x`.
*Every row has a zero dot product with* :math:`\x`.
Then :math:`\x` is also perpendicular to every *combination* of the rows.
The whole row space :math:`\bs{C}(A^T)` is orthogonal to :math:`\bs{N}(A)`.

The vectors in the row space are combinations :math:`A^T\y` of the rows.
Take the dot product of :math:`A^T\y` with any :math:`\x` in the nullspace.
*These vectors are perpendicular*.

**Nullspace orthogonal to row space**:

.. math::

    \x^T(A^T\y) = (A\x)^T\y = \0^T\y =0.

.. note::

    Every vector :math:`\y` in the nullspace of :math:`A^T` is perpendicular to every column of :math:`A`.
    **The left nullspace** :math:`\bs{N}(A^T)` **and the column space** 
    :math:`\bs{C}(A)` **are orthogonal in** :math:`\R^m`.

Orthogonal Complements
----------------------

**Important**: The fundamental subspaces are more than just orthogonal (in pairs).
Their dimensions are also right.
Two lines could be perpendicular in :math:`\R^3`, 
**but those lines could not be the row space and nullspace of a 3 by 3 matrix**.

**DEFINITION**: The **orthogonal complement** of a subspace :math:`\bs{V}` 
contains **every** vector that is perpendicular to :math:`\bs{V}`.
This orthogonal subspace is denoted by :math:`\bs{V}^{\perp}`.

By this definition, the nullspace is the orthogonal complement of the row space.
*Every* :math:`\x` that is perpendicular to the rows satisfies :math:`A\x=\0`, and lies in the nullspace.
The reverse is also true.
**If** :math:`\v` **is orthogonal to the nullspace, it must be in the row space**.

.. note::

    **Fundamental Theorem of Linear Algebra, Part 2**:

    * :math:`\bs{N}(A)` **is the orthogonal complement of the row space** :math:`\bs{C}(A^T)` (**in** :math:`\R^n`).

    * :math:`\bs{N}(A^T)` **is the orthogonal complement of the column space** :math:`\bs{C}(A)` (**in** :math:`\R^m`).

Part 1 gave the dimensions of the subspaces.
Part 2 gives the :math:`90^{\circ}` angles between them.
The point of "complements" is that every :math:`\x` can be split into a 
*row space component* :math:`\x_r` and a *nullspace component* :math:`\x_n`.
When :math:`A` multiplies :math:`\x=\x_r=\x_n`:

    * The nullspace omponent goes to zero: :math:`A\x_n=\0`.

    * The row space component goes to the column space: :math:`A\x_r=A\x`.

*Every vector* :math:`\b` *in the column space comes from one and only one vector* :math:`\x_r` *in the row space*.

**Proof**: If :math:`A\x_r=A\x^{\pr}_r`, the difference :math:`\x_r-\x^{\pr}_r` is in the nullspace.
It is also in the row space, where :math:`\x_r` and :math:`\x^{\pr}_r` came from.
This difference must be the zero vector, because the nullspace and row space are perpendicular.
Therefore :math:`\x_r = \x^{\pr}_r`.

There is an :math:`r` by :math:`r` invertible matrix hiding inside :math:`A`, if we throw away the two nullspaces.
**From the row space to the column space**, :math:`A` **is invertible**.

Every matrix can be diagonalized, when we choose the right bases for :math:`\R^n` and :math:`\R^m`.
This **Singular Value Decomposition** has become extremely important in applications.

A row of :math:`A` can't be in the nullspace of :math:`A` (except for a zero row).
The only vector in two orthogonal subspaces is the zero vector.
**If a vector** :math:`\v` **is orthogonal to itself then** :math:`\v` **is the zero vector**.

Drawing the Big Picture
-----------------------

Refer to the textbook Page 199.

Combining Bases from Subspaces
------------------------------

.. note::

    * Any :math:`n` independent vectors in :math:`\R^n` must span :math:`\R^n`. So they are a basis.

    * Any :math:`n` vectors that span :math:`\R^n` must be independent. So they are a basis.

.. note::

    * If the :math:`n` columns of :math:`A` are independent, they space :math:`\R^n`. So :math:`A\x=\b` is solvable.

    * If the :math:`n` columns span :math:`\R^n`, they are independent. So :math:`A\x=\b` has only one solution.

Uniqueness implies existence and existence implies uniqueness.
**Then** :math:`A` **is invertible**.If there are no free variables, the solution :math:`\x` is unique.
There must be :math:`n` pivot columns.
Then back substitution solves :math:`A\x=\b` (the solution exists).

Starting in the opposite direction, suppose that :math:`A\x=\b` can solved for 
every :math:`\b` (*existence of solutions*).
Then elimination produced no zero rows.
There are :math:`n` pivots and no free variables.
The nullspace contains only :math:`\x=\0` (*uniqueness of solutions*).

With bases for the row space and the nullspace, we have :math:`r+(n-r)=n` vectors.
This is the right number.
Those :math:`n` vectors are independent.
*Therefore they span* :math:`\R^n`.

.. tip::

    Each :math:`\x` is the sum :math:`\x_r+\x_n` of a row space vector :math:`\x_r` and a nullspace vector :math:`\x_n`.


