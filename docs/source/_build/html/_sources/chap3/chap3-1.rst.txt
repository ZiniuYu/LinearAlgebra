Chapter 3.1 Spaces of Vectors
=============================

The vector spaces are denoted by :math:`\R^1, \R^2, \R^3, \cds`.
Each space :math:`\R^n` consists of a whole collection of vectors.

.. Note::

    **DEFINITION**: The space :math:`\R^n` consists of all column vectors :math:`\v` with :math:`n` components.

The components of :math:`\v` are real numbers, which is the reason for the letter :math:`\R`.
A vector whose :math:`n` components are complex numebrs lies in the space :math:`\bs{\rm{C}}^n`.

The vector space :math:`\R^2` is represented by the usual :math:`xy` plane.
Each vector :math:`\v` in :math:`\R^2` has two components that give the 
:math:`x` and :math:`y` coordinates of a point in the plane :math:`\v=(x,y)`.

The vectors in :math:`\R^3` correspond to points :math:`(x,y,z)` in three-dimensional space.
The one-dimensional space :math:`\R^1` is a line (like the :math:`x` axis).

The two essential vector operations go on *inside the vector space*, and they produce **linear combinations**:

.. Tip::

    We can add any vectors in :math:`\R^n`, and we can multiply any vector :math:`\v` by any scalar :math:`c`.

"Inside the vector space" means that **the result stays in the space**.

*A real vector space is a set of "vectors" together with rules for vector addition and for multiplication by real numbers*.

.. note::

    * :math:`\bs{\rm{M}}`: The vector space of **all real 2 by 2 matrices**.

    * :math:`\bs{\rm{F}}`: The vector space of **all real functions** :math:`f(x)`.

    * :math:`\bs{\rm{Z}}`: The vector space that consists only of a **zero vector**.

The function space :math:`\bs{\rm{F}}` is infinite-dimensional.
A smaller function space is :math:`\bs{\rm{P}}`, or :math:`\bs{\rm{P}}_n`, 
containing all polynomials :math:`a_0 + a_1x + \cds + a_nx^n` of degree 
:math:`n`.

The spzce :math:`\bs{\rm{Z}}` is zero-dimensional.
:math:`\bs{\rm{Z}}` is the smallest possible vector space.
The vector space :math:`\bs{\rm{Z}}` contains exactly *one vector* (zero).
Each space has its own zero vector.

Subspaces
---------

.. note::

    **DEFINITION**: A **subspace** of a vector space is a set of vectors 
    (including :math:`\bs{0}`) that satisfies two requirements:
    **If** :math:`\v` **and** :math:`\w` **are in the subspace and** :math:`c` 
    **is any scalar, then**

    #. :math:`\v+\w` is in the subspace;
    #. :math:`c\v` is in the subspace.

In short, **all linear combinations stay in the subspace**.

**Every subspace contains the zero vector**.
Planes that don't contain the origin fail those tests.
Those planes are not subspaces.

**Lines through the origin are also subspaces**.
Another subspace is all of :math:`\R^3`.
The whole space is a subspace (*of itself*).

A list of all the possible subspace of :math:`\R^3`:

#. :math:`\bs{\rm{L}}`: Any line through :math:`(0,0,0)`
#. :math:`\bs{\rm{P}}`: Any plane through :math:`(0,0,0)`
#. :math:`\R^3`: The whole space
#. :math:`\bs{\rm{Z}}`: The single vector :math:`(0,0,0)`

**The quater-plane is not a subspace**.
**Two quarter-planes don't make a subspace**.

.. note::

    **A subspace containing** :math:`\v` **and** :math:`\w` **must contain all linear combinations** :math:`c\v+d\w`.

The Column Space of :math:`A`
-----------------------------

Start with the columns of :math:`A` and **take all their linear combinations**.
This produces the column space of :math:`A`.
**It is a vector space made up of column vectors**.

.. note::

    **DEFINITION**: The **column space** consists of **all linear combinations of the columns**
    The combinations are all possible vectors :math:`A\x`.
    They fill the column space :math:`\bs{C}(A)`.

**To solve** :math:`A\x=\b` **is to express** :math:`\b` **as a combination of the columns**.

.. note::

    **The system** :math:`A\x=\b` **is solvable if and only if** :math:`\b` **is in the column space of** :math:`A`.

Suppose :math:`A`is an :math:`m` by :math:`n` matrix.
Its columns have :math:`m` components.
So the columns belong to :math:`\R^m`.
**The column space of** :math:`A` **is a subspace of** :math:`\R^m`.

**Notation**: The column space of :math:`A` is denoted by :math:`\bs{C}(A)`.
Start with the columns and take all their linear combinations.
We might get the whole :math:`\R^m` or only a subspace.

**Important**: Instead of columns in :math:`\R^m`, we could start with any set 
:math:`\bs{\rm{S}}` of vectors in a vector space :math:`\bs{\rm{V}}`.
To get a *subspace** :math:`\bs{\rm{SS}}` of :math:`\bs{\rm{V}}`, we take
*all combinations* of the vectors in that set:

* :math:`\bs{\rm{S}}` = set of vectors in :math:`\bs{\rm{V}}` (probably not a subspace)

* :math:`\bs{\rm{SS}}` = all combinations of vectors in :math:`\bs{\rm{S}}` (definitely a subspace)

.. note::

    :math:`\bs{\rm{SS}}` = all :math:`c_1\v_1 + \cds + c_N\v_N` 
    = **the subspace of** :math:`\bs{\rm{V}}` "spanned" by :math:`\bs{\rm{S}}`

When :math:`\bs{\rm{S}}` is the set of columns, :math:`\bs{\rm{SS}}` is the column space.
When there is only one nonzero vector :math:`\v` in :math:`\bs{\rm{S}}`, the 
subsapce :math:`\bs{\rm{SS}}` is the line through :math:`\v`.
*Always* :math:`\bs{\rm{SS}}` *is the smallest subspace containing* :math:`\bs{\rm{S}}`.

The columns "span" the column space.

.. Tip::

    The subspace :math:`\bs{\rm{SS}}` is the "span" of :math:`\bs{\rm{S}}`, 
    containing all combinations of vectors in :math:`\bs{\rm{S}}`.