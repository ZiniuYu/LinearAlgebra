Chapter 6.2 Diagonalizing a Matrix
==================================

When :math:`\x` is an eigenvector, multiplication by :math:`A` is just 
multiplication by a number :math:`\ld`: :math:`A\x=\ld\x`.

The point of this section is very direct.
**The matrix** :math:`A` **turns into a diagonal matrix** :math:`\Ld` **when we use the eigenvectors properly**.

.. note::

    **Diagonalization**: Suppose the :math:`n` by :math:`n` matrix :math:`A` has 
    :math:`n` linearly independent eigenvectors :math:`\x1,\cds,\x_n`.
    Put them into the columns of an **eigenvector matrix** :math:`X`.
    Then :math:`X\im AX` is the **eigenvalue matrix** :math:`\Ld`:

    * **Eigenvector matrix** :math:`X`, **Eigenvalue matrix** :math:`\Ld`:
      :math:`X\im AX=\Ld=\bb \ld_1\\&\dds\\&&\ld_n \eb`.

The matrix :math:`A=\bb 1&5\\0& 6\eb` is triangular so its eigenvalues are on the diagonal: :math:`\ld_1=1,\ld_2=6`.

.. note::

    **Eigenvectors go into** :math:`X`:

    * :math:`\bb 1\\0 \eb\bb 1\\1 \eb`.

.. math::

    \bb 1&-1\\0&1 \eb\bb 1&5\\0&6 \eb\bb 1&1\\0&1 \eb=\bb 1&0\\0&6 \eb.

In other words :math:`A=X\Ld X\im`.
Then :math:`A^2=X\Ld X\im X\Ld X\im=X\Ld^2X\im`.

:math:`A^2` **has the same eigenvectors in** :math:`X` **and squared eigenvalues in** :math:`\Ld^2`.

**Why is** :math:`AX=X\Ld`?
:math:`A` multiplies its eigenvectors, which are the columns of :math:`X`.
The first column of :math:`AX` is :math:`A\x_1`.
That is :math:`\ld_1\x_1`.
Each column of :math:`X` is multiplied by its eigenvalue:

:math:`A` **times** :math:`X`:

.. math::

    AX=A\bb \\\ \x_1&\cds&\x_n \\\ \eb=\bb \\\ \ld_1\x_1&\cds&\ld_n\x_n \\\ \eb.

The trick is to split thsis matrix :math:`AX` into :math:`X` times :math:`\Ld`:

:math:`X` **times** :math:`\Ld`:

.. math::

    \bb \\\ \ld_1\x_1&\cds&\ld_n\x_n \\\ \eb=\bb \\\ \x_1&\cds&\x_n \\\ \eb\bb \ld_1\\&\dds\\&&\ld_n \eb=X\Ld.

Keep those matrices in the right order.
Then :math:`\ld_1` multiplies the first column :math:`\x_1`, as shown.
The diagonalization is complete, and we can write :math:`AX=X\Ld` in two good ways:

.. note::

    :math:`AX=X\Ld` is :math:`X\im AX=\Ld` or :math:`A=X\Ld X\im`.

The matrix :math:`X` has an inverse, because its columns (the eigenvectors of 
:math:`A`) were assumede to be linearly independent.
*Without* :math:`n` *independent eigenvectors, we can't diagonalize*.

:math:`A` and :math:`\Ld` have the same eigenvalues :math:`\ld_1,\cds,\ld_n`.
The eigenvectors are different.
The :math:`k`th power will be :math:`A^k=X\Ld^kX\im` which is easy to compute:

.. math::

    A^k=(X\Ld X\im)(X\Ld X\im)\cds(X\Ld X\im)=X\Ld^kX\im.

**Powers of** :math:`A`:

.. math::

    \bb 1&5\\0&6 \eb^k=\bb 1&1\\0&1 \eb\bb 1\\&6^k \eb\bb 1&-1\\0&1 \eb=\bb 1&6^k-1\\0&6^k \eb=A^k.

**Remark 1**: Suppose the eigenvalues :math:`\ld_1,\cds,\ld_n` are all different.
Then it is automatic that the eigenvectors :math:`\x_1,cds,\x+n` are independent.
The eigenvector matrix :math:`X` will be *invertible*.
**Any matrix that has no repeated eigenvalues can be diagonalized**.

