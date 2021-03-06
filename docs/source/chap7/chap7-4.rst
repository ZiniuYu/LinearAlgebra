Chapter 7.4 The Geometry of the SVD
===================================

The SVD separates a matrix into three steps: :math:`(`\ **orthogonal**\ 
:math:`)\times(`\ **diagonal**\ :math:`)\times(`\ **orthogonal**\ :math:`)`.
Ordinary words can express the geometry behind it: :math:`(`\ **rotation**\ 
:math:`)\times(`\ **stretching**\ :math:`)\times(`\ **rotation**\ :math:`)`.
:math:`U\Sg V^T\x` starts with the rotation to :math:`V^T\x`.
Then :math:`\Sg` stretches that vector to :math:`\Sg V^T\x`, and :math:`U` rotates to :math:`A\x=U\Sg V^T\x`.

.. math::

    \bb a&b\\c&d \eb=\bb \cos\theta&-\sin\theta\\\sin\theta&\cos\theta \eb
    \bb \sg_1\\&\sg_2 \eb\bb \cos\phi&\sin\phi\\-\sin\phi&\cos\phi \eb=U\Sg V^T.

The four numbers :math:`a,b,c,d` in the matrix :math:`A` led to four numbers :math:`\theta,\sg_1,\sg_2,\phi` in its SVD.

#. **The norm** :math:`\lv A\rv` **of a matrix**--its maximum growth factor.

#. **The polar decomposition** :math:`A=QS`--orthogonal :math:`Q` times positive definite :math:`S`.

#. **The pseudoinverse** :math:`A^+`--the best inverse when the matrix :math:`A` is not invertible.

The Norm of a Matrix
--------------------

.. note::

    **The norm** :math:`\lv A\rv` **is the largest ratio** 
    :math:`\dp \frac{\lv A\x\rv}{\lv\x\rv}`:
    :math:`\dp\lv A\rv=\max_{\x\neq\0}\frac{\lv A\x\rv}{\lv\x\rv}=\sg_1`

Two valuable properties of that number norm(:math:`A`) come directly from its denifition:

.. note::

    * **Triangle inequality**: :math:`\lv A+B \rv\leq\lv A \rv+\lv B\rv`.

    * **Product inequality**: :math:`\lv AB \rv\leq\lv A \rv\lv B \rv`.

**For vectors**:

.. math::

    \lv(A+B)\x\rv\leq\lv A\x\rv+\lv B\x\rv\leq\lv A \rv\lv\x\rv+\lv B\rv\lv\x\rv.

Divide this by :math:`\lv\x\rv`.
Take the maximum over all :math:`\x`.
Then :math:`\lv A+B \rv\leq\lv A \rv+\lv B \rv`.

The product inequality comes quickly from :math:`\lv AB\x \rv\leq\lv A\rv\lv B\x\rv\leq\lv A\rv\lv B\rv\lv \x\rv`.
Again divide by :math:`\lv \x \rv`.
Take the maximum over all :math:`\x`.
The result is :math:`\lv AB \rv\leq\lv A\rv\lv B\rv`.

**The closet rank** :math:`k` **matrix to** :math:`A` **is** :math:`A_k=\sg_1\u_1\v_1^T+\cds+\sg_k\u_k\v_k^T`.

This is the key fact in matrix approximation: The Eckart-Young-Mirsky Theorem 
says that :math:`\lv A-B \rv\leq\lv A-A_k\rv=\sg_{k+1}` **for all matrices**
:math:`B` **of rank** :math:`k`.

The :math:`\v`'s and :math:`\u`'s give orthonormal bases for the four 
fundamental subspaces, and the *first* :math:`k` :math:`\v`\ *'s and* :math:`\u`
\ *'s and* :math:`\sg`\ *'s* give the best matrix approximation to :math:`A`.

Polar Decomposition :math:`A=QS`
--------------------------------

