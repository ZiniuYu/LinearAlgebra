Chapter 3.3 The Complete Solution to :math:`Ax=b`
=================================================

The last section totally solved :math:`A\x=\0`.
Elimination converted the problem to :math:`R\x=\0`.
Now the right side :math:`\b` is not zero.
:math:`A\x=\b` is reduced to a simple system :math:`R\x=\bs{d}` with the same solutions.
One way to organize that is to **add** :math:`\b` **as an extra column of the matrix**.

.. math::

    \bb 1&3&0&2\\0&0&1&4\\1&3&1&6 \eb\bb x_1\\x_2\\x_3\\x_4 \eb=\bb 1\\6\\7 \eb
    \quad\begin{matrix} \rm{has\ the}\\\rm{augmented}\\\rm{matrix} \end{matrix}
    \quad\bb 1&3&0&2&1\\0&0&1&4&6\\1&3&1&6&7 \eb=\bb A&\b \eb

When we apply the usual elimination steps to :math:`A`, reacehing :math:`R`, we also apply them to :math:`\b`.

.. math::

    \bb 1&3&0&2\\0&0&1&4\\0&0&0&0 \eb\bb x_1\\x_2\\x_3\\x_4 \eb=\bb 1\\6\\0 \eb
    \quad\begin{matrix} \rm{has\ the}\\\rm{augmented}\\\rm{matrix} \end{matrix}
    \quad\bb 1&3&0&2&1\\0&0&1&4&6\\0&0&0&0&0 \eb=\bb R&\bs{d} \eb

The very last zero is crucial.
The third equation has become :math:`0=0`.
So the equations can be solved.

Here are the same augmented matrices for a general :math:`\b = (b_1,b_2,b)`:

.. math::

    \bb A&\b \eb=\bb 1&3&0&2&b_1\\0&0&1&4&b_2\\1&3&1&6&b_3 \eb\rightarrow
    \bb 1&3&0&2&b_1\\0&0&1&4&b_2\\0&0&0&0&b_3-b_1-b_2 \eb=\bb R&\bs{d} \eb

Now we get :math:`0=0` in the third equation only of :math:`b_3-b_1-b_2=0`.
This is :math:`b_1+b_2=b_3`.

One Particular Solution :math:`Ax_p=b`
--------------------------------------

For an easy solution :math:`\x_p`, *choose the free variables to be zero*: :math:`x_2=x_4=0`.
Then the two nonzero equations give the two pivot variables :math:`x_1=1` and :math:`x_3=6`.

.. Tip::

    **For a solution to exist, zero rows in** :math:`R` **must also be zero in** :math:`\bs{d}`.
    **Since** :math:`I` **is in the pivot rows and pivot columns of** :math:`R`, 
    **the pivot variables in** :math:`x_{\rm{particular}}` **come from**
    :math:`\bs{d}`:

    * :math:`R\x_p=\bb 1&3&0&2\\0&0&1&4\\0&0&0&0 \eb\bb 1\\0\\6\\0 \eb=\bb 1\\6\\0 \eb`

Notice how we *choose* the free variables (as zero) and *solve* for the pivot variables.
When the free variables are zero, the pivot variables for :math:`\x_p` are 
already seen in the right side vector :math:`\bs{d}`.

.. note::

    :math:`\x_{\rm{particular}}`: The particular solution solves :math:`A\x_p=\b`.

    :math:`\x_{\rm{nullspace}}`: The :math:`n-r` special solutions solve :math:`A\x_n=\0`.

That particular solution is :math:`(1,0,6,0)`.
The two special (nullspace) solutions to :math:`R\x=\0` come from the two free 
columns of :math:`R`, by reversing signs of 3, 2, and 4.

.. note::

    **Complete solution one** :math:`\x_p` **many** :math:`\x_n`:

    * :math:`\x=\x_p+\x_n=\bb 1\\0\\6\\0 \eb+x_2\bb -3\\1\\0\\0 \eb+x_4\bb -2\\0\\-4\\1 \eb`.

**Question**: Suppose :math:`A` is a square invertible matrix, :math:`m=n=r`.
Whar are :math:`\x_p` and :math:`\x_n`?

**Answer**: The particular solution is the one and *only* solution :math:`\x_p=A^{-1}\b`.
There are no special solutions or free variables.
:math:`R=I` has no zero rows.

The only vector in the nullspace is :math:`\x_n=\0`.
The complete solution is :math:`\x=\x_p+\x_n=A^{-1}\b+\0`.

An important case: :math:`A` has *full column rank*.
Every column has a pivot.
*The rank is* :math:`r=n`.
The matrix is tall and thin (:math:`m\geq n`).
Row reduction puts :math:`I` at the top, when :math:`A` is reduced to :math:`R` with rank :math:`n`:

