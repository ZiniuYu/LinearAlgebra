Chapter 4.4 Orthonormal Bases and Gram-Schmidt
==============================================

The vectors :math:`\q_1,\cds,\q_n` are **orthogonal** when their dot products :math:`\q_i\cd\q_j` are zero.
More exactly :math:`\q_i^T\q_j=0` whenever :math:`i\neq j`.
With one more step--just *divide each vector by its length*--the vectors become **orthogonal unit vectors**.
Their lengths are all 1 (normal).
Then the basis is called **orthonormal**.

.. note::

    **DEFINITION**: The vectors :math:`\q_1,\cds,\q_n` are **orthonormal** if:

    * :math:`\q_i^T\q_j=\left\{\begin{matrix}0\quad\rm{\ when\ } i \neq j\quad(\rm{orthogonal\ vectors})\ \ \ \quad\\1\quad\rm{\ when\ } i = j\quad(\rm{unit\ vectors}: \lv \q_i \rv=1)\end{matrix}\right.`.

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
    
    **When** :math:`Q` **is square**, :math:`Q^TQ=I` **means that** :math:`Q^T=Q\im`: **transpose** = **inverse**.

If the columns are only orthogonal (not unit vectors), dot products still give a
diagonal matrix (not the identity matrix).
This diagonal matrix is almost as good as :math:`I`.

*To repeat*: :math:`Q^TQ=I` even when :math:`Q` is rectangular.
In that case :math:`Q^T` is only an inverse from the left.
For square matrices we also have :math:`QQ^T=I`, so :math:`Q^T` is the two-sided inverse of :math:`Q`.
The rows of a square :math:`Q` are orthonormal like the columns.
**The inverse is the transpose**.
In this square case we call :math:`Q` an **orthogonal matrix**.

**Rotation**: :math:`Q` rotates every vector in the plane by the angle :math:`\theta`:

    .. math::

        Q=\bb \cos\theta&-\sin\theta\\\sin\theta&\cos\theta \eb\quad\rm{and}\quad
        Q^T=Q\im =\bb \cos\theta&\sin\theta\\-\sin\theta&\cos\theta\eb.

    Those columns give an **orthonormal basis** for the plane :math:`\R^2`.

**Permutation**: These matrices change the order to :math:`(y,z,x)` and :math:`(y,x)`:

    .. math::

        \bb 0&1&0\\0&0&1\\1&0&0 \eb\bb x\\y\\z \eb=\bb y\\z\\x \eb\quad\rm{and}\quad
        \bb 0&1\\1&0 \eb\bb x\\y \eb=\bb y\\x \eb.

    *The inverse of a permutation matrix is its transpose*: :math:`Q\im=Q^T`:

    .. math::
        
        \bb 0&0&1\\1&0&0\\0&1&0 \eb\bb y\\\\x \eb=\bb x\\y\\z \eb\quad\rm{and}\quad    
        \bb 0&1\\1&0 \eb\bb y\\x \eb=\bb x\\y \eb.

**Every permutation matrix is an orthogonal matrix**.

**Reflection**: If :math:`\u` is any unit vector, set :math:`Q=I-2\u\u^T`.
Notice that :math:`\u\u^T` is a matrix while :math:`\u^T\u` is the number :math:`\lv\u\rv^2=1`.
Then :math:`Q^T` and :math:`Q\im` both equal :math:`Q`:

    .. math::

        Q^T=I-2\u\u^T=Q \quad\rm{and}\quad Q^TQ=I-4\u\u^T+4\u\u^T\u\u^T=I.

    Reflection matrices :math:`I-2\u\u^T` are symmetric and also orthogonal.
    Notice :math:`\u^T\u=1` inside :math:`4\u\u^T\u\u^T`.

Rotations preserve the length of every vector.
So do reflections.
So do permutations.
So does multiplication by any orthogonal matrix :math:`Q`--**lengths and angles don't change**.

**Proof**: :math:`\lv Q\x\rv^2` equals :math:`\lv\x\rv^2` because :math:`(Q\x)^T(Q\x)=\x^TQ^TQ\x=\x^TI\x=\x^T\x`.

.. note::

    **If** :math:`Q` **has orthonormal columns** :math:`(Q^TQ=I)`, **it leaves lengths unchanged**:

    * **Same length for** :math:`Q\x`: :math:`\lv Q\x\rv=\lv\x\rv` **for every vector** :math:`\x`.

    :math:`Q` also preserves dot products: :math:`(Q\x)^T(Q\y)=\x^TQ^TQ\y=\x^T\y`.
    Just use :math:`Q^TQ=I`.

Projections Using Orthonormal Bases: :math:`Q` Replaces :math:`A`
-----------------------------------------------------------------

