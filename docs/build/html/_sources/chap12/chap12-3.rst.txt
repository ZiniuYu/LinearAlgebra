Chapter 12.3 Multivariate Gaussian and Weighted Least Squares
=============================================================

**Mean** :math:`m` **and variance** :math:`\sg^2`:

.. math::

    p(x)=\frac{1}{\sqrt{2\pi}\sg}e^{-(x-m)^2/2\sg^2}.

.. math::

    \int_{-\infty}^\infty p(x)dx=1\quad\rm{and}\quad
    \int_{m-\sg}^{m+\sg}p(x)dx=\frac{1}{\sqrt{2\pi}}\int_{-1}^1e^{-X^2/2}dX
    \approx\frac{2}{3}.

Every Gaussian turns into a **standard Gaussian** :math:`p(x)` with mean :math:`m=0` and variance :math:`\sg^2=1`.
**The standard ormal distribution** :math:`N(0,1)` **has** :math:`\dp p(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}`.

Integrating :math:`p(x)` from :math:`-\infty` to :math:`x` gives the cumulative 
distribution :math:`F(x)`: the probability that a random sample is below 
:math:`x`.
The probability will be :math:`F=\frac{1}{2}` at :math:`x=0`.

Two-dimensional Gaussians
-------------------------

**Independent** :math:`x` **and** :math:`y`:

.. math::

    p(x,y)=\frac{1}{2\pi\sg_1\sg_2}e^{-(x-m_1)^2/2\sg_1^2}e^{-(y-m_2)^2/2\sg_2^2}.

The covariance of :math:`x` and :math:`y` will be :math:`\sg_{12}=0`.
The covariance matrix :math:`V` will be *diagonal*.

Notice that the two exponents can be combined into 
:math:`-\frac{1}{2}(\x-\bs{m})^TV\im(\x-\bs{m})` with :math:`V\im` in the middle:

.. math::

    -\frac{(x-m_1)^2}{2\sg_1^2}-\frac{(y-m_2)^2}{2\sg_2^2}=-\frac{1}{2}
    \bb x-m_1&y-m_2 \eb\bb \sg_1^2&0\\0&\sg_2^2 \eb\im\bb x-m_1\\y-m_2 \eb.

Non-independent :math:`x` and :math:`y`
---------------------------------------

.. note::

    **Multivariate Gaussian probability distribution**:

    * :math:`\dp p(\x)=\frac{1}{(\sqrt{2\pi})^M\sqrt{\det V}}e^{-(\x-\bs{m})^TV\im(\x-\bs{m})/2}`.

.. math::

    X=\x-\bs{m}\quad(\x-\bs{m})^TV\im(\x-\bs{m})=X^TQ\Ld\im Q^TX=Y^T\Ld\im Y.

Notice that the combinations :math:`Y=Q^TX=Q^T(\x-\bs{m})` are statistically independent.
*Their covariance matrix* :math:`\Ld` *is diagonal*.

.. math::

    \int\cds\int e^{-Y^T\Ld\im Y/2}dY=
    \bigg(\int_{-\infty}^{\infty}e^{y_1^2/2\ld_1}dy_1\bigg)\cds
    \bigg(\int_{-\infty}^{\infty}e^{y_M^2/2\ld_M}dy_M\bigg)

    =(\sqrt{2\pi\ld_1})\cds(\sqrt{2\pi\ld_M})=(\sqrt{2\pi})^M\sqrt{\det V}.

**Vector** :math:`\bs{m}` **of means**:

.. math::

    \int\cds\int\x p(\x)d\x=(m_1,m_2,\cds)=\bs{m}.

**Covariance matrix** :math:`V`:

.. math::

    \int\cds\int(\x-\bs{m})p(\x)(\x-\bs{m})^Td\x=V.

Weighted Least Squares
----------------------

The good measure of error is :math:`E=(\b-A\x)^TV\im(\b-A\x)`.

