Chapter 6.3 Systems of Differential Equations
=============================================

*The derivative of* :math:`e^{\ld t}` *is* :math:`\ld e^{\ld t}`.
The whole point of the section is this: **To convert constant-coefficient differential equations into linear algebra**.

The ordinary equations :math:`\dp\frac{du}{dt}=u` and :math:`\dp\frac{du}{dt}=\ld u` are solved by exponentials:

.. math::

    \frac{du}{dt}=u\rm{\ produces\ }u(t)=Ce^t\quad\frac{du}{dt}=\ld u\rm{\ produces\ }u(t)=Ce^{\ld t}.

At time :math:`t=0` those solutions include :math:`e^0=1`.
So they both reduce to :math:`u(0)=C`.
This "initial value" tells us the right choice for :math:`C`.
**The solutions that start from the number** :math:`u(0)` **at time** 
:math:`t=0` **are** :math:`u(t)=u(0)e^t` **and** :math:`u(t)=u(0)e^{\ld t}`.

Linear algebra moves from 1 by 1 problems to :math:`n` by :math:`n`.
The unknown is a vector :math:`\u`.
It starts from the initial vector :math:`\u(0)`, which is given.
The :math:`n` equations contain a square matrix :math:`A`.
We expect :math:`n` exponents :math:`e^{\ld t}` in :math:`\u(t)`, from :math:`n\ \ld`'s:

.. note::

    **System of** :math:`n` **equations**: :math:`\dp\frac{d\u}{dt}=A\u` 
    starting from the vector :math:`\u(0)=\bb u_1(0)\\\vds\\u_n(0) \eb` at
    :math:`t=0`.

These differential equations are *linear*.
If :math:`\u(t)` and :math:`\v(t)` are solutions, so is :math:`C\u(t)+D\v(t)`.
We will need :math:`n` constants like :math:`C` and :math:`D` to match the :math:`n` components of :math:`\u(0)`.
Our first job is to find :math:`n` "pure exponential solutions" :math:`\u=e^{\ld t}\x` by using :math:`A\x=\ld\x`.

Notice that :math:`A` is a *constant* matrix.
In other linear equations, :math:`A` changes as :math:`t` changes.
In nonlinear equations, :math:`A` changes as :math:`\u` changes.
:math:`d\u/dt=A\u` is "linear with constant coefficients".

.. tip::

    **Solve linear constant coefficient equations by exponentials** :math:`e^{\ld t}\x`, **when** :math:`A\x=\ld\x`.

Solution of :math:`d\boldsymbol{u}/dt=A\boldsymbol{u}`
------------------------------------------------------

Our pure exponential solution will be :math:`e^{\ld t}` times a fixed vector :math:`\x`.
:math:`\ld` is an eigenvalue of :math:`A` and :math:`\x` **is the eigenvector**.
Substitute :math:`\u(t)=e^{\ld t}\x` into the equation :math:`d\u/dt=A\u`, and
the factor :math:`e^{\ld t}` will cancel to leave :math:`\ld\x=A\x`:

.. note::

    **Choose** :math:`\u=e^{\ld t}\x` **when** :math:`A\x=\ld\x`:

    * :math:`\dp\frac{d\u}{dt}=\ld e^{\ld t}\x` agrees with :math:`A\u=Ae^{\ld t}\x`.

All components of this special solution :math:`\u=e^{\ld t}\x` share the same :math:`e^{\ld t}`.
The solution grows when :math:`\ld>0`.
It decays when :math:`\ld<0`.
If :math:`\ld` is a complex number, its real part decides growth or decay.
The imaginary part :math:`\omega` gives oscillation :math:`e^{i\omega t}` like a sine wave.








Second Order Equations
----------------------









Difference Equations (optional)
-------------------------------









Stability of 2 by 2 Matrices
----------------------------









The Exponential of a Matrix
---------------------------









