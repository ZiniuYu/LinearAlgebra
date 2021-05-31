Chapter 3.2 The Nullspace of :math:`A`: Solving :math:`Ax = 0` and :math:`Rx=0`
=================================================================================

For a :math:`m` by :math:`n` matrix, one immediate solution to :math:`A\x=\bs{0}` is :math:`\x=\bs{0}`.
For invertible matrices this is the only solution.
For other non-invertible matrices, there are nonzero solutions to :math:`A\x=\bs{0}`.
*Each solution* :math:`\x` *belongs to the nullspace of* :math:`A`.

.. note::

    The nullspace :math:`N(A)` consists of all solutions to :math:`A\x=\bs{0}`.
    These vectors :math:`\x` are in :math:`\R^n`.

The solution vectors :math:`\x` have :math:`n` components.
They are vectors in :math:`\R^n`, so *the nullspace is a subspace of* :math:`\R^n`.
The column space :math:`\bs{C}(A)` is a subspace of :math:`\R^m`.

.. note::

    **Special solution** :math:`A\bs{s}=\bs{0}`: The nullspace of 
    :math:`A=\bb 1&2\\3&6 \eb` contains all multiples of 
    :math:`\bs{s} = \bb -2\\1 \eb`.

This is the best way to describe the nullspace, by computing special solutions to :math:`A\x=\bs{0}`.
**The solution is special because we set the free variable to** :math:`\bs{x_2=1}`.

.. Tip::

    The nullspace of :math:`A` consists of all combinations of the special solutions to :math:`A\x=\bs{0}`.

.. math::

    \bb 1&2&3 \eb\bb x\\y\\z \eb = 0 \mathrm{\ has\ two\ special\ solutions\ }
    \bs{s}_1 = \bb -2\\1\\0 \eb \mathrm{\ and\ } \bs{s}_2 = \bb -3\\0\\1 \eb.

*The last two components of* :math:`\bs{s}_1` *and* :math:`\bs{s}_2` 
*are "free" and we choose them specially as* 1,0 *and* 0,1.
Then the first components -2 and -3 are determined by the equation :math:`A\x=\bs{0}`.

Pivot Columns and Free columns
------------------------------

The first column of :math:`A=\bb 1&2&3 \eb` contains the only pivot, so the first component of :math:`\x` is *not free*.
**The free components correspond to columns with no pivots**.
The special choice (one or zero) is only for the free variables in the special solutions.

.. math::

    A = \bb 1&2\\3&8 \eb \quad
    B = \bb A\\2A \eb = \bb 1&2\\3&8\\2&4\\6&16 \eb \quad
    C = \bb A&2A \eb = \bb 1&2&2&4\\3&8&6&16 \eb.

The equation :math:`A\x=\bs{0}` has only the zero solution :math:`\x=\bs{0}`.
The *nullspace is* :math:`\bs{Z}`.
It contains only the single point :math:`\x=\bs{0}` in :math:`\R^2`.

.. math::

    A\x = \bb 1&2\\3&8 \eb\bb x_1\\x_2 \eb = \bb 0\\0 \eb \rm{\ yields\ }
    \bb 1&2\\0&2 \eb\bb x_1\\x_2 \eb = \bb 0\\0 \eb \rm{\ and\ }
    \bb x_1=0\\x_2=0 \eb.

:math:`A` is invertible.
There are no special solutions.
Both columns of this matrix have pivots.

The rectangular matrix :math:`B` has the same nullspace :math:`\bs{Z}`.
The extra rows impose more conditions on the vectors :math:`\x` in the nullspace.

The rectangular matrix :math:`C` has extra columns instead of extra rows.
The solution vector :math:`\x` has *four* components.
Elimination will produce pivots in the first two columns of :math:`C`, but
**the last two columns of** :math:`C` **and** :math:`U` **are "free"**.
**They don't have pivots**:

