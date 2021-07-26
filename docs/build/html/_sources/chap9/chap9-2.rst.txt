Chapter 9.2 Hermitian and Unitary Matrices
==========================================

**when you transpose a complex vector** :math:`z` **or matrix** :math:`A`, **take the complex conjugate too**.

**Conjugate transpose**:

.. math::

    \bar{z}^T=\bb \bar{z}_1&\cds&\bar{z}_n \eb=\bb a_1-ib_1&\cds&a_n-ib_n \eb.

**Length squared**: :math:`\bar{\bs{z}}^T\bs{z}=\lv\bs{z}\rv^2`

.. math::

    \bb \bar{z}_1&\cds&\bar{z}_n \eb\bb z_1\\\vds\\z_n \eb=|z_1|^2+\cds+|z_n|^2.

.. note::

    **The length** :math:`\lv\bs{z}\rv^2` **is the square root of** 
    :math:`\bar{\bs{z}}^T\bs{z}=\bs{z}^H\bs{z}=|z_1|^2+\cds+|z_n|^2`.

:math:`\bs{z}^H=\bar{\bs{z}}^T` is the *conjugate transpose* of :math:`\bs{z}`.

:math:`A^H` **is** :math:`A` **Hermitian**:

.. math::

    \rm{If\ }A=\bb 1&i\\0&1+i \eb\rm{\ then\ }A^H=\bb 1&0\\-i&1-i \eb.

Complex Inner Products
----------------------

.. note::

    **DEFINITION**: The inner product of real or complex vectors :math:`\u` and :math:`\v` is :math:`\u^H\v`:

    * :math:`\u^H\v=\bb \bar{u}_1&\cds&\bar{u}_n \eb\bb v_1\\\vds\\v_n \eb=\bar{u}_1v_1+\cds+\bar{u}_nv_n`.

With complex vectors, :math:`\u^H\v` is different from :math:`\v^H\u`.
*The order of the vectors is now important*.
In fact :math:`\v^H\u=\bar{v}_1u_1+\cds+\bar{v}_nu_n` is the complex conjugate of :math:`\u^H\v`.

**A zero inner product still means that the complex vectors are orthogonal**.

**The inner product of** :math:`A\u` **with** :math:`\v` 
**equals the inner product of** :math:`\u` **with** :math:`A^H\v`:

* :math:`A^H` **is also called the "adjoint" of** :math:`A`: :math:`(A\u)^H\v=\u^H(A^H\v)`.

.. note::

    **The conjugate transpose of** :math:`AB` **is** :math:`(AB)^H=B^HA^H`.

Hermitian Matrices :math:`S=S^H`
--------------------------------

**Hermitian matrices**: :math:`S=S^H`.
The condition on the entries is :math:`s_{ij}=\bar{s_{ji}}`.
*Every real symmetric matrix is Hermitian*, because taking its conjugate has no effect.

.. note::

    **If** :math:`S=S^H` **and** :math:`\bs{z}` 
    **is any real or complex column vector, the number** :math:`\bs{z}^HS\bs{z}` 
    **is real**.

Quick proof: :math:`(\bs{z}^HS\bs{z})^H=\bs{z}^HS^H(\bs{z}^H)^H` which is :math:`\bs{z}^HS\bs{z}` again.
So the number :math:`\bs{z}^HS\bs{z}` equals its conjugate and must be real.

.. note::

    **Every eigenvalue of a Hermitian matrix is real**.

**Proof**: Suppose :math:`S\bs{z}=\ld\bs{z}`.
*Multiply both sides by* :math:`\bs{z}^H` *to get* :math:`\bs{z}^HS\bs{z}=\ld\bs{z}^H\bs{z}`.
On the left side, :math:`\bs{z}^HS\bs{z}` is real.
On the right side, :math:`\bs{z}^H\bs{z}` is the length squared, real and positive.
So the ratio :math:`\ld=\bs{z}^HS\bs{z}/\bs{z}^H\bs{z}` is a real number.

.. note::

    **The eigenvectors of a Hermitian matrix are orthogonal** (when they correspond to different eigenvalues).
    If :math:`S\bs{z}=\ld\bs{z}` and :math:`S\y=\beta\y` then :math:`\y^H\bs{z}=0`.

**Proof**: Multiply :math:`S\bs{z}=\ld\bs{z}` on the left by :math:`\y^H`.
Multiply :math:`\y^HS^H=\beta\y^H` on the right by :math:`\bs{z}`:

.. math::

    \y^HS\bs{z}=\ld\y^H\bs{z}\quad\rm{and}\quad\y^HS^H\bs{z}=\beta\y^H\bs{z}.

The left sides are equal so :math:`\ld\y^H\bs{z}=\beta\y^H\bs{z}`.
Then :math:`\y^H\bs{z}` **must be zero**.

When :math:`S` is real and symmetric, :math:`X` is :math:`Q`--an orthogonal matrix.
Now :math:`S` is complex and Hermitian.
Its eigenvectors are complex and orthonormal.
**The eigenvector matrix** :math:`X` **is like** :math:`Q`, **but complex**: :math:`Q^HQ=I`.

Unitary Matrices
----------------

A **unitary matrix** :math:`Q` is a (complex) square matrix that has **orthonormal columns**.

**Unitary matrix that diagonalizes** :math:`S`:

.. math::

    Q=\frac{1}{\sqrt{3}}\bb 1&1-i\\1+i&-i \eb.