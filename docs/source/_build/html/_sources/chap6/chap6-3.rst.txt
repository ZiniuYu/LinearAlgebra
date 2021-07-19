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

To display a circle on a screen, replace :math:`y\ppr=-y` by a **difference equation**.
Here are three choices using :math:`Y(t+\Delta t)-2Y(t)+Y(t+\Delta t)`.
Divide by :math:`(\Delta t)^2` to approximate :math:`y\ppr`.

.. note::

    :math:`\dp\begin{matrix}F\\C\\B\end{matrix}\quad
    \begin{matrix}\rm{Forward\ from\ }n-1\ \ \\\rm{Centered\ at\ time\ }n\quad\
    \\\rm{Backward\ from\ }n+1\end{matrix}\quad
    \frac{Y_{n+1}-2Y_n+Y_{n-1}}{(\Delta t)^2}=
    \begin{matrix}Y_{n-1}\\Y_n\ \ \ \ \\Y_{n+1}\end{matrix}`

The three difference methods *don't* complete a perfect circle in 32 time steps of length :math:`\Delta t=2\pi/32`.
Those pictures will be explained by eigenvalues:

**Forward** :math:`|\ld|>1` (**spiral out**)
**Centered** :math:`|\ld|=1` (**best**)
**Backward** :math:`|\ld|<1` (**spiral in**)

The 2-step equations reduce to 1-step systems :math:`\bs{U}_{n+1}=A\bs{U}_n`.
Instead of :math:`\u=(y,y\pr)` the discrete unknown is :math:`\bs{U}_n=(Y_n,Z_n)`.
We take :math:`n` time steps :math:`\Delta t` starting from :math:`\bs{U}_0`:

.. note::

    **Forward**: :math:`\begin{matrix}Y_{n+1}=Y_n+\Delta tZ_n\\
    Z_{n+1}=Z_n-\Delta tY_n\end{matrix}` becomes 
    :math:`\bs{U}_{n+1}=\bb 1&\Delta t\\-\Delta t&1\eb\bb Y_n\\Z_n\eb=A\bs{U}_n`.

Those are like :math:`Y\pr=Z` and :math:`Z\pr=-Y`.
They are first order equations involving times :math:`n` and :math:`n+1`.
Eliminating :math:`A` would bring back the "forward" second order equation.

.. note::

    **Eigenvales of** :math:`A`: :math:`\ld=1\pm i\Delta t`.
    **Then** :math:`|\ld|>1` **and** :math:`(Y_n,Z_n)` **spirals out**.

**Backward**: :math:`\begin{matrix}Y_{n+1}=Y_n+\Delta tZ_{n+1}\\
Z_{n+1}=Z_n-\Delta tY_{n+1}\end{matrix}` is :math:`\bb 1&-\Delta t\\\Delta t&1\eb
\bb Y_{n+1}\\Z_{n+1}\eb=\bb Y_n\\Z_n \eb=\bs{U}_n`.

That matrix has eigenvalues :math:`1+\pm i\Delta t`.
But we *inver* it to reach :math:`\bs{U}_{n+1}` from :math:`\bs{U}_n`.
Then :math:`|ld|<1` explains why *the solution spirals in* to :math`(0,0)` for backward differences.

The second difference :math:`Y_{n+1}-2Y_n+Y_{n-1}` is the **leapfrog method** 
that "leaps over" that center value :math:`Y_n` and is constantly used.

Stability of 2 by 2 Matrices
----------------------------

For the solution of :math:`d\u/dt=A\u`, there is a fundamental question.
*Does the solution approach* :math:`\u=\0` *as* :math:`t\rightarrow \infty`?
A solution that includes :math:`e^t` is unstable.
Stability depends on the eigenvalues of :math:`A`.

