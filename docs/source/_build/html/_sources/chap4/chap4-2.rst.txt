Chapter 4.2 Projections
=======================

The projection of :math:`\b` is :math:`P\b`.

#. What are the projection of :math:`\b=(2,3,4)` onto the :math:`z` axis and the :math:`xy` plane?

#. What matrices :math:`P_1` and :math:`P_2` produce those projections onto a line and a plane?

When :math:`\b` is projected onto a line, **its projection** :math:`p` **is the part of** :math:`\b` **along that line**.
If :math:`\b` is projected onto a plane, :math:`\p` is the part in that plane.
**The projection** :math:`\p` **is** :math:`P\b`.

The projection matrix :math:`P` multiplies :math:`\b` to give :math:`\p`.

The projection onto the :math:`z` axis we call :math:`\p_1`.
The second projection drops straight down to the :math:`xy` plane.
Start with :math:`\b=(2,3,4)`.
The projection across gives :math:`\p_1=(0,0,4)`.
The projection down gives :math:`\p_2=(2,3,0)`.
Those are the parts of :math:`\b` along the :math:`z` axis and in the :math:`xy` plane.

**Projection Matirx** Onto the :math:`z` axis:

.. math::

    P_1 = \bb 0&0&0\\0&0&0\\0&0&1 \eb.

**Projection Matirx** Onto the :math:`xy` plane:

.. math::

    P_2 = \bb 1&0&0\\0&1&0\\0&0&0 \eb.

:math:`P_1` picks out the :math:`z` component of every vector.
:math:`P_2` picks out the :math:`x` and :math:`y` components.

.. math::

    \p_1=P_1\b=\bb 0&0&0\\0&0&0\\0&0&1 \eb\bb x\\y\\z \eb=\bb 0\\0\\z \eb\quad
    \p_2=P_2\b=\bb 1&0&0\\0&1&0\\0&0&0 \eb\bb x\\y\\z \eb=\bb x\\y\\0 \eb.

In this case the projections :math:`p_1` and :math:`p_2` are perpendicular.
The :math:`xy` plane and the :math:`z` axis are **orthogonal subspaces**.
More than just orthogonal, the line and plane are **orthogonal complements**.
The projections :math:`\p_1` and :math:`\p_2` are exactly those two parts of :math:`\b`:

* The vectors give :math:`\p_1+\p_2=\b`.

* The matrices give :math:`P_1+P_2=I`.

Our problem is **to project any** :math:`\b` **onto the column space of any** :math:`m` **by** :math:`n` **matrix**.
Start with a line (dimension :math:`n=1`).
The matrix :math:`A` will have only one column.
Call it :math:`\a`.

Projection Onto a Line
----------------------

A line goes through the origin in the direction of :math:`\a=(a_1,\cds,a_m)`.
Along that line, we want the point :math:`\p` closest to :math:`\b=(b_1,\cds,b_m)`.
The key to projection is orthogonality: **The line from** :math:`\b` **to** 
:math:`\p` **is perpendicular to the vector** :math:`\a`.
We now compute :math:`\p` by algebra.

The projection :math:`\p` will be some multiple of :math:`\a`.
Call it :math:`\p=\wh{x}\a=` ":math:`x` hat" times :math:`\a`.
Computing this number :math:`\wh{x}` will give the vector :math:`\p`.
Then from the formula for :math:`\p`, we will read off the projection matrix :math:`P`.
These three steps will lead to all projection matrices: **find** :math:`\wh{x}`,
**then find the vector** :math:`\p`, **then find the matrix** :math:`P`.

:math:`\b-\p` is the "error" :math:`\e=\b-\wh{x}\a`.
It is perpendicular to :math:`\a`--this will determine :math:`\wh{x}`.
Use the fact that :math:`\b-\wh{x}\a` **is perpendicular to** :math:`\a` when their dot product is zero:

.. note::

    Projecting :math:`\b` onto :math:`\a` with error :math:`\e=\b-\wh{x}\a`:
    :math:`\a\cd(\b-\wh{x}\a)=0` or :math:`\a\cd\b-\wh{x}\a\cd\a=0`:

    * :math:`\dp\wh{x}=\frac{\a\cd\b}{\a\cd\a}=\frac{\a^T\b}{\a^T\a}`.