.. math::

    C=\bb 1&2&2&4\\3&8&6&16 \eb\rm{\ becomes\ } U=\bb 1&2&2&4\\0&2&0&4 \eb
    
    \uparrow\quad\uparrow\quad\uparrow\quad\uparrow\;\;

    \rm{pivot}\quad\;\rm{free}\;\;

For the free variables :math:`x_3` and :math:`x_4`, we make special choices of ones and zeros.
First :math:`x_3=1, x_4=0` and second :math:`x_3=0, x_4=1`.
We get two special solutions in the nullspace of :math:`C` which is also the nullspace of :math:`U`:

.. math::

    \bs{s_1}=\bb -2\\0\\1\\0 \eb\rm{\ and\ }\bs{s_2}=\bb 0\\-2\\0\\1 \eb
    \begin{matrix} \leftarrow\rm{pivot}\\ \leftarrow\rm{variables}\\ 
    \leftarrow\rm{free}\\ \leftarrow\rm{variables} \end{matrix}

The Reduced Row Echelon Form :math:`R`
--------------------------------------

.. note::

    #. **Produce zeros above the pivots**. Use pivot rows to eliminate upward in :math:`R`.

    #. **Produce ones in the pivots**. Divide the whole pivot row by its pivot.

The nullspace stay the same: :math:`\N(A)=\N(U)=\N(R)`.
This nullspace becomes easiest to see when we reach the **reduced row echelon form** :math:`R = \rm{rref}(A)`.
**The pivot columns of** :math:`R` **contains** :math:`I`.

.. note::

    **Reduced form** :math:`R`: :math:`U=\bb 1&2&2&4\\0&2&0&4 \eb` becomes
    :math:`R=\bb 1&0&2&0\\0&1&0&2 \eb`.

Now (**free column 3**) = **2** (**pivot column 1**), so -2 appears in :math:`\bs{s}_1=(-2,0,1,0)`.
Second special solution :math:`\bs{s}_2=(0,-2,0,1)`.  

The case of a zero nullspace :math:`\bs{\rm{Z}}` is of the greatest importance.
It says that the columns of :math:`A` are **independent**.

**Pivot Variables and Free Variables in the Echelon Matrix** :math:`R`:

.. math::

    A=\bb p&p&f&p&f\\|&|&|&|&|\\|&|&|&|&|\\|&|&|&|&|\\ \eb \quad
    R=\bb 1&0&a&0&c\\0&1&b&0&d\\0&0&0&1&e\\0&0&0&0&0\\ \eb \quad
    \bs{s}_1=\bb -a\\-b\\1\\0\\0 \eb \quad \bs{s}_2=\bb -c\\-d\\0\\-e\\1 \eb

* :math:`A`: 3 pivot columns :math:`p`, 2 free columns :math:`f` to be revealed by :math:`R`.

* :math:`R`: :math:`I` in pivot columns, :math:`F` in free columns; 3 pivots: rank :math:`r=3`.

* Special :math:`R\bs{s}_1=\bs{0}` and :math:`R\bs{s}_2=\bs{0}` take :math:`-a` 
  to :math:`-e` from :math:`R`; 
  :math:`R\bs{s}=\bs{0}` means :math:`A\bs{s}=\bs{0}`.

Here are those steps for a 4 by 7 **reduced row echolon matrix** :math:`R` with three pivots:

.. note::

    :math:`R=\bb 1&0&x&x&x&0&x\\0&1&x&x&x&0&x\\0&0&0&0&0&1&x\\0&0&0&0&0&0&0 \eb`

    * Three pivot variables :math:`x_1, x_2, x_6`
  
    * Four free variables :math:`x_3, x_4, x_5, x_7`
  
    * Four special solutions :math:`s` in :math:`N(R)`
  
    * The pivot rows and columns contain :math:`I`

*The column space* :math:`\bs{C}(R)` *consists of all vectors of the form* :math:`(b_1,b_2,b_3,0)`.
The nullspace :math:`\bs{N}(R)` is a subspace of :math:`\R^7`.
The solutions to :math:`R\x=\0` are all the combinations of the four special 
solutions -- *one for each free variable*:

