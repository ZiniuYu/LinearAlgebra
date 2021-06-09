Chapter 5.2 Permutations and Cofactors
======================================

.. math::

    A=\bb 2&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&2 \eb\quad\rm{has}\quad\det A=5.

We can find this determinant in all three ways: **pivots**, **big formula**, **cofactors**.

1. The product of the pivots is :math:`2\cd\frac{3}{2}\cd\frac{4}{3}\cd\frac{5}{4}`.
   Cancellation produces 5.

2. The "big formula" has :math:`4!=24` terms.
   Only five terms are nonzero:
   
.. math::

    \det A=16-4-4-4+1=5.

3. The numbers :math:`2,-1,0,0` in the first row multiply their cofactors :math:`4,3,2,1` from the other rows.
   That gives :math:`2\cd 4-1\cd 3=5`.
   Those cofactors are 3 by 3 determinants.
   Cofactors use the rows and columns that are *not* used by the entry in the first row.

.. tip::

    **Every term in a determinant uses each row and column once!**

The Pivot Formula
-----------------

When elimination leads to :math:`A=LU`, the pivots :math:`d_1,\cds,d_n` are on 
the diagonal of the upper triangular :math:`U`.
If no row exchanges are involved, **multiply those pivots** to find the determinant:

.. math::

    \det A=(\det L)(\det U)=(1)(d_1 d_2\cds d_n).

.. note::

    :math:`(\det P)(\det A)=(\det L)(\det U)` gives :math:`\det A=\pm(d_1 d_2 \cds d_n)`.

The first pivots of this tridiagonal matrix :math:`A` are :math:`2,\frac{3}{2},\frac{4}{3}`.
The next are :math:`\frac{5}{4}` and :math:`\frac{6}{5}` and eventually :math:`\frac{n+1}{n}`.
Factoring this :math:`n` by :math:`n` matrix reveals its determinant:

.. math::

    \bb 2&-1\\-1&2&-1\\&-1&2&\cd\\&&\cd&\cd&-1\\&&&-1&2 \eb=
    \bb 1\\-\frac{1}{2}&1\\&-\frac{2}{3}&1\\&&\cd&\cd\\&&&-\frac{n-1}{n}&1 \eb
    \bb 2&-1\\&\frac{3}{2}&-1\\&&\frac{4}{3}&-1\\&&&\cd&\cd\\&&&&\frac{n+1}{n} \eb.

The pivots are on the diagonal of :math:`U` (the last matrix).
*The* :math:`n` *by* :math:`n` *determinant is* :math:`n+1`:

**-1, 2, -1 matrix**:

.. math::

    \det A=(2)\left(\frac{3}{2}\right)\left(\frac{4}{3}\right)\cds\left(\frac{n+1}{n}\right)=n+1.

Important point: The first pivots depend only on the *upper left corner* of the original matrix :math:`A`.
This is a rule for all matrices without row exchanges.

    The first :math:`k` pivots come from the :math:`k` by :math:`k` matrix 
    :math:`A_k` in the top left corner of :math:`A`.
    **The determinant of that corner submatrix** :math:`A_k` **is** 
    :math:`d_1d_2\cds d_k` (**first** :math:`k` **pivots**).

Elimination deals with the matrix :math:`A_k` in the upper left corner while starting on the whole matrix.
We assume no row exchanges--then :math:`A=LU` and :math:`A_k=L_kU_k`.
Dividing one determinant by the previous determinant (:math:`\det A_k` divided 
by :math:`\det A_{k-1}`) cancels everything but the latest pivot :math:`d_k`.
**Each pivot is a ratio of determinants**:

.. note::

    **Pivots from determinants**: **The** :math:`k`\ **th pivot is** 
    :math:`\dp d_k=\frac{d_1d_2\cds d_k}{d_1d_2\cds d_{k-1}}=\frac{\det A_k}{\det A_{k-1}}`

*We don't need row exchanges when all the upper left submatrices have* :math:`\det A_k\neq 0`.

The Big Formula for Determinants
--------------------------------

**The formula has ** :math:`n!` **terms**.
Half the terms have minus signs (as in :math:`-bc`).
The other half have plus signs (as in :math:`ad`).
For :math:`n=3` there are :math:`3!=(3)(2)(1)=6` terms:

.. note::

    3 by 3 determinant: :math:`\bv a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}
    \\a_{31}&a_{32}&a_{33} \ev=
    \begin{matrix}+a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\\
    -a_{11}a_{23}a_{32}-a_{12}a_{21}a_{33}-a_{13}a_{22}a_{31}\end{matrix}`.

Notice the pattern.
Each product like :math:`a_{11}a_{23}a_{32}` has **one entry from each row**.
It also has **one entry from each column**.
The column order 1, 3, 2 means that this particular term comes with a minus sign.
The column 3, 1, 2 in :math:`a_{13}a_{21}a_{32}` has a plus sign.
It will be "permutations" that tell us the sign.

To derive the big formula I start with :math:`n=2`.
The goal is to reach :math:`ad-bc` in a systematic way.
Break each row into two simpler rows:

.. math::

    \bb a&b \eb=\bb a&0 \eb+\bb 0&b \eb\quad\rm{and}\quad\bb c&d \eb=\bb c&0 \eb+\bb 0&d \eb.

Now apply linearity, first in row 1 (with row 2 fixed) and then in row 2 (with row 1 fixed):

.. math::

    \bv a&b\\c&d \ev=\bv a&0\\c&d \ev+\bv 0&b\\c&d \ev=\bv a&0\\c&0 \ev+\bv a&0\\0&d \ev+\bv 0&b\\c&0 \ev+\bv 0&b\\0&d \ev.

