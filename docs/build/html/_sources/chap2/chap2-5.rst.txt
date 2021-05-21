Chapter 2.5 Inverse Matrices
============================

Suppose :math:`A` is a square matrix. 
We look for an "**inverse matrix**" :math:`A^{-1}` of the same size, such that 
:math:`A^{-1}` *times* :math:`A` *equals* :math:`I`.
*But* :math:`A^{-1}` *might not exist*.

.. note::

    **DEFINITION**: The matrix :math:`A` is **invertible** if there exists a 
    matrix :math:`A^{-1}` that "inverts" :math:`A`:

    * **Two-sided inverse**: :math:`A^{-1}A = I` and :math:`AA^{-1} = I`.

**Not all matrices have inverses**:

* **Note 1**: The inverse exists if and onlyu if elimination produces :math:`n` pivots (row exchanges are allowed).

* **Note 2**: The matrix :math:`A` cannot have two different inverses.
  Suppose :math:`BA=I` and also :math:`AC=I`.
  Then :math:`B =C`:

  .. math::
  
    B(AC) = (BA)C\ \mathrm{gives}\ BI=IC\ \mathrm{or}\ B=C.

  This shows that a *left-inverse* :math:`B` and a *right-inverse* :math:`C` must be the *same matrix*.

* **Note 3**: If :math:`A` is invertible, the one and only solution to :math:`A\x=\b` is :math:`\x=A^{-1}\b`:

.. note::

    **Multiply** :math:`A\x=\b` **by** :math:`A^{-1}`. **Then** :math:`\x = A^{-1}A\x = A^{-1}\b`.

* **Note 4**: **Suppose there is a nonzero vector** :math:`\x` **such that** :math:`A\x = \bs{0}`.
  *Then* :math:`A` *connot have an inverse*.
  no matrix can bring :math:`\bs{0}` back to :math:`\x`.

.. Tip::

    If :math:`A` is invertible, then :math:`A\x=\bs{0}` can only have the zero solution :math:`\x=A^{-1}\bs{0}=\bs{0}`.

The Inverse of a Product :math:`AB`
-----------------------------------

Calculating :math:`A^{-1}` by Gauss-Jordan Elimination
------------------------------------------------------

Singular versus Invertible
--------------------------

Recognizing an Invertible Matrix
--------------------------------