**Suppose the basis vectors are actually orthonormal**.
The :math:`\a`'s become the :math:`\q`'s.
Then :math:`A^TA` *simplifies to* :math:`Q^TQ=I`.

.. tip::

    **The least squares solution of** :math:`Q\x=\b` **is** :math:`\wh{\x}=Q^T\b`.
    **The projection matrix is** :math:`QQ^T`.

There are no matrices to invert.
The "coupling matrix" or "correlation matirx" :math:`A^TA` is now :math:`Q^TQ=I`.
There is no coupling.
When :math:`A` is :math:`Q`, with orthonormal columns, here is :math:`\p=Q\wh{\x}=QQ^T\b`:

.. note::

    **Projection onto** :math:`\q`\ **'s**: 
    :math:`\p=\bb |&&|\\\q_1&\cds&\q_n\\|&&| \eb\bb \q_1^T\b\\\vds\\\q_n^T\b \eb
    =\q_1(\q_1^T\b)+\cds+\q_n(\q_n^T\b)`.

**Important case**: When :math:`Q` is square and :math:`m=n`, the subspace is the whole space.
Then :math:`Q^T=Q\im` and :math:`\wh{\x}=Q^T\b` is the same as :math:`\x=Q\im\b`.
The solution is exact.
The projection of :math:`\b` onto the whole space is :math:`\b` itself.
In this case :math:`\p=\b` and :math:`P=QQ^T=I`.

When :math:`\p=\b`, our formula assembles :math:`\b` out of its 1-dimensional projections.
If :math:`\q_1,\cds,\q_n` is an orthonormal basis for the whole space, then :math:`Q` is square.
Every :math:`\b=QQ^T\b` *is the sum of its components along the* :math:`\q`'s:

.. note::

    :math:`\b=\q_1(\q_1^T\b)+\q_2(\q_2^T\b)+\cds+\q_n(\q_n^T\b)`.

**Transforms**: :math:`QQ^T=I` is the foundation of Fourier series and all the 
great "transforms" of applied mathematics.
They break vectors :math:`\b` or functions :math:`f(x)` into perpendicular pieces.
By adding the pieces, the inverse transform puts :math:`\b` and :math:`f(x)` back together.

The Gram-Schmidt Process
------------------------

Start with three independent vectors :math:`\a,\b,\C`.
We intend to construct three orthogonal vectors :math:`\A,\B,\C`.
Then (at the end may be easiest) we divide :math:`\A,\B,\C` by their lengths.
That produces three orthonormal vectors :math:`\q_1=\A/\lv\A\rv,\q_2=\B/\lv\B\rv,\q_3=\C/\lv\C\rv`.

**Gram-Schmidt**: Begin by choosing :math:`\A=\a`.
This first direction is accepted as it comes.
The next direction :math:`\B` must be perpendicular to :math:`\A`.
**Start with** :math:`\b` **and subtract its projection along** :math:`\A`.
This leaves the perpendicular part, which is the orthogonal vector :math:`\B`:

.. note::

    **First Gram-Schmidt step**: :math:`\dp \B=\b-\frac{\A^T\b}{\A^T\A}\A`.

Multiply the equation by :math:`\A^T` to verify that :math:`\A^T\B=\A^T\b-\A^T\b=0`.
This vector :math:`\B` is what we have called the error vector :math:`\e`, perpendicular to :math:`\A`.
Notice that :math:`\B` is not zero (otherwise :math:`\a` and :math:`\b` would be dependent).
The directions :math:`\A` and :math:`\B` are now set.

The third direction starts with :math:`\C`.
This is not a combination of :math:`\A` and :math:`\B` (because :math:`\C` is 
not a combination of :math:`\a` and :math:`b`).
But most likely :math:`\C` is not perpendicular to :math:`\A` and :math:`\B`.
So subtract off its components in those two directions to get a perpendicular direction :math:`\C`:

.. note::

    **Next Gram-Schmidt step**: :math:`\dp \C=\C-\frac{\A^T\C}{\A^T\A}\A-\frac{\B^T\C}{\B^T\B}\B`.

This is the one and only idea of the Gram-Schmidt process.
**Subtract from every new vector its projections in the directions already set**.
That idea is repeated at every step.
If we had a fourth vector :math:`\bs{d}`, we would subtract three projections 
onto :math:`\A,\B,\C` to get :math:`\bs{D}`.

At the end, or *immediately when each one is found*, divide the orthogonal 
vectors :math:`\A,\B,\C,\bs{D}` by their lengths.
The resulting vectors :math:`\q_1,\q_2,\q_3,\q_4` are orthonormal.

The Factorization :math:`A=QR`
------------------------------

