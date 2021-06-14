Chapter 6.2 Diagonalizing a Matrix
==================================

When :math:`\x` is an eigenvector, multiplication by :math:`A` is just 
multiplication by a number :math:`\ld`: :math:`A\x=\ld\x`.

The point of this section is very direct.
**The matrix** :math:`A` **turns into a diagonal matrix** :math:`\Ld` **when we use the eigenvectors properly**.

.. note::

    **Diagonalization**: Suppose the :math:`n` by :math:`n` matrix :math:`A` has 
    :math:`n` linearly independent eigenvectors :math:`\x1,\cds,\x_n`.
    Put them into the columns of an **eigenvector matrix** :math:`X`.
    Then :math:`X\im AX` is the **eigenvalue matrix** :math:`\Ld`:

    * **Eigenvector matrix** :math:`X`, **Eigenvalue matrix** :math:`\Ld`:
      :math:`X\im AX=\Ld=\bb \ld_1\\&\dds\\&&\ld_n \eb`.

The matrix :math:`A=\bb 1&5\\0& 6\eb` is triangular so its eigenvalues are on the diagonal: :math:`\ld_1=1,\ld_2=6`.

.. note::

    **Eigenvectors go into** :math:`X`:

    * :math:`\bb 1\\0 \eb\bb 1\\1 \eb`.

.. math::

    \bb 1&-1\\0&1 \eb\bb 1&5\\0&6 \eb\bb 1&1\\0&1 \eb=\bb 1&0\\0&6 \eb.

In other words :math:`A=X\Ld X\im`.
Then :math:`A^2=X\Ld X\im X\Ld X\im=X\Ld^2X\im`.

:math:`A^2` **has the same eigenvectors in** :math:`X` **and squared eigenvalues in** :math:`\Ld^2`.

**Why is** :math:`AX=X\Ld`?
:math:`A` multiplies its eigenvectors, which are the columns of :math:`X`.
The first column of :math:`AX` is :math:`A\x_1`.
That is :math:`\ld_1\x_1`.
Each column of :math:`X` is multiplied by its eigenvalue:

:math:`A` **times** :math:`X`:

.. math::

    AX=A\bb \\\ \x_1&\cds&\x_n \\\ \eb=\bb \\\ \ld_1\x_1&\cds&\ld_n\x_n \\\ \eb.

The trick is to split thsis matrix :math:`AX` into :math:`X` times :math:`\Ld`:

:math:`X` **times** :math:`\Ld`:

.. math::

    \bb \\\ \ld_1\x_1&\cds&\ld_n\x_n \\\ \eb=\bb \\\ \x_1&\cds&\x_n \\\ \eb\bb \ld_1\\&\dds\\&&\ld_n \eb=X\Ld.

Keep those matrices in the right order.
Then :math:`\ld_1` multiplies the first column :math:`\x_1`, as shown.
The diagonalization is complete, and we can write :math:`AX=X\Ld` in two good ways:

.. note::

    :math:`AX=X\Ld` is :math:`X\im AX=\Ld` or :math:`A=X\Ld X\im`.

The matrix :math:`X` has an inverse, because its columns (the eigenvectors of 
:math:`A`) were assumede to be linearly independent.
*Without* :math:`n` *independent eigenvectors, we can't diagonalize*.

:math:`A` and :math:`\Ld` have the same eigenvalues :math:`\ld_1,\cds,\ld_n`.
The eigenvectors are different.
The :math:`k`th power will be :math:`A^k=X\Ld^kX\im` which is easy to compute:

.. math::

    A^k=(X\Ld X\im)(X\Ld X\im)\cds(X\Ld X\im)=X\Ld^kX\im.

**Powers of** :math:`A`:

.. math::

    \bb 1&5\\0&6 \eb^k=\bb 1&1\\0&1 \eb\bb 1\\&6^k \eb\bb 1&-1\\0&1 \eb=\bb 1&6^k-1\\0&6^k \eb=A^k.

**Remark 1**: Suppose the eigenvalues :math:`\ld_1,\cds,\ld_n` are all different.
Then it is automatic that the eigenvectors :math:`\x_1,cds,\x+n` are independent.
The eigenvector matrix :math:`X` will be *invertible*.
**Any matrix that has no repeated eigenvalues can be diagonalized**.

**Remark 2**: **We can multiply eigenvectors by any nonzero constants**.
:math:`A(c\x)=\ld(c\x)` is still true.

