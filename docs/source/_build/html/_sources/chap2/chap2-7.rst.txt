Chapter 2.7 Transposes and Permutations
=======================================

The **transpose** of :math:`A` is denoted by :math:`A^T`.
The columns of :math:`A^T` are the rows of :math:`A`.
When :math:`A` is an :math:`m` by :math:`n` matrix, the transpose is :math:`n` by :math:`m`:

.. math::

    \mathrm{If\ }A=\bb 1&2&3\\0&0&4\eb\mathrm{\ then\ }A^T=\bb 1&0\\2&0\\3&4\eb.

.. note::

    **Exchange rows and columns**: :math:`(A^T)_{ij}=A_{ji}`.

The rules for transposes:

* **Sum**: :math:`(A+B)^T = A^T+B^T`

* **Product**: :math:`(AB)^T = B^TA^T`

* **Inverse**: :math:`(A^{-1})^T = (A^T)^{-1}`.

.. Tip::

    :math:`A\x` **combines the columns of** :math:`A` **while** :math:`\x^TA^T` **combines the rows of** :math:`A^T`.

Transposing :math:`AB=\bb A\x_1&A\x_2&\cds\eb` gives :math:`\bb\x_1^TA^T\\\x_2^TA^T\\\vdots\eb` which is :math:`B^TA^T`.

The reverse order rule extends to three or more factors: :math:`(ABC)^T=C^TB^TA^T`.

* **If** :math:`A=LDU` **then** :math:`A^T=U^TD^TL^T`. **The pivot matrix has** :math:`D=D^T`.

**Transpose of inverse**:

.. math::

    A\im A = I\ \mathrm{is\ transposed\ to\ } A^T(A\im)^T=I.

:math:`A^T` **is invertible exactly when** :math:`A` **is invertible**.

The Meaning of Inner Products
-----------------------------

The dot product :math:`\x\cd\bs{y}` is the sum of numbers :math:`x_iy_i`.
Use matrix notation instead:

* :math:`^T` **is inside**: The dot product or inner product is :math:`x^Ty\quad(1\times n)(n\times 1)`.

* :math:`^T` **is outside**: The rank one product or outer product is :math:`xy^T\quad(n\times 1)(1\times n)`.

:math:`\x^T\y` is a number, :math:`\x\y^T` is a matrix.

Examples where the inner product has meaning:

* **From mechanics**: Work = (Movements) (Forces) = :math:`\x^T\bs{f}`

* **From circuits**: Heat loss = (Voltage drops) (Currents) = :math:`e^T\y`

* **FRom economics**: Income = (Quantities) (Prices) = :math:`\bs{q}^T\bs{p}`

:math:`A^T` is the matrix that makes these two inner products equal for every :math:`\x` and :math:`\y`:

.. Tip::

    :math:`(A\x)^T\y = \x^T(A^T\y)` Inner product of :math:`A\x` with 
    :math:`\y =` Inner product of :math:`\x` with :math:`A^T\y`.

Symmetric Matrices
------------------

.. note::

    **DEFINITION**: A **symmetric matrix** has :math:`S^T=S`.
    This means that :math:`s_{ji}=s_{ij}`.

**The inverse of a symmetric matrix is also symmetric**.
The transpose of :math:`S\im` is :math:`(S\im)^T=(S^T)\im=S\im`.
That says :math:`S\im` is symmetric (when :math:`S` is invertible).

Symmetric Products :math:`A^TA` and :math:`AA^T` and :math:`LDL^T`
------------------------------------------------------------------

The product :math:`S=A^TA` is automatically a square symmetric matrx:

.. Tip::

    The transpose of :math:`A^TA` is :math:`A^T(A^T)^T` which is :math:`A^TA` again.

The :math:`(i,j)` entry of :math:`A^TA` is the dot product of row :math:`i` of 
:math:`A^T` (column :math:`i` of :math:`A`) with column :math:`j` of :math:`A`.
The :math:`(j,i)` entry is the same dot product, column :math:`j` with column :math:`i`.
So :math:`A^TA` is symmetric.

The product :math:`A^TA` is :math:`n` by :math:`n`.
:math:`AA^T` is :math:`m` by :math:`m`.
Both are sysmetric, with positive diagonal.
But even if :math:`m=n`, it is very likely that :math:`A^TA\neq AA^T`.

