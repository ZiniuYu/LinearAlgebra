Chapter 6.4 Symmetric Matrices
==============================

**What is special about** :math:`S\x=\ld\x` **when** :math:`S` **is symmetric**?

.. note::

    **1. A symmetric matrix has only real eigenvalues**.

    **2. The eigenvectors can be chosen orthonormal**.

Those :math:`n` orthonormal eigenvectors go into the columns of :math:`X`.
Every symmetric matrix can be diagonalized.
**Its eigenvector matrix** :math:`X` **becomes an orthogonal matrix** :math:`Q`.
Orthogonal matrices have :math:`Q\im=Q^T`.

The eigenvectors do not *have* to be unit vectors.
Their lengths are chosen to be unit vectors.
Then :math:`A=X\Ld X\im` is in its special and particular form :math:`S=Q\Ld Q\im` for symmetric matrices.

.. note::

    **(Spectral Theorem)**: Every symmetric matrix has the factorization 
    :math:`S=Q\Ld Q^T` with real eigenvalues in :math:`\Ld` and orthonormal
    eigenvectors in the columns of :math:`Q`:

    * **Symmetric diagonalization**: :math:`S=Q\Ld Q\im=Q\Ld Q^T` with :math:`Q\im=Q^T`.

The *spectral theorem* will be proved in three steps:

#. By an example, showing real :math`\ld`'s in :math:`\Ld` and orthonormal :math:`\x`'s in :math:`Q`.

#. By a proof of those facts when no eigenvalues are repeated.

#. By a proof that allows repeated eigenvalues.

For :math:`S=\bb 1&2\\2&4 \eb`, the determinant of :math:`S-\ld I` is :math:`\ld^2-5\ld`.
The eigenvalues are 0 and 5 (*both real*).
:math:`\ld=0` is an eigenvalue because :math:`S` is singular, and :math:`\ld=5`
matches the *trace* down the diagonal of :math:`S`: :math:`0+5` agrees with
:math:`1+4`.

Two eigenvectors are :math:`(2,-1)` and :math:`(1,2)`--orthogonal but not yet orthonormal.
The eigenvector for :math:`\ld=0` is in the *nullspace* of :math:`A`.
The eigenvector for :math:`\ld=5` is in the *column space*.
The Fundamental Theorem says that the nullspace is perpendicular to the **row space**--not the column space.
But our matrix is *symmetric*!
Its row and column spaces are the same.
Its eigenvectors :math:`(2,-1)` and :math:`(1,2)` must be (and are) perpendicular.

Divide them by their lengths :math:`\sqrt{5}` to get unit vectors.
Put those unit eigenvectors into the columns of :math:`Q`.
Then :math:`Q\im SQ` is :math:`\Ld` and :math:`Q\im=Q^T`.

.. math::

    Q\im SQ=\frac{1}{\sqrt{5}}\bb 2&-1\\1&2 \eb\bb 1&2\\2&4 \eb\frac{1}{\sqrt{5}}\bb 2&1\\-1&2 \eb=\bb 0&0\\0&5 = \Ld.

Now comes the :math:`n` by :math:`n` case.
The :math:`\ld`'s are real when :math:`S=S^T` and :math:`S\x=\ld\x`.

.. note::

    **Real Eigenvalues**: All the eigenvalues of a real symmetric matrix are real.

**Proof**: Suppose that :math:`S\x=\ld\x`.
Until we know otherwise, :math:`\ld` might be a complex number :math:`a+ib` (:math:`a` and :math:`b` real).
*Its complex conjugate* is :math:`\bar{\ld}=a-ib`.
Similarly the components of :math:`\x` may be complex numbers, and switching the 
signs of their imaginary parts gives :math:`\bar{\x}`.

    :math:`\bar{\ld}` times :math:`\bar{\x}` is always the conjugate of :math:`\ld` times :math:`\x`.
    So we can take conjugates of :math:`S\x=\ld\x`, remembering that :math:`S` is real:

    .. math::

        S\x=\ld\x\rm{\ leads\ to\ }S\bar{\x}=\bar{\ld}\bar{\x}.\quad\rm{Transpose\ to}\quad\bar{\x}^TS=\bar{\x}^T\bar{\ld}.

    The left sides are the same so the right sides are equal.
    One equation has :math:`\ld`, the other has :math:`\bar{\ld}`.
    They multiply :math:`\bar{\x}^T\x=|x_1|^2+|x_2|^2+\cds=` length squared which is not zero.
    *Therefore* :math:`\ld` *must equal* :math:`\bar{\ld}`, and :math:`a+ib` equals :math:`a-ib`.
    So :math:`b=0` and :math:`\ld=a=real`. Q.E.D.

The eigenvectors come from solving the real equation :math:`(S-\ld I)\x=\0`.
So the :math:`\x`'s are also real.
The important fact is that they are perpendicular.