**Remark 3**: The eigenvectors in :math:`X` come in the same order as the eigenvalues in :math:`Ld`.
To reverse the order in :math:`\Ld`, put the eigenvector :math:`(1,1)` before :math:`(1,0)` in :math:`X`:

    **New order** :math;`6,1`:

    .. math::

        \bb 0&1\\1&-1 \eb\bb 1&5\\0&6 \eb\bb 1&1\\1&0 \eb=\bb 6&0\\0&1 \eb=\Ld_{\rm{new}}.

    To diagonalize :math:`A` we *must* use an eigenvector matrix.
    From :math:`X\im AX=\Ld` we know that :math:`AX=X\Ld`.
    Suppose the first column of :math:`X` is :math:`\x`.
    Then the first columns of :math:`AX` and :math:`X\Ld` are :math:`A\x` and :math:`\ld_1\x`.
    For those to be equal, :math:`\x` must be an eigenvector.

**Remark 4** (repeated warning for repeated eigenvalues): Some matrices have too few eigenvectors.
*Those matrices cannot be diagonalized*.

    **Not diagnoalizable**:

    .. math::

        A=\bb 1&-1\\1&-1 \eb\quad \rm{and} \quad B=\bb 0&1\\0&1 \eb.

    Their engenvalues happen to be 0 and 0.
    Nothing is special about :math:`\ld=0`, the problem is the repetition of :math:`\ld`.
    All eigenvectors of the first matrix are multiples of :math:`(1,1)`:

    **Only one line of eigenvectors**:

    .. math::

        A\x=0\x \quad\rm{means}\quad \bb 1&-1\\1&-1 \eb\bb \\\ \x\\\ \eb=\bb 0\\0 \eb\quad\rm{and}\quad \x=c\bb 1\\1 \eb.

    There is no second eigenvector, so this unusual matrix :math:`A` cannot be diagonalized.
    
    * **Invertibility** is concerned with the **eigenvalues** (:math:`\ld=0` or :math:`\ld\neq 0`).

    * **Diagonalizability** is concerned with the **eigenvectors** (too few or enough for :math:`X`).

    Each eigenvalue has at least one eigenvector.
    :math:`A-\ld I` is singular.
    If :math:`(A-\ld I)\x=\0` leads you to :math:`\x=\0`, :math:`\ld` is *not* an eigenvalue.
    Look for a mistake in solving :math:`\det(A-\ld I)=0`.

    .. tip::

        **Eigenvectors for** :math:`n` **different** :math:`\ld`\ **'s are independent**.
        **Then we can diagonalize** :math:`A`.

    .. note::

        **Independent** :math:`\x` **from different** :math:`\ld`: Eigenvectors
        :math:`\x_1,\cds,\x_j` that correspond to distinct (all different)
        eigenvalues are linearly independent.
        An :math:`n` by :math:`n` matrix that has :math:`n` different 
        eigenvalues (no repeated :math:`\ld`'s) must be diagonalizable.

    **Proof**: Suppose :math:`c_1\x_1+c_2\x_2=\0`.
    Multiply by :math:`A` to find :math:`c_1\ld_1\x_1+c_2\ld_2\x_2=\0`.
    Multiply by :math:`\ld_2` to find :math:`c_1\ld_2\x_1+c_2\ld_2\x_2=\0`.
    Now subtract one from the other: Subtraction leaves :math:`(\ld_1-\ld_2)c_1\x_1=\0`.
    Therefore :math:`c_1=0`.

        Since the :math:`\ld`'s are different and :math:`\x_1\neq\0`, we are forced to the conclusion that :math:`c_1=0`.
        Similarly :math:`c_2=0`.
        Only the combination with :math:`c_1=c_2=0` gives :math:`c_1\x_1+c_2\x_2=\0`.
        So the eigenvectors :math:`\x_1` and :math:`\x_2` must be independent.

    This proof extends directly to :math:`j` eigenvectors.
    Suppose that :math:`c_1\x_1+\cds+c_j\x_j=\0`,
    Multiply by :math:`A`, multiply by :math:`\ld_j` and subtract.
    This multiplies :math:`\x_j` by :math:`\ld_j-\ld_j=0`, and :math:`\x_j` is gone.
    Now multiply by :math:`A` and by :math:`\ld_{j-1}` and subtract.
    This removes :math:`\x_{j-1}`.
    Eventually only :math:`\x_1` is left: We reach 
    :math:`(\ld_1-\ld_2)\cds(\ld_1-\ld_j)c_1\x_1=\0` which forces :math:`c_1=0`.

    Similarly every :math:`c_i=0`.
    When the :math:`\ld`'s are all different, the eigenvectors are independent.
    A full set of eigenvectors can go into the columns of the eigenvector matrix :math:`X`.

.. note::

    **Question**: When does :math:`A^k\rightarrow zero\ matrix`?
    **Answer**: All :math:`|\ld|<1`.

Similar Matrices: Same Eigenvalues
----------------------------------









Fibonacci numbers
-----------------









Matrix Powers :math:`A^k`
-------------------------










Nondiagonalizable Matrices (Optional)
-------------------------------------