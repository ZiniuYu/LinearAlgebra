Chapter 8.1 The Idea of a Linear Transformation
===============================================

.. note::

    A **transformation** :math:`T` assigns an output :math:`T(\v)` to each input vector :math:`\v` in :math:`\bs{V}`.
    The transformation is **linear** if it meets these requirements for all :math:`\v` and :math:`\w`:

    * :math:`T(\v+\w)=T(\v)+T(\w)`.

    * :math:`T(c\v)=cT(\v)` for all :math:`c`.

If the input is :math:`\v=\0`, the output must be :math:`T(\v)=\0`.

.. note::

    **Linear transformation**: :math:`T(c\v+d\w)` **must equal** :math:`cT(\v)+dT(\w)`.

**Shift is not linear**:

.. math::

    \v+\w+\u_0\quad\rm{is\ not}\quad T(\v)+T(\w)=(\v+\u_0)+(\w+\u_0).

The exception is when :math:`\u_0=\0`.
The transformation reduces to :math:`T(\v)=\v`.
This is the **identity transformation**.

The linear-plus-shift transformation :math:`T(\v)=A\v+\u_0` is called "*affine*".

Lines to Lines, Triangles to Triangles, Basis Tells All
-------------------------------------------------------

Linearity: **Equally spaced points go to equally spaced poitns**.

.. note::

    **Linearity**: :math:`\u=c_1\v_1+c_2\v_2+\cds+c_n\v_n` **must transform to**
    :math:`T(\u)=c_1T(\v_1)+c_2T(\v_2)+\cds+c_nT(\v_n)`.

.. note::

    **Suppose you know** :math:`T(\v)` **for all vectors** :math:`\v_1,\cds,\v_n` 
    **in a basis, then you know** :math:`T(\u)` **for every vector** :math:`\u`
    **in the space**.



Examples of Transformations (mostly linear)
-------------------------------------------








Linear Transformations of the Plane
-----------------------------------