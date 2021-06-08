Chapter 5.1 The Properties of Determinants
==========================================

The determinant of a square matrix is a single number.
**The determinant is zero when the matrix has no inverse**.
When :math:`A` is invertible, the determinant of :math:`A\im` is :math:`1/(\det A)`.
In fact the determinant leads to a formula for every entry in :math:`A\im`.

This is one use for determinants--to find formulas for inverse matrices and pivots and solutions :math:`A\im\b`.
For a large matrix we seldom use those formulas, because elimination is faster.

.. math::

    A=\bb a&b\\c&d \eb\rm{\ has\ inverse\ }A\im=\frac{1}{ad-bc}\bb d&-b\\-c&a \eb.

When the determinant is :math:`ad-bc=0`, we are asked to divide by zero and we can't--then :math:`A` has no inverse.
Dependent rows always lead to :math:`\det A=0`.

The determinant is also connected to the pivots.
For a 2 by 2 matrix the pivots are :math:`a` and :math:`d-(c/a)b`.
**The product of the pivots is the determinant**:

**Product of pivots**: :math:`\dp a(d-\frac{c}{a}b)=ad-bc` **which is** :math:`\det A`.

Aftere a row exchange the pivots change to :math:`c` and :math:`b-(a/c)d`.
Those new pivots multiply to give :math:`bc-ad`.
The row exchange to :math:`\bb c&d\\a&b \eb` reversed the sign of the determinant.

The determinant of an :math:`n` by :math:`n` matrix can be found in three ways:

#. **Pivot formula**: Multiply the :math:`n` pivots (times 1 or -1).

#. **"Big" formula**: Add up :math:`n!` terms (times 1 or -1).

#. **Cofactor formula**: Combine :math:`n` smaller determinants (times 1 or -1).

**The determinant changes sign when two rows (or two columns) are exchanged**.

The identity matrix has determinant :math:`+1`.
Exchange two rows and :math:`\det P=-1`.
Exchange two more rows and the new permutation has :math:`\det P=+1`.
Half of all permutations are *even* (:math:`\det P=1`) and half are *odd* (:math:`\det P=-1`).
Starting from :math:`I`, half of the :math:`P`'s involve an even number of exchanges and half require an odd number.
In the 2 by 2 case, :math:`ad` has a plus sign and :math:`bc` has minus--coming from the row exchange:

.. math::

    \det \bb 1&0\\0&1 \eb = 1 \rm{\ and\ } \det \bb 0&1\\1&0 \eb = -1

The Properties of the Determinant
---------------------------------

**The determinant is written in two ways**, :math:`\det A` **and** :math:`\bv A \ev`.
Notice: Brackets for the matrix, straight bars for its determinant.

.. math::

    \rm{The\ determinant\ of\ } \bb a&b\\c&d \eb \rm{\ is\ } \bv a&b\\c&d \ev = ad - bc.

We will check all rules with the 2 by 2 formula, but do not forget: The rules 
apply to any :math:`n` by :math:`n` matrix :math:`A`.

**1. The determinant of the** :math:`n` **by** :math:`n` **identity matrix is 1**.


**2. The determinant changes sign when two rows are exchanged** (sign reversal).


**3. The determinant is a linear function of each row separately** (all other rows stay fixed).


**4. If two rows of** :math:`A` **are equal**, **then** :math:`\det A=0`.


**5. Subtracting a multiple of one row from another row leaves** :math:`\det A` **unchanged**.


**6. A matrix with a row of zeros has** :math:`\det A=0`.


**7. If** :math:`A` **is triangular then** :math:`\det A=\a_{11}\a_{22}\cds\a_{nn}=` **product of diagonal entries**.


**8. If** :math:`A` **is singular then** :math:`\det A=0`. **If** :math:`A` **is invertible then** :math:`\det A\neq 0`.


**9. The determinant of** :math:`AB` **is** :math:`\det A` **times** :math:`\det B`: :math:`\bv AB\ev=\bv A\ev\bv B\ev`.


**10. The transpose** :math:`A^T` **has the same determinant as** :math:`A`.