.. note::

    **Weighted least squares**: :math:`A^TV\im A\wh{\x}=A^TV\im\b`.

The most important examples have :math:`m` *independent* errors in :math:`\b`.
Those errors have variances :math:`\ld_1^2,\cds,\ld_m^2`.
By independence, :math:`V` is a diagonal matrix.
The good weights :math:`1/\ld_1^2,\cds,1/\ld_m^2` come from :math:`V\im`.
*We are weighting the errors in* :math:`\b` *to have* **variance = 1**:

.. note::

    **Weighted least squares; Independent errors in** :math:`\b`:

    * Minimize :math:`\dp E=\sum_{i=1}^m\frac{(\b-A\x)_i^2}{\sg_i^2}`.

#. Start with :math:`A\x=\b` (:math:`m` equations, :math:`n` unknonws, :math:`m>n` no solution)

#. Each right side :math:`b_i` has mean zero and variance :math:`\sg_i^2`.
   The :math:`b_i` are independent.

#. Divide the :math:`i`\ th equation by :math:`\sg_i` to have variance = 1 for every :math:`b_i/\sg_i`.

#. That division turns :math:`A\x=\b` into :math:`V^{-1/2}A\x=V^{-1/2}\b` with 
   :math:`V^{-1/2}=\rm{diag}(1/\sg_1,\cds,1/\sg_m)`.

#. Ordinary least squares on those weighted equations has 
   :math:`A\rightarrow V^{-1/2}A` and :math:`\b\rightarrow V^{-1/2}\b`.

.. note::

    :math:`(V^{-1/2}A)^T(V^{-1/2}A)\wh{\x}=(V^{-1/2}A)^TV^{-1/2}\b` is :math:`A^TV\im A\wh{\x}=A^TV\im\b`.

The Variance in the Estimated :math:`\widehat{x}`
-------------------------------------------------

.. note::

    **Variance-covariance matrix** :math:`W` **for** :math:`\wh{\x}`:

    * :math:`\rm{E}[(\wh{\x}-\x)(\wh{\x}-\x)^T]=(A^TV\im A)\im`.

The smallest possible variance comes from the best possible weighting, which is :math:`V\im`.

**If** :math:`\b` **has covariance matrix** :math:`V`, **then** 
:math:`\wh{\x}=L\b` **has covariance matrix** :math:`LVL^T`.

.. math::

    LVL^T=(A^TV\im A)\im A^TV\im\quad V\quad V\im A(A^TV\im A)\im=(A^TV\im A)\im

The Kalman Filter
-----------------

The :math:`\wh{\x}_k` will be our best least squares estimate of the latest 
solution :math:`\x_k` to the **whole history of observation equations and**
**update equations (state equations) up to time** :math:`k`.

**OLD**: :math:`A_0\x_0=\b_0` leads to the weighted equation :math:`A_0^TV_0\im A_0\wh{\x}_0=A_0^TV_0\im\b_0`.

**NEW**: :math:`\bb A_0\\A_1 \eb\wh{\x}_1=\bb \b_0\\b_1 \eb` leads to the 
following weighted equation for :math:`\wh{\x}_1`:

.. math::

    \bb A_0^T&A_1^T \eb\bb V_0\im\\&V_1\im \eb\bb A_0\\A_1 \eb\wh{\x}_1=
    \bb A_0^T&A_1^T \eb\bb V_0\im\\&V_1\im \eb\bb \b_0\\\b_1 \eb.

.. note::

    **Kalman update gives** :math:`\wh{\x}_1` **from** :math:`\wh{\x}_0`:

    * :math:`\wh{\x}_1=\wh{\x}_0+K_1(\b_1-A_1\wh{\x}_0)`.

.. note::

    **Covariance** :math:`W_1` **of errors in** :math:`\wh{\x}_1`:
    :math:`W_1\im=W_0\im+A_1^TV_1\im A_1`.
    
    **Kalman gain matrix** :math:`K_1`: :math:`K_1=W_1A_1^TV_1\im`.