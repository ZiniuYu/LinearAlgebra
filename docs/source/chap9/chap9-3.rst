Chapter 9.3 The Fast Fourier Transform
======================================

**We want to multiply quickly by** :math:`F` **and** :math:`F\im`, **the Fourier matrix and its inverse**.
This is achieved by the Fast Fourier Transform.
An ordinary product :math:`F\bs{c}` uses :math:`n^2` multiplications (:math:`F` has :math:`n^2` entries).
The FFT needs only :math:`n` times :math:`\frac{1}{2}\log_2n`.

Roots of Unity and the Fourier Matrix
-------------------------------------

The solutions :math:`z` of :math:`z^1` are the :math:`n`\ th roots of unity.
They are :math:`n` evenly spaced points around the unit circle in the complex plane.

**Fourier matrix** :math:`n=4`, :math:`w=i`:

.. math::

    F=\bb 1&1&1&1\\1&w&w^2&w^3\\1&w^2&w^4&w^6\\1&w^3&w^6&w^9 \eb=
    \bb 1&1&1&1\\1&i&i^2&i^3\\1&i^2&i^4&i^6\\1&i^3&i^6&i^9 \eb.

The matrix is symmetric (:math:`F=F^T`).
It is *not* Hermitian.
Its main diagonal is not real.
But :math:`\frac{1}{2}F` is a **unitary matrix**, which means that :math:`(\frac{1}{2}F^H)(\frac{1}{2}F)=I`:

.. note::

    **The columns of** :math:`F` **give** :math:`F^HF=4I`.
    **Its inverse is** :math:`\frac{1}{4}F^H` **which is** :math:`F\im=\frac{1}{4}\bar{F}`.

Every column has length :math:`\sqrt{n}`. So the unitary matrices are 
:math:`Q=F/\sqrt{n}` and :math:`Q\im=\bar{F}/\sqrt{n}`.
We avoid :math:`\sqrt{n}` and just use :math:`F` and :math:`F\im=\bar{F}/n`.
The main point is to multiply :math:`F` times :math:`c_0,c_1,c_2,c_3`:

**4-point Fourier series**:

.. math::

    \bb y_0\\y_1\\y_2\\y_3 \eb=F\bs{c}=\bb 1&1&1&1\\1&w&w^2&w^3\\1&w^2&w^4&w^6\\
    1&w^3&w^6&w^9 \eb\bb c_0\\c_1\\c_2\\c_3 \eb.

The first output :math:`y_0=c_0+c_1+c_2+c_3` is the value of the Fourier series :math:`\sum c_ke^{ikx}` at :math:`x=0`.
*The second output is the alue of that series* :math:`\sum c_ke^{ikx}` at :math:`x=2\pi/4`:

.. math::

    y_1=c_0+c_1e^{i2\pi/4}+c_2e^{i4\pi/4}+c_3e^{i6\pi/4}=c_0+c_1w+c_2w^2+c_3w^3.

The third and fourth outputs :math:`y_2` and :math:`y_3` are the values of 
:math:`\sum c_ke^{ikx}` at :math:`x=4\pi/4` and :math:`x=6\pi/4`.
These are *finite* Fourier series!
*They contain* :math:`n=4` *terms and they are evaluated at* :math:`n=4` *points*.
Those points :math:`x=0,2\pi/4,4\pi/4,6\pi/4` are equally spaced.

We follow the convention that :math:`j` **and** :math:`k` **go from** :math:`0` 
**to** :math:`n-1` (instead of :math:`1` to :math:`n`).

The :math:`n` by :math:`n` Fourier matrix contains powers of :math:`w=e^{2\pi i/n}`:

.. math::

    F_n\bs{c}=\bb 1&1&1&\cd&1\\1&w&w^2&\cd&w^{n-1}\\1&w^2&w^4&\cd&w^{2(n-1)}\\
    \cd&\cd&\cd&\cd&\cd\\1&w^{n-1}&w^{2(n-1)}&\cd&w^{(n-1)^2} \eb
    \bb c_0\\c_1\\c_2\\\cd\\c_{n-1} \eb=\bb y_0\\y_1\\y_2\\\cd\\y_{n-1} \eb=\y.

:math:`F_n` is symmetric but not Hermitian.
**Its columns are orthogonal**, and :math:`F_n\bar{F}_n=nI`.
*Then* :math:`F\im_n` *is* :math:`\bar{F}_n/n`.
The inverse contains powers of :math:`\bar{w}_n=e^{-2\pi i/n}`.

.. note::

    **The entry in** row :math:`j`, column :math:`k` **is** :math:`w^{jk}`.
    **Row zero and column zero contain** :math:`w^0=1`.

