Chapter 6.1 Introduction to Eigenvalues
=======================================

The key idea is to avoid all the complications presented by the matrix :math:`A`.
Suppose the solution vector :math:`\u(t)` stays in the direction of a fixed vctor :math:`\x`.
Then we only need to find the number (changing with time) that muiltiplies :math:`\x`.
A number is easier than a vector.
**We want "eigenvectors"** :math:`\x` **that don't change direction when you multiply by** :math:`A`.

Almost all vectors change direction, when they are multiplied by :math:`A`.
**Certain exceptional vectors** :math:`\x` **are in the same direction as** :math:`A\x`.
**Those are the "eigenvectors"**.
multiply an eigenvector by :math:`A`, and the vector :math:`A\x` is a number :math:`\ld` times the original :math:`\x`.

.. tip::

    **The basic equation is** :math:`A\x=\ld\x`.
    **The number** :math:`\ld` **is an eigenvalue of** :math:`A`.

The eigenvalue :math:`\ld` tells whether the special vector :math:`\x` is 
stretched or shrunk or reversed or left unchanged--when it is multiplied by 
:math:`A`.
The eigenvalue :math:`\ld` could be zero.
Then :math:`A\x=0\x` means that this eigenvector :math:`\x` is in the nullspace.

If :math:`A` is the identity matrix, every vector has :math:`A\x=\x`.
All vectors are eigenvectors of :math:`I`.
All eigenvalues "lambda" are :math:`\ld=1`.
Most 2 by 2 matrices have *two* eigenvector directions and *two* eigenvalues.
We will show that :math:`\det(A-\ld I)=0`.

The matrix :math:`A=\bb .8&.3\\.2&.7 \eb` has two eigenvalues :math:`\ld=2` and :math:`\ld=1/2`.
The eigenvectors :math:`\x_1=(.6,.4)` and :math:`\x_2=(1.-1)` are in the 
nullspaces of :math:`A-I` and :math:`A-\frac{1}{2}I`.

If :math:`\x_1` is multiplied again by :math:`A`, we still get :math:`\x_1`.
Every power of :math:`A` will give :math:`A^n\x_1=\x_1`.
Multiplying :math:`\x_2` by :math:`A` gave :math:`\frac{1}{2}\x_2`, and if we
multiply again we get :math:`(\frac{1}{2})^2` times :math:`\x_2`.

.. tip::

    **When** :math:`A` **is squared, the eigenvectors stay the same**.
    **The eigenvalues are squared**.

**Separate into eigenvectors then multiply by** :math:`A`:

.. math::

    \bb .8\\.2 \eb=\x_1+(.2)\x_2=\bb .6\\.4 \eb+\bb .2\\-.2 \eb.

When we multiply separately for :math:`\x_1` and :math:`(.2)\x_2`, :math:`A` 
multiplies :math:`\x_2` by its eigenvalue :math:`\frac{1}{2}`

**Multiply each** :math:`\x_i` **by** :math:`\ld_i`:

.. math::

    A\bb .8\\.2 \eb\rm{ \ is\ }\x_1+\frac{1}{2}(.2)\x_2=\bb .6\\.4 \eb+\bb .1\\-.1 \eb=\bb .7\\.3 \eb.

**Each eigenvector is multiplied by its eigenvalue**, when we multiply by :math:`A`.

.. math::

    A^{99}\bb .8\\.2 \eb\rm{\ is\ really\ }\x_1+(.2)(\frac{1}{2})^{99}\x_2=
    \bb .6\\.4 \eb+\bb \rm{very}\\\rm{small}\\\rm{vector} \eb.

The eigenvector :math:`\x_1` is a "steady state" that doesn't change (because :math:`\ld_1=1`).
The eigenvector :math:`\x_2` is a "decaying mode" that virtually disappears (because :math:`\ld_2=.5`).
The higher the power of :math:`A`, the more closely its columns approach the steady state.

The particular :math:`A` is a **Markov matrix**.
Its largest eigenvalue is :math:`\ld=1`.
Its eigenvector :math:`\x_1=(.6,.4)` is the *steady state*--which all columns of :math:`A^k` will approach.

**For projection matrices** :math:`P`, we can see when :math:`P\x` is parallel to :math:`\x`.
The eigenvectors for :math:`\ld=1` and :math:`\ld=0` fill the column space and nullspace.
The column space doesn't move (:math:`P\x=\x`).
The nullspace goes to zero (:math:`P\x=0\x`).

.. note::

    **The projection matrix** :math:`P=\bb .5&.5\\.5&.5 \eb` has eigenvalues :math:`\ld=1` and :math:`\ld=0`.