**Symmetric matrices in elimination**: the symmetry is in the triple product :math:`S=LDU`.

.. math::

    \bb 1&2\\2&7 \eb = \bb 1&0\\2&1 \eb \bb 1&2\\0&3 \eb

    \bb 1&2\\2&7 \eb = \bb 1&0\\2&1 \eb \bb 1&0\\0&3 \eb \bb 1&2\\0&1 \eb

.. note::

    If :math:`S=S^T` is factored into :math:`LDU` with no rwo exchanges, then :math:`U` is exactly :math:`L^T`.

.. Tip::

    The symmetric factorization of a symmetric matrix is :math:`S=LDL^T`.

Permutation Matrices
--------------------

The row exchanges :math:`P_{ij}` are constructed by exchanging two rows :math:`i` and :math:`j` of :math:`I`.

.. note::

    **DEFINITION**: A **permutation matrix** :math:`P` has the rows of the identity :math:`I` in any order.

There are :math:`n!` permutation matrices of order :math:`n`.
:math:`P\im` is also a permutation matrix.
:math:`P\im` is always the same as :math:`P^T`.

The :math:`PA=LU` Factorization with Row Exchanges
--------------------------------------------------

Sometimes row exchanges are needed to produce pivots.
Then :math:`A=(E\im \cds P\im \cds E\im \cds P\im \cds)U`.
Every row exchange is carried out by a :math:`P_{ij}` and inverted by that :math:`P_{ij}`.
We now compress those row exchanges into a *single permutation matrix* :math:`P`.

#. The row exchanges can be done *in advance*. 
   Their product :math:`P` puts the rows of :math:`A` in the right order, so
   that no exchanges are needed for :math:`PA`.
   **Then** :math:`\bs{PA=LU}`.

#. If we hold row exchanges until *after elimination*, the pivot rows are in a strange order.
   :math:`P_1` puts them in the correct triangular order in :math:`U_1`.
   **Then** :math:`\bs{A=L_1P_1U_1}`.

.. note::

    If :math:`A` is invertible, a permutation :math:`P` will put its rows inthe right order to factor :math:`PA=LU`.
    There must be a full set of pivots after row exchanges for :math:`A` to be invertible.

The Transpose of a Derivative
-----------------------------

**The matrix changes to a derivative so** :math:`\bs{A=d/dt}`.
The inner product changes from the sum of :math:`x_ky_k` to the *integral* of :math:`x(t)y(t)`.

.. note::

    **Inner product of functions**: :math:`\dp x^Ty=(x,y)=\int^{\infty}_{-\infty}x(t)y(t)\ dt`.

The word "adjoint" is more correct than "transpose" when we are working with derivatives.

The transpose of a matrix has :math:`(A\x)^T\y=\x^T(A^T\y)`.
The adjoint of :math:`A=\frac{d}{dt}` has

.. math::

    (Ax,y) = \int^{\infty}_{-\infty} \frac{dx}{dt}y(t)dt = 
    \int^{\infty}_{-\infty} x(t)\left( -\frac{dy}{dt} \right)dt = (x,A^Ty)

The dirivative moves from the first function :math:`x(t)` to the second function :math:`y(t)`.
During that move, a minus sign appears.
**The transpose of the derivative is minus the derivative**.

The derivative is *antisymmetric*: :math:`\bs{A=d/dt}` and :math:`\bs{A^T=-d/dt}`.
Symmetric matrices have :math:`S^T=S`, antisymmetric matrices have :math:`A^T=-A`.

This antisymmetry of the derivative applies also to centered difference matrices.

.. math::

    A = \bb 0&1&0&0\\-1&0&1&0\\0&-1&0&1\\0&0&-1&0 \eb\mathrm{\ transposes\ to\ }
    A^T=\bb 0&-1&0&0\\1&0&-1&0\\0&1&0&-1\\0&0&1&0 \eb = -A.

A forward difference matrix transposes to a backward difference matrix, *multiplied by* -1.
In differential equations, the second derivative (acceleration) is *symmetric*.
The first derivative (damping proportional to velocity) is *antisymmetric*.