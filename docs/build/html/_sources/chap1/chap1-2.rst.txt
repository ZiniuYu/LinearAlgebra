Chapter 1.2 Lengths and Dot Products
====================================

.. note::

    The **dot product** or **inner product** of :math:`\v = (v_1, v_2)` and 
    :math:`\w = (w_1, w_2)` is the number :math:`\v\cd\w`:
    
    * :math:`\v\cd\w = v_1w_1 + v_2w_2`.

The dot product of **perpendicular vectors** is **zero**.

.. tip::

    The dot product :math:`\w\cd\v` equals :math:`\v\cd\w`.
    The order of :math:`\v` and :math:`\w` makes no difference.

**Main point:** For :math:`\v\cd\w`, multiply each :math:`v_i` times :math:`w_i`.
Then :math:`\v\cd\w = v_1w_1 + \cds + v_nw_n`.

Lengths and Unit Vectors
------------------------

.. note:: 

    **DEFINITION**: The **length** :math:`\lv\v\rv` of a vector :math:`\v` is the
    square root of :math:`\v\cd\v`:
    
    * **length** :math:`=\lv\v\rv=\sqrt{\v\cd\v} = (v_1^2 + v_2^2 + \cds + v_n^2)^{1/2}`.

.. note:: 

    **DEFINITION**: A unit vector :math:`\u` is a vector whose length equals one.
    Then :math:`\u\cd\u = \bs{1}`.

The standard unit vectors along the *x* and *y* axes are written :math:`\i` and
:math:`\j`.

For a unit vector, **divide any nonzero vector** :math:`\v` **by its length**
:math:`\lv\v\rv`.

.. note::

    **Unit vector:** :math:`\u = \v/\lv\v\rv` is a unit vector in the same
    direction as :math:`\v`.

The Angle Between Two Vectors
-----------------------------

.. note::

    **Right angles:** The dot product is :math:`\v\cd\w = 0` when :math:`\v` is
    perpendicular to :math:`\w`.

**Proof:** When :math:`\v` and :math:`\w` are perpendicular, they form two sides
of a right triangle. The third side is :math:`\v - \w`. The *Pythagoras Law* for
the sides of a right triangle is :math:`a^2 + b^2 = c^2`.

    **Perpendicular vectors**:
    :math:`\lv\v\rv^2 + \lv\w\rv^2 = \lv\v - \w\rv^2`

    Writing out the formulars for those lengths in two dimensions, this equation
    is Pythagoras:
    
    .. math::
        
        (v_1^2 + v_2^2) + (w_1^2 + w_2^2) &= (v_1 - w_1)^2 + (v_2 - w_2)^2 \\
        0 &= -2v_1w_1 - 2v_2w_2

    which leads to :math:`\v_1\w_1 + \v_2\w_2 = \bs{0}`.

    **Conclusion**: Right angles produce :math:`\v\cd\w = 0`. The dot product is
    zero when the angle is :math:`\theta = 90^\circ`. Then :math:`\cos\theta = 0`.
    The zero vector :math:`\v = \bs{0}` is perpendicular to every vector 
    :math:`\v` because :math:`\bs{0}\cd\w` is always zero.

The angle between :math:`\v` and :math:`\w` is

* less than :math:`90^\circ` when :math:`\v\cd\w` is positive.
* greater than :math:`90^\circ` when :math:`\v\cd\w` is negative.

.. note::

    Unit vector :math:`\u` and :math:`\bs{U}` at angle :math:`\theta` have
    :math:`\u\cd\bs{U} = \cos\theta`. Certainly :math:`|\u\cd\bs{U}| \leq 1`.

*The dot product of unit vectors is between* -1 *and* 1. The cosine of
:math:`\theta` is revealed by :math:`\u\cd\bs{U}`.

When the vectors are :math:`\u = (\cos\alpha, \sin\alpha)` and 
:math:`\bs{U} = (1, 0)`, the dot product is :math:`\u\cd\bs{U} = \cos\theta`.
That is the cosine of the angle between them.

After rotation through any angle :math:`\alpha`, these are still unit vectors.
The vector :math:`\bs{U}` rotates to :math:`(\cos\alpha, \sin\alpha)`. The
vector :math:`\u` rotates to :math:`(\cos\beta, \sin\beta)` with
:math:`\beta = \alpha + \theta`. Their dot product is 
:math:`\cos\alpha\cos\beta + \sin\alpha\sin\beta = \cos(\beta-\alpha) = \cos\theta`.

.. note::

    **COSINE FORMULA**: If :math:`\v` and :math:`\w` are nonzero vectors Then
    :math:`\dp\frac{\v\cd\w}{\lv\v\rv\lv\w\rv} = \cos\theta`

Since :math:`\cos\theta` never exceeds 1, the cosine formula gives two great
inequalities:

.. note::

    **SCHWARZ INEQUALITY**: :math:`|\v\cd\w| \leq \lv\v\rv\lv\w\rv`

    **TRIANGLE INEQUALITY**: :math:`\lv\v+\w\rv \leq \lv\v\rv + \lv\w\rv`

.. tip::

    **Geometric mean** :math:`\leq` **Arithmetic mean**

    :math:`\dp ab \leq \frac{a^2 + b^2}{2}`,
    :math:`\dp \sqrt{xy} \leq \frac{x + y}{2}`

Notes on Computing
------------------