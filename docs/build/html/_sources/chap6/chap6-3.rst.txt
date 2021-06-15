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

For :math:`\dp\frac{d\u}{dt}=A\u=\bb 0&1\\1&0 \eb\u` starting from 
:math:`\u(0)=\bb 4\\2 \eb`, this is a vector equation for :math:`\u`.
It contains two scalar equations for the components :math:`y` and :math:`z`:

.. math::

    \frac{d\u}{dt}=A\u\quad\frac{d}{dt}\bb y\\z \eb=\bb 0&1\\1&0 \eb\bb y\\z \eb
    \rm{\ means\ that\ }\frac{dy}{dt}=z\rm{\ and\ }\frac{dz}{dt}=y.

The idea of eigenvectors is to combine those equations in a way that gets back to 1 by 1 problems.
The combinations :math:`y+z` and :math:`y-z` will do it.
Add and subtract equations:

.. math::

    \frac{d}{dt}(y+z)=z+y\quad\rm{and}\quad\frac{d}{dt}(y-z)=-(y-z).

The combination :math:`y+z` grows like :math:`e^t`, because it has :math:`\ld=1`.
The combination :math:`y-z` decays like :math:`e^{-1}`, because it has :math:`\ld=-1`.

This matrix :math:`A` has eigenvalues 1 and -1.
The eigenvectors :math:`\x` are :math:`(1,1)` and :math:`(1,-1)`.
The pure exponential solutions :math:`\u_1` and :math:`\u_2` take the form 
:math:`e^{\ld t}\x` with :math:`\ld_1=1` and :math:`\ld_2=-1`:

.. note::

    :math:`\u_1(t)=e^{\ld_1t}\x_1=e^t\bb 1\\1 \eb` and :math:`\u_2(t)=e^{\ld_2t}\x_2=e^{-t}\bb 1\\-1 \eb`.

Notice: These :math:`\u`'s satisfy :math:`A\u_1=\u_1` and :math:`A\u_2-\u_2`, just like :math:`\x_1` and :math:`\x_2`.
The factors :math:`e^t` and :math:`e^{-1}` change with time.
Those factors give :math:`d\u_1/dt=\u_1=A\u_1` and :math:`d\u_2/dt=-\u_2=A\u_2`.
**We have two solutions to** :math:`d\u/dt=A\u`.
To find all other solutions, **multiply those special solutions by any numbers** :math:`C` **and** :math:`D` **and add**:

**Complete solution**:

.. math::

    \u(t)=Ce^t\bb 1\\1 \eb+De^{-t}\bb 1\\-1 \eb=\bb Ce^t+De^{-t}\\Ce^t-De^{-t} \eb.

With these two constants :math:`C` and :math:`D`, we can match any starting vector :math:`\u(0)=(u_1(0),u_2(0))`.
Set :math:`t=0` and :math:`e^0=1`.
For :math:`\u(0)=(4,2)`:

:math:`\u(0)` **decides** :math:`C,D`:

.. math::

    C\bb 1\\1 \eb+D\bb 1\\-1 \eb= \bb 4\\2 \eb\quad\rm{yields}\quad C=3\rm{\ and\ }D=1.

The same three steps that solved :math:`\u_{k+1}=A\u_k` now solve :math:`d\u/dt=A\u`:

#. Wirte :math:`\u(00` as a **combination** :math:`c_1\x_1+\cds+c_n\x_n` **of the eigenvectors of** :math:`A`.

#. Multiply each eigenvector :math:`\x_i` by **its growth factor** :math:`e^{\ld_it}`.

#. The solution is the same combination of those pure solutions :math:`e^{\ld t}\x`:

    .. note::

        :math:`\u(t)=c_1e^{\ld_1t}\x_1+\cds+c_ne^{\ld_nt}\x_n`.

*Not included*: If two :math:`\ld`'s are equal, with only one eigenvector, another solution is needed.
(It will be :math:`te^{\ld t}\x`.
Step 1 needs to diagonalize :math:`A=X\Ld X\im`: a basis of :math:`n` eigenvectors.

Second Order Equations
----------------------

**The most important equation in meechanics is** :math:`my\ppr+by\pr+ky=0`.
This is a second-order equation because it contains the second derivative :math:`y\ppr=d^2y/dt^2`.
It is still linear with constant coefficients :math:`m,b,k`.

The method of solution is to substitute :math:`y=e^{\ld t}`.
Each derivative of :math:`y` brings down a factor :math:`\ld`.
We want :math:`y=e^{\ld t}` to solve the equation:

.. note::

    :math:`\dp m\frac{d^2y}{dt^2}+b\frac{dy}{dt}+ky=0` becomes :math:`(m\ld^2+b\ld+k)e^{\ld t}=0`.

Everything depends on :math:`m\ld^2+b\ld+k=0`.
This equation for :math:`\ld` has two roots :math:`\ld_1` and :math:`\ld_2`.
Then the equation for :math:`y` has two pure solutions :math:`y_1=e^{\ld_1t}` and :math:`y_2=e^{\ld_2t}`.
Their combinations :math:`c_1y_1+c_2y_2` give the complete solution unless :math:`\ld_1=\ld_2`.

We turn the scalar equation (with :math:`y\ppr`) into a *vector equation for* 
:math:`y` *and* :math:`y\pr`: first derivative only.
Suppose :math:`m=1`.
Two equations for :math:`\u=(y,y\pr)` give :math:`d\u/dt=A\u`:

.. math::

    \begin{matrix}dy/dt=y\pr\\dy\pr/dt=-ky-by\pr\end{matrix}\quad\rm{converts\ to}
    \quad\frac{d}{dt}\bb y\\y\pr \eb=\bb 0&1\\-k&-b \eb\bb y\\y\pr \eb=A\u.

The first equation :math:`dy/dt=y\pr` is trivial (but true).
The second is equation connecting :math:`y\ppr` to :math:`y\pr` and :math:`y`.
Together they connect :math:`\u\pr` to :math:`\u`.
So we solve :math:`\u\pr=A\u` by eigenvalues of :math:`A`:

.. note::

    :math:`A-\ld I=\bb -\ld&1\\-k&-b-\ld \eb` has determinant :math:`\ld^2+b\ld+k=0`.

**The euqation for the** :math:`\ld`'s **is still** :math:`\ld^2+b\ld+k=0`, **since** :math:`m=1`.
The roots :math:`\ld_1` and :math:`\ld_2` are now *eigenvalues of* :math:`A`.
The eigenvectors and the solution are:

.. math::

    \x_1=\bb 1\\\ld_1 \eb\quad\x_2=\bb 1\\\ld_2 \eb\quad\u(t)=c_1e^{\ld_1t}\bb 1\\\ld_1 \eb+c_2e^{\ld_2t}\bb 1\\ld_2 \eb.

The first component of :math:`\u(t)` has :math:`y=c_1e^{\ld_1t}+c_2e^{\ld_2t}`--the same solution as before.
The vector problem is completely consistent with the scalar problem.
The 2 by 2 matrix :math:`A` is called a *companion matrix*-- a companion to the second order equation with :math:`t\ppr`.


Difference Equations (optional)
-------------------------------









Stability of 2 by 2 Matrices
----------------------------









The Exponential of a Matrix
---------------------------









