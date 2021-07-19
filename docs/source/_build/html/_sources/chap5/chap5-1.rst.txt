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

    .. math::

        \bv 1&0\\0&1 \ev=1 \quad\rm{and}\quad \bv 1\\&\ddots\\&&1 \ev=1.

**2. The determinant changes sign when two rows are exchanged** (sign reversal).

    .. math::

        \bv c&d\\a&b \ev=-\bv a&b\\c&d \ev.

    We can find :math:`\det P` for any permutation matrix.
    Just exchange rows of :math:`I` until you reach :math:`P`.
    Then :math:`\det P=+1` for an **even** number of row exchanges and :math:`\det P=-1` for an **odd** number.

**3. The determinant is a linear function of each row separately** (all other rows stay fixed).

    If the first row is multiplied by :math:`t`, the determinant is multiplied by :math:`t`.
    If first rows are added, determinants are added.
    This rule only applies when the other rows do not change!
    Notice how :math:`c` and :math:`d` stay the same:

    .. note::

        **Multiply row 1 by any number** :math:`t`, :math:`\det` **is multiplied by** :math:`t`:

        * :math:`\bv ta&tb\\c&d \ev=t \bv a&b\\c&d \ev`.

        **Add row 1 of** :math:`A` **to row 1 of** :math:`A^{\pr}`, **then determinants add**:

        * :math:`\bv a+a^{\pr}&b+b^{\pr}\\c&d \ev=\bv a&b\\c&d \ev+\bv a^{\pr}&b^{\pr}\\c&d \ev`.

    In the first case, both sides are :math:`tad-tbc`.
    Then :math:`t` factors out.
    In the second case, both sides are :math:`ad+a^{\pr}d-bc-b^{\pr}c`.
    These rules still apply when :math:`A` is :math:`n` by :math:`n`, and **one row changes**.
    
    Combining multiplication and addition, we get *any linear combination in one row*.
    Row 2 for row exchanges can put that row into the first row and back again.

    This rule does not mean that :math:`\det 2I=2\det I`.
    To obtain :math:`2I` we have to multiply *both* rows by 2, and the factor 2 comes out both times:

    .. math::

            \bv 2&0\\0&2 \ev=2^2=4\quad\rm{and}\quad\bv t&0\\0&t \ev=t^2.

**4. If two rows of** :math:`A` **are equal**, **then** :math:`\det A=0`.

    **Equal rows**:

    .. math::

        \bv a&b\\a&b \ev=0.

    Rule 4 follows from rule 2.
    *Exchange the two equal rows*.
    The determinant :math:`D` is supposed to change sign.
    But also :math:`D` has to stay the same, because the matrix is not changed.
    The only number with :math:`-D=D` is :math:`D=0`--this must be the determinant.

    A matrix with two equal rows has no inverse.
    Rule 4 makes :math:`\det A=0`.
    But matrices can be singular and determinants can be zero without having equal rows!

**5. Subtracting a multiple of one row from another row leaves** :math:`\det A` **unchanged**.

    :math:`l` **times row 1 from row 2**:

    .. math::

        \bv a&b\\c-la&d-lb \ev=\bv a&b\\c&d \ev

    Rule 3 (linearity) splits the left side into the right side plus another term :math:`-l\bv a&b\\c&d \ev`.
    This extra term is zero by rule 4: equal rows.

    **Conclusion**: *The determinant is not changed by the usual elimination steps from* :math:`A` *to* :math:`U`.
    Thus :math:`\det A=\det U`.
    If we can find determinants of triangular matrices :math:`U`, we can find determinants of all matrices :math:`A`.
    Every row exchange reverses the sign, so always :math:`\det A=\pm \det U`.

**6. A matrix with a row of zeros has** :math:`\det A=0`.

    **Row of zeros**:

    .. math::

        \bv 0&0\\c&d \ev=0\quad\rm{and}\quad\bv a&b\\0&0 \ev=0.

**7. If** :math:`A` **is triangular then** :math:`\det A=\a_{11}\a_{22}\cds\a_{nn}=` **product of diagonal entries**.

    **Triangular**:

    .. math::

        \bv a&b\\0&d \ev=ad\quad\rm{and\ also}\quad\bv  a&0\\c&d \ev=ad.

    Suppose all diagonal entries are nonzero.
    Remove the off-diagonal entries by elimination!
    By rule 5 the determinant is not changed--and now the matrix is diagonal:

    **Diagonal matrix**:

    .. math::

        \det\bb a_{11}&&&0\\&a_{22}\\&&\ddots\\0&&&a_{nn} \eb=(a_{11})(a_{22})\cds(a_{nn}).

