Chapter 2.1 Vectors and linear Equations
========================================

.. note::

    **Two euqtions, Two unknowns**:
    :math:`\begin{matrix} x - 2y = 1 \\ 3x + 2y = 11 \end{matrix}`

The point :math:`(3,1)` lies on both lines and solves both equations.

.. note::

    **ROWS**: The row picture shows two lines meeting at a single point (the
    solution).

Separating the original system into its columns instead of its rows, we get a
vector equations:

**Combination equals** :math:`\b`

.. math::
    
    x \bb 1\\3 \eb + y \bb -2 \\2 \eb = \bb 1 \\ 11 \eb = \b.

The problem is *to find the combination of those vectors that equals the vector on the right*.
The right choices produce :math:`3(\bs{col1})+1(\bs{col2})=\b`.

.. note::

    **COLUMNS**: The column picture combines the column vectors on the left side
    to produce the vector :math:`\b` on the right side.

The left side of the vector equation is a **linear combination** of the columns.

.. note::

    **Linear combination**:
    :math:`3\bb 1\\3 \eb + \bb -2\\2 \eb = \bb 1\\11 \eb`.

The **coefficient matrix** on the lieft side of the equations is the 2 by 2
matrix :math:`A`:

.. math::

    A = \bb 1 & -2 \\ 3 & 2 \eb

.. note::

    **Matrix equation** :math:`A\x=\b`:
    :math:`\bb 1 & -2 \\ 3 & 2 \eb \bb x\\y \eb = \bb 1\\11 \eb`

.. note::

    **Dot products with rows**, **Combination of columns**:

    * :math:`A\x=\b\ ` is :math:`\ \bb 1 & -2 \\ 3 & 2 \eb \bb 3\\1 \eb = \bb 1\\11 \eb`

Four steps to understanding elimination using matrices:

#. Elimination goes from :math:`A` to a triangular :math:`U` by a sequence of matrix steps :math:`E_{ij}`.
#. The triangular system is solved by **back substitution**: working bottom to top.
#. In matrix language :math:`A` is factored into :math:`LU =` (lower triangular) (upper triangular).
#. Elimination succeeds if :math:`A` is invertible. (But it may need rwo exchanges.)

Three Equations in Three unknowns
---------------------------------

The three unknowns are :math:`x,y,z`. We have three linear equations:

.. math::
    A\x = \b \quad
    \begin{matrix}
    x + 2y + 3z = 6 \\
    2x + 5y + 2z = 4 \\
    6x - 3y + z = 2
    \end{matrix}

Before solving the problem, we visualize it both ways:

    **ROW**: The row picture shows three planes meeting at a single point.

    **COLUMN**: The column picture combines three columns to produce
    :math:`\b = (6,4,2)`.

The column picture starts with the vector form of the equations :math:`A\x = \b`:

    **Combine columns**:
    :math:`x\bb 1\\2\\6 \eb + y\bb 2\\5\\-3 \eb + z\bb 3\\2\\1 \eb = \bb 6\\4\\2 \eb = \b`.

    **Correct combination** :math:`(x,y,z)=(\bs{0},\bs{0},\bs{2})`:
    :math:`\bs{0}\bb 1\\2\\6 \eb + \bs{0}\bb 2\\5\\-3 \eb + \bs{2}\bb 3\\2\\1 \eb = \bb 6\\4\\2 \eb`.

The Matrix Form of the Equations
--------------------------------

**The "coefficient matrix" in** :math:`A\x = \b` **is**:
:math:`A = \bb 1&2&3 \\ 2&5&2 \\ 6&-3&1 \eb`.



Matrix Notation
---------------

Multiplication in MATLAB
------------------------

Programming Languages for Mathematics and Statistics
----------------------------------------------------