The complete solution :math:`\u(t)` is built from pure solutions :math:`e^{\ld t}\x`.
If the eigenvalue :math:`\ld` is real, *the number* :math:`\ld` *must be negative* 
for :math:`e^{\ld t}` to approach zero.
If the eigenvalue is a complex number :math:`\ld=r+is`, *the real part* :math:`r` *must be negavtive*.
When :math:`e^{\ld t}` splits into :math:`e^{rt}e^{ist}`, the factor :math:`e^{ist}` has absolute value fixed at 1:

.. math::

    e^{ist}=\cos st+i\sin st\quad\rm{has}\quad|e^{ist}|^2=\cos^2st+\sin^2st=1.

The real part of :math:`\ld` controls the growth (:math:`r>0`) or the decay (:math:`r<0`).

**Which matrices have negative eigenvalues?**
When are the **real parts of the** :math:`\ld`\ **'s all negative?**

.. note::

    **Stability**: :math:`A` is **stable** and :math:`\u(t)\rightarrow\0` when 
    all eigenvalues :math:`\ld` have **negative real parts**.
    The 2 by 2 matrix :math:`A=\bb a&b\\c&d \eb` must pass two tests:

    * :math:`\ld_1+\ld_2<0`: The trace :math:`T=a+d` must be negative.

    * :math:`\ld_1\ld_2>0`: The determinant :math:`D=ad-bc` must be positive.

**Reason**: If :math:`\ld`'s are real and negative, their sum is negative.
This is the trace :math:`T`.
Their product is positive.
This is the determinant :math:`D`.
The argument also goes in the reverse direction.
If :math:`D=\ld_1\ld_2` is positve, then :math:`\ld_1` and :math:`\ld_2` have the same sign.
If :math:`T=\ld_1+\ld_2` is negative, that sign will be negative.
We can test :math:`T` and :math:`D`.

If the :math:`\ld`'s are complex numbers, they must have the form :math:`r+is` and :math:`r-is`.
Otherwise :math:`T` and :math:`D` will not be real.
The determinant :math:`D` is automatically positive, since :math:`(r+is)(r-is)=r^2+s^2`.
The trace :math:`T` is :math:`r+is+r-is=2r`.
So a negative trace :math:`T` means that the real part is negative and the matrix is stable.

The Exponential of a Matrix
---------------------------

**We want to write the solution** :math:`\u(t)` **in a new form** :math:`e^{At}\u(0)`.
The direct defination of :math:`e^x` is by the infinite series :math:`1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+\cds`.
Change :math:`x` to a square matrix :math:`At` to define the matrix exponential :math:`e^{At}`:

.. note::

    **Matrix exponential** :math:`e^{At}`: :math:`e^{At}=I+At+\frac{1}{2}(At)^2+\frac{1}{6}(At)^3+\cds`.

    **Its** :math:`t` **derivative is** :math:`Ae^{At}`: :math:`A+A^2t+\frac{1}{2}A^3t^2+\cds=Ae^{At}`.

    **Its eigenvalues are** :math:`e^{\ld t}`: 
    :math:`(I+At+\frac{1}{2}(At)^2+\cds)\x=(1+\ld t+\frac{1}{2}(\ld )^2+\cds)\x`.

The number that divides :math:`(At)^n` is :math:`n!`.
The factorials grow quickly.
The series always converges and its derivative is always :math:`Ae^{At}`.
Therefore :math:`e^{At}\u(0)` solves the differential equation with one quick 
formula--*even if there is a shortage of eigenvectors*.

Assume :math:`A` does have :math:`n` independent eigenvectors, so it is diagonalizable.
Substitute :math:`A=X\Ld X\im` into the series for :math:`e^{At}`.
Whenever :math:`X\Ld X\im X\Ld X\im` appears, cancel :math:`X\im X` in the middle:

**Use the series**: :math:`e^{At}=I+X\Ld X\im t+\frac{1}{2}(X\Ld X\im t)(X\Ld X\im t)+\cds`

