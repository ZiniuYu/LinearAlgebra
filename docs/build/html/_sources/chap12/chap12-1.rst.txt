Chapter 12.1 Mean, Variance, and Probability
============================================

* The **mean** is the *average value* or expected value.

* The **variance** :math:`\sg^2` measures the average *squared distance* from the mean :math:`m`.

* The **probabilities** of :math:`n` different outcomes are positive numbers :math:`p_1,\cds,p_n` adding to 1.

The sample mean starts with :math:`N` samples :math:`x_1,\cds,\x_N` from a completed trial.
Their mean is the *average* of the :math:`N` observed samples:

**Sample mean**: :math:`\dp m=\mu=\frac{1}{N}(x_1+x_2+\cds+x_N)`.

The **expected value of** :math:`\x` starts with the probabilities :math:`p_1,\cds,p_n` of :math:`x_1,\cds,x_n`:

.. note::

    **Expected value**: :math:`m=\rm{E}[x]=p_1x_1+p_2x_2+\cds+p_nx_n`.

This is :math:`\p\cd\x`.
Notice that :math:`m=\bs{E}[x]` tells us what to expect, :math:`m=\mu` tells us what we got.

Variance (around the mean)
--------------------------

The **variance** :math:`\sg^2` measures expected distance (squared) from the expected mean :math:`\bs{E}[x]`.
The **sample variance** :math:`S^2` measures actual distance (squared) from the sample mean.
The square root is the **standard deviation** :math:`\sg` **or** :math:`S`.

.. note::

    **Sample variance**: :math:`\dp S^2=\frac{1}{N-1}[(x_1-m)^2+\cds+(x_N-m)^2]`.

Statisticians divide by math:`N-1` and not :math:`N` so that :math:`S^2` is an unbiased estimate of :math:`\sg^2`.
One degree of freedom is already accounted for in the sample mean.

An important identity comes from splitting each :math:`(x-m)^2` into :math:`x^2-2mx+m^2`:

sum of :math:`(x_i-m)^2=(`\ sum of :math:`x_i^2)-2m(`\ sum of :math:`x_i)+(`\ sum of :math:`m^2)`

:math:`=(`\ sum of :math:`x_i^2)-2m(Nm)+Nm^2=(`\ sum of :math:`x_i^2)-Nm^2`.

.. note::

    **Variance**: :math:`\sg^2=\rm{E}[(x=m)^2]=p_1(x_1-m)^2+\cds+p_n(x_n-m)^2`.

Continuous Probability Distributions
------------------------------------

:math:`F=` **integral of** :math:`p`: **Probability of** :math:`\dp a\leq x\leq b=\int_a^b p(x)dx=F(b)-F(a)`.

Mean and Variance of :math:`p(x)`
---------------------------------

.. note::

    **Mean**: :math:`\dp m=\rm{E}[x]=\int xp(x)dx`.

.. note::

    **Variance**: :math:`\dp\sg^2=\rm{E}[(x-m)^2]=\int p(x)(x-m)^2dx`.

.. note::

    **Uniform distribution for** :math:`0\leq x\leq a`; **Density** 
    :math:`\dp p(x)=\frac{1}{a}`; **Cumulative** :math:`\dp F(x)=\frac{x}{a}`:

    * **Mean**: :math:`\dp m=\frac{a}{2}` halfway

    * **Variance**: :math:`\dp \sg^2=\int_0^a\frac{1}{a}\left(x-\frac{a}{2}\right)^2dx=\frac{a^2}{12}`.

Normal Distribution: Bell-shaped Curve
--------------------------------------

.. note::

    **Central Limit Theorem (informal)**: The average of :math:`N` samples of 
    "any" probability distribution approaches a normal distribution as
    :math:`N\rightarrow\infty`.

The standard normal distribution is symmetric around :math:`x=0`, so its mean value is :math:`m=0`.
It is chosen to have a standard variance :math:`\sg^2=1`.
It is called :math:`\bs{\rm{N}}(0,1)`.

.. note::

    **Standard normal distribution**: :math:`\dp p(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}`

* **Total probability** :math:`=1`: 
  :math:`\dp \int_{-\infty}^{\infty}p(x)dx=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-x^2/2}dx=1`

* **Mean** :math:`\rm{E}[x]=0`: :math:`\dp m=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}xe^{-x^2/2}dx=0`

* **Variance** :math:`\rm{E}[x^2]=1`: :math:`\dp\sg^2=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}(x-0)^2e^{-x^2/2}dx=1`

The probability that a random sample falls between :math:`-\sg` and :math:`\sg` 
is :math:`F(\sg)-F(-\sg)\approx\frac{2}{3}`.
This is because :math:`\int_{-\sg}^{\sg}p(x)dx` equals 
:math:`\int_{-\infty}^{\sg}p(x)dx-\int_{-\infty}^{-\sg}p(x)dx=F(\sg)-F(-\sg)`.

Similarly, the probability that a random :math:`x` lies between :math:`-2\sg` 
and :math:`2\sg` is :math:`F(2\sg)-F(-2\sg)\approx 0.95`.

