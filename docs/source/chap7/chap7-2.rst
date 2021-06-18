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









An Extreme Matrix
-----------------









Sigular Value Stability versus Eigenvalue Instability
-----------------------------------------------------









Computing the Eigenvalues of :math:`S` and Singular Values of :math:`A`
-----------------------------------------------------------------------