Its eigenvectors are :math:`\x_1=(1,1)` and :math:`\x_2=(1,-1)`.
For those vectors, :math:`P\x_1=\x_1` (steady state) and :math:`P\x_2=\0` (nullspace).
This example illustrates mrkov matrices and singular matrices and (most important) symmetric matrices.
All have special :math:`\ld`'s and :math:`\x`'s:

#. **Markov matrix**: Each column of :math:`P` adds to 1, so :math:`\ld=1` is an eigenvalue.

#. :math:`P` is **singular**, so :math:`\ld=0` is an eigenvalue.

#. :math:`P` is **symmetric**, so its eigenvectors :math:`(1,1)` and :math:`(1,-1)` are perpendicular.

The only eigenvalues of a projection matrix are 0 and 1.
The eigenvectors for :math:`\ld=0` (which means :math:`P\x=0\x`) fill up the nullspace.
The eigenvectors for :math:`\ld=1` (which means :math:`P\x=\x`) fill up the column space.
The nullspace is projected to zero.
The column space projects onto itself.
The projection keeps the column space and destroys the nullspace:

    **Project each part** :math:`\v=\bb 1\\-1 \eb+\bb 2\\2 \eb` **projects onto** :math:`P\v=\bb 0\\0 \eb+\bb 2\\2 \eb`.

Projections have :math:`\ld=0` and :math:`1`.
Permutations have all :math:`|\ld|=1`.
The next matrix :math:`R` is a reflection an at the same time a permutation.
:math:`R` also has special eigenvalues.

.. note::

    **The reflection matrix** :math:`R=\bb 0&1\\1&0 \eb` **has eigenvalues 1 and -1**.

The eigenvector :math:`(1,1)` is unchanged by :math:`R`.
The second eigenvector is :math:`(1,-1)`--its signs are reversede by :math:`R`.
A matrix with no negative entries can still have a negative eigenvalue.
The eigenvectors for :math:`R` are the same as for :math:`P`, because :math:`reflection=2(projection)-I`:

:math:`R=2P-I`:

.. math::

    \bb 0&1\\1&0 \eb=2\bb .5&.5\\.5&.5 \eb-\bb 1&0\\0&1 \eb.

**When a matrix is shifted by** :math:`I`, **each** :math:`\ld` **is shifted by 1**.
No change in eigenvectors.

The Equation for the Eigenvalues
--------------------------------

For projection matrices we found :math:`\ld`'s and :math:`\x`'s by geometry: :math:`P\x=\x` and :math:`P\x=\0`.
For other matrices we use determinants and linear algebra.

**First move** :math:`\ld\x` **to the left side**.
Write the equation :math:`A\x=\ld\x` as :math:`(A-\ld I)\x=\0`.
The matrix :math:`A-\ld I` times the eigenvector :math:`\x` is the zero vector.
**The eigenvectors make up the nullspace of** :math:`A-\ld I`.
When we know an eigenvalue :math:`\ld`, we find an eigenvector by solving :math:`(A-\ld I)\x-\0`.

If :math:`(A-\ld I)\x=\0` has a nonzero solution, :math:`A-\ld I` is not invertible.
**The determinant of** :math:`A\ld I` **must be zero**.
This is how to recognize an eigenvalue :math:`\ld`:

.. note::

    **Eigenvalues**: The number :math:`\ld` is an eigenvalue of :math:`A` if and only if :math:`A-\ld I` is singular.

    * **Equation for the eigenvalues**: :math:`\det (A-\ld I)=0`.

This "*characteristic polynomial*" :math:`\det(A-\ld I)` involves only :math:`\ld`, not :math:`\x`.
When :math:`A` is :math:`n` by :math:`n`, :math:`\det(A-\ld I)` has degree :math:`n`.
Then :math:`A` has :math:`n` eigenvalues (repeats possible).
Each :math:`\ld` leads to :math:`\x`:

.. note::

    **For each eigenvalue** :math:`\ld` **solve** :math:`(A-\ld I)\x=\0` or 
    :math:`A\x=\ld\x` **to find an eigenvector** :math:`\x`.

**Summary**: To solve the eigenvalue problem for an :math:`n` by :math:`n` matrix, follow these steps:

.. note::

    **1. Compute the determinant of** :math:`A-\ld I`.
    With :math:`\ld` subtracted along the diagonal, this determinant starts with :math:`\ld^n` or :math:`-\ld^n`.
    It is a polynomial in :math:`\ld` of degree :math:`n`.

    **2. Find the roots of this polynomial**, by solving :math:`\det(A-\ld I)=0`.
    The :math:`n` roots are the :math:`n` eigenvalues of :math:`A`2.
    They make :math:`A-\ld I` singular.

    **3.** For each eigenvalue :math:`\ld`, **solve** :math:`(A-\ld I)\x=\0` **to find an eigenvector** :math:`\x`.

