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

**Question**: Find the eigenvalues and all possible Jordan forms if :math:`A^2=` zero matrix.

**Answer**: The eigenvalues must all be zero, because :math:`A\x=\ld\x` leads to :math:`A^2\x=\ld^2\x=0\x`.
The Jordan form of :math:`A` has :math:`J^2=0` because :math:`J^2=(B\im AB)(B\im AB)=B\im A^2B=0`.
Every block in :math:`J` has :math:`\ld=0` on the diagonal.
Look at :math:`J^2_k` for block sizes :math:`1,2,3`:

.. math::

    \bb 0 \eb^2=\bb 0 \eb\quad\bb 0&1\\0&0 \eb^2=\bb 0&0\\0&0 \eb\quad
    \bb 0&1&0\\0&0&1\\0&0&0 \eb^2=\bb 0&0&1\\0&0&0\\0&0&0 \eb.

Conclusion: If :math:`J^2=0` then all block sizes must be 1 or 2.
:math:`J^2` is not zero for 3 by 3.

The rank of :math:`J` (and :math:`A`) will be the total number of 1's.
**The maximum rank is** :math:`n/2`.
This happens when there are :math:`n/2` blocks, each of size 2 and rank 1.

**4.** :math:`B_{\rm{in}}=B_{\rm{out}}=` **Fourier matrix** :math:`F`.
**Then** :math:`F\x` **is a Discrete Fourier Transform of** :math:`\x`.

    We are starting with the eigenvectors :math:`(1,\ld,\ld^2,\ld^3)` and 
    finding the matrices that have those eigenvectors:

    .. math::

        \rm{If\ }\ld^4=1\rm{\ then}\quad 
        P\x=\bb 0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\eb
        \bb 1\\\ld\\\ld^2\\\ld^3 \eb=\ld\bb 1\\\ld\\\ld^2\\\ld^3 \eb=\ld\x.

    **The eigenvector matrix** :math:`F` **diagonalizes the permutation matrix** :math:`P`:

    * **Eigenvalue matrix** :math:`\Ld`:

    .. math::

        \bb 1\\&i\\&&-1\\&&&-i \eb

    * **Eigenvector matrix is Fourier matrix** :math:`F`:

    .. math::

        \bb 1&1&1&1\\1&i&-1&-i\\1&i^2&1&(-i)^2\\1&i^3&-1&(-i)^3 \eb.

.. math::

    P^2\x=\bb 0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\eb
    \bb 1\\\ld\\\ld^2\\\ld^3 \eb=\ld^2\bb 1\\\ld\\\ld^2\\\ld^3 \eb=\ld^2\x
    \rm{\ when\ }\ld^4=1.

The fourth power is special because :math:`P^4=I`.
If :math:`P` and :math:`P^2` and :math:`P^3` and :math:`P^4=I` have the same 
eigenvector matrix :math:`F`, so does any combination 
:math:`C=c_1P+c_2P^2+c_3P^3+c_0I`:

* **Circulant matrix**:

.. math::
    
    C=\bb c_0&\bs{c_1}&c_2&c_3\\c_3&c_0&\bs{c_1}&c_2\\c_2&c_3&c_0&\bs{c_1}\\\bs{c_1}&c_2&c_3&c_0 \eb

* **The four eigenvalues of** :math:`C` **are given by the Fourier transform** :math:`F\bs{c}`:

.. math::

    F\bs{c}=\bb 1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i \eb
    \bb c_0\\c_1\\c_2\\c_3 \eb=\bb c_0+c_1+c_2+c_3\\c_0+ic_1-c_2-ic_3\\
    c_0-c_1+c_2-c_3\\c_0-ic_1-c_2+ic_3 \eb.

Notice that **circulant matrices have constant diagonals**.
Constancy down the diagonals is a crucial property of :math:`C`.
It corresponds to *constant coefficients* in a differential equation.

    The equation :math:`\dp\frac{d^2u}{dt^2}=-u` is solved by :math:`u=c_0\cos t+c_1\sin t`.

    The equation :math:`\dp\frac{d^2u}{dt^2}=tu` cannot be solved by elementary functions.
    
