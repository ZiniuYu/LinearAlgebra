Chapter 4.3 Least Squares Approximations
========================================

It often happens that :math:`A\x=\b` has no solution.
The usual reason is: *too manu equations*.
The matrix :math:`A` has more rows than columns (:math:`m` is greater than :math:`n`).

We cannot always get the error :math:`\e=\b-A\x` down to zero.
When :math:`\e` is zero, :math:`\x` is an exact solution to :math:`A\x=\b`.
*When the length of* :math:`\e` *is as small as possible*, :math:`\wh{\x}` *is a least squares solution*.

.. note::

    **When** :math:`A\x=\b` **has no solution, multiply by** :math:`A^T` **and solve** :math:`A^TA\wh{\x}=A^T\b`.

A crucial application of least squares is ftting a straight line to :math:`m` points.
Start with three points: *Find the closest line to the points* :math:`(0,6),(1,0),(2,0)`.

No straight linge :math:`b=C+Dt` goes through those three points.
This 3 by 2 system has *no solution*: :math:`\b=(6,0,0)` is not a combination of 
the columns :math:`(1,1,1)` and :math:`(0,1,2)`.

:math:`A\x=\b` is *not* solvable:

.. math::

    A=\bb 1&0\\1&1\\1&2 \eb\quad \x=\bb C\\D \eb\quad \b=\bb 6\\0\\0 \eb.

We computed :math:`\wh{\x}=(5,-3)`.
**Those numbers are the best** :math:`C` **and** :math:`D`, **so** :math:`5-3t` 
**will be the bset line for the 3 points**.

Minimizing the Error
--------------------

How do we make the error :math:`\e=\b-A\x` as small as possible?

**By geometry**: Every :math:`A\x` lies in the plane of the columns :math:`(1,1,1)` and :math:`(0,1,2)`.
*The nearest point to* :math:`\b` *is the projection* :math:`\p`.

    The best choice for :math:`A\x` is :math:`\p`.
    The smallest possible error is :math:`\e=\b-\p`, perpendicular to the columns.
    *The three points at heights* :math:`(p_1,p_2,p_3)` *do lie on a line*, 
    because :math:`\p` is in the column space of :math:`A`.
    In fitting a straight line, :math:`\wh{\x}` is the best choice for :math:`(C,D)`.

**By algebra**: Every vector :math:`\b` splits into two parts.
The part in the column space is :math:`\p`.
The perpendicular part is :math:`\e`.
There is an equation we cannot sove (:math:`A\x=\b`).
There is an equation :math:`A\wh{\x}=\p` we can and do solve:

    .. math::

        A\x=\b=\p+\e \rm{\ is\ impossible}\quad A\wh{\x}=\p \rm{\ is\ solvable}
        \quad \wh{\x} \rm{\ is\ } (A^TA)^{-1}A^T\b.

    The solution to :math:`A\wh{\x}=\p` leaves the least possible error (which is :math:`\e`):

    **Squared length for any** :math:`\x`:

    .. math::

        \lv A\x-\b \rv^2=\lv A\x-\p \rv^2+\lv e \rv^2.

    This is the law :math:`c^2=a^2+b^2` for a right triangle.
    The vector :math:`A\x-\p` in the column space is perpendicular to :math:`\e` in the left nullspace.
    We reduce :math:`A\x-\p` to **zero** by choosing :math:`\x=\wh{\x}`.
    That leaves the smallest possible error :math:`\e=(e_1,e_2,e_3)` which we can't reduce.

    The *squared length* of :math:`A\x-\b` is minimized:

    .. note::

        **The least squares solution** :math:`\wh{\x}` **makes** :math:`E=\lv A\x-\b \rv^2` **as small as possible**.

    The closest line misses by distance :math:`e_1,e_2,e_2=1,-2,1`.
    *Those are vertical distances*.
    The least squares line minimizes :math:`E=e_1^2+e_2^2+e_3^2`.

    Notice that the erros :math:`1,-2,1` add to zero.
    *Reason*: The error :math:`\e=(e_1,e_2,e_3)` is perpendicular to the first column :math:`(1,1,1)` in :math:`A`.
    The dot product gives :math:`e_1+e_2+e_3=0`.

**By calculus**: Most functions are minimized by calculus!
The graph bottoms out and the derivative in every direction is zero.
Here the error function :math:`E` to be minimized is a *sum of squares* 
:math:`e_1^2+e_2^2+e_3^2` (the square of the error in each equation):

    .. math::

        E=\lv a\x-\b \rv^2=(C+D\cd 0-6)^2+(C+D\cd 1)^2+(C+D\cd 2)^2.

    With two unknonws :math:`C,D`, there are *two derivatives*--both zero at the minimum.
    They are "partial derivatives" because :math:`\partial{E}/\partial{C}`
    treats :math:`D` as constant and :math:`\partial{E}/\partial{D}` treats
    :math:`C` as constant:

    .. math::

        \partial{E}/\partial{C}=2(C+D\cd 0-6)+2(C+D\cd 1)+2(C+D\cd 2)=0

        \partial{E}/\partial{D}=2(C+D\cd 0-6)(0)+2(C+D\cd 1)(1)+2(C+D\cd 2)(2)=0

        3C+3D=6

        3C+5D=0

    **This matrix** :math:`\bb 3&3\\3&5 \eb` **is** :math:`A^TA`.

    **These equations are identical with** :math:`A^TA\wh{\x}=A^T\b`.
    The best :math:`C` and :math:`D` are the components of :math:`\wh{\x}`.
    The equations from calculus are the same as the "normal equations" from linear algebra.
    These are the key equations of least squares:

    .. tip::

        **The partial derivatives of** :math:`\lv A\x-\b\rv^2` **are zero when** :math:`A^TA\wh{\x}=A^T\b`.

    The solution is :math:`C=5` and :math:`D=-3`.
    Threfore :math:`b=5-3t` is the best line.
    The errors are :math:`1,-2,1` which are the same as components of vector :math:`\e`.