.. note::

    **The projection of** :math:`\b` **onto the line through** :math:`\a` 
    **is the vector**: :math:`\dp\p=\wh{x}\a=\frac{\a^T\b}{\a^T\a}\a`.

    * Special case 1: If :math:`\b=\a` then :math:`\wh{x}=1`. The projection of :math:`\a` onto :math:`\a` is itself. :math:`P\a=\a`.

    * Special case 2: If :math:`\b` is perpendicular to :math:`\a` then :math:`\a^T\b=0`. The projection is :math:`\p=\0`.

Look at the right triangle of :math:`\b,\p,\e`.
The vector :math:`\b` is split into two parts--its component along the line is 
:math:`\p`, its perpendicular part is :math:`\e`.
Those two sides :math:`\p` and :math:`\e` have length
:math:`\lv\p\rv=\lv\b\rv\cos\theta` and :math:`\lv\e\rv=\lv\b\rv\sin\theta`.
Trigonometry matches the dot product:

.. math::

    \p=\frac{\a^T\b}{\a^T\a}\a\rm{\ has\ length\ }\lv\p\rv=
    \frac{\lv\a\rv\lv\b\rv\cos\theta}{\lv\a\rv^2}\lv\a\rv=\lv\b\rv\cos\theta.

The dot product is alot simpler than getting involved with :math:`\cos\theta` and the length of :math:`\b`.

.. note::

    **Projection matrix** :math:`P`: :math:`\dp\p=\a\wh{x}=\a\frac{\a^T\b}{\a^T\a}=P\b`
    when the matrix is :math:`\dp P=\frac{\a\a^T}{\a^T\a}`.

:math:`P` is a column times a row!
The column is :math:`\a`, the row is :math:`\a^T`.
Then divide by the number :math:`\a^T\a`.
The projection matrix :math:`P` is :math:`m` by :math:`m`, but **its rank is one**.
We are projecting onto a one-dimensional subspace, the line through :math:`\a`.
*That line is the column space of* :math:`P`.

**Projecting a second time doesn't change anything, so** :math:`P^2=P`.

Note that :math:`(I-P)\b=\b-\p=\e`. 
**When** :math:`P` **projects onto one subspace**, :math:`I-P` **projects onto the perpendicular subspace**.
Here :math:`I-P` projects onto the plane perpendicular to :math:`\a`.

Projection Onto a Subspace
--------------------------

Start with :math:`n` vectors :math:`\a_1,\cds,\a_n` in :math:`\R^m`.
Assume that these :math:`\a`'s are linearly independent.

**Problem: Find the combination** :math:`\p=\wh{x}_1\a_1+\cds+\wh{x}_n\a_n` **closest to a given vector** :math:`\b`.
We are projecting each :math:`\b` in :math:`\R^m` onto the subspace spanned by the :math:`\a`'s.

With :math:`n=1` (one vector :math:`\a_1`) this is projection onto a line.
The line is the column space of :math:`A`, which has just one column.
In general the matrix :math:`A` has :math:`n` columns :math:`\a_1,\cds,\a_n`.

The combination in :math:`\R^m` are the vectors :math:`A\x` in the column space.
We are looking for the particular combination :math:`\p=A\wh{\x}`.
That choise is :math:`\wh{x}=\a^T\b/\a^T\a` when :math:`n=1`.

We compute projections onto :math:`n`-dimensional subspaces in three steps as 
before: **Find the vector** :math:`\wh{\x}`, **find the projection** 
:math:`\p=A\wh{\x}`, **find the proection matrix** :math:`P`.

**The error vector** :math:`\b-A\wh{\x}` **is perpendicular to the subspaces**.
It makes a right angle with all the vectors :math:`\a_1,\cds,\a_n` in the base:

.. note::

    :math:`\begin{matrix}\a_1^T(\b-A\wh{\x})=0\\\vdots\\\a_n^T(\b-A\wh{\x})=0\end{matrix}\quad`
    or :math:`\quad\bb -&\a_1^T&-\\&\vdots&\\-&\a_n^T&- \eb\bb \\\b-A\wh{\x}\\\ \eb=\bb \\\0\\\ \eb`.

The matrix with those rows :math:`\a_i^T` is :math:`A^T`.
The :math:`n` equations are exactly :math:`A^T(\b-A\wh{\x})=\0`.

