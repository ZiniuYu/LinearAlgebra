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


One Step of the Fast Fourier Transform
--------------------------------------











The Full FFT by Recursion
-------------------------