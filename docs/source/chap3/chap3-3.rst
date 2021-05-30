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

The Complete Solution
---------------------