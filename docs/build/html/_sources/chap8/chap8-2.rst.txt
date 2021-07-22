Chapter 8.2 The Matrix of a Linear Transformation
=================================================

For ordinary column vectors, the input :math:`\v` is in :math:`\bs{\rm{V}}=\R^n` and 
the output :math:`T(\v)` is in :math:`\bs{\rm{W}}=\R^m`.
The matrix :math:`A` for this transformation will be :math:`m` by :math:`n`.
Our choice of bases in :math:`\bs{\rm{V}}` and :math:`\bs{\rm{W}}` will decide :math:`A`.

All vector spaces :math:`\bs{\rm{V}}` and :math:`\bs{\rm{W}}` have bases.
Each choice of those bases leads to a matrix for :math:`T`.
When the input basis is different from the output basis, the matrix for 
:math:`T(\v)=\v` will not be the identity :math:`I`.
It will be the "change of basis matrix".

.. note::

    Suppose we know :math:`T(\v)` for the input basis vectors :math:`\v_1` to :math:`\v_n`.
    Columns :math:`1` to :math:`n` of the matrix will contain those outputs :math:`T(\v_1)` to :math:`T(\v_n)`.
    :math:`A` times :math:`c =` matrix times vector :math:`=` combination of those :math:`n` columns.
    :math:`Ac` is the correct combination :math:`c_1T(\v_1)+\cds+c_nT(\v_n)=T(\v)`.

**Reason**: Every :math:`\v` is a unique combination :math:`c_1\v_1+\cds+c_n\v_n` of the basis vectors :math:`\v_j`.
Since :math:`T` is a linear transformation, :math:`T(\v)` must be 
**the same combination** :math:`c_1T(\v_1)+\cds+c_nT(\v_n)` **of the outputs** 
:math:`T(\v_j)` **in the columns**.

Change of Basis
---------------

Suppose the input space :math:`\bs{\rm{V}}=\R^2` is also the output space :math:`\bs{\rm{W}}=\R^2`.
*Suppose that* :math:`T(\v)=\v` *is the identity transformation*.
The matrix is :math:`I` only when the input basis is the same as the output basis.

For this special case :math:`T(\v)=\v`, call the matrix :math:`B` instead of :math:`A`.
We are just changing basis from the :math:`\v`'s to the :math:`\w`'s.
Each :math:`\v` is a combination of :math:`\w_1` and :math:`\w_2`.

**Input basis**:

.. math::

    \bb \\\ \v_1&\v_2 \\\ \eb=\bb 3&6\\3&8 \eb

**Output basis**:

.. math::

    \bb \\\ \w_1&\w_2 \\\ \eb=\bb 3&0\\1&2 \eb

**Change of basis**:

.. math::

    \begin{matrix} \v_1=1\w_1+1\w_2\\ \v_2=2\w_1+3\w_2\end{matrix}

We apply the identity transformation :math:`T` to each input basis vector: :math:`T(\v_1)=\v_1` and :math:`T(\v_2)=\v_2`.
**Then we write those outputs** :math:`\v_1` **and** :math:`\v_2` 
**in the output basis** :math:`\w_1` **and** :math:`\w_2`.
:math:`WB=V` so :math:`B=W\im V`.

**Matrix** :math:`B` **for change of basis**:

.. math::

    \bb \\\ \w_1&\w_2 \\\ \eb\bb \\\ B \\\ \eb=\bb \\\ \v_1&\v_2 \\\ \eb\quad
    \rm{is}\quad\bb 3&0\\1&2 \eb\bb 1&2\\1&3 \eb=\bb 3&6\\3&8 \eb.

.. note::

    When the input basis is in the columns of a matrix :math:`V`, and the output 
    basis is in the columns of :math:`W`, the change of basis matrix for 
    :math:`T=I` is :math:`B=W\im V`.

**The key**: Suppose the same vector :math:`\u` is written in the input basis of 
:math:`\v`'s and the output basis of :math:`\w`'s.

.. math::

    \begin{matrix}\u=c_1\v_1+\cds+c_n\v_n\\\u=d_1\w_1+\cds+d_n\w_n\end{matrix}
    \rm{\ is\ }\bb \\\ \v_1\cds\v_n \\\ \eb\bb c_1\\\vds\\c_n \eb=
    \bb \\\ \w_1\cds\w_n \\\ \eb\bb d_1\\\vds\\d_n \eb\rm{\ and\ }
    V\bs{c}=W\bs{d}.

The coefficients :math:`\bs{d}` in the new basis of :math:`\w`'s are :math:`\bs{d}=W\im V\bs{c}`.
Then :math:`B` is :math:`W\im V`.

:math:`\bb x\\y \eb` in the standard basis has coefficients 
:math:`\bb \\\ \w_1&\w_2\\\ \eb\im\bb x\\y \eb` in the :math:`\w_1,\w_2` basis.

Construction of the Matrix
--------------------------

Suppose :math:`T` transforms the space :math:`\bs{\rm{V}}` (:math:`n`
-dimensional) to the space :math:`\bs{\rm{W}}` (:math:`m`-dimensional).
We choose a basis :math:`\v_1,\cds,\v_n` for :math:`\bs{\rm{V}}` and we choose a 
basis :math:`\w_1,\cds,\w_m` for :math:`\bs{\rm{W}}`.
The matrix :math:`A` will be :math:`m` by :math:`n`.
To find the first column of :math:`A`, apply :math:`T` to the first basis vector :math:`\v_1`.
The output :math:`T(\v_1)` is in :math:`\bs{\rm{W}}`.