Bases for Function Space
------------------------

If we had vectors instead of functions, the test for a good basis would look at :math:`B^TB`.
This matrix contains all inner products between the basis vectors (columns of :math:`B`).
*The basis is orthonormal when* :math:`B^TB=I`.
That is best possible.
But the basis :math:`1,x,x^2,\cds` produces the evil **Hilbert matrix**: 
:math:`B^TB` has an enormous ratio between its largest and smallest eigenvalues.

*Note*: Now the columns of :math:`B` are functions instead of vectors.
We still use :math:`B^TB` to test for independence.
So we need to know the dot product (inner product is a better name) of two 
functions--those are the numbers in :math:`B^TB`.
The inner product of functions will integrate instead of adding:

    Inner product :math:`(\bs{f},\bs{g})=\int f(x)g(x)dx`

    Comlex inner product :math:`(\bs{f},\bs{g})=\int\bar{f(x)}g(x)dx`, :math:`\bar{f}=` complex conjugate

    Weighted inner product :math:`(\bs{f},\bs{g})_w=\int w(x)\bar{f(x)}g(x)dx`, :math:`w=` weight functions

When the integrals go from :math:`x=0` to :math:`x=1`, the inner product of :math:`x^i` with :math:`x^j` is

.. math::

    \int^1_0 x^ix^jdx=\frac{x^{i+j+1}}{i+j+1}\bigg]^{x=1}_{x=0}=\frac{1}{i+j+1}=
    \rm{\ entries\ of\ Hilbert\ matrix\ }B^TB

By changing to the symmetric interval from :math:`x=-1` to :math:`x=1`, we 
immediately have *orthogonality between all even functions and all odd functions*:

**Interval [-1, 1]**:

.. math::

    \int^1_{-1}x^2x^5dx=0\quad\int^1_{-1}\bs{\rm{even}}(x)\bs{\rm{odd}}(x)dx=0.

Orthogonal Bases for Function Space
-----------------------------------

Here are the three leading even-odd bases for theoretical and numerical computations:

.. note::

    **5.** The **Fourier basis**: :math:`1,\sin x,\cos x,\sin 2x,\cos 2x,\cds`

    **6.** The **Legendre basis**: :math:`1,x,x^2-\frac{1}{3},x^3-\frac{3}{5}x,\cds`

    **7.** The **Chebyshev basis**: :math:`1,x,2x^2-1,4x^3-3x,\cds`

The Fourier basis functions (sines and cosines) are all *periodic*.
They repeat over every :math:`2\pi` inteval because :math:`\cos(x+2\pi)=\cos x` and :math:`\sin(x+2\pi)=\sin x`.
This basis is also *orthogonal*.
Every sine and cosine is orthogonal to every other sine and cosine.
The sine-cosine basis is also *excellent for approximation*.

The *Fourier transform* onnects :math:`f(x)` to the coefficient :math:`a_k` and :math:`b_k` in its Fourier series:

.. note::

    **Fourier series**: :math:`f(x)=a_0+b_1\sin x+a_1\cos x+b_2\sin 2x+a_2\cos 2x+\cds`

We see that **function space is infinite-dimensional**.
It takes infinitely many basis functions to capture perfectly a typical :math:`f(x)`.
But the formula for each coefficient (for example :math:`a_3`) is just like the 
formula :math:`\b^T\a/\a^T\a` for projecting a vector :math:`\b` onto the line 
through :math:`\a`.

Here we are projecting the function :math:`f(x)` onto the line in function space through :math:`\cos 3x`:

**Fourier coefficient**:

.. math::

    a_3=\frac{(f(x),\cos 3x)}{(\cos 3x,\cos 3x)}=\frac{\int f(x)\cos 3xdx}{\int \cos 3x\cos 3xdx}.

**Fourier series is just linear algebra in function space**.

Legendre Polynomials and Chebyshev Polynomials
----------------------------------------------