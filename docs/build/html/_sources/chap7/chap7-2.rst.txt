Chapter 7.2 Bases and Matrices in the SVD
=========================================

:math:`A` is any :math:`m` by :math:`n` matrix, square or rectangular.
Its rank is :math:`r`.
We will daigonalize this :math:`A`, but not by :math:`X\im AX`.
The eigenvectors in :math:`X` have three big problems: They are usually not
orthogonal, there are not always enough eigenvectors, and :math:`A\x=\ld\x`
requires :math:`A` to be a square matrix.
The **singular vectors** of :math:`A` solve all those problems in a perfect way.

We want from the SVD are **the right bases for the four subspaces**.
The steps to find those basis vectors will be described **in order of importance**.

The price we pay is to have **two sets of singular vectors**, :math:`\u`'s and :math:`\v`'s.
The :math:`\u`'s are in :math:`\R^m` and the :math:`\v`'s are in :math:`\R^n`.
They will be the columns of an :math:`m` by :math:`m` matrix :math:`\bs{U}` and 
an :math:`n` by :math:`n` matrix :math:`\bs{V}`.

**Using vectors**: The :math:`\u`'s and :math:`\v`'s give bases for the four fundamental subspaces:

    .. note::

        * :math:`\u_1,\cds,\u_r` is an orthonormal basis for the **column space**

        * :math:`\u_{r+1},\cds,\u_m` is an orthonormal basis for the **left nullspace** :math:`\N(A^T)`

        * :math:`\v_1,\cds,\v_r` is an orthonormal basis for the **row space**

        * :math:`\v_{r+1},\cds,\v_n` is an orthonormal basis for the **nullspace** :math:`\N(A)`.

    More than just orthogonality, these basis vectors diagonalize the matrix :math:`A`:

    .. note::

        **"**\ :math:`A` **is diagonalized"**: :math:`A\v_1=\sg_1\u_1\quad A\v_2=\sg_2\u_2\quad\cds\quad A\v_r=\sg_r\u_r`.

    Those **singular values** :math:`\sg_1` **to** :math:`\sg_r` will be positive 
    numbers: :math:`\sg_i` *is the length of* :math:`A\v_i`.
    The :math:`\sg`'s go into a diagonal matrix that is otherwise zero.
    That matrix is :math:`\Sg`.

**Using matrices**: Since the :math:`\u`'s are orthonormal, the matrix 
:math:`U_r` with those :math:`r` columns has :math:`U_r^TU_r=I`.
Since the :math:`\v`'s are orthonormal, the matrix :math:`V_r` has :math:`V_r^TV_r=I`.
Then the equations :math:`A\v_i=\sg_i\u_i` tell us column by column that :math:`AV_r=U_r\Sg_r`:

    .. math::

        AV_r=U_r\Sg_r\quad A\bb \\\ \v_1&\cds&v_r \\\ \eb=\bb \\\ \u_1&\cds&\u_r \\\ \eb\bb \sg_1\\&\dds\\&&\sg_r \eb.

    Those :math:`\v`'s and :math:`\u`'s account for the row space and column space of :math:`A`.
    We have :math:`n-r` more :math:`\v`'s and :math:`m-r` more :math:`\u`'s, from 
    the nullspace :math:`\N(A)` and the left nullspace :math:`\N(A^T)`.
    They are automatically orthogonal to the first :math:`\v`'s and :math:`\u`'s 
    (because the whole nullspace are orthogonal).
    We now include all the :math:`\v`'s and :math:`\u`'s in :math:`V` and :math:`U`, so these matrices become *square*.
    **We still have** :math:`AV=U\Sg`.

    .. math::

        AV=U\Sg\quad A\bb \\\ \v_1\ \cds\ \v_r\ \cds\ \v_n \\\ \eb=
        \bb \\\ \u_1\ \cds\ \u_r\ \cds\ \u_m \\\ \eb\bb \sg_1\\&\dds\\&&\sg_r&& \\\ \eb.

    The new :math:`\Sg` is :math:`m` by :math:`n`.
    It is just the :math:`r` by :math:`r` matrix with :math:`m-r` extra zero rows and :math:`n-r` new zero columns.
    The real change is in the shapes of :math:`U` and :math:`V`.
    Those are square matrices and :math:`V\im=V^T`.
    So :math:`AV=U\Sg` becomes :math:`A=U\Sg V^T`.
    This is the **Singular Value Decomposition**.
    I can multiply columns :math:`\u_i\sg_i` from :math:`U\Sg` by rows of :math:`V^T`:

    .. note::

        **SVD**: :math:`A=U\Sg V^T=\u_1\sg_1\v_1^T+\cds+\u_r\sg_r\v_r^T`.

    We will see that each :math:`\sg_i^2` is an eigenvalue of :math:`A^TA` and also :math:`AA^T`.
    When we put the singular values in descending order, 
    :math:`\sg_1\geq\sg_2\geq\cds\sg_r>0`, the splitting gives the :math:`r` 
    rank-one pieces of :math:`A` **in order of importance**.