.. note::

    The combination :math:`\p=\wh{x}_1\a_1+\cds+\wh{x}_n\a_n=A\wh{\x}` that is
    closest to :math:`\b` comes from :math:`\wh{\x}`:

    * **Find** :math:`\wh{\x}\ (n \times 1):\quad A^T(\b-A\wh{\x})=\0\quad\rm{or}\quad A^A\wh{\x}=A^T\b`.

    This symmetric matrix :math:`A^TA` is :math:`n` by :math:`n`.
    It is invertible if the :math:`\a`'s are independent.
    The solution is :math:`\wh{\x}=(A^TA)^{-1}A^T\b`.
    The **projection** of :math:`\b` onto the subspace is :math:`\p`:

    * **Find** :math:`\p\ (m \times 1):\quad \p=A\wh{\x}=A(A^TA)^{-1}A^T\b`.

    The next formula picks out the **projection matrix** that is multiplying :math:`\b`:

    * **Find** :math:`P\ (m \times m):\quad P=A(A^TA)^{-1}A^T`.

Compare with projection onto a line, when :math:`A` has only one column: :math:`A^A` is :math:`\a^T\a`.

.. note::

    **For** :math:`n=1`: :math:`\dp\wh{x}=\frac{\a^T\b}{\a^T\a}` and
    :math:`\dp\p=\a\frac{\a^T\b}{\a^T\a}` and :math:`\dp P=\frac{\a\a^T}{\a^T\a}`.

The key step was :math:`A^T(\b-A\wh{\x})=\0`.
We used geometry (:math:`\e` is orthogonal to each :math:`\a`).
*Linear algebra gives this "normal equation" too*, in a very quick and beautiful way:

#. Our subspace is the column space of :math:`A`.

#. The error vector :math:`\b-A\wh{\x}` is perpendicular to that column space.

#. Therefore :math:`\b-A\wh{\x}` is in the nullspace of :math:`A^T`! This means :math:`A^T(\b-A\wh{\x})=\0`.

The left nullspace is important in projections.
That nullspace of :math:`A^T` contains the error vector :math:`\e-\b-A\wh{\x}`.
The vector :math:`\b` is being split into the projection :math:`\p` and the error :math:`\e=\b-\p`.
Projection produces a right triangle with sides :math:`\p,\e,\b`.

.. warning::

    The matrix :math:`P=A(A^TA)^{-1}A^T` is deceptive.
    You cannot split :math:`(A^TA)^{-1}` into :math:`A^{-1}` times :math:`(A^T)^{-1}`.
    **The matrix** :math:`A` **is rectangular**.
    **It has no inverse matrix**.

.. Tip::

    :math:`A^TA` **is invertible if and only if** :math:`A` **has linearly independent columns**.

**Proof**: :math:`A^TA` is a square matrix (:math:`n` by :math:`n`).
For every matrix :math:`A`, we will now show that :math:`A^TA` **has the same nullsapce as** math:`A`.

    Let :math:`A` be any matrix.
    If :math:`\x` is in tis nullspace, then :math:`A\x=\0`.
    Multiplying by :math:`A^T` gives :math:`A^TA\x=\0`.
    So :math:`\x` is also in the nullsapce of :math:`A^TA`.

    **From** :math:`A^TA\x=\0` **we must prove** :math:`A\x=\0`.
    Since we can't multiply by :math:`(A^T)^{-1}`, which generally doesn't exist.
    Just multiply by :math:`\x^T`.

    .. math::

        (\x^T)A^TA\x=0 \quad\rm{or}\quad (A\x)^T(A\x)=0 \quad\rm{or}\quad \lv A\x\rv ^2=0.

    We have shown: If :math:`A^TA\x=\0` then :math:`A\x` has length zero.
    Therefore :math:`A\x=\0`.
    Every vector :math:`\x` in one nullspace is in the other nullspace.
    If :math:`A^TA` has dependent column, so has :math:`A`.
    If :math:`A^TA` has independent columns, so has :math:`A`.
    This is the good case: :math:`A^TA` is invertible.

.. tip::

    When :math:`A` has independent columns, :math:`A^TA` is square, symmetric, and invertible.

**Very brief summary**: To find the projection :math:`\p=\wh{x}_1\a_1+\cds+\wh{x}_n\a_n`, solve :math:`A^TA\wh{\x}=A^T\b`.
This gives :math:`\wh{\x}`.
The projection is :math:`\p=A\wh{\x}` and the error is :math:`\e=\b-p=\b-A\wh{\x}`.
The projection matrix :math:`P=A(A^TA)^{1}A^T` gives :math:`\p=P\b`.

**This matrix satsfies** :math:`P^2=P`.
**The distance from** :math:`\b` **to the subspace** :math:`\bs{C}(A)` **is** :math:`\lv\e\rv`.