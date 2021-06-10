Chapter 5.3 Cramer's Rule, Inverses, and Volumes
================================================

**Cramer's Rule solves** :math:`A\x=\b`.
A neat idea gives the first component :math:`x_1`.
Replacing the first column of :math:`I` by :math:`\x` gives a matrix with determinant :math:`x_1`.
When you multiply it by :math:`A`, *the first column becomes* :math:`A\x` *which is* :math:`\b`.
The other columns of :math:`B_1` are copied from :math:`A`:

**Key idea**:

.. math::

    \bb \\\ &A& \\\ \eb\bb x_1&0&0\\x_2&1&0\\x_3&0&1 \eb=
    \bb b_1&a_{12}&a_{13}\\b_2&a_{22}&a_{23}\\b_3&a_{32}&a_{33} \eb=B_1.

We multiplied a column at a time.
*Take determinants of the three matrices to find* :math:`x_1`:

**Product rule**:

.. math::

    (\det A)(x_1)=\det B_q1\quad\rm{or}\quad x_1=\frac{\det B_1}{\det A}.

This is the first component of :math:`\x` in Cramer's Rule!
Changing a column of :math:`A` gave :math:`B_1`.
To find :math:`x_2` and :math:`B_2`, put the vectors :math:`\x` and :math:`\b` 
into the *second* column of :math:`I` and :math:`A`:

**Same idea**: 

.. math::

    \bb \\\ \a_1&\a_2&\a_3\\\ \eb\bb 1&x_1&0\\0&x_2&0\\0&x_3&1 \eb=\bb \\\ \a_1&\b&\a_3\\\ \eb=B_2.

Take determinants to find :math:`(\det A)(\x_2)=\det B_2`.
This gives :math:`x_2=(\det B_2)/(\det A)`.

.. note::

    **CRAMER's RULE**: If :math:`\det A` is not zero, :math:`A\x=\b` is solved by determinants:

    * :math:`\dp x_1=\frac{\det B_1}{\det A}\quad x_2=\frac{\det B_2}{\det A}\quad\cds\quad x_n=\frac{\det B_n}{\det A}`.

    **The matrix** :math:`B_j` **has the** :math:`j`\ **th column of** :math:`A` **replaced by the vector** :math:`\b`.