When is :math:`A=U\Sg V^T` (singular values) the *same* as :math:`X\Ld X\im` (eigenvalues)?

:math:`A` needs orthonormal eigenvalues to allow :math:`X=U=V`.
:math:`A` also needs eigenvalues :math:`\ld\geq 0` if :math:`\Ld=\Sg`.
So :math:`A` must be a **positive semidefinite (or difinite) symmetric matrix**.
Only then will :math:`A=X\Ld X\im` which is also :math:`Q\Ld Q^T` coincide with :math:`A=U\Ld V^T`.

Proof of the SVD
----------------

We need to show how those :math:`\u`'s and :math:`\v`'s can be constructed.
The :math:`\v`'s will be **orthonormal eigenvectors of** :math:`A^TA`.
This must be true because we are aiming for

.. math::

    A^TA=(U\Sg V^T)^T(U\Sg V)^T=V\Sg^TU^TU\Sg V^T=V\Sg^T\Sg V^T.

On the right you see the eigenvector matrix :math:`V` for the symmetric positive (semi) definite matrix :math:`A^TA`.
And (:math:`\Sg^T\Sg`) must be the eigenvalue matrix of (:math:`A^TA`): *Each* :math:`\sg^2` *is* :math:`\ld(A^TA)`.

Now :math:`A\v_i=\sg_i\u_i` tells us the unit vectors :math:`\u_1` to :math:`\u_r`.
This is the key equation.
The essential point--the whole reason that the SVD succeeds--is that those unit 
vectors :math:`\u_1` to :math:`\u_r` are automatically orthogonal to each other
(*because the* :math:`\v`'s *are orthogonal*):

**Key step** :math:`i\neq j`:

.. math::

    \u_i^T\u_j=\left(\frac{A\v_i}{\sg_i}\right)^T\left(\frac{A\v_j}{\sg_j}\right)
    =\frac{\v_i^TA^TA\v_j}{\sg_i\sg_j}=\frac{\sg_j^2}{\sg_i\sg_j}\v_i^T\v_j
    =\bs{\rm{zero}}.

The :math:`\v`'s are eigenvectors of :math:`A^TA` (symmetric).
They are orthogonal and now the :math:`\u`'s are also orthogonal.
*Actually those* :math:`\u`'s *will be eigenvectors of* :math:`AA^T`.

Finally we complete the :math:`\v`'s and :math:`\u`'s to :math:`n` :math:`\v`'s
and :math:`m` :math:`\u`'s with any orthonormal bases for the nullspace
:math:`\N(A)` and :math:`\N(A^T)`.
We have found :math:`V` and :math:`\Sg` and :math:`U` in :math:`A=U\Sg V^T`.

An Example of the SVD
---------------------

For a rank 2 matrix :math:`A=\bb 3&0\\4&5 \eb`:

.. math::

    A^TA=\bb 25&20\\20&25 \eb\quad AA^T=\bb 9&12\\12&41 \eb.

Those have the same trace 50 and the same eigenvalues :math:`\sg_1^2=45` and :math:`\sg_2^2=5`.
The square roots are :math:`\sg_1=\sqrt{45}` and :math:`\sg_2=\sqrt{5}`.
Then :math:`\sg_1\sg_2=15` and this is t he determinant of :math:`A`.

**Right singular vectors**:

.. math::

    \v_1=\frac{1}{\sqrt{2}}\bb 1\\1 \eb\quad\v_2=\frac{1}{\sqrt{2}}\bb -1\\1 \eb.

**Left singular vectors**:

.. math::
    \u_i=\frac{A\v_i}{\sg_i}.

Now compute :math:`A\v_1` and :math:`A\v_2` which will be 
:math:`\sg_1\u_1=\sqrt{45}\u_1` and :math:`\sg_2\u_2=\sqrt{5}\u_2`:

.. math::

    A\v_1=\frac{3}{\sqrt{2}}\bb 1\\3 \eb=\sqrt{45}\frac{1}{\sqrt{10}}\bb 1\\3 \eb=\sg_1\u_1

    A\v_2=\frac{1}{\sqrt{2}}\bb -3\\1 \eb=\sqrt{5}\frac{1}{\sqrt{10}}\bb -3\\1 \eb=\sg_2\u_2

.. note::

    :math:`\dp U=\frac{1}{\sqrt{10}}\bb 1&-3\\3&1 \eb\quad
    \Sg=\bb \sqrt{45}\\&\sqrt{5} \eb\quad V=\frac{1}{\sqrt{2}}\bb 1&-1\\1&1 \eb`.

:math:`U` and :math:`V` contain orthonormal bases for the column space and the 
row space (both spaces are just :math:`\R^2`).
The matrix :math:`A` splits into a combination of two rank-one matrices, columns times rows:

.. math::

    \sg_1\u_1\v_1^T+\sg_2\u_2\v_2^T=\frac{\sqrt{45}}{\sqrt{20}}\bb 1&1\\3&3 \eb+
    \frac{\sqrt{5}}{\sqrt{20}}\bb 3&-3\\-1&1 \eb=\bb 3&0\\4&5 \eb=A.

An Extreme Matrix
-----------------

The matrix :math:`A` is badly lopsided (strictly triangular).
All its eigenvalues are zero with the only eigenvector :math:`(1,0,0,0)`.
The singular values are :math:`\sg=3,2,1` and singular vectors are columns of :math:`I`:

.. math::

    A=\bb 0&1&0&0\\0&0&2&0\\0&0&0&3\\0&0&0&0 \eb.

:math:`A^TA` and :math:`AA^T` are diagonal:

.. math::

    A^TA=\bb 0&0&0&0\\0&1&0&0\\0&0&4&0\\0&0&0&9 \eb \quad AA^T=\bb 1&0&0&0\\0&4&0&0\\0&0&9&0\\0&0&0&0 \eb.

The eigenvectors (:math:`\u`'s for :math:`AA^T` and :math:`\v`'s for :math:`A^TA`) 
go in decreasing order :math:`\sg_1^2>\sg_2^2>\sg_3^2` of the eigenvalues.
Those eigenvalues are :math:`\sg^2=9,4,1`.

.. math::

    U=\bb 0&0&1&0\\0&1&0&0\\1&0&0&0\\0&0&0&1\eb\quad\Sg=\bb 3\\&2\\&&1\\&&&0 \eb
    \quad V=\bb 0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0 \eb.

.. note::

    :math:`A=U\Sg V^T=3\u_1\v_1^T+2\u_2\v_2^T+1\u_3\v_3^T`.

*Note*: Removing the zero row of :math:`A` (now :math:`3\times 4`) just removes 
the last row of :math:`\Sg` and also the last row and column of :math:`U`.
Then :math:`(3\times 4)=U\Sg V^T=(3\times 3)(3\times 4)(4\times 4)`.
The SVD is totally adapted to rectangular matrices.

Sigular Value Stability versus Eigenvalue Instability
-----------------------------------------------------

**The singular values of any matrix are stable**.

Singular Vectors of :math:`A` and Eigenvectors of :math:`S=A^TA`
----------------------------------------------------------------

We have proved the SVD *all at once*.
The singular vectors :math:`\v_i` are the eigenvectors :math:`\q_i` of :math:`S=A^TA`.
The eigenvalues :math:`\ld_i` of :math:`S` are the same as :math:`\sg_i^2` for :math:`A`.
The rank :math:`r` of :math:`S` equals the rank of :math:`A`.
The expansions in eigenvectors and singular vectors are perfectly parallel.

.. note::

    * **Symmetric** :math:`S`: :math:`S=Q\Ld Q^T=\ld_1\q_1\q_1^T+\ld_2\q_2\q_2^T+\cds+\ld_r\q_r\q_r^T`.

    * **Any matrix** :math:`A`: :math:`A=U\Sg V^T=\sg_1\u_1\v_1^T+\sg_2\u_2\v_2^T+\cds+\sg_r\u_r\v_r^T`.

The :math:`\q`'s are orthonormal, the :math:`\u`'s are orthonormal, the :math:`\v`'s are orthonormal.

If :math:`\ld` is a *double* eigenvalue of :math:`S`, we can and must find *two* orthonormal eigenvectors.
We want to understand the eigenvalues :math:`\ld` (of :math:`S`) and the singular
values :math:`\sg` (of :math:`A`) **one at a time instead of all at once**.

Start with the larget eigenvalue :math:`\ld_1` of :math:`S`.
It solves this problem"

    :math:`\dp\ld_1=\rm{maximum\ ratio\ }\frac{\x^TS\x}{\x^T\x}`.
    The winning vector is :math:`\x_1=\q_1` with :math:`S\q_1=\ld_1\q_1`.

    Compare with the largest singular value :math:`\sg_1` of :math:`A`.
    It solves this problem:

    :math:`\dp\sg_1=\rm{maximum\ ratio\ }\frac{\lv A\x \rv}{\lv\x\rv}`.
    The winning vector is :math:`\x=\v_1` with :math:`A\v_1=\sg_1\u_1`.

This "one at a time approach" applies also to :math:`\ld_2` and :math:`\sg_2`.
But not all :math:`\x`'s are allowed:

    :math:`\dp\ld_2=\rm{maximum\ ratio\ }\frac{\x^TS\x}{\x^T\x}` among all :math:`\x`'s with :math:`\q_A^T\x=0`.
    :math:`\x=\q_2` will win.

    :math:`\dp\sg_2=\rm{maximum\ ratio\ }\frac{\lv A\x \rv}{\lv\x\rv}` among all :math:`\x`'s with :math:`\v_1^T\x=0`.
    :math:`\x=\v_2` will win.

When :math:`S=A^TA` we find :math:`\ld_1=\sg_1^2` and :math:`\ld_2=\sg_2^2`.

Start with the ratio :math:`r(\x)=\x^TS\x/\x^T\x`.
This is called the *Rayleigh quotient*.
To maximize :math:`r(\x)`, set its partial derivatives to zero: :math:`\pd r/\pd x_i=0` for :math:`i=1,\cds,n`.
Those derivatives are messy and here is the result: one vector equation for the winning :math:`\x`:

* **The derivatives of** :math:`\dp r(\x)=\frac{\x^TS\x}{\x^T\x}` **are zero when** :math:`S\x=r(\x)\x`.

So the winning :math:`\x` is an eigenvector of :math:`S`.
The maximum ratio :math:`r(\x)` is the largest eigenvalue :math:`\ld_1` of :math:`S`.
Notice the connection to :math:`S=A^TA`:

* Maximizing :math:`\dp\frac{\lv A\x \rv}{\lv\x\rv}` also maximizes 
  :math:`\dp\left(\frac{\lv A\x \rv}{\lv\x\rv}\right)^2=\frac{\x^TA^TA\x}{\x^T\x}
  =\frac{\x^TS\x}{\x^T\x}`.

So the winning :math:`\x=\v_1` is the same as the top eigenvector :math:`\q_1` of :math:`S=A^TA`.



Computing the Eigenvalues of :math:`S` and Singular Values of :math:`A`
-----------------------------------------------------------------------