We started with a matrix :math:`A`, whose columns were :math:`\a,\b,\C`.
We ended with a matrix :math:`Q`, whose columns are :math:`\q_1,\q_2,\q_3`.
Since the vectors :math:`\a,\b,\C` are combinations of the :math:`\q`'s (and 
vice versa), there must be a third matrix connecting :math:`A` to :math:`Q`.
This third matrix is the triangular :math:`R` in :math:`A=QR`.

* The vectors :math:`\a` and :math:`\A` and :math:`\q_1` are all along a single line.

* The vectors :math:`\a,\b` and :math:`\A,\B` amd :math:`\q_1,\q_2` are all in the smae plane.

* The vectors :math:`\a,\b,\C` and :math:`\A,\B,\C` and :math:`\q_1,\q_2,\q_3` are in one subspace.

At every step :math:`\a_1,\cds,\a_k` are combinations of :math:`\q_1,\cds,\q_k`.
Later :math:`\q`'s are not involved.
The connecting matrix :math:`R` is **triangular**, and we have :math:`A=QR`:

.. note::

    :math:`\bb \\\a&\b&\C\\\ \eb=\bb \\\q_1&\q_2&\q_3\\\ \eb
    \bb\q_1^T\a&\q_1^T\b&\q_1^T\C\\&\q_2^T\b&\q_2^T\C\\&&\q_3^T\C\eb`
    or :math:`A=QR`.

:math:`A=QR` is Gram-Schmidt in a nutshell.
Multiply by :math:`Q^T` to recognize :math:`R=Q^TA` above.

.. note::

    **Gram-Schmidt**: From independent vectors :math:`\a_1,\cds,\a_n`, 
    Gram-Schmidt constructs orthonormal vectors :math:`\q_1,\cds,\q_n`.
    The matrices with these columns satisfy :math:`A=QR`.
    Then :math:`R=Q^TA` is **upper triangular** because later :math:`\q`'s are orthogonal to earlier :math:`\a`'s.

Any :math:`m` by :math:`n` matrix :math:`A` with independent columns can be factored into :math:`A=QR`.
The :math:`m` by :math:`n` matrix :math:`Q` has orthonormal columns, and the 
square matrix :math:`R` is upper triangular with positive diagonal.
We must not forget why this is usefull for least squares: :math:`\bs{A^TA=(QR)^TQR=R^TQ^TQR=R^TR}`.
The least squares equation :math:`A^TA\wh{\x}=A^T\b` simplifies to :math:`R^TR\wh{\x}=R^TQ^T\b`.
Then finally we reach :math:`R\wh{\x}=Q^T\b`.

.. note::

    **Least squares**: :math:`R^TR\wh{\x}=R^TQ^T\b` or :math:`R\wh{\x}=Q^T\b` or :math:`\wh{\x}R\im Q^T\b`.

Instead of solving :math:`A\x=\b`, which is impossible, we solve 
:math:`R\wh{\x}=Q^T\b` by back substitution--which is very fast.
The real cost is the :math:`mn^2` multiplications in the Gram-Schmidt process, 
which are needed to construct the orthogonal :math:`Q` and the triangular 
:math:`R` with :math:`A=QR`.

Below is an informal code.
The last line of that code normalizes :math:`\v` (divides by 
:math:`r_{jj}=\lv\lv\rv`) to get the unit vector :math:`\q_j`:

.. math::

    r_{kj}=\sum_{i=1}^{m}q_{ik}v_{ij}\rm{\ and\ }v_{ij}=v_{ij}-q_{ik}r_{kj}
    \rm{\ and\ }r_{jj}=\left(\sum_{i=1}^{m}v_{ij}^2\right)^{1/2}\rm{\ and\ }
    q_{ij}=\frac{v_{ij}}{r_{jj}}.

Starting from :math:`\a,\b,\C=\a_1,\a_2,\a_3` this code will construct 
:math:`\q_1`, then :math:`\B,\q_2`, then :math:`\C,\q_3`:

.. math::

    \q_1=\a_1/\lv\a_1\rv\quad\B=\a_2-(\q_1^T\a_2)\q_1\quad\q_2=\B/\lv\B\rv

    \C^*=\a_3-(\q_1^T\a_3)\q_1\quad\C=\C^*-(\q_2^T\C^*)\q_2\quad\q_3=\C/\lv\C\rv

.. code-block:: MATLAB

    for j = 1:n
        V = A(:,j);
        for i = 1:j-1
            R(i,j) = Q(:,i)' * v;
            v = v - R(i,j) * Q(:, i);
        end
        R(j,j) = norm(v);
        Q(:,j) = v/R(j,j);
    end

To recover column :math:`j` of :math:`A`, undo the last step and the middle steps of the code:

.. math::

    R(j,i)\q_j=(\v\rm{\ minus\ its\ projections})=(\rm{column\ }j\rm{\ of\ }A)-\sum_{i=1}^{j-1}R(i,j)\q_i.