A note on the eigenvectors of 2 by 2 matrices.
When :math:`A-\ld I` is singular, both rows are multiples of a vector :math:`(a,b)`.
*The eigenvector is any multiple of* :math:`(b,-a)`.
There is a whole *line of eigenvectors*--any nonzero multiple of :math:`\x` is as good as :math:`\x`.

Some 2 by 2 matrices have only *one* line of eigenvectors.
This can only happen when two eigenvalues are equal.
(On the other hand :math:`A=I` has equal eigenvalues and plenty of eigenvectors.)
Without a full set of eigenvectors, we don't have a basis.
We can't write every :math:`\v` as a combination of eigenvectors.

Determinant and Trace
---------------------

*Elimination does not preserve the* :math:`\ld`'s.
The triangular :math:`U` has *its* eigenvalues sitting along the diagonal--they are the pivots.
But they are not the eigenvalues of :math:`A`!

The *product* :math:`\ld_1` *times* :math:`\ld_2` *and the sum* 
:math:`\ld_1+\ld_2` *can be found quickly from the matrix*.

.. note::

    **The product of the** :math:`n` **eigenvalues equals the determinant**.
    **The sum of the** :math:`n` **eigenvalues equals the sum of the** :math:`n` **diagonal entries**.

The sum of the entries along the main diagonal is called the **trace** of :math:`A`:

.. note::

    :math:`\ld_1+\ld_2+\cds+\ld_n=\bs{trace}=a_{11}+a_{22}+\cds+a_{nn}`.

.. tip::

    **Why do the eigenvalues of a triangular matrix lie along its diagonal?**

Imaginary Eigenvalues
---------------------

The eigenvalues might not be real numbers.

.. note::

    **The** :math:`90^{\circ}` **rotation** :math:`Q=\bb 0&-1\\1&0 \eb` **has no real eigenvectors**.
    **Its eigenvalues are** :math:`\ld_1=i` **and** :math:`\ld_2=-i`.
    Then :math:`\ld_1+\ld_2=trace=0` and :math:`\ld_1\ld_2=determinant=1`.

After a rotation, *no real vector* :math:`Q\x` *stays in the same direection as* :math:`\x` (:math:`\x=\0` is useless).
There cannot be an eigenvector, unless we go to **imaginary numbers**.

To see how :math:`i=\sqrt{-1}` can help, look at :math:`Q^2` which is :math:`-I`.
If :math:`Q` is rotation through :math:`90^{\circ}`, then :math:`Q^2` is rotation through :math:`180^{\circ}`.
Its eigenvalues are -1 and 1.
(Certainly :math:`-I\x=1\x`.)
Squaring :math:`Q` will square each :math:`\ld`, so we must have :math:`\ld^2=-1`.
*The eigenvalues of the* :math:`90^\circ` *rotation matrix* :math:`Q` *are* 
:math:`+i` *and* :math:`-1`, because :math:`i^2=-1`.

Those :math:`\ld`'s come as usual from :math:`\det(Q-\ld I)=0`.
This equation gives :math:`\ld^2+1=0`.
Its root are :math:`i` and :math:`-i`.
We meet the imaginary number :math:`i` also in the eigenvectors:

**Complex eigenvectors**:

.. math::

    \bb 0&-1\\1&0 \eb\bb 1\\i \eb=-i\bb 1\\i \eb\quad\rm{and}\quad\bb 0&-1\\1&0 \eb\bb i\\1 \eb=i\bb i\\1 \eb.

Somehow these complelx vectors :math:`\x_1=(1,i)` and :math:`\x_2=(i,1)` keep their direction as they are rotated.
The particualr eigenvalues :math:`i` and :math:`-i` also illustrate two special properties of :math:`Q`:

    #. :math:`Q` is an orthogonal matrix so the absolute value of each :math:`\ld` is :math:`|\ld|=1`.

    #. :math:`Q` is a skew-symmetric matrix so each :math:`\ld` is pure imaginary.

A symmetric matrix (:math:`S^T=S`) can be compared to a real number.
A skew-symmetric matrix (:math:`A^T=-A`) can be compared to an imaginary number.
An orthogonal matrix matrix (:math:`Q^TQ=I`) corresponds to a complex number with :math:`|\ld=1|`.
For the eigenvalues of :math:`S` and :math:`A` and :math:`Q`, those are more than analogies.

The eigenvectors for all these special matrices are perpendicular.

Eigenvalues of :math:`AB` and :math:`A+B`
-----------------------------------------

.. note::

    :math:`A` and :math:`B` share the same :math:`n` *independent* eigenvectors if and only if :math:`AB=BA`.

**Heisenberg's uncertainty principle**: In quantum mechancis, the position 
matrix :math:`P` and the momemtum matrix :math:`Q` do not commute.
In fact :math:`QP-PQ=I` (these are infinite matrices).