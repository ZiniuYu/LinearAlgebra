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











Positive Semidefinite Matrices
------------------------------










The Ellipse :math:`ax^2+2bxy+xy^2=1`
------------------------------------










Important Application: Test for a Minimum
-----------------------------------------