.. note::

    :math:`T(\v_1)` **is a combination** :math:`a_{11}\w_1+\cds+a_{m1}\w_m` 
    **of the output basis for** :math:`\bs{\rm{W}}`.

*These numbers** :math:`\a_{11},\cds,\a_{m1}` *go into the first column of* :math:`A`.
Transforming :math:`\v_!` to :math:`T(\v_1)` matches multiplying :math:`(1,0,\cds,0)` by :math:`A`.
It yields that first column of the matrix.
When :math:`T` is the derivative and the first basis vector is 1, its derivative is :math:`T(\v_1)=\0`.
So for the derivative matrix below, the first column of :math:`A` is all zero.

.. note::

    **Key rule**: The :math:`j`\ th column of :math:`A` is found by applying 
    :math:`T` to the :math:`j`\ th basis vector :math:`\v_j`:

    * :math:`T(\v_j)=` combination of output basis vectors :math:`=a_{1j}\w_1+\cds+a_{mj}\w_m`.

These numbers :math:`a_{ij}` go into :math:`A`.
*The matrix is constructed to get the basis vectors right*.
**Then linearity gets all other vectors right**.
Every :math:`\v` is a combination :math:`c_1\v_1+\cds+c_n\v_n`, and :math:`T(\v)` is a combination of the :math:`\w`'s.
When :math:`A` multiplies the vector :math:`\bs{c}=(c_1,\cds,c_n)` in the 
:math:`\v` combination, :math:`A\bs{c}` produces the coefficients in the 
:math:`T(\v)` combination.
This is because matrix multiplication (combining columns) is linear like :math:`T`.

The matrix :math:`A` tells us what :math:`T` does.
Every linear transformation from :math:`\bs{\rm{V}}` to :math:`\bs{\rm{W}}` can be converted to a matrix.
This matrix depends on the bases.

If you integrate a function and then differentiate, you get back to the start.
But if you differentiate before integrating, the constant term is lost.
**If we differentiate and then integrate, we can multiply their matrices** :math:`A^+A`.

Matrix Products :math:`AB` Match Transformations :math:`TS`
-----------------------------------------------------------

When we apply the transformation :math:`T` to the output from :math:`S`, we get 
:math:`TS` by this rule: :math:`(TS)(\u)` *is defined to be* :math:`T(S(\u))`.
The output :math:`S(\u)` becomes the input to :math:`T`.

When we apply the matrix :math:`A` to the output from :math:`B`, we multiply
:math:`AB` by this rule: :math:`(AB)(\x)` is defined to be :math:`A(B\x)`.
The output :math:`B\x` becomes the input to :math:`A`.
**Matrix multiplication gives the correct matrix** :math:`AB` **to represent** :math:`TS`.

.. note::

    **Multiplication**: The linear transformation :math:`TS` starts with any 
    vector :math:`\u` in :math:`\bs{\rm{U}}`, goes to :math:`S(\u)` in 
    :math:`\bs{\rm{V}}` and then to :math:`T(S(\u))` in :math:`\bs{\rm{W}}`.
    The matrix :math:`AB` starts with any :math:`\x` in :math:`\R^p`, goes to
    :math:`B\x` in :math:`\R^n` and tehn to :math:`AB\x` in :math:`\R^m`.
    **The matrix** :math:`AB` **correctly represents** :math:`TS`:

    * :math:`TS: \bs{\rm{U}}\rightarrow\bs{\rm{V}}\rightarrow\bs{\rm{W}}\quad`
      :math:`AB: (m\rm{\ by\ }n)(n\rm{\ by\ }p)=(m\rm{\ by\ }p)`

**Product of transfromations** :math:`TS` **mathces product of matrices** :math:`AB`.

Choosing the Best Bases
-----------------------

**Choose bases that diagonalize the matrix**.
With the standard basis (the columns of :math:`I`) our transformation :math:`T` 
produces some matrix :math:`A`--probably not diagonal.
That same :math:`T` is represented by different matrices when we choose different bases.
The two greate choices are eigenvectors and singular vectors:

    **Eigenvectors**: If :math:`T` transforms :math:`\R^n` to :math:`\R^n`, its matrix :math:`A` is square.
    But using the standard basis, that matrix :math:`A` is probably not diagonal.
    If there are :math:`n` independent eigenvectors, *choose those as the input and output basis*.
    In this good basis, **the matrix for** :math:`T` **is the diagonal eigenvalue matrix** :math:`\Ld`.

.. note::

    :math:`A_{\rm{new}}=B\im AB` **in the new basis of** :math:`\b`
    \ **'s is similar to** :math:`A` **in the standard basis**:
    
    * :math:`A_{\b\rm{'s\ to\ }\b\rm{'s}}=B\im_{\rm{standard\ to\ }\b\rm{'s}}A_{\rm{standard}}B_{\b\rm{'s\ to\ standard}}`

Finally we allow *different spaces* :math:`V` *and* :math:`W`, *and different bases* :math:`\v`'s and :math:`\w`'s.

    **Singular vectors**: The SVD says that :math:`U\im AV=\Sg`.
    The right singular vectors :math:`\v_1,\cds,\v_n` will be the input basis.
    The left singular vectors :math:`\u_1,\cds,\u_m` will be the output basis.
    By the rule for matrix multiplication, the matrix for the same 
    transformation in these new bases is :math:`B\im_{\rm{out}}AB_{\rm{in}}=U\im AV=\Sg`.

:math:`\Sg` is "**isometric**" to :math:`A`: :math:`C=Q_1\im AQ_2` 
*is isometric to* :math:`A` *if*` :math:`Q_1` *and* :math:`Q_2` *are orthogonal*.