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
-----------------

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
-----------------------------------

The square root of :math:`a^2+b^2` is :math:`|z|`.
This is the **absolute value** (or **modulus**) of the number :math:`z=a+ib`.
The square root :math:`|z|` is also written :math:`r`, because it is the distance from :math:`0` to :math:`z`.
**The real number** :math:`r` **in the polar form gives the size of the complex number** :math:`z`:

    The absolute value of :math:`z=a+ib` is :math:`|z|=\sqrt{a^2+b^2}`.
    **This is called** :math:`r`.

**The angle doubles when the number is squared**.

.. note::

    **The number** :math:`z=a+ib` **is also** :math:`z=r\cos\th+ir\sin\th`.
    **Tis is** :math:`re^{i\th}`.

*Note*: :math:`\cos\th+i\sin\th` **has absolute value** :math:`r=1` **because** :math:`\cos^2\th+\sin^2\th=1`.
Thus :math:`\cos\th+i\sin\th` lies on the circle of radius 1--*the unit circle*.

**If** :math:`z` **is at angle** :math:`\th`, **its conjugate** :math:`\bar{z}` 
**is at** :math:`2\pi-\th` **and also at** :math:`-\th`.
:math:`1=e^0=e^{2\pi i}`.

Powers and Products: Polar Form
-------------------------------

.. note::

    **The** :math:`n`\ **th power of** :math:`z=r(\cos\th+i\sin\th)` **is** :math:`z^n=r^n(\cos n\th+i\sin n\th)`.

To multiply :math:`z` times :math:`z\pr`, **multiply** :math:`r`\ **'s and add angles**:

.. math::

    r(\cos\th+i\sin\th)\rm{\ times\ }r\pr(\cos\th\pr+i\sin\th\pr)=rr\pr(\cos(\th+\th\pr)+i\sin(\th+\th\pr)).

One way to understand this is by trigonometry.

.. math::

    (\cos\th+i\sin\th)\times(\cos\th+i\sin\th)=\cos^2\th+i^2\sin^2\th+2i\sin\th\cos\th
    
    =\cos^2\th-\sin^2\th+i2\sin\th\cos\th=\cos 2\th+i\sin 2\th

The second way to understand the rule for :math:`z^n` is by Euler's Formula

.. math::

    e^x=1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\cds\rm{\ becomes\ }
    e^{i\th}=1+i\th+\frac{1}{2}i^2\th^2+\frac{1}{6}i^3\th^3+\cds

Write :math:`-1` for :math:`i^2` to see :math:`1-\frac{1}{2}\th^2`.
**The complex number** :math:`e^{i\th}` **is** :math:`\cos\th+i\sin\th`

.. note::

    **Euler's Formula**: :math:`e^{i\th}=\cos\th+i\sin\th` gives :math:`z=r\cos\th+ir\sin\th=re^{i\th}`.

The special choice :math:`\th=2\pi` gives :math:`\cos 2\pi+i\sin 2\pi` which is 1.
Somehow the infinite series :math:`e^{2\pi i}=1+2\pi i+\frac{1}{2}(2\pi i)^2+\cds` adds up to 1.

The powers :math:`(re^{i\th})^n` are equal to :math:`r^ne^{in\th}`.
They stay on the unit circle when :math:`r=1` and :math:`r^n=1`.
Then we find :math:`n` different numbers whose :math:`n`\ th powers equal 1:

.. note::

    **Set** :math:`w=e^{2\pi i/n}`.
    **The** :math:`n`\ **th powers of** :math:`1,w,w^2,\cds,w^{n-1}` **all equal 1**.

Those are the :math:`n`\ th roots of 1.
They solve the equation :math:`z^n=1`.
They are equally spaced around the unit circle, where the full :math:`2\pi` is divided by :math:`n`.
Multiply their angles by :math:`n` to take :math:`n`\ th powers.
That gives :math:`w^n=e^{2\pi i}` which is 1.