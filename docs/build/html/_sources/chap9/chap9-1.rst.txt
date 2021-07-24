Chapter 9.1 Complex Numbers
===========================

.. note::

    **A complex number is a real number plus an imaginary number**.
    Addtion keeps the real and imaginary parts separate.
    Multiplication uses :math:`i^2=-1`:

    * **Add**: :math:`(3+2i)+(3+2i)=6+4i`

    * **Multiply**: :math:`(3+2i)(1-i)=3+2i-3i-2i^2=5-i`.

The **real part** is :math:`a=\Re (a+bi)`.
The **imagenary part** is :math:`b=\Im (a+bi)`.

The Complex Plane
=================

Complex numbers correspond to points in a plane.
Real numbers go along the :math:`x` axis.
Plane imaginary numbers are on the :math:`y` axis.
**The complex number** :math:`3+2i` **is at the point with coordinates** :math:`(3,2)`.
The number zero, which is :math:`0+0i`, is at the origin.

The **conjugate** of :math:`z=a+bi` is :math:`\bar{z}=a-bi`.
The imagenary parts of :math:`z` and :math:`\bar{z}` have opposite signs.
In the complex plane, :math:`\bar{z}` is the image of :math:`z` on the other side of the real axis.

**When we multiply conjugates** :math:`\bar{z}_1` **and** :math:`\bar{z}_2`, **we get the conjugate of** :math:`z_1z_2`.
And when we add :math:`\bar{z}_1` and :math:`\bar{z}_2`, we get the conjugate of :math:`z_1+z_2`.

By taking conjugates of :math:`A\x=\ld\x`, when :math:`A` we have another 
eigenvalue :math:`\bar{\ld}` and its eigenvecctor :math:`\bar{\x}`:

.. tip::

    **Eigenvalues** :math:`\ld` **and** :math:`\bar{\ld}`: 
    **If** :math:`A\x=\ld\x` **and** :math:`A` **is real then** 
    :math:`A\bar{\x}=\bar{\ld}\bar{\x}`.

:math:`z+\bar{z}=` **real**:

The sum of :math:`z=a+bi` and its conjugate :math:`\bar{z}=a-bi` is the real number :math:`2a`.
The product of :math:`z` times :math:`\bar{z}` is the real number :math:`a^2+b^2`:

.. note::

    **Multiply** :math:`z` **times** :math:`\bar{z}` **to get** 
    :math:`|z|^2=r^2`: :math:`(a+bi)(a-bi)=a^2+b^2`

.. math::

    \frac{1}{z}=\frac{1}{a+ib}=\frac{1}{a+ib}\frac{a-ib}{a-ib}=\frac{a-ib}{a^2+b^2}

In case :math:`a^2+b^2=1`, this says that :math:`(a+ib)\im` is :math:`a-ib`.
**On the unit circle**, :math:`1/z` **equals** :math:`\bar{z}`.

The Polar Form :math:`re^{i\theta}`
===================================









Powers and Products: Polar Form
===============================