.. note::

    **Orthogonal Eigenvectors**: Eigenvectors of a real symmetric matrix (when 
    they correspond to different :math:`\ld`'s) are always perpendicular.

**Proof**: Suppose :math:`S\x=\ld_1\x` and :math:`S\y=\ld_2\y`.
We are assuming here that :math:`\ld_1\neq\ld_2`.
Take dot products of the first equation with :math:`\y` and the second with :math:`\x`:

    **Use** :math:`S^T=S`:

    .. math::

        (\ld_1\x)^T\y=(S\x)^T\y=\x^TS^T\y=\x^TS\y=\x^T\ld_2\y.

    The left side is :math:`\x^T\ld_1\y`, the right side is :math:`\x^T\ld_2\y`.
    Since :math:`\ld_1\neq\ld_2`, this proves that :math:`\x^T\y=0`.
    The eigenvector :math:`\x` (for :math:`\ld_1`) is perpendicualr to the eigenvector :math:`\y` (for :math:`\ld_2`).

The eigenvectors of a 2 by 2 symmetric matrix have a special form:

**Not widely known**:

.. math::

    S=\bb a&b\\b&c \eb\rm{\ has\ }\x1+\bb b\\\ld_1-a \eb\rm{\ and\ }\x_2=\bb \ld_2-c\\b \eb.

:math:`\x_1` is perpendicular to :math:`\x_2`:

.. math::

    \x_1^T\x_2=b(\ld_2-c)+(\ld_1-a)b=b(\ld_1+\ld_2-a-c)=0.

This is zero because :math:`\ld_1+\ld_2` equals the trace :math:`a+c`.
Thus :math:`\x_1^T\x_2=0`.
This also fits for the special case when :math:`S=I`.

**Symmetric matrices** :math:`S` **have orthogonal eigenvector matrices** :math:`Q`:

.. tip::

    **Symmetry**: :math:`S=X\Ld X\im` becomes :math:`S=Q\Ld Q^T` with :math:`Q^TQ=I`.

This says that every 2 by 2 symmetric matrix is (**rotation**)(**stretch**)(**rotate back**)

.. math::

    S=Q\Ld Q^T=\bb \\\ \q_1&\q_2 \\\ \eb\bb \ld_1\\&\ld_2 \eb\bb &\q_1^T&\\&\q_2^T \eb.

**Columns** :math:`\q_1` **and** :math:`\q_2` **multiply rows** 
:math:`\ld_1\q_1^T` **and** :math:`\ld_2\q_2^T` **to produce**
:math:`S=\ld_1\q_1\q_1^T+\ld_2\q_2\q_2^T`.

.. tip::

    **Every symmetric matrix**: :math:`S=Q\Ld Q^T=\ld_1\q_1\q_1^T+\cds+\ld_n\q_n\q_n^T`.

.. note::

    :math:`S` **has correct eigenvectors**; **Those** :math:`q`\ **'s are orthonormal**:

    * :math:`S\q_i=(\ld_1\q_1\q_1^T+\cds+\ld_n\q_n\q_n^T)\q_i=\ld_i\q_i`.

Complex Eigenvalues of Real Matrices
------------------------------------

.. note::

    **For real matrices, complex** :math:`\ld`\ **'s and** :math:`\x`\ **'s come in "conjugate pairs."**

    * :math:`\begin{matrix}\ld=a+ib\\\bar{\ld}=a-ib\end{matrix}\quad` **If**
      :math:`A\x=\ld\x` **then** :math:`A\bar{\x}=\bar{\ld}{\x}`.

:math:`A=\bb \cos\theta&-\sin\theta\\\sin\theta&\cos\theta\eb` has
:math:`\ld_1=\cos\theta+i\sin\theta` and :math:`\ld_2=\cos\theta-i\sin\theta`.

Those eigenvalues are conjugate to each other.
They are :math:`\ld` and :math:`\bar{\ld}`.
The eigenvectors must by :math:`\x` and :math:`\bar{\x}`, because :math:`A` is real:

    * **This is** :math:`\ld\x` :math:`A\x=\bb \cos\theta&-\sin\theta\\
      \sin\theta&\cos\theta\eb\bb 1\\-i \eb=(\cos\theta+i\sin\theta)\bb 1\\-i\eb`.

    * **This is** :math:`\ld\bar{\x}` :math:`A\x=\bb \cos\theta&-\sin\theta\\
      \sin\theta&\cos\theta\eb\bb 1\\i \eb=(\cos\theta-i\sin\theta)\bb 1\\i\eb`.

For this rotation matrix the absolute value is :math:`|\ld|=1`, because :math:`\cos^2\theta+\sin^2\theta=1`.
**This fact** :math:`|\ld|=1` **holds for the eigenvalues of every orthogonal matrix** :math:`Q`.

Eigenvalues versus Pivots
-------------------------

The only connection between eigenvalues and pivots is:

    **product of pivots = determinant = product of eigenvalues**.

We are assuming a full set of pivots :math:`d_1,\cds,d_n`.
There are :math:`n` real eigenvalues :math:`\ld_1,\cds,\ld_n`.
The :math:`d`'s and :math:`\ld`'s are not the same, but they come from the same symmetric matrix.
**For symmetric matrices the pivots and the eigenvalues have the same signs**:

.. tip::

    **The number of positive eigenvalues of** :math:`S=S^T` **equals the number of positive pivots**.

Special case: :math:`S` have all :math:`\ld_i>0` if and only if all pivots are positive.

All Symmetric Matrices are Diagonalizable
-----------------------------------------