**Full Column Rank**:

.. math::

    R=\bb I\\0 \eb=\bb n\rm{\ by\ }n\rm{\ identity\ matrix}\\m-n \rm{\ rows\ of\ zeros}\eb.

There are no free columnso r free variables.
The nullspace is :math:`\bs{\rm{Z}}` = {zero vector}.

.. note::

    Every matrix :math:`A` with **full column rank** :math:`(r=n)` has all these properties:

    #. All columns of :math:`A` are pivot columns.

    #. There are no free variables or special solutions.

    #. The nullspace :math:`\bs{N}(A)` contains only the zero vector :math:`\x=\0`.

    #. If :math:`A\x=\b` has a solution (it might not) then it has only *one solution*.

In the essential language of the next section, this :math:`A` has **independent columns**.
:math:`A\x=\0` only happens when :math:`\x=\0`.
*The square matrix* :math:`A^TA` *is invertible when the rank is* :math:`n`.

In this case the nullspace of :math:`A`(and :math:`R`) has shrunk to the zero vector.
The solution to :math:`A\x=\b` is *unique* (if it exists).
There will be :math:`m-n` zero rows in :math:`R`.
So there are :math:`m-n` conditions on :math:`\b` in order to have :math:`0=0` 
in those rows, and :math:`\b` in the column space.

.. Tip::

    With full column rank, :math:`A\x=\b` has *one* solution or *no* solution (:math:`m>n` is overdetermined).

The Complete Solution
---------------------

The other extreme case is full row rank.
Now :math:`A\x=\b` has *one or infinitely many* solutions.
In this case :math:`A` must be *short and wide* :math:`(m\leq n)`.
**A matrix has full row rank if** :math:`\bs{r=m}`.

**Full row rank** (rank :math:`r=m=2`):

.. math::

    x+y+z&=3

    x+2y-z&=4

The particular solution will be one point on the line.
Adding the nullspace vectors :math:`\x_n` will move us along the line.
Then :math:`\x=\x_p+\x_n` gives the whole line of solutions.

.. Tip::

    Complete solution = *one* particular solution + *all* nullspace solutions.

.. math::

    \bb 1&1&1&3\\1&2&-1&4 \eb\rightarrow\bb 1&1&1&3\\0&1&-2&1 \eb\rightarrow\bb 1&0&3&2\\0&1&-2&1 \eb=\bb R&\bs{d} \eb.

*The particular solution has free variable* :math:`x_3=0`.
The special solution has :math:`x_3=1`:

* :math:`\x_{\rm{particular}}` comes directly from :math:`\bs{d}` on the right side: :math:`\x_p=(2,1,0)`.

* :math:`\x_{\rm{special}}` comes from the third column (free column) of :math:`R`: :math:`\bs{s}=(-3,2,1)`.

.. note::

    **Complete solution**: :math:`\x=\x_p+\x_n=\bb 2\\1\\0 \eb+x_3\bb -3\\2\\1\eb`.

If :math:`m<n` the equation :math:`A\x=\b` is **underdetermined** (many solutions).

.. note::

    Every matrix :math:`A` with **full row rank** :math:`\bs{r=m}` has all these properties:

    #. All rows have pivots, and :math:`R` **has no zero rows**.

    #. :math:`A\x=\b` has a **solution for every right side** :math:`\b`.

    #. The column space is the whole space :math:`\bs{R}^m`.

    #. There are :math:`n-r=n-m` special solutions in the nullspace of :math:`A`.

In this case with :math:`m` pivots, the rows are "**linearly independent**".
So the columns of :math:`A^T` are linearly independent.
The nullspace of :math:`A^T` is the zero vector.

**The four possibilities for linear equations depend on the rank** :math:`\bs{r}`.
The reduced :math:`R` will fall in the same category as the matrix :math:`A`.
:math:`F` is the free part of :math:`R`:

#. :math:`r=m` and :math:`r=n` *Square and invertible* :math:`A\x=\b` has 1 solution: :math:`R=\bb I \eb`.

#. :math:`r=m` and :math:`r<n` *Short and wide* :math:`A\x=\b` has :math:`\infty` solution: :math:`R=\bb I&F \eb`.

#. :math:`r<m` and :math:`r=n` *Tall and thin* :math:`A\x=\b` has 0 or 1 solution: :math:`R=\bb I\\0 \eb`.

#. :math:`r<m` and :math:`r<n` *Not full rank* :math:`A\x=\b` has 0 or :math:`\infty` solution: :math:`R=\bb I&F\\0&0 \eb`.