The last line has :math:`2^2=4` determinants.
The first and fourth are zero because one row is a multiple of the other row.
We are left with :math:`2!=2` determinants to compute:

.. math::

    \bv a&0\\c&d \ev+\bv 0&b\\c&d \ev=ad\bv 1&0\\0&1 \ev+bc\bv 0&1\\1&0 \ev=ad-bc.

The splitting led to permutation matrices.
Their determinants give a plus or minus sign.
The permutation tells the column sequence.
In this case the column order is (1,2) or (2,1).

Now try :math:`n=3`.
We pay attention only when **the entries** :math:`a_{ij}` **come rom different columns**, like :math:`(3,1,2)`:

.. note::

    :math:`\bv a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33} 
    \ev=\begin{matrix}\bv a_{11}\\&a_{22}\\&&a_{33} \ev+\bv &a_{12}\\&&a_{23}
    \\a_{31} \ev+\bv &&a_{13}\\a_{21}\\&a_{32} \ev \\
    +\bv a_{11}\\&&a_{23}\\&a_{32} \ev+\bv &a_{12}\\a_{21}\\&&a_{33} \ev+\bv
    &&a_{13}\\&a_{22}\\a_{31} \ev\end{matrix}`.

**There are** :math:`3!=6` **ways to order the columns, so six determinants**.
The six permutations of :math:`(1,2,3)` include the identity permutation  :math:`(1,2,3)` from :math:`P=I`.

.. math::

    \bs{\rm{Column\ numbers}} = (1,2,3),(2,3,1),(3,1,2),(1,3,2),(2,1,3),(3,2,1).

The last three are *odd permutations* (one exchange).
The first three are *even permutations* (0 or 2 exchanges).
Factor out the :math:`a_{ij}`:

.. math::

    \det A=a_{11}a_{22}a_{33}\bv 1\\&1\\&&1 \ev+a_{12}a_{23}a_{31}\bv &1\\&&1\\1 
    \ev+a_{13}a_{21}a_{32}\bv &&1\\1\\&1 \ev

    +a_{11}a_{23}a_{32}\bv 1\\&&1\\&1 \ev+a_{12}a_{21}a_{33}\bv &1\\1\\&&1 \ev+
    a_{13}a_{22}a_{31}\bv &&1\\&1\\1 \ev.

The first three (even) permutations have :math:`\det P=+1`, the last three (odd) permutations have :math:`\det P=-1`.

Now you can see the :math:`n` by :math:`n` formula.
There are :math:`n!` orderings of the columns.
The columns :math:`(1,2,\cds,n)` go in each possible order :math:`(\alpha,\beta,\cds,\omega)`.
Taking :math:`a_{1\alpha}` from row 1 and :math:`a_{2\beta}` from row 2 and 
eventually :math:`a_{n\omega}` from row :math:`n`, the determinant contains the
product :math:`a_{1\alpha}a_{2\beta}\cds a_{n\omega}` times :math:`+1` or
:math:`-1`.

The determinant of :math:`A` is the sum of these :math:`n!` simple determinants, times 1 or -1.
The simple determinants :math:`a_{1\alpha}a_{2\beta}\cds a_{n\omega}` choose **one entry from every row and column**.

.. note::

    **BIG FORMULA**: :math:`\det A=` sum over all :math:`n!` column permutations 
    :math:`P=(\alpha,\beta,\cds,\omega)=\sum(\det P)a_{1\alpha}a_{2\beta}\cds a_{n\omega}`.

Determinant by Cofactors
------------------------

**When you separate out the factor** :math:`a_{11}` **or** :math:`a_{12}` **or** 
:math:`a_{1\alpha}` **that comes from the first row**, you see linearity.
For 3 by 3, separate the usual 6 terms of the determinant into 3 pairs:

.. note::

    :math:`\det A=a_{11}(a_{22}a_{33}-a_{23}a_{32})+a_{12}(a_{23}a_{31}-a_{21}a_{33})+a_{13}(a_{21}a_{32}-a_{22}a_{31})`.

Those three quantities in parentheses are called "**cofactors**".
They are **2 by 2 determinants**, from row 2 and 3.
The first row contributes the factors :math:`a_{11},a_{12},a_{13}`.
*The lower rows contribute the cofactors* :math:`C_{11},C_{12},C_{13}`.
Certainly the determinant :math:`a_{11}C_{11}+a_{12}C_{12}+a_{13}C_{13}` depends linearly on :math:`a_{11},a_{12},a_{13}`.

The cofactor of :math:`a_{11}` is :math:`C_{11}=a_{22}a_{33}-a_{23}a_{32}`.
You can see it in this splitting:

.. math::

    \bv a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33} \ev=
    \bv a_{11}\\&a_{22}&a_{23}\\&a_{32}&a_{33} \ev+
    \bv &a_{12}&\\a_{21}&&a_{23}\\a_{31}&&a_{33} \ev+
    \bv &&a_{13}\\a_{21}&a_{22}&\\a_{31}&a_{32}& \ev.

We are still choosing **one entry from each row and column**.
Since :math:`a_{11}` uses up row 1 and column 1, that leaves a 2 by 2 determinant as its cofactor.

The sign pattern for cofactors along the first row is *plus-minus-plus-minus*.
**You cross out row 1 and column** :math:`j` **to get a submatrix** :math:`M_{1j}` **of size** :math:`n-1`.
Multiply its determinant by the sign :math:`(-1)^{1+j}` to get the cofactor:

    The cofactors along row 1 are :math:`C_{1j}=(-1)^{1+j}\det M_{1j}`.

    **The cofactor expansion is** :math:`\det A=a_{11}C_{11}+a_{12}+C_{12}+\cds+a_{1n}C_{1n}`.


