Chapter 6.5 Positive Definite Matrices
======================================

Symmetric matrices with all positive eigenvalues are called **positive definite**.

Here are two goals of this section:

* To find *quick tests* on a symmetric matrix that guarantee *positive eigenvalues*.

* To explain important applications of positive definiteness.

Every eigenvalue is real because the matrix is symmetric.

**Start with 2 by 2. When does** :math:`S=\bb a&b\\b&c \eb` **have** :math:`\ld_1>0` **and** :math:`\ld_2>0`?

.. note::

    **Test: The eigenvalues of** :math:`S` **are positive if and only if** :math:`a > 0` **and** :math:`ac-b^2>0`.

*Proof that the 2 by 2 test is passed when* :math:`\ld_1>0` *and* :math:`\ld_2>0`.
Their product :math:`\ld_1\ld_2` is the determinant so :math:`ac-b^2>0`.
Their sum :math:`\ld_1+\ld_2` is the trace so :math:`a+c>0`.
Then :math:`a` and :math:`c` are both positive (if :math:`a` or :math:`c` is not positive, :math:`ac-b^2>0` will fail).

This test uses the 1 by 1 determinant :math:`a` and the 2 by 2 determinant :math:`ac-b^2`.
When :math:`S` is 3 by 3, :math:`\det S>0` is the third part of the test.
The next test requires *postive pivots*.

.. note::

    **Test: The eigenvalues of** :math:`S` **are positive if and only if the pivots are positive**:

    * :math:`a>0` and :math:`\dp\frac{ac-b^2}{a}>0\xrightarrow[\text{world}]{\text{hello}}`.

.. math::

    \bb a&b\\b&c \eb \xrightarrow[\rm{The\ multiplier\ is\ }b/a]
    {\rm{The\ first\ pivot\ is\ }a}\bb a&b\\0&c-\frac{b}{a}b \eb.

This connects two big parts of linear algebra.
**Positive eigenvalues mean positive pivots and vice versa**.
Each pivot is a ratio of upper left determinant.
The pivots give a quick test for :math:`\ld>0`, and they are a lot faster to compute than the eigenvalues.

Energy-based Definition
-----------------------

From :math:`S\x=\ld\x`, nultiply by :math:`\x^T` to get :math:`\x^TS\x=\ld\x^T\x`.
The right side is a positive :math:`\ld` times a positive number :math:`\x^T\x=\lv\x\rv^2`.
So the left side :math:`\x^TS\x` is positive for any eigenvector.

*Important point*: The new idea is that :math:`\x^TS\x` 
**is positive for all nonzero vectors** :math:`\x`, not just the eigenvectors.
In many application this number :math:`\x^TS\x` (or :math:`\frac{1}{2}\x^TS\x` ) is the **energy** in the system.
The requirement of positive energy gives *another definition* of a positive definite matrix.

Eigenvalues and pivots are two equivalent ways to test the new requirement :math:`\x^TS\x>0`.

.. note::

    **Definition**: :math:`S` **is positive definite if** :math:`\x^TS\x>0` **for every nonzero vector** :math:`\x`:

    * **2 by 2**: :math:`\x^TS\x=\bb x&y \eb\bb a&b\\b&c \eb\bb x\\y \eb=ax^2+2bxy+cy^2>0`.

The four entries :math:`a,b,b,c` give the four parts of :math:`\x^TS\x`.
From :math:`a` and :math:`c` come the pure squares :math:`ax^2` and :math:`xy^2`.
From :math:`b` and :math:`b` off the diagonal come the cross terms :math:`bxy` and :math:`byx` (the same).
Adding those four parts gives :math:`\x^TS\x`.
This energy-based definition leads to a basic fact:

.. tip::

    **If** :math:`S` **and** :math:`T` **are symmetric positive deffinite**, **so is** :math:`S+T`.

**Reason**, :math:`\x^T(S+T)\x` is simply :math:`\x^TS\x+\x^T\x`.
Those two terms are positive (for :math:`\x\neq\0`) so :math:`S+T` is also positive definite.

:math:`\x^TS\x` also connects with our final way to recognize a positive definite matrix.
For any matrix :math:`A`, possibly rectangular, we know that :math:`S=A^TA` is square and symmetric.

    **Test: If the columns of** :math:`A` **are independent, then** :math:`S=A^TA` **is positive definite**.

:math:`\x^TS\x=\x^TA^TA\x=(A\x)^T(A\x)=\lv A\x \rv^2`.
The vector :math:`A\x` is not zero when :math:`\x\neq\0` (this is the meaning of independent columns).
Then :math:`\x^TS\x` is the positive number :math:`\lv A\x \rv^2` and the matrix :math:`S` is positive definite.

.. note::

    **When a symmetric matrix** :math:`S` **has one of these five properties, it has them all:**

    #. All :math:`n` **pivots** of :math:`S` are positive.

    #. All :math:`n` **upper left determinants** are positive.

    #. All :math:`n` **eigenvalues** of :math:`S` are positive.

    #. :math:`\x^TS\x` is positive except at :math:`\x=\0`.
       This is the **energy-based** definition.

    #. :math:`S` eequals :math:`A^TA` for a matrix :math:`A` with **independent columns**.

Positive Semidefinite Matrices
------------------------------

Often we are at the edge of positive definiteness.
The determinant is zero.
The smallest eigenvalue is zero.
The energy in its eigenvector is :math:`\x^TS\x=\x^T0\x=0`.
These matrices on the edge are called *positive semidefinite*.

The matrix :math:`S=\bb 1&2\\2&4 \eb` factors into :math:`A^TA` with **dependent columns** in :math:`A`:

