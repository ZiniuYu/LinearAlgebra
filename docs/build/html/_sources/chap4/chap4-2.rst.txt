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
Call it :math:`\a`.l

Projection Onto a Line
----------------------





Projection Onto a Subspace
--------------------------