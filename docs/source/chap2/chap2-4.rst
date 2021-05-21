Chapter 2.4 Rules for Matrix Operations
=======================================

**The entry in row** :math:`i` **and column** :math:`j` **is called** :math:`a_{ij}` **or** :math:`A(i,j)`.

.. tip::

    **To multiply** :math:`AB`: If :math:`A` has :math:`n` columns, :math:`B` must have :math:`n` rows.


**Every column of** :math:`B` **is multiplied by** :math:`A`.

.. note::

    **Fundamental Law of Matrix Multiplication**: :math:`AB` times :math:`C` equals :math:`A` times :math:`BC`.

The parentheses can move safely in :math:`(AB)C=A(BC)`.

Suppose :math:`A` is :math:`m` by :math:`n` and :math:`B` is :math:`n` by :math:`p`.
The product :math:`AB` is :math:`m` by :math:`p`.

.. math::

    (\bs{m} \times n)(n \times \bs{p}) = (\bs{m} \times \bs{p}).

A row times a column is 1 by :math:`n` multiplies :math:`n` by 1.
The result will by 1 by 1.
That single number is the "dot product".

.. note::

    **1. The entry in row** :math:`i` **and column** :math:`j` **of** :math:`AB` 
    **is** (row :math:`i` of :math:`A`) :math:`\cd` (column :math:`j` of :math:`B`).

If :math:`A` and :math:`B` are :math:`n` by :math:`n`, so is :math:`AB`.
It contains :math:`n^2` dot products, row of :math:`A` times column of :math:`B`.
Each dot product need :math:`n` multiplications, so **the computation of** 
:math:`AB` **uses** :math:`n^3` **separate multiplications**.

The Second and Third Ways: Rows and Columns
-------------------------------------------

Each column of :math:`AB` is a combination of the columns of :math:`A`.

**2. Matrix** :math:`\bs{A}` **times every column of** :math:`\bs{B}`:

.. math::

    A \bb \b_1 \cds \b_p \eb = \bb A\b_1 \cds A\b_p \eb.

Every row of :math:`AB` is a combination of the rows of :math:`B`.

**3. Every row of** :math:`\bs{A}` **times matrix** :math:`\bs{B}`:

.. math::

    \bb \bs{\mathrm{row}}\ i\ \bs{\mathrm{of}}\ A \eb
    \bb 1&2&3 \\ 4&5&6 \\ 7&8&9 \eb = 
    \bb \bs{\mathrm{row}}\ i\ \bs{\mathrm{of}}\ AB \eb.

:math:`AB = (m \times n)(n \times p) = (m \times p)`: :math:`mp` dot products with :math:`n` steps each.

The Fourth Way: Columns Multiply Rows
-------------------------------------

**4. Multiply columns 1 to** :math:`\bs{n}` **of** :math:`\bs{A}` 
**times rows 1 to** :math:`\bs{n}` **of** :math:`\bs{B}`\ **. Add those matrices.**

.. math::

    \bb \bs{\mathrm{col\ 1}}&\bs{\mathrm{col\ 2}}&\bs{\mathrm{col\ 3}}\\
    \cd&\cd&\cd \\ \cd&\cd&\cd \eb
    \bb \bs{\mathrm{row\ 1}}&\cd&\cd \\ \bs{\mathrm{row\ 2}}&\cd&\cd \\
    \bs{\mathrm{row\ 3}}&\cd&\cd \eb
    
    = (\bs{\mathrm{col\ 1}})(\bs{\mathrm{row\ 1}})
    + (\bs{\mathrm{col\ 2}})(\bs{\mathrm{row\ 2}})
    + (\bs{\mathrm{col\ 3}})(\bs{\mathrm{row\ 3}}).

For 2 by 2 matrices:

.. math::

    AB = \bb a&b\\c&d \eb \bb E&F\\G&H \eb = \bb aE+bG&aF+bH \\ cE+dG&cF+dH \eb

.. note::

    **Add columns of** :math:`A` **times rows of** :math:`B`:\
    :math:`AB = \bb a\\c \eb \bb E&F \eb + \bb b\\d \eb \bb G&H \eb`

This uses the same :math:`mnp` steps as in the dot products but in a new order.

The Laws for Matrix Operations
------------------------------

**Laws that matrix operations obey**:

* Commutative law: :math:`A+b=B+A`
* Distributive law: :math:`c(A+B) = cA+cB`
* Associative law: :math:`A+(B+C) = (A+B)+C`
* Distributive law from the left: :math:`A(B+C) = AB+AC`
* Distributive law from the right: :math:`(A+B)C = AC + BC`
* Associative law for :math:`ABC` (**parentheses not needed**): :math:`A(BC) = (AB)C`

**The commutative "law" is usually broken**: :math:`AB \neq BA`.

.. note::

    :math:`A^p = AAA\cds A` (:math:`p` **factors**):
    :math:`(A^p)(A^q) = A^{p+q} \quad (A^p)^q = A^{pq}`

Block Matrices and Block Multiplication
---------------------------------------

4 by 6 matrix, 2 by 2 blocks give 2 by 3 block matrix:

.. math::

    A = 
    \left[\begin{array}{cc|cc|cc}
    1&0&1&0&1&0 \\ 0&1&0&1&0&1 \\ \hline
    1&0&1&0&1&0 \\ 0&1&0&1&0&1
    \end{array}\right]
    = \bb I&I&I \\ I&I&I \eb


.. note::

    **Block multiplication**: If blocks of :math:`A` can multiply blocks of 
    :math:`B`, then block multiplication of :math:`AB` is allowed.
    Cuts between columns of :math:`A` match cuts between rows of :math:`B`.

    * :math:`\bb A_{11}&A_{12} \\ A_{21}&A_{22} \eb \bb B_{11}\\B_{21} \eb = \bb A_{11}B_{11}+A_{12}B_{21} \\ A_{21}B_{11}+A_{22}B_{21} \eb`

**Important special case**: Let the blocks of :math:`A` be its :math:`n` columns.
Let the blocks of :math:`B` be its :math:`n` rows. 
Then block multiplication :math:`AB` adds up **columns times rows**:

.. math::

    \bb |&&| \\ a_1&\cds &a_n \\ |&&| \eb
    \bb - &b_1& - \\ & \vdots & \\ - &b_n& - \eb
    = \bb a_1b_1 + \cds + a_nb_n \eb.

For example,

.. math::

        \bb 1&4\\1&5 \eb\bb 3&2\\1&0 \eb
        =\bb 1\\1 \eb\bb 3&2 \eb+\bb 4\\5 \eb\bb 1&0 \eb
        =\bb 3&2\\3&2 \eb+\bb 4&0\\5&0 \eb=\bb 7&2\\8&2 \eb.

the usual way, rows times columns, gives four dot products (8 multiplications).
The new way, columns times rows, gives two full matrices (the same 8 multiplications).

**Elimination by blocks**: Suppose a matrix has four blocks :math:`A, B, C, D`:

.. math::

    \left[\begin{array}{c|c}
    I & 0 \\ \hline
    -CA^{-1} & I
    \end{array}\right]
    \left[\begin{array}{c|c}
    A & B \\ \hline
    C & D
    \end{array}\right]
    \left[\begin{array}{c|c}
    A & B \\ \hline
    0 & D-CA^{-1}B
    \end{array}\right]

The final block is :math:`D-CA^{-1}B`, just like :math:`d-cb/a`.
This is called the **Schur complement**.