**8. If** :math:`A` **is singular then** :math:`\det A=0`. **If** :math:`A` **is invertible then** :math:`\det A\neq 0`.

    **Singular**:

    .. math::

        \bb a&b\\c&d \eb \rm{\ is\ singular\ if\ and\ only\ if\ } ad-bc=0.

    **Proof**:
    Elimination goes from :math:`A` to :math:`U`.
    If :math:`A` is singular then :math:`U` has a zero row.
    The rules give :math:`\det A=\det U=0`.
    If :math:`A` is invertible then :math:`U` has the pivots along its diagonal.
    The product of nonzero pivots (using rule 7) gives a nonzero determinant:

    .. note::

        **Multiply pivots** :math:`\det A=\pm \det U=\pm(\rm{product\ of\ the\ pivots})`.

    The pivots of a 2 by 2 matrix (if :math:`a\neq 0`) are :math:`a` and :math:`d-(c/a)b`:

    .. math::

        \bv a&b\\c&d \ev=\bv a&b\\0&d-(c/a)b \ev=ad-bc.

    *This is the first formula for the determinant*.
    The sign in :math:`\pm\det U` depends on whether the number of row exchanges
    is even or odd: :math:`+1` or :math:`-1` is the determinant of the
    permutation :math:`P` that exchanges rows.

    With no row exchanges, :math:`P=I` and :math:`\det A=\det U=` *product of pivots*.
    And :math:`\det L=1`:

    .. math::

        \rm{If\ }PA=LU\rm{\ then\ }\det P=\det A=\det L\det U\rm{\ and\ }\det A=\pm\det U.

**9. The determinant of** :math:`AB` **is** :math:`\det A` **times** :math:`\det B`: :math:`\bv AB\ev=\bv A\ev\bv B\ev`.

    **Product rule**:

    .. math::

        \bv a&b\\c&d \ev\bv p&q\\r&s \ev=\bv ap+br&aq+bs\\cp+dr&cq+ds \ev.

    When the matrix is :math:`A\im`, *this rule says that the determinant of* :math:`A\im` is :math:`1/\det A`:

    :math:`A` **times** :math:`A\im`:

    .. math::

        AA\im=I\quad\rm{so}\quad(\det A)(\det A\im)=\det I=1.

    For the :math:`n` by :math:`n` case, here is a snappy proof that :math:`\bv AB\ev=\bv A\ev\bv B\ev`.
    When :math:`\bv B \ev` is not zero, consider the ratio :math:`D(A)=\bv AB \ev/\bv B \ev`.
    *Check that this ratio* :math:`D(A)` *has the following properties 1,2,3*.
    Then :math:`D(A)` has to be the determinant and we have :math:`\bv AB \ev/\bv B \ev=\bv A \ev`.

    **Property 1** (*Determinant of* :math:`I`): If :math:`A=I` then the ratio 
    :math:`D(A)` becomes :math:`\bv B \ev/\bv B \ev=1`

    **Property 2** (*Sign reversal*): When two rows of :math:`A` are exchanged, so are the same two rows of :math:`AB`.
    Therefore :math:`\bv AB \ev` changes sign and so does the ratio :math:`\bv AB \ev/\bv B \ev`.

    **Property 3** (*Linearity*): When row 1 of :math:`A` is multiplied by :math:`t`, so is row 1 of :math:`AB`.
    This multiplies the determinant :math:`\bv AB \ev` by :math:`t`.
    So the ratio :math:`\bv AB \ev/\bv B \ev` is multiplied by :math:`t`.

        Add row 1 of :math:`A` to row 1 of :math:`A^{\pr}`.
        Then row 1 of :math:`AB` adds to row 1 of :math:`A^{\pr}B`.
        By rule 3, determinants add.
        After dividing by :math:`\bv B \ev`, the ratios add--as desired.
    
    *Conclusion*: This ratio :math:`\bv AB \ev/\bv B \ev` has the same three properties that define :math:`\bv A \ev`.
    Therefore it equals :math:`\bv A \ev`.
    This proves the product rule :math:`\bv AB\ev=\bv A\ev\bv B\ev`.
    The case :math:`\bv B \ev=0` is separate and easy, because :math:`AB` is singular when :math:`B` is singular.
    Then :math:`\bv AB\ev=\bv A\ev\bv B\ev` is :math:`0=0`.

**10. The transpose** :math:`A^T` **has the same determinant as** :math:`A`.

    **Transpose**:

    .. math::

        \bv a&b\\c&d \ev=\bv a&c\\b&d \ev\rm{\ since\ both\ sides\ equal\ }ad-bc.

    The equation :math:`\bv A^T \ev=\bv A \ev` becomes :math:`0=0` when 
    :math:`A` is singular (we know that :math:`A^T` is also singular).
    Otherwise :math:`A` has the usual factorization :math:`PA=LU`.
    Transposing both sides gives :math:`A^TP^T=U^TL^T`.
    The proof of :math:`\bv A \ev=\bv A^T \ev` comes by using rule 9 for products:

    .. math::

        \rm{Compare\ }\det P\det A=\det L\det U\rm{\ with\ }\det A^T\det P^T=\det U^T\det L^T.

    First, :math:`\det L=\det L^T=1` (both have 1's on the diagonal).
    Second, :math:`\det U=\det U^T` (those triangular matrices have the same diagonal).
    Third, :math:`\det P=\det P^T` (permutations have :math:`P^TP=I`, so 
    :math:`\bv P^T \ev\bv P \ev =1` by rule 9; thus :math:`\bv P \ev` and
    :math:`\bv P^T \ev` both equal 1 or both equal -1).
    So :math:`L,U,P` have the same determinants as :math:`L^T,U^T,P^T` and this leaves :math:`\det A=\det A^T`.

**Important comment on columns**: Every rule for the rows can apply to the 
columns (just by transposing, since :math:`\bv A \ev=\bv A^T \ev`).
That determinant changes sign when two columns are exchanged.
*A zero column or two equal columns will make the determinant zero*.
If a column is multiplied by :math:`t`, so is the determinant.
The determinant is a linear function of each column separately.