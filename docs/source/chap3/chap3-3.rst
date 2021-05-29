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


The Complete Solution
---------------------