**Remark 2**: **We can multiply eigenvectors by any nonzero constants**.
:math:`A(c\x)=\ld(c\x)` is still true.

**Remark 3**: The eigenvectors in :math:`X` come in the same order as the eigenvalues in :math:`Ld`.
To reverse the order in :math:`\Ld`, put the eigenvector :math:`(1,1)` before :math:`(1,0)` in :math:`X`:

    **New order** :math;`6,1`:

    .. math::

        \bb 0&1\\1&-1 \eb\bb 1&5\\0&6 \eb\bb 1&1\\1&0 \eb=\bb 6&0\\0&1 \eb=\Ld_{\rm{new}}.

    To diagonalize :math:`A` we *must* use an eigenvector matrix.
    From :math:`X\im AX=\Ld` we know that :math:`AX=X\Ld`.
    Suppose the first column of :math:`X` is :math:`\x`.
    Then the first columns of :math:`AX` and :math:`X\Ld` are :math:`A\x` and :math:`\ld_1\x`.
    For those to be equal, :math:`\x` must be an eigenvector.

**Remark 4** (repeated warning for repeated eigenvalues): Some matrices have too few eigenvectors.
*Those matrices cannot be diagonalized*.

    **Not diagnoalizable**:

    .. math::

        A=\bb 1&-1\\1&-1 \eb\quad \rm{and} \quad B=\bb 0&1\\0&1 \eb.

    Their engenvalues happen to be 0 and 0.
    Nothing is special about :math:`\ld=0`, the problem is the repetition of :math:`\ld`.
    All eigenvectors of the first matrix are multiples of :math:`(1,1)`:

    **Only one line of eigenvectors**:

    .. math::

        A\x=0\x \quad\rm{means}\quad \bb 1&-1\\1&-1 \eb\bb \\\ \x\\\ \eb=\bb 0\\0 \eb\quad\rm{and}\quad \x=c\bb 1\\1 \eb.

    There is no second eigenvector, so this unusual matrix :math:`A` cannot be diagonalized.
    
    * **Invertibility** is concerned with the **eigenvalues** (:math:`\ld=0` or :math:`\ld\neq 0`).

    * **Diagonalizability** is concerned with the **eigenvectors** (too few or enough for :math:`X`).

    Each eigenvalue has at least one eigenvector.
    :math:`A-\ld I` is singular.
    If :math:`(A-\ld I)\x=\0` leads you to :math:`\x=\0`, :math:`\ld` is *not* an eigenvalue.
    Look for a mistake in solving :math:`\det(A-\ld I)=0`.

    .. tip::

        **Eigenvectors for** :math:`n` **different** :math:`\ld`\ **'s are independent**.
        **Then we can diagonalize** :math:`A`.

    .. note::

        **Independent** :math:`\x` **from different** :math:`\ld`: Eigenvectors
        :math:`\x_1,\cds,\x_j` that correspond to distinct (all different)
        eigenvalues are linearly independent.
        An :math:`n` by :math:`n` matrix that has :math:`n` different 
        eigenvalues (no repeated :math:`\ld`'s) must be diagonalizable.

    **Proof**: Suppose :math:`c_1\x_1+c_2\x_2=\0`.
    Multiply by :math:`A` to find :math:`c_1\ld_1\x_1+c_2\ld_2\x_2=\0`.
    Multiply by :math:`\ld_2` to find :math:`c_1\ld_2\x_1+c_2\ld_2\x_2=\0`.
    Now subtract one from the other: Subtraction leaves :math:`(\ld_1-\ld_2)c_1\x_1=\0`.
    Therefore :math:`c_1=0`.

        Since the :math:`\ld`'s are different and :math:`\x_1\neq\0`, we are forced to the conclusion that :math:`c_1=0`.
        Similarly :math:`c_2=0`.
        Only the combination with :math:`c_1=c_2=0` gives :math:`c_1\x_1+c_2\x_2=\0`.
        So the eigenvectors :math:`\x_1` and :math:`\x_2` must be independent.

    This proof extends directly to :math:`j` eigenvectors.
    Suppose that :math:`c_1\x_1+\cds+c_j\x_j=\0`,
    Multiply by :math:`A`, multiply by :math:`\ld_j` and subtract.
    This multiplies :math:`\x_j` by :math:`\ld_j-\ld_j=0`, and :math:`\x_j` is gone.
    Now multiply by :math:`A` and by :math:`\ld_{j-1}` and subtract.
    This removes :math:`\x_{j-1}`.
    Eventually only :math:`\x_1` is left: We reach 
    :math:`(\ld_1-\ld_2)\cds(\ld_1-\ld_j)c_1\x_1=\0` which forces :math:`c_1=0`.

    Similarly every :math:`c_i=0`.
    When the :math:`\ld`'s are all different, the eigenvectors are independent.
    A full set of eigenvectors can go into the columns of the eigenvector matrix :math:`X`.

.. note::

    **Question**: When does :math:`A^k\rightarrow zero\ matrix`?
    **Answer**: All :math:`|\ld|<1`.

Similar Matrices: Same Eigenvalues
----------------------------------

Suppose the eigenvalue matrix :math:`\Ld` is fixed.
As we change the eigenvector matrix :math:`X`, we get a whole family of 
different matrices :math:`A=X\Ld X\im`--*all with the same eigenvalues in* 
:math:`\Ld`.
All those matrices :math:`A` (with the same :math:`\Ld`) are called *similar**.

This idea extends to matrices that can't be diagonalized.
Again we choose one constant matrix :math:`C` (not necessariily :math:`\Ld`).
And we look at the whole family of matrices :math:`A=BCB\im`, allowing all invertible matrices :math:`B`.
Again those matrices :math:`A` and :math:`C` are called **similar**.

We are using :math:`C` instead of :math:`\Ld` because :math:`C` might not be diagonal.
We are using :math:`B` instead of :math:`X` because the columns of :math:`B` might not be eigenvectors.
We only require that :math:`B` is invertible--its columns can cantain any basis for :math:`\R^n`.
**Similar matrices** :math:`A` **and** :math:`C` **have the same eigenvalues**.

.. note::

    **All the matrices** :math:`A=BCB\im` **are "similar"**. 
    **They all share the eigenvalues of** :math:`C`.

**Proof**: Suppose :math:`C\x=\ld\x`.
Then :math:`BCB\im`has the same eigenvalue :math:`\ld` with the new eigenvector :math:`B\x`:

.. math::

    Same\ \ld\quad(BCB\im)(B\x)=BC\x=B\ld\x=\ld(B\x).

A fixed matrix :math:`C` produces a family of similar matrices :math:`BCB\im`, allowing all :math:`B`.
When :math:`C` is the identity matrix, the "family" is very small.
The only member is :math:`BIB\im=I`.
The identity matrix is the only diagonalizable matrix with all eigenvalues :math:`\ld=1`.

The family is larger when :math:`\ld=1` and :math:`1` *with only one eigenvector* (not diagonalizable).
The simpliest :math:`C` is the *Jordan form*.
All the similar :math:`A`'s have two parameters :math:`r` and :math:`s`, not 
both zero: always determinant = 1 and trace = 2.

.. math::

    C=\bb 1&1\\0&1 \eb=\rm{\ Jordan\ form\ gives\ }A=BCB\im=\bb 1-rs&r^2\\-s^2&1+rs \eb.

Fibonacci numbers
-----------------

**Every new Fibonacci number is the sum of the two previous** :math:`F`\ **'s**:

.. note::

    **The sequence** :math:`0,1,1,2,3,5,8,13,\cds` **comes from** :math:`F_{k+2}=F_{k+1}+F_k`.

**Problem: Find the Fibonacci number** :math:`F_{100}`: The slow way is to apply the rule :math:`F_{k+2}=F_{k+1}+F_k`.
Linear algebra gives a better way.

The key is to begin with a matrix equation :math:`\u_{k+1}=A\u_k`.
That is a *one-step* rule for vectors, while Fibonacci gave a two-step rule for scalars.
We match those rules by putting two Fibonacci numbers into a vector.
Then you will see the matrix :math:`A`.

.. note::

    Let :math:`\u_k=\bb F_{k+1}\\F_k \eb`.
    The rule :math:`\begin{matrix}F_{k+2}=F_{k+1}+F_k\\F_{k+1}=F_{k+1}\quad\quad
    \end{matrix}` is :math:`\u_{k+1}=\bb 1&1\\1&0 \eb\u_k`.

**Every step multiplies by** :math:`A=\bb 1&1\\1&0 \eb`.
After 100 steps we reach :math:`\u_{100}=A^{100}\u_0`:

.. math::

    \u_0=\bb 1\\0 \eb, \u_1=\bb 1\\1 \eb, \u_2=\bb 2\\1 \eb, \u_3=\bb 3\\2 \eb, \cds, \u_{100}=\bb F_{101}\\F_{100} \eb.

Subtract :math:`\ld` from the diagonal of :math:`A`:

.. math::

    A=\ld I=\bb 1-\ld&1\\1&-\ld \eb\quad\rm{leads\ to}\quad\det(A-\ld I)=\ld^2-\ld-1.

.. note::

    **Eigenvalues**: :math:`\dp\ld_1=\frac{1+\sqrt{5}}{2}\approx 1.618` and 
    :math:`\dp\ld_2=\frac{1-\sqrt{5}}{2}\approx -.618`.

These eigenvalues lead to eigenvectors :math:`\x_1=(\ld_1,1)` and :math:`\x_2=(\ld_2,1)`.
Step 2 finds the combination of those eigenvectors that gives :math:`\u_0=(1,0)`:

.. math::

    \bb 1\\0 \eb=\frac{1}{\ld_1-\ld_2}\left(\bb\ld_1\\1\eb-\bb\ld_2\\1\eb\right)
    \quad\rm{or}\quad\u_0=\frac{\x_1-\x_2}{\ld_1-\ld_2}.

Step 3 multiplies :math:`u_0` by :math:`A^{100}` to find :math:`u_{100}`.
The eigenvectors :math:`\x_1` and :math:`\x_2` stay separate!
They are multiplied by :math:`(\ld_1)^{100}` and :math:`(\ld_2)^{100}`:

**100 steps from** :math:`\u_0`:

.. math::

    \u_{100}=\frac{(\ld_1)^{100}\x_1-(\ld_2)^{100}\x_2}{\ld_1-\ld_2}.

We want :math:`F_{100}=` second component of :math:`\u_{100}`.
The second components of :math:`\x_1` and :math:`\x_2` are 1.
The difference between :math:`\ld_1=(1+\sqrt{5})/2` and :math:`\ld_2=(1-\sqrt{5})/2` is :math:`\sqrt{5}`.
And :math:`\ld_2^{100}\approx 0`.

100th Fibonacci number :math:`=\dp\frac{\ld_1^{100}-\ld_2^{100}}{\ld_1-\ld_2}=`
nearest integer to :math:`\dp\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^{100}`.

Every :math:`F_k` is a whole number.
The ratio :math:`F_{101}/F_{100}` must be very close to the limiting ratio :math:`(1+\sqrt{5})/2`.
This number is the "*golden mean*".

Matrix Powers :math:`A^k`
-------------------------

Fibonacci's example is a typical difference equation :math:`\u_{k+1}=A\u_k`.
**Each step multiplies by** :math:`A`.
The solution is :math:`\u_k=A^k\u_0`.

The eigenvector matrix :math:`X` produces :math:`A=X\Ld X\im`.
This is a factorization of the matrix, like :math:`A=LU` or :math:`A=QR`.
The new factorization is perfectly suited to computing powers, because 
**every time** :math:`X\im` **multiplies** :math:`X` **we get** :math:`I`:

**Powers of** :math:`A`:

.. math::

    A^k\u_0=(X\Ld X\im)\cds(X\Ld X\im)\u_0=X\Ld^kX\im\u_0.

I will split :math:`X\Ld^kX\im\u_0` into three steps that show how eigenvalues work:

#. Write :math:`\u_0` as a combination :math:`c_1\x_1+\cds+n_n\x_n` of the eigenvectors.
   Then :math:`\bs{c}=X\im\u_0`.

#. Multiply each eigenvector :math:`\x_i` by :math:`(\ld_i)^k`.
   Now we have :math:`\Ld^kX\im\u_0`.

#. Add up the pieces :math:`c_i(\ld_i)^k\x_i` to find the solution :math:`\u_kA^k\u_0`.
   This is :math:`X\Ld^kX\im\u_0`.

.. note::

    **Solution for** :math:`\u_{k+1}=A\u_k`: :math:`\u_k=A^k\u_0=c_1(\ld_1)^k\x_1+\cds+c_n(\ld_n)^k\x_n`.

In matrix language :math:`A^k` equals :math:`(X\Ld X\im)^k` which is :math:`X` times :math:`\Ld^k` times :math:`X\im`.
In Step 1, the eigenvectors in :math:`X` lead to the :math:`c`'s in the combination :math:`\u_0=c_1\x_1+\cds+c_n\x_n`:

**Step 1**: :math:`\u_0=\bb \\\ \x_1&\cds&\x_n\\\ \eb\bb c_1\\\vds\\c_n \eb`.
This says that :math:`\u_0=X\bs{c}`.

The coefficients in Step 1 are :math:`\bs{c}=X\im\u_0`.
Then Step 2 multiplies by :math:`\Ld^k`.
The final result :math:`\u_k=\sum c_i(\ld_i)^k\x_i` in Step 3 is the product of 
:math:`X` and :math:`\Ld^k` and :math:`X\im\u_0`:

.. math::

    A^k\u_0=X\Ld^kX\im\u_0=X\Ld^k\bs{c}=\bb \\\ \x_1&\cds&\x_n \\\ \eb
    \bb (\ld_1)^k\\&\dds\\&&(\ld_n)^k \eb\bb c_1\\\vds\\c_n \eb.

The result is exactly :math:`\u_k=c_1(\ld_1)^k\x_1+\cds+c_n(\ld_n)^k\x_n`.
It solves :math:`\u_{k+1}=A\u_k`.

Nondiagonalizable Matrices (Optional)
-------------------------------------

Suppose :math:`\ld` is an eigenvalue of :math:`A`.
We discover that fact in two ways:

**1. Eigenvectors** (geometric): There are nonzero solutions to :math:`A\x=\ld\x`.

**2. Eigenvalues** (algebraic): The determinant of :math:`A-\ld I` is zero.

The number :math:`\ld` may be a simple eigenvalue or a multiple eigenvalue, and we want to know its **multiplicity**.
Most eigenvalues have multiplicity :math:`M=1` (simple eigenvalues).
Then there is a single line of eigenvectors, and :math:`\det(A-\ld I)` does not have a double factor.

For exceptional matrices, an eigenvalue can be **repeated**.
Then there are two different ways to count its multiplicity.
Always GM :math:`\leq` AM for each :math:`\ld`:

#. (Geometric Multiplicity = GM): Count the **independent eigenvectors** for :math:`\ld`.
   The GM is the dimension of the nullspace of :math:`A-\ld I`.

#. (Algebraic Multiplicity = AM): AM counts the **repetitions of** :math:`\ld` among the eigenvalues.
   Look at the :math:`n` roots of :math:`\det(A-\ld I)=0`.

If :math:`A` has :math:`\ld=4,4,4`, then that eigenvalue has AM = 3 and GM = 1, 2, or 3.

**The shortage of eigenvectors when** GM **is below** AM **means that** :math:`A` **is not diagonalizable**.

----

**If** :math:`A` **is** :math:`m` **by** :math:`n` **and** :math:`B` **is** 
:math:`n` **by** :math:`m`, **then** :math:`AB` **and** :math:`BA` 
**have same nonzero eigenvalues**.

**Proof**: Start with this identity between square matrices (easily checked).
The first and third matrices are inverses.
The "size matrix" shows the shapes of all blocks.

.. math::

    \bb I&-A\\0&I \eb\bb AB&0\\B&0 \eb\bb I&A\\0&I \eb=\bb 0&0\\B&BA \eb\quad
    \bb m \times m&m \times n\\n \times m&n \times n \eb

This equation :math:`D\im ED=F` says :math:`F` **is similar to** :math:`E`--they have the same :math:`m+n` eigenvalues.

    :math:`E=\bb AB&0\\B&0 \eb` has the :math:`m` eigenvalues of :math:`AB`, plus :math:`n` zeros

    :math:`F=\bb 0&0\\B&BA \eb` has the :math:`n` eigenvalues of :math:`BA`, plus :math:`m` zeros

So :math:`AB` and :math:`BA` have the **same eigenvalues** except for :math:`|n-m|` zeros.