When a function :math:`f(x)` has period :math:`2\pi`, and we change :math:`x` to 
:math:`e^{i\th}`, the function is defined around the unit circle (where 
:math:`z=\e^{i\th}`).
The Discrete Fourier Transform is the same as interpolation.
Find the polynomial :math:`p(z)=c_0+c_1z+\cds+c_{n-1}z^{n-1}` that matches :math:`n` values :math:`f_0,\cds,f_{n-1}`:

.. note::

    **Interpolation**: Find :math:`c_0,\cds,c_{n-1}` so that :math:`p(z)=f` at :math:`n` points :math:`z=1,\cds,w^{n-1}`.

The Fourier matrix is the Vandermonde matrix for interpolation at those :math:`n` special points.

One Step of the Fast Fourier Transform
--------------------------------------

**The key idea of FFT is to connect** :math:`F_n` **with the half-size Fourier matrix** :math:`F_{n/2}`.
Assume that :math:`n` is a power of 2.
We will connect :math:`F_4` to **two copies of** :math:`F_2`:

.. math::

    F_4=\bb 1&1&1&1\\1&i&i^2&i^3\\1&i^2&i^4&i^6\\1&i^3&i^6&i^9 \eb\quad\rm{and}
    \quad\bb \\\ &F_2\\&&F_2& \\\ \eb=\bb 1&1\\1&i^2\\&&1&1\\&&1&i^2 \eb

**Factors for FFT**:

.. math::

    F_4=\bb 1&&1\\&1&&i\\1&&-1\\&1&&-i \eb\bb 1&1\\1&i^2\\&&1&1\\&&1&i^2 \eb\bb 1\\&&1\\&1\\&&&1 \eb.

.. note::

    :math:`F_{1024}=\bb I_{512}&D_{512}\\I_{512}&-D_{512}\eb\bb F_{512}\\&F_{512}\eb\bb\rm{even-odd}\\\rm{permutation}\eb`.

:math:`I_{512}` is the identity matrix.
:math:`D_{512}` is the diagonal matrix with entries :math:`(1,w,\cds,w^{511})`.
The two copies of :math:`F_{512}` use the 512th root of unity (which is nothing but :math:`w^2`).
The permutation matrix separates the incoming vector :math:`\bs{c}` into its 
even and odd parts :math:`\bs{c}\pr=(c_0,c_2,\cds,c_{1022})` and
:math:`\bs{c}\ppr=(c_1,c_3,\cds,c_{1023})`.

.. note::

    **One step of the FFT**: **Set** :math:`m=\frac{1}{2}n`.
    The first :math:`m` and last :math:`n` components of :math:`\y=F_n\bs{c}` 
    combine the half-size transform :math:`\y\pr=F_m\bs{c}\pr` and 
    :math:`\y\ppr=F_m\bs{c}\ppr`.

    * :math:`y_j=y_j\pr+(w_n)^jy_j\ppr,j=0,\cds,m-1`

    * :math:`y_{j+m}=y_j\pr-(w_n)^jy_j\ppr,j=0,\cds,m-1`.

    Split :math:`\bs{c}` into :math:`\bs{c}\pr` and :math:`\bs{c}\ppr`, 
    transform them by :math:`F_m` into :math:`\y\pr` and :math:`\y\ppr`, 
    then reconstructs :math:`\y`.

Those formulas come from separating :math:`c_0,\cds,c_{n-1}` into even 
:math:`c_{2k}` and odd :math:`c_{2k+1}`: :math:`w` is :math:`w_n`.

.. math::

    \y=\bs{Fc}\quad y_j=\sum_0^{n-1}w^{jk}c_k=\sum_0^{m-1}w^{2jk}c_{2k}+
    \sum_0^{m-1}w^{j(2k+1)}c_{2k+1}\rm{\ with\ }m=\frac{1}{2}n.

The even :math:`c`'s go into :math:`\bs{c}\pr=(c_0,c_2,\cds)` and the odd 
:math:`c`'s go into :math:`\bs{c}\ppr=(c_1,c_3,\cds,)`.
Then come the transforms :math:`F_mc\pr` and :math:`F_mc\ppr`.
**The key is** :math:`w_n^2=w_m`.
This gives :math:`w_n^{2jk}=w_m^{jk}`.

.. math::

    y_j=\sum(w_m)^{jk}c_k\pr+(w_n)^j\sum(w_m)^{jk}c_k\ppr=y_j\pr+(w_n)^jy_j\ppr.

For :math:`j\geq m`, the minus sign comes from factoring out :math:`(w_n)^m=-1` from :math:`(w_n)^j`.

The Full FFT by Recursion
-------------------------

**The final count for size** :math:`n=2^l` **is reduced from** :math:`n^2` **to** :math:`\frac{1}{2}nl`.