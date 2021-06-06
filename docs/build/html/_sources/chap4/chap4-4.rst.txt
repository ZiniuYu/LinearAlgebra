Chapter 4.4 Orthonormal Bases and Gram-Schmidt
==============================================

The vectors :math:`\q_1,\cds,\q_n` are **orthogonal** when their dot products :math:`\q_i\cd\q_j` are zero.
More exactly :math:`\q_i^T\q_j=0` whenever :math:`i\neq j`.
With one more step--just *divide each vector by its length*--the vectors become **orthogonal unit vectors**.
Their lengths are all 1 (normal).
Then the basis is called **orthonormal**.

.. note::

    **DEFINITION**: The vectors :math:`\q_1,\cds,\q_n` are **orthonormal** if:

    * :math:`q_i^Tq_j=\left\{\begin{matrix}
    0\quad\rm{\ when\ } i \neq j\quad(\rm{orthogonal\ vectors})\\
    1\quad\rm{\ when\ } i = j\quad(\rm{unit\ vectors}: \lv \q_i \rv=1)
    \end{matrix}\right.`

    A matrix with orthonormal columns is assigned the special letter :math:`Q`.

**The matrix** :math:`Q` **is easy to work with because** :math:`Q^TQ=I`.
:math:`Q` is not required to be square.

.. note::

    **A matrix** :math:`Q` **with orthonormal columns satisfies** :math:`Q^TQ=I`:

    * :math:`Q^TQ=\bb -\q_1^T-\\-\q_2^T-\\\vds\\-\q_n^T- \eb\bb |&|&&|\\\q_1&\q_2&\cds&\q_n\\|&|&&| \eb=\bb 1&0&\cds&0\\0&1&\cds&0\\\vds&\vds&\ddots&\vds\\0&0&\cds&1 \eb=I`.

When row :math:`i` of :math:`Q^T` multiplies column :math:`j` of :math:`Q`, the dot product is :math:`\q_i^T\q_j`.
Off the diagonal (:math:`i\neq j`) that dot product is zero by orthogonality.
On the diagonal (:math:`i=j`) the unit vectors give :math:`\q_i^T\q_i=\lv\q_i\rv^2=1`.
Often :math:`Q` is rectangular (math:`m>n`).
Sometimes :math:`m=n`.

.. tip::
    
    **When** :math:`Q` **is square**, :math:`Q^TQ=I` **means that** :math:`Q^T=Q^{-1}`: **transpose** = **inverse**.

If the columns are only orthogonal (not unit vectors), dot products still give a
diagonal matrix (not the identity matrix).
This diagonal matrix is almost as good as :math:`I`.




Projections Using Orthonormal Bases: :math:`Q` Replaces :math:`A`
-----------------------------------------------------------------










The Gram-Schmidt Process
------------------------










The Factorization :math:`A=QR`
------------------------------