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



Polar Decomposition :math:`A=QS`
--------------------------------









The Pseudoinverse :math:`A^+`
-----------------------------









Least Squares with Dependent Columns
------------------------------------