The Big Picture for Least Squares
---------------------------------

Refer to the textbook Page 222.

Fitting a Straight Line
-----------------------

Fitting a line is the clearest application of least squares.
It starts with :math:`m>2` points, hopefully near a straigt line.
At times :math:`t_1,\cds,t_m` those :math:`m` points are at heights :math:`b_1,\cds,b_m`.
The best line :math:`C+Dt` misses the points by vertical distances :math:`e_1,\cds,e_m`.
No line is perfect, and the least squares line minimizes :math:`E=e_1^2+\cds+e_m^2`.

Now we allow :math:`m` points (and :math:`m` can be large).

A line goes through the :math:`m` points when we exactly solve :math:`A\x=\b`.
To fit the :math:`m` points, we are trying to solve :math:`m` equations (and we only jave two unknowns!).

.. math::

    A\x=\b \quad\rm{is}\quad
    \begin{matrix}C+Dt_1=b_1\\C+Dt_2=b_2\\\vdots\\C+Dt_m=b_m\end{matrix}
    \quad\rm{with}\quad A=\bb 1&t_1\\1&t_2\\\vdots&\vdots\\1&t_m\eb.

When :math:`\b` happens to lie in the column space, the points happen to lie on a line.
In that case :math:`\b=\p`.
Then :math:`A\x=\b` is solvable and the errors are :math:`\e=(0,\cds,0)`.

.. tip::

    **The closest line** :math:`C+Dt` **has heights** :math:`p_1,\cds,p_m` **with errors** :math:`e_1,\cds,e_m`.
    **Solve** :math:`A^TA\wh{\x}=A^T\b` **for** :math:`\wh{\x}=(C,D)`.
    **The errors are** :math:`\e_i=\b_i-C-Dt_i`.

Fitting points by a straight line is so important that we give the two equations 
:math:`A^TA\wh{\x}=A^T\b`, once and for all.
The two columns of :math:`A` are independent (unless all times :math:`t_i` are the same).
So we turn to least squares and solve :math:`A^TA\wh{\x}=A^T\b`.

**Dot-product matrix**:

.. math::

    A^TA=\bb 1&\cds&1\\t_1&\cds&t_m \eb\bb 1&t_1\\\vds&\vds\\1&t_m \eb=\bb m&\sum t_i\\\sum t_i&\sum t_i^2\eb.

On the right side of the normal equation is the 2 by 1 vector :math:`A^T\b`:

.. math::

    A^T\b=\bb 1&\cds&1\\t_1&\cds&t_m \eb\bb b_1\\\vds\\b_m \eb=\bb \sum b_i\\\sum t_ib_i \eb. 

In a specific problem, these numbers are given.
The best :math:`\wh{\x}=(C,D)` is :math:`(A^TA)^{-1}A^T\b`.

.. note::

    The line :math:`C+Dt` minimizes :math:`e_1^2+\cds+e_m^2=\lv A\x-\b \rv^2` when :math:`A^TA\wh{\x}=A^T\b`:

    * :math:`A^TA\wh{\x}=A^T\b\quad\bb m&\sum t_i\\\sum t_i&\sum t_i^2\eb\bb C\\D\eb=\bb \sum b_i\\\sum t_ib_i \eb`.

The vertical errors at the :math:`m` points on the line are the components of :math:`\e=\b-\p`.
This error vector (the *residual*) :math:`\b-A\wh{\x}` is perpendicular to the columns of :math:`A` (geometry).
The error is in the nullspace of :math:`A^T` (linear algebra).
The best :math:`\wh{\x}=(C,D)` minimizes the total error :math:`E`, the sum of squares (calculus):

.. math::

    E(\x)=\lv A\x-\b \rv^2=(C+Dt_1-b_1)^2+\cds+(C+Dt_m-b_m)^2.

Calculus set the derivatives :math:`\partial{E}/\partial{C}` and 
:math:`\partial{E}/\partial{D}` to zero, and produces :math:`A^TA\wh{\x}=A^T\b`.

Other least squares problems have more than two unknowns.
Fitting by the best parabola has :math:`n=3` coefficients :math:`C,D,E`.
In general we are fitting :math:`m` data points by :math:`n` parameters :math:`x_1,\cds,x_n`.
The matrix :math:`A` has :math:`n` columns and :math:`n<m`.
The derivatives of :math:`\lv A\x=\b \rv^2` give the :math:`n` equations :math:`A^TA\wh{\x}=A^T\b`.
**The derivative of a square is linear**.
This is why the method of least squares is so popular.

:math:`A` has *orthogonal columns* when the measurement times :math:`t_i` add to zero.
When the columns of :math:`A` are orthogonal, :math:`A^TA` will be a diagonal matrix.
Orthogonal columns are so helpful that it is worth 
*shifting the times by subtracting the average time*
:math:`\wh{t}=(t_1+\cds+t_m)/m`.

Dependent Columns in :math:`A`: What is :math:`\widehat{\boldsymbol{x}}`?
-------------------------------------------------------------------------

In Section 7.4, the "*pseudoinverse*" of :math:`A` will choose the **shortest solution to** :math:`A\wh{\x}=\p`.

Fitting by a Parabola
---------------------
