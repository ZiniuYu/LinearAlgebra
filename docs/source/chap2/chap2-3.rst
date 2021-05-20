Chapter 2.3 Elimination Using Matrices
======================================

#. To see how each step is a matrix multiplication.
#. To assemble all those steps :math:`E_{ij}` into one elimination matrix :math:`E`.
#. To see how each :math:`E_{ij}` is inverted by its inverse matrix :math:`E_{ij}^{-1}`.
#. To assemble all those inverse :math:`E_{ij}^{-1}` (in the right order) into :math:`L`.

Matrix times Vectors and :math:`Ax = b`
---------------------------------------

The 3 by 3 example in the previous section has the short form :math:`A\x=\b`:

.. math::

    2x_1+4x_2-2x_3 &= 2
    
    4x_1+9x_2-3x_3 &= 8

    -2x_1-3x_2+7x_3 &= 10

is the same as

.. math::

    \bb 2&4&-2 \\ 4&9&-3 \\-2&-3&7 \eb \bb x_1\\x_2\\x_3 \eb = \bb 2\\8\\10 \eb.

The unknown is :math:`\x = \bb x_1\\x_2\\x_3 \eb` and the solution is :math:`\x = \bb -1\\2\\2 \eb`.

**Column form**

.. math::

    A\x = (-1) \bb 2\\4\\-2 \eb + 2 \bb 4\\9\\-3 \eb + 2 \bb -2\\-3\\7 \eb = \bb 2\\8\\10 \eb = \b.

:math:`A\x` **is a combination of the columns of** :math:`A`.
We use the **row form** of matrix multiplication.
**Components of** :math:`A\x` **are dot products with rows of** :math:`A`.

    The first component of :math:`A\x` above is :math:`(-1)(2) + (2)(4) + (2)(-2)`.

    The :math:`i`\ th component of :math:`A\x` is 
    :math:`(row\ i) \cd \x = a_{i1}x_1 + a_{i2}x_2 + \cds + a_{in}x_n = \Sigma_{j=1}^n a_{ij}x_j`.

General rule: :math:`A_{ij} = A(i,j)` is in **row i**, **column j**.

The Matrix Form of One Elimination Step
---------------------------------------

2 times the first equation is subtracted from the second equation.
On the right side, 2 times the frist component of :math:`\b` is subtracted from the second component.

**First step**: :math:`\b = \bb 2\\8\\10 \eb` changes to :math:`\b_{\mathrm{new}} = \bb 2\\4\\10 \eb`.

The same result :math:`\b_{\mathrm{new}} = E\b` is achieved when we multiply an 
"elimination matrix" :math:`E` times :math:`\b`.
It subtracts :math:`2b_1` from :math:`b_2`:

.. note::

    **The elimination matrix is** :math:`E = \bb 1&0&0 \\ -2&1&0 \\ 0&0&1 \eb`.

**Multiplication by** :math:`E` **subtracts 2 times row 1 from row 2**.
Rows 1 and 3 stay the same:

.. math::

    \bb 1&0&0 \\ -2&1&0 \\ 0&0&1 \eb \bb 2\\8\\10 \eb = \bb 2\\4\\10 \eb \quad
    \bb 1&0&0 \\ -2&1&0 \\ 0&0&1 \eb \bb b_1\\b_2\\b_3 \eb == \bb b_1 \\b_2-2b_1\\b_3 \eb

.. note::

    The **idendity matrix** has 1's on the diagonal and otherwise 0's.
    Then :math:`i\b = \b` for all :math:`\b`.
    The **elementary matrix or elimination matrix** :math:`E_{ij}` has the extra
    nonzero entry :math:`-l` in the :math:`i,j` position.
    Then :math:`E_{ij}` subtracts a multiple :math:`l` of row :math:`j` from row :math:`i`.

Matrix Multiplication
---------------------

The Matrix :math:`P_{ij}` for a Row Exchange
--------------------------------------------

The Augmented Matrix
--------------------