**Dependent columns in** :math:`A`; **Positive semidefinite** :math:`S`:

.. math::

    \bb 1&2\\2&4 \eb=\bb 1&0\\2&0 \eb\bb 1&2\\0&0 \eb=A^TA.

If 4 is increased by any small number, the matrix :math:`S` will become positive definite.

Positive semidefinite matrices have all :math:`\ld\geq 0` and all :math:`\x^TS\x\geq 0`.
Those weak inequalities (:math:`\geq` **instead of** :math:`>`) include positive
definite :math:`S` and also the singular matrices at the edge.

The Ellipse :math:`ax^2+2bxy+xy^2=1`
------------------------------------

Think of a tilted ellipse :math:`\x^TS\x=1`.
Its center is :math:`(0,0)`.
Turn it to line up with the coordinate axes (:math:`X` and :math:`Y` axes).
These two pictures show the geometry behind the factorization :math:`S=Q\Ld Q\im=Q\Ld Q^T`:

#. The tilted ellipse is associated with :math:`S`.
   Its equation is :math:`\x^TS\x=1`.

#. The lined-up ellipse is associated with :math:`\Ld`.
   Its equation is :math:`\bs{X}^T\Ld\bs{X}=1`.

#. The rotation matrix that lines up the ellipse is the eigenvector matrix :math:`Q`.

**The axes of the tilted ellipse point along those eigenvectors**.
This explains why :math:`S=Q\Ld Q^T` is called the "principal axis theorem"--it displays the axes.
Not only the axis directions (from the eigenvectors) but also the axis lengths (from the eigenvalues).
Notice: The *bigger* eigenvalue :math:`\ld_1` gives the *shorter* axis.

In the :math:`xy` system, the axes are along the eigenvectors of :math:`S`.
In the :math:`XY` system, the **axes are along the eigenvectors of** :math:`\Ld`--the coordinate axes.
All comes from :math:`S=Q\Ld Q^T`.

.. note::

    :math:`S=Q\Ld Q^T` is positive definite when all :math:`\ld_i>0`.
    The graph of :math:`\x^TS\x=1` is an ellipse:

    * :math:`\bb x&y \eb Q\Ld Q^T\bb x\\y \eb=\bb X&Y \eb\Ld\bb X\\Y \eb=\ld_1X^2+\ld_2Y^2=1`.

    The axes point along eigenvectors of :math:`S`.
    The half-lengths are :math:`1/\sqrt{\ld_1}` and :math:`1/\sqrt{\ld_2}`.

:math:`S=I` gives the circle :math:`x^2+y^2=1`.
If one eigenvalue is negative, the ellipse changes to a *hyperbola8.
The sum of squares becomes a *difference of squares*.
For a negative definite matrix like :math:`S=-I`, with both :math:`\ld`'s 
negative, the graph of :math:`-x^2-y^2=1` has no points at all.

If :math:`S` is :math:`n` by :math:`n`, :math:`\x^TS\x=1` is an "ellipsoid" in :math:`\R^n`.
Its axes are the eigenvectors of :math:`S`.

Important Application: Test for a Minimum
-----------------------------------------

For :math:`f(x)`, the test for a minimum comes from calculus: :math:`df/dx` is zero and :math:`d^2f/dx^2>0`.
Two variables in :math:`F(x,y)` produce a symmetric matrix :math:`S`.
It contains *four second derivatives*.
**Positive** :math:`d^2f/dx^2` **changes to positive definite** :math:`S`:

**Second derivatives**:

.. math::

    S=\bb \pd^2F/\pd x^2&\pd^2F/\pd x\pd y\\\pd^2F/\pd y\pd x&\pd^2F/\pd y^2 \eb.

:math:`F(x,y)` **has a minimum if** :math:`\pd F/\pd x=\pd F/\pd y=0` **and** :math:`S` **is positive definite**.

Reason: :math:`S` reveals the all-important terms :math:`ax^2+2bxy+cy^2` near :math:`(x,y)=(0,0)`.
The second derivatives of :math:`F` are :math:`2a,2b,2b,2c`.
For :math:`F(x,y,z)` the matrix :math:`S` will be 3 by 3.

Table of Eigenvalues and Eigenvectors
-------------------------------------

.. list-table:: 
    :widths: 40 25 35

    * - **Symmetric**: :math:`S^T=S=Q\Ld Q^T`
      - real eigenvalues
      - orthogonal :math:`\x_i^T\x_j=0`
    * - **Orthogonal**: :math:`Q^T=Q\im`
      - all :math:`|\ld|=1`
      - orthogonal :math:`\bar{\x}_i^T\x_j=0`
    * - **Skew-symmetric**: :math:`A^T=-A`
      - imaginary :math:`\ld`'s
      - orthogonal :math:`\bar{\x}_i^T\x_j=0`
    * - **Complex Hermitian**: :math:`\bar{S}^T=S`
      - real :math:`\ld`'s
      - orthogonal :math:`\bar{\x}_i^T\x_j=0`
    * - **Positive Definite**: :math:`\x^TS\x>0`
      - all :math:`\ld>0`
      - orthogonal since :math:`S^T=S`
    * - **Markov**: :math:`m_{ij}>0, \sum_{i=1}^nm_{ij}=1`
      - :math:`\ld_{\rm{max}}=1`
      - steady state :math:`\x>0`
    * - **Similar**: :math:`A=BCB\im`
      - :math:`\ld(A)=\ld(C)`
      - :math:`B` times eigenvector of :math:`C`\
    * - **Projection**: :math:`P=P^2=P^T`
      - :math:`\ld=1;0`
      - column space; nullspace