**Factor out** :math:`X` **and** :math:`X\im`: :math:`e^{At}=X[I+\Ld t+\frac{1}{2}(\Ld t)^2+\cds]X\im`

:math:`e^{At}` **is diagonalized**: :math:`e^{At}=Xe^{\Ld t}X\im`.

:math:`e^{At}` has the same eigenvector matrix :math:`X` as :math:`A`.
Then :math:`\Ld` is a diagonal matrix and so is :math:`e^{\Ld t}`.
The numbers :math:`e^{\ld_it}` are on the diagonal.
Multiply :math:`Xe^{\Ld t}X\im\u(0)` to recognize :math:`\u(t)`:

.. math::

    e^{At}\u(0)=Xe^{\Ld t}X\im\u(0)=\bb \\\ \x_1&\cds&\x_n \\\ \eb
    \bb e^{\ld_1t}\\&\dds\\&&e^{\ld_nt} \eb\bb c_1\\\vds\\c_n \eb.

The solution :math:`e^{At}\u(0)` is the same answer that came in previous equation from three steps:

#. :math:`\u(0)=c_1\x_1+\cds+c_n\x_n=X\bs{c}`.
   Here we need :math:`n` independent eigenvectors.

#. Multiply each :math:`\x_i` by its growth factor :math:`e^{\ld_it}` to follow it forward in time.

#. The best form of :math:`e^{At}\u(0)` is :math:`\u(t)=c_1e^{\ld_1t}\x_1+\cds+c_ne^{\ld_nt}\x_n`.

For an antisymmetric matrix (:math:`A^T=-A`), its exponential :math:`e^{At}` is an orthogonal matrix.
The eigenvalues of :math:`A` are :math:`i` and :math:`-i`.
The eigenvalues of :math:`e^{At}` are :math:`e^{it}` and :math:`e^{-it}`.
Three rules:

#. :math:`e^{At}` **always has the inverse** :math:`e^{-At}`.

#. **The eigenvalues of** :math:`e^{At}` **are always** :math:`e^{\ld t}`.

#. **When** :math:`A` **is antisymmetric**, :math:`e^{At}` **is orthogonal**.
   :math:`Inverse = transpose = e^{-At}`.

Antisymmetric is the smae as "skey-symmetric".
Those matrices have pure imaginary eigenvalues like :math:`i` and :math:`-i`.
Then :math:`e^{At}` has eigenvalues like :math:`e^{it}` and :math:`e^{-it}`.
Their absolute value is 1: neutual stability, pure oscillation, energy is conserved.
So :math:`\lv\u(t)\rv=\lv\u(0)\rv`.

Notes on a Differential Equations Course
----------------------------------------

1. The second order equation :math:`mu\ppr+bu\pr+ku=0` has major importance in applications.
   The exponents :math:`\ld` in the solution :math:`u=e^{\ld t}` solve :math:`m\ld^2+b\ld+k=0`.
   The damping coefficient :math:`b` is crucial:

   **Underdamping**: :math:`b^2<4mk`; **Critical damping**: :math:`b^2=4mk`; **Overdamping**: :math:`b^2>4mk`.

   This decides whether :math:`\ld_2` and :math:`\ld_2` are real roots or repeated roots or complex roots.
   With complex :math:`\ld`'s the solution :math:`u(t)` oscillates as it decays.

2. Our equation had no forcing term :math:`f(t)`.
   We were finding the "nullspace solution".
   To :math:`\u_n(t)` we need to add a particular solution :math:`u_p(t)` that balances the force :math:`f(t)`:

   **Input** :math:`f(t)` **at time** :math:`s`; **Growth factor** 
   :math:`e^{A(t-s)}`; **Add up output at time** :math:`t`:

   .. math::

       \u_{\rm{particular}}=\int_0^t e^{A(t-s)}f(s)\ ds.

   This solution can also be discovered and studied by *Laplace transform*--that 
   is the established way to convert linear differential equations to linear 
   algebra.