**Every complex number** :math:`x+iy` **has the polar form** :math:`re^{i\th}`.
A number :math:`r\geq 0` multiplies a number :math:`e^{i\th}` on the unit circle.
We have :math:`x+iy=r\cos\th+ir\sin\th=r(\cos\th+i\sin\th)=re^{i\th}`.
Think of these numbers as 1 by 1 matrices.
Then :math:`e^{i\th}` is an orthogonal matrix :math:`Q` and :math:`r\geq 0` is a 
*positive semidefinite matrix* (call it :math:`S`).
The **polar decomposition** extends the same idea to :math:`n` by :math:`n` 
matrices: orthogonal times positive semidefinite, :math:`A=QS`.

.. note::

    Every real square matrix can be factored into :math:`A=QS`, where :math:`Q` 
    is **orthogonal** and :math:`S` is **symmetric positive semidefinite**.
    If :math:`A` is invertible, :math:`S` is positive definite.

For the proof we just insert :math:`V^TV=I` into the middle of the SVD:

**Polar decomposition**:

.. math::

    A=U\Sg V^T=(UV^T)(V\Sg V^T)=(Q)(S).

If :math:`A` is invertible then :math:`Sg` and :math:`S` are also invertible.
:math:`S` **is the symmetric positive definite square root of** :math:`A^TA`, because :math:`S^2=V\Sg^2V^T=A^TA`.
So the eigenvalues of :math:`S` are the singular values of :math:`A`.
The eigenvectors of :math:`S` are the singular vectors :math:`\v` of :math:`A`.

There is also a polar decomposition :math:`A=KQ` in the reverse order.
:math:`Q` is the same but now :math:`K=U\Sg U^T`.
Then :math:`K` is the symmetric positive definite square root of :math:`AA^T`.

:math:`Q=UV^T` is the **nearest orthogonal matrix** to :math:`A`.
This :math:`Q` makes the norm :math:`\lv Q-A \rv` as small as possible.
That corresponds to the fact that :math:`e^{i\th}` is the nearsest number on the unit circle to :math:`re^{i\th}`.

.. note::

    **The nearest singular matrix** :math:`A_0` **to** :math:`A` 
    **comes by changing the smallest** :math:`\sg_{\min}` **to zero**.

The Pseudoinverse :math:`A^+`
-----------------------------

**Pseudoinverse of** :math:`A`:

.. math::

    A^+=V\Sg^+U^T=\bb \\\ \v_1\cds\v_r\cds\v_n \\\ \eb
    \bb \sg_1^{-1}\\&\dds\\&&\sg_r^{-1}\\&&& \eb
    \bb \\\ \u_1\cds\u_r\cds\u_m \\\ \eb^T.

The **pseudoinverse** :math:`A^+` is an :math:`n` by :math:`m` matrix.
If :math:`A^{-1}` exists, than :math:`A^+` is the same as :math:`A^{-1}`.
In that case :math:`m=n=r` and we are inverting :math:`U\Sg V^T` to get :math:`V\Sg^{-1}U^T`.
The new symbol :math:`A^+` is needed when :math:`r<m` or :math:`r<n`.
Then :math:`A` has no two-sided inverse, but it has a *pseudo*\ inverse :math:`A^+` with that same rank :math:`r`:

.. math::

    A^+\u_i=\frac{1}{\sg_i}\v_i\quad\rm{for\ }i\leq r\quad\rm{and}\quad A^+\u_i=\0\quad\rm{for\ }i>r.

.. note::

    **Trying for** :math:`AA\im=A\im A=I`:

    * :math:`AA^+=` projection matrix onto the column space of :math:`A`.

    * :math:`A^+A=` projection matrix onto the row space of :math:`A`.

Least Squares with Dependent Columns
------------------------------------

.. note::

    :math:`\x^+=A^+\b=(1,1)` **is the shortest solution to** :math:`A^TA\wh{\x}=A^T\b` and :math:`A\wh{\x}=\p`.