#. Columns 3, 4, 5, 7 have no pivots.
   So the four free variables are :math:`x_3, x_4, x_5, x_7`.

#. Set one free variable to 1 and set the other three free variables to zero.

#. To find :math:`\bs{s}`, solve :math:`R\bs{x}=\bs{0}` for the pivot variables :math:`x_1, x_2, x_6`.

.. note::

    Suppose :math:`A\x=\0` has more unknowns than equations (:math:`\bs{n}>\bs{m}`, more columns than rows).
    There must be at least one free column.
    **Then** math:`A\x=\0` **has nonzero solutions**.

*A short vide matrix* (:math:`n>m`) *always has nonzero vectors in its nullspace*.
There must be at least :math:`n-m` free variables, since the number of pivots cannot exceed :math:`m`.
A row might have *no* pivot -- which means an extra free variable.
When there is a free variabl, it can be set to 1.
Then the equation :math:`A\x=\0` has at least a line of nonzero solutions.

*The nullspace is a subspace*.
*Its "Dimension" is the number of free variables*.

The Rank of a Matrix
--------------------

**The true size of** :math:`A` **is given by its rank**.

.. note::

    **DEFINITION OF RANK**: The rank of :math:`A` is the number of pivots.
    This number is :math:`r`.

**Every "free column" is a combination of earlier pivot columns**.

Rank One
--------

Matrices of **rank one** have only *one pivot*.
*Every row is a multiple of the pivot row*.

**Rank one matrix**:

.. math::

    A=\bb 1&3&10\\2&6&20\\3&9&30 \eb\rightarrow R=\bb 1&3&10\\0&0&0\\0&0&0 \eb.

:math:`A =` **column times row** :math:`= \u\v^T`:

.. math::

    \bb 1&3&10\\2&6&20\\3&9&30 \eb=\bb 1\\2\\3 \eb\bb 1&3&10 \eb.

With rank one :math:`A\x=\0` is easy to understand.
That equation :math:`\u(\v^T\x)=\0` leads us to :math:`\v^t\x=0`.
All vectors :math:`\x` in the nullspace must be orthogonal to :math:`\v` in the row space.
This is the geometry when :math:`r=1`:
*row space = line*, *null space = perpendcular plane*.

The second definition of rank: **the number of independent rows**.
This is also **the number of independent columns**.

The third definition of rank: **the "dimention" of the column space**.
It is also **the dimension of the row space**.
:math:`n-r` is **the dimension of the nullspace**.

**Every** :math:`m` **by** :math:`n` **matrix of rank** :math:`r` **reduces to** 
(:math:`m` by :math:`r`) **times** (:math:`r` by :math:`n`):

.. note::

    :math:`A=(\rm{pivot\ columns\ of\ }A) (\rm{first\ }r\rm{\ rows\ of\ }R)=(\bs{\rm{COL}})(\bs{\rm{ROW}})`.

Elimination: The Big Picture
----------------------------

**Question 1 Is this column a combination of previous columns?**

If the column contains a pivot, the answer is no.
Pivot columns are "independent" of previous columns.
If column 4 has no pivot, it is a combination of columns 1, 2, 3.

**Question 2 Is this row a combination of previous rows?**

If the row contains a pivot, th answer is no.
Pivot rows are "independent" of previous rows.
If row 3 ends up with no pivot, it is a zero row and it is moved to the bottom of :math:`R`.

In other words, :math:`R` **tells us the special solutions to** :math:`A\x=\0`.
:math:`R` reveals a "basis" for three fundamental subspaces:

    The **column space** of :math:`A`--choose the pivot columns of :math:`A` as a basis.

    The **row space** of :math:`A`--choose the nonzero rows of :math:`R` as a basis.

    The **nullspace** of :math:`A`--choose the speial solutions to :math:`R\x=\0` (and :math:`A\x=\0`).

We learn from elimination the single most important number--**the rank** :math:`\bs{r}`.
That number counts the pivot columns and the pivot rows.
Then :math:`n-r` counts the free columns and the special solutions.