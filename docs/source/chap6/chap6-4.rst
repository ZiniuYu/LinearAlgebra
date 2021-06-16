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






Complex Eigenvalues of Real Matrices
------------------------------------










Eigenvalues versus Pivots
-------------------------










All Symmetric Matrices are Diagonalizable
-----------------------------------------