The normal distribution with any mean :math:`m` and standard deviation 
:math:`\sg` comes by shifting and stretching the standard 
:math:`\bs{\rm{N}}(0,1)`.
**Shift** :math:`x` **to** :math:`x-m`.
**Stretch** :math:`x-m` **to** :math:`(x-m)/\sg`.

.. note::

    **Gaussian density** :math:`p(x)`; **Normal distribution** :math:`\bs{\rm{N}}(m,\sg)`:

    * :math:`\dp p(x)=\frac{1}{\sg\sqrt{2\pi}}e^{-(x-m)^2/2\sg^2}`

The integral of :math:`p(x)` is :math:`F(x)`--the probability that a random sample will fall below :math:`x`.
The differential :math:`p(x)dx=F(x+dx)-F(x)` is the probability that a random 
sample will fall between :math:`x` and :math:`x+dx`. 
There is no simple formula to integrate :math:`e^{-x^2/2}`, so this cumulative 
distribution :math:`F(x)` is computed and tabulated very carefully.

:math:`N` Coin Flips and :math:`N\rightarrow \infty`
----------------------------------------------------

.. note::

    **Linearity**: :math:`x_{\rm{new}}=ax_{\rm{old}}+b` has 
    :math:`m_{\rm{new}}=am_{\rm{old}}+b` and 
    :math:`\sg_{\rm{new}}^2=a^2\sg_{\rm{\old}}^2`.

.. note::

    **Shafted and scaled**: :math:`\dp X=\frac{x-m}{\sg}=\frac{x-\frac{1}{2}N}{\sqrt{N}/2}`

    * **Subtracting** :math:`m` **is "centering" or "detrending"**. 
      **The mean of** :math:`X` **is zero**.
    
    * **Dividing by** :math:`\sg` **is "normalizing" or "standardizing"**.
      **The variance of** :math:`X` **is 1**.

.. note::

    The center probability :math:`\dp\bigg(\frac{N}{2}` heads, 
    :math:`\dp\frac{N}{2}` tails\ :math:`\bigg)` is
    :math:`\dp\frac{1}{2^N}\frac{N!}{(N/2)!(N/2)!}`.

For large :math:`N`, Stirling's formula :math:`\sqrt{2\pi N}(N/e)^N` is a close approximation to :math:`N!`/
Use Stirling for :math:`N` and twice for :math:`N/2`:

**Limit of coin-flip Center probability**:

.. math::

    p_{N/2}\approx\frac{1}{2^N}\frac{\sqrt{2\pi N}(N/e)^N}{\pi N(N/2e)^N}=
    \frac{\sqrt{2}}{\sqrt{\pi N}}=\frac{1}{\sqrt{2\pi}\sg}.

Monte Carlo Estimation Methods
------------------------------

Applied mathematics has moved to **accepting uncertainty in the inputs and estimating the variance in the outputs**.
**Monte Carlo method** approximates an expected value :math:`\rm{E}[x]` by a sample average :math:`(x_1+\cds+x_N)/N`.

Each sample comes from a set of data :math:`b_k`.
*Monte Carlo randomly chooses this data* :math:`b_k`, *it computes the outputs* 
:math:`x_k`, *and then it averages those* :math:`x`'s.
Decent accuracy for :math:`\rm{E}[x]` often requires many samples :math:`b` and huge computing cost.
The error in approimating :math:`\rm{E}[x]` by :math:`(x_1+\cds+x_N)/N` is normally of order :math:`1/\sqrt{N}`.
*Slow improvements as* :math:`N` *increases*.

Suppose it is much simpler to simulate another variable :math:`y(b)` close to :math:`x(b)`.
Then use :math:`N` computationis of :math:`y(b_k)` and only :math:`N^*<N` 
computations of :math:`x(b_k)` to estimate :math:`rm{E}[x]`.

.. note::

    **2-level Monte Carlo**:

    * :math:`\dp \rm{E}[x]\approx\frac{1}{N}\sum_1^N y(b_k)+\frac{1}{N^*}\sum_1^{N^*}[x(b_k)-y(b_k)]`.

The idea is that :math:`x-y` has a smaller variance :math:`\sg^*` than the original :math:`x`/
Therefore :math:`N^*` can be smaller than :math:`N`, with the same accuracy for :math:`\rm{E}[x]`.
We do :math:`N` cheap simulations to find the :math:`y`'s.
Those cost :math:`C` each.
We only do :math:`N^*` expensive simulations involving :math:`x`'s.
Those cost :math:`C^*` each.
The total computing cost is :math:`NC+N^*C^*`.

Calculus minimizes the overall variance for a fixed total cost.
The optimal ratio :math:`N^*/N` is :math:`\sqrt{C/C^*}\sg^*/\sg`.
Three-level Monte Carlo would simulate :math:`x,y` and :math:`z`:

.. math::

    \rm{E}[x]\approx\frac{1}{N}\sum_1^N z(b_k)+\frac{1}{N^*}\sum_1^{N^*}[y(b_k)-
    z(b_k)]+\frac{1}{N^{**}}\sum_1^{N^{**}}[x(b_k)-y(b_k)].

Review: Three Formulas for the Mean and the Variance
----------------------------------------------------