To solve an :math:`n` by :math:`n` system, Cramer's Rule evaluates :math:`n+1` 
determinants (of :math:`A` and the :math:`n` different :math:`B`'s).

:math:`A\im` **involves the cofactors**.
When the right side is a column of the identity matrix :math:`I`, as in
:math:`AA\im=I`, **the determinant of each** :math:`B_j` 
**in Cramer's Rule is a cofactor of** :math:`A`.

You can see those cofactors for :math:`n=3`.
Solve :math:`A\x=(1,0,0)` to find column 1 of :math:`A\im`:

**Determinant of** :math:`B`\ **'s = Cofactors of** :math:`A`:

.. math::

    \bv 1&a_{12}&a_{13}\\0&a_{22}&a_{23}\\0&a_{32}&a_{33} \ev\quad
    \bv a_{11}&1&a_{13}\\a_{21}&0&a_{23}\\a_{31}&0&a_{33} \ev\quad
    \bv a_{11}&a_{12}&1\\a_{21}&a_{22}&0\\a_{31}&a_{32}&0 \ev

The first determinant :math:`\bv B_1 \ev` is the cofactor :math:`C_{11}=a_{22}a_{33}-a_{23}a_{32}`.
Then :math:`\bv B_2 \ev` is the cofactor :math:`C_{12}`.
Notice that the correct minus sign appears in :math:`-(a_{21}a_{33}-a_{23}a_{31})`.
This cofactor :math:`C_{12}` goes into column 1 of :math:`A\im`.
When we divide by :math:`\det A`, we have the inverse matrix.

.. note::

    **The** :math:`i,j` **entry of** :math:`A\im` **is the cofactor** 
    :math:`C_{ji}` **(not** :math:`C_{ij}`\ **) divided by** :math:`\det A`.

    * **FORMULA FOR** :math:`A\im`: :math:`\dp(A\im)_{ij}=\frac{C_{ji}}{\det A}\quad\rm{and}\quad A\im=\frac{C^T}{\det A}`.

The cofactors :math:`C_{ij}` go into the "*cofactor matrix*" :math:`C`.
**The transpose of** :math:`C` **leads to** :math:`A\im`.
To compute the :math:`i,j` entry of :math:`A\im`, cross out row :math:`j` and column :math:`i` of :math:`A`.
Multiply the determinant by :math:`(-1)^{i+j}` to get the cofactor :math:`C_{ji}`, and divide by :math:`\det A`.

*Summary*: In solving :math:`AA\im=I`, each column of :math:`I` leads to a column of :math:`A\im`.
Every entry of :math:`A\im` is a ratio: determinant of size :math:`n-1/` determinant of size :math:`n`.

**Direct proof of the formula** :math:`A\im=C^T/\det A`: This means :math:`AC^T=(\det A)I`:

.. note::

    :math:`\bb a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33} 
    \eb\bb C_{11}&C_{12}&C_{13}\\C_{21}&C_{22}&C_{23}\\C_{31}&C_{32}&C_{33} \eb=
    \bb \det A&0&0\\0&\det A&0\\0&0&\det A \eb`.

(Row 1 of :math:`A`) times (column 1 of :math:`C^T`) yields the first :math:`\det A` on the right:

.. math::

    a_{11}C_{11}+a_{12}C_{12}+a_{13}C_{13}=\det A

This is exactly the cofactor rule.

Similarly row 2 of :math:`A` times column 2 of :math:`C^T` (*notice the transpose*) also yields :math:`\det A`.
The entries :math:`a_{2j}` are multiplying cofactors :math:`C_{2j}` as they should, to give the determinant.

**Row 2 of** :math:`A`, **Row 1 of** :math:`C`:

.. math::

    a_{21}C_{11}+a_{22}C_{12}+a_{23}C_{13}=0.

Tjis is the cofactor rule for a new matrix, when the second row of :math:`A` is copied into its first row.
The new matrix :math:`A^*` has two equal rows, so :math:`\det A^*=0`.
Notice that :math:`A^*` has the same cofactors :math:`C_{11},C_{12},C_{13}` as 
:math:`A`--because all rows agree after the first row.
Thus the remarkable multiplication is correct:

.. math::

    AC^T=(\det A)I\quad\rm{or}\quad A\im=\frac{C^T}{\det A}.

*The inverse of a triangular matrix is triangular*.
Cofactors give a reason why.

Area of a Triangle
------------------

**If we know the corners** :math:`(x_1,y_1)` **and** :math:`(x_2,y_2)` **and**
:math:`(x_3,y_3)` **of a triangle, what is the area?**
Using the corners to find the base and height is not a good way to compute area.

Determinants are the best way to find area.
**The area of a triangle is half of a 3 by 3 determinant**.
The square roots in the base and height cancel out in the good formula.
If one corner is at the origin, the determinant is only 2 by 2.

.. note::

    The triangle with corners :math:`(x_1,y_1)` and :math:`(x_2,y_2)` and
    :math:`(x_3,y_3)` has :math:`\dp\rm{area}=\frac{\rm{determinant}}{2}`:

    * **Area of triangle**: :math:`\dp\frac{1}{2}\bv x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1 \ev\quad`
      :math:`\dp\rm{Area}=\frac{1}{2}\bv x_1&y_1\\x_2&y_2 \ev\rm{\ when\ }(x_3,y_3)=(0,0)`.

.. math::

    \rm{Area} = \frac{1}{2}\bv x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1 \ev = \frac{1}{2}
    (x_1y_2-x_2y_1)+\frac{1}{2}(x_2y_3-x_3y_2)+\frac{1}{2}(x_3y_1-x_1y_3).

If :math:`(0,0)` is outside the triangle, two of the special areas can be negative--but the sum is still correct.
The real problem is to explain the area of a triangle with corner :math:`(0,0)`.

Why is :math:`\frac{1}{2}|x_1y_2-x_2y_1|` the area of this triangle?
We can remove the factor :math:`\frac{1}{2}` for a parallelogram (twice as big).
We now prove that the parallellogram area is the determinant :math:`x_1y_2-x_2y_1`.





The Cross Product
-----------------










Triple Product = Determinant = Volume
-------------------------------------