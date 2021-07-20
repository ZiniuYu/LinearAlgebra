Chapter 8.2 The Matrix of a Linear Transformation
=================================================

For ordinary column vectors, the input :math:`\v` is in :math:`\bs{V}=\R^n` and 
the output :math:`T(\v)` is in :math:`\bs{W}=\R^m`.
The matrix :math:`A` for this transformation will be :math:`m` by :math:`n`.
Our choice of bases in :math:`\bs{V}` and :math:`\bs{W}` will decide :math:`A`.

All vector spaces :math:`\bs{V}` and :math:`\bs{W}` have bases.
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

Suppose the input space :math:`\bs{V}=\R^2` is also the output space :math:`\bs{W}=\R^2`.
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


Construction of the Matrix
--------------------------









Matrix Products :math:`AB` Match Transformations :math:`TS`
-----------------------------------------------------------