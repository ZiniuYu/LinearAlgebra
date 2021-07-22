Chapter 8.3 The Search for a Good Basis
=======================================

The input basis vectors will be the columns of :math:`B_{\rm{in}}`.
The output basis vectors will be the columnso f :math:`B_{\rm{out}}`.

**Pure algebra**: If :math:`A` is the matrix for a transformation :math:`T` in 
the standard basis, then :math:`B\im_{\rm{out}}AB_{\rm{in}}` is the matrix in
the new bases.

The standard basis vectors are the *columns of the identity*: 
:math:`B_{\rm{in}}=I_{n\times n}` and :math:`B_{\rm{out}}=I_{m\times m}`.
Now we are choosing special bases to make the matrix clearer and simpler than :math:`A`.
When :math:`B_{\rm{in}}=B_{\rm{out}}=B`, the square matrix :math:`B\im AB` is *similar* to :math:`A`.

**Applied algebra**: Applications are allabout choosing good bases.

    **1.** :math:`B_{\rm{in}}=B_{\rm{out}}=` **eigenvector matrix** :math:`X`.
       
        Then :math:`X\im AX=` **eigenvalues in** :math:`\Ld`.
        This choice requires :math:`A` to be a square matrix with :math:`n` independent eigenvectors.
        We get :math:`\Ld` when :math:`B_{\rm{in}}=B_{\rm{out}}` is the eigenvector matrix :math:`X`.
    
    **2.** :math:`B_{\rm{in}}=V` and :math:`B_{\rm{out}}=U`: **singular vectors of** :math:`A`.
       
        Then :math:`U\im AV=` **diagonal** :math:`\Sg`.
        :math:`\Sg` is the singular matrix (with :math:`\sg_1,\cds,\sg_r` on its 
        diagonal) when :math:`B_{\rm{in}}` and :math:`B_{\rm{out}}` are the
        singular vector matrices :math:`V` and :math:`U`.
        Recall that those columns of :math:`B_{\rm{in}}` and :math:`B_{\rm{out}}` 
        are orthonormal eigenvectors of :math:`A^TA` and :math:`AA^T`.
        Then :math:`A=U\Sg V^T` gives :math:`\Sg=U\im AV`.
    
    **3.** :math:`B_{\rm{in}}=B_{\rm{out}}=` **generalized eigenvectors of** :math:`A`.
    Then :math:`B\im AB=` **Jordan form** :math:`J`.

        :math:`A` is a square matrix but it may only have :math:`s` independent eigenvectors.
        (If :math:`s=n` then :math:`B` is :math:`X` and :math:`J` is :math:`\Ld`.)
        In all cases Jordan constructed :math:`n-s` additional "generalized" 
        eigenvectors, aiming to make the Jordan form :math:`J` 
        *as diagonal as possible*:

            i) There are :math:`s` square blocks along the diagonal of :math:`J`.

            ii) Each block has one eigenvalue :math:`\ld`, one eigenvector, and 1's above the diagonal.

        The good case has :math:`n` :math:`1\times 1` blocks, each containing an eigenvalue.
        Then :math:`J` is :math:`\Ld` (diagonal).

The Jordan Form
---------------

For every :math:`A`, we want to choose :math:`B` so that :math:`B\im AB` is as **nearly diagonal as possible**.
When :math:`A` has a full set of :math:`n` eigenvectors, they go into the columns of :math:`B`.
Then :math:`B=X`.
The matrix :math:`X\im AX` is diagonal.
This is the Jordan form of :math:`A`--when :math:`A` can be diagonalized.
In the general case, eigenvectors are missing and :math:`\Ld` can't be reached.

Suppose :math:`A` has :math:`s` independent eigenvectors.
Then it is similar to a Jordan matrix with :math:`s` blocks.
Each block has an *eigenvalue on the diagonal with* 1's *just above it*.
This block accounts for exactly one eigenvector of :math:`A`.
Then :math:`B` contains generalized eigenvectors as well as ordinary eigenvectors.

When there are :math:`n` eigenvectors, all :math:`n` blocks will be 1 by 1.
In that case :math:`J=\Ld`.

The Jordan form solves the diefferential equation :math:`d\u/dt=A\u` for **any square matrix** :math:`A=BJB\im`.
The solution :math:`e^{At}\u(0)` becomes :math:`\u(t)=Be^{Jt}B\im\u(0)`.
:math:`J` is triangular and its matrix exponential :math:`e^{Jt}` involves 
:math:`e^{\ld t}` times powers :math:`1,t,\cds,t^{s-1}`.

.. note::

    **Jordan form**: If :math:`A` has :math:`s` independent eigenvectors, it is 
    similar to a matrix :math:`J` that has :math:`s` Jordan blocks 
    :math:`J_1,\cds,J_s` on its diagonal.
    Some matrix :math:`B` puts :math:`A` into Jordan form:

    * **Jordan form**: :math:`B\im AB=\bb J_1\\&\dds\\&&J_s \eb=J`.

    Each block :math:`J_i` has one eigenvalue :math:`\ld_i`, one eigenvector, and :math:`1`'s just above the diagonal:

    * **Jordan block**: :math:`J_i=\bb \ld_1&1\\&\cd &\cd\\&&\cd &1\\&&&\ld_i \eb`.

    **Matrices are similar if they share the same Jordan form** :math:`J`--**not otherwise**.









Bases for Function Space
------------------------









Orthogonal Bases for Function Space
-----------------------------------









Legendre Polynomials and Chebyshev Polynomials
----------------------------------------------