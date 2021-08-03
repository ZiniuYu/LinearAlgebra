Chapter 12.2 Covariance Matrices and Joint Probabilities
========================================================

:math:`p_{ij}=` **Probability that experiment 1 produces** :math:`x_i` **and experiment 2 produces** :math:`y_j`.

.. note::

    **Covariance**: :math:`\dp\sg_{12}=\sum_{\rm{all}}\sum_{i,j}p_{ij}(x_i-m_1)(y_j-m_2)`.

**Probability matrix**:

.. math::

    P=\bb p_{11}&p_{12}\\p_{21}&p_{22} \eb

Notice the row sums :math:`p_i` and column sums :math:`P_i` and the total sum = 1.
Those numbers :math:`p_1,p_2` and :math:`P_1,P_2` are called the **marginals** of the matrix :math:`P`.

.. note::

    **Zero covariance** :math:`\sg_{12}` **for independent trials**:

    * :math:`V=\bb \sg_1^2&0\\0&\sg_2^2 \eb=` **diagonal covariance matrix**.

Independent experiments have :math:`\sg_{12}=0` because every :math:`p_{ij}=(p_i)(p_j)` in equation:

.. math::

    \sg_{12}=\sum_i\sum_j(p_i)(p_j)(x_i-m_1)(y_j-m_2)=
    
    \bigg[\sum_i(p_i)(x_i-m_1)\bigg]\bigg[\sum_j(p_j)(y_j-m_2)\bigg]=[0][0].

**Always** :math:`\sg_1^2\sg_2^2\geq\sg_{12}^2`.
Thus :math:`\sg_{12}` is *between* :math:`-\sg_1\sg_2` *and* :math:`\sg_1\sg_2`.
The covariance matrix :math:`V` is **positive (semi)definite**.
This is an important fact about :math:`M` by :math:`M` covariance matrices for :math:`M` experiments.

Note that the **sample covariance matrix** :math:`S` from :math:`N` trials is certainly semidefinite.
Every new sample :math:`X` contributes to the **sample mean** :math:`\bar{\X}` and to :math:`S`.
Each term :math:`(X_i-\bar{\X})(X_i-\bar{\X})^T` is positive semidefinite and we just add to reach :math:`S`:

.. note::

    :math:`\dp\bar{\X}=\frac{X_1+\cds+X_N}{N}`
    
    :math:`\dp S=\frac{(X_1-\bar{\X})(X_1-\bar{\X})^T+\cds+(X_N-\bar{\X})(X_N-\bar{\X})^T}{N-1}`

The Covariance Matrix :math:`V` is Positive Semidefinite
--------------------------------------------------------

**Total probability (all pairs) is 1**: 

.. math::
    
    \sum_{\rm{all}}\sum_{i,j}p_{ij}=1.

**Row sum** :math:`p_i` **of** :math:`P`:

.. math::

    \sum_{j=1}^np_{ij}=\rm{probability\ }p_i\rm{\ of\ }x_i\rm{\ in\ experiment\ 1}.

.. note::

    **Covariance matrix** :math:`V=\Sg\Sg V_{ij}`:

    * :math:`\dp V=\sum_{\rm{all}}\sum_{i,j}p_{ij}\bb (x_i-m_1)^2&(x_i-m_1)(y_j-m_2)\\(x_i-m_1)(y_j-m_2)&(y_j-m_2)^2\eb`.

.. math::

    V_{11}=\sum_{\rm{all}}\sum_{i,j}p_{ij}(x_j-m_1)^2=\sum_{\rm{all\ }i}(\rm{probability\ of\ }x_i)(x_i-m_1)^2=\sg_1^2.

The matrix :math:`V_{ij}` for each pair of outcomes :math:`i,j` is **positive semidefinite**.
:math:`V_{ij}` has diagonal entries :math:`p_{ij}(x_i-m_1)^2\geq 0` and 
:math:`p_{ij}(y_j-m_2)^2\geq 0` and :math:`\det(V_{ij})=0`.
That matrix :math:`V_{ij}` has rank 1.

.. math::

    \bb (x_i-m_1)^2&(x_i-m_1)(y_j-m_2)\\(x_i-m_1)(y_j-m_2)&(y_j-m_2)^2\eb=
    \bb x_i-m_1\\y_j-m_2 \eb\bb x_i-m_1&y_j-m_2 \eb.

*Every matrix* :math:`UU^T` *is positive semidefinite*.
Sothe whole matrix :math:`V` (combining these matrices :math:`UU^T` with weights 
:math:`p_{ij}\geq 0`) is **at least semidefinite**.

**The covariance matrix** :math:`V` **is positive definite unless the experiments are dependent**.

.. note::

    **Covariance matrix**: :math:`V=\rm{E}[(\X-\bar{\X})(\X-\bar{\X})^T]

.. math::

    \rm{Variance\ of\ }c^T\X=\rm{E}[(c^T\X-c^T\bar{\X})(c^T\X-c^T\bar{\X})^T]
    
    =c^T\rm{E}[(\X-\bar{\X})(\X-\bar{\X})]c=c^TVc

*The variance of* :math:`c^T\X` *can never be negative*.
So :math:`c^TVc\geq 0`.
*The covariance matrix* :math:`V` *is therefore positive semidefinite by the energy test* :math:`c^TVc\geq 0`.

:math:`V` equals :math:`Q\Ld Q^T` with eigenvalues :math:`\ld_i\geq 0` and 
orthonormal eigenvectors :math:`\q_1` to :math:`\q_M`.
**Diagonalizing the covariance matrix means finding** :math:`M` 
**independent experiments as combinations of the original** :math:`M`
**experiments**.

.. note::

    **Covariance matrix**: :math:`\dp V=\iiint p(x,y,z)UU^Tdxdydz` with 
    :math:`U=\bb x-\bar{x}\\y-\bar{y}\\z-\bar{z} \eb`.

* **Independent variables** :math:`x,y,z`: :math:`p(x,y,z)=p_1(x)p_2(y)p_3(z)`.

* **Dependeent variables** :math:`x,y,z`: :math:`p(x,y,z)=0` except when :math:`cy+dy+ez=0`.

The Mean and Variance of :math:`z=x+y`
--------------------------------------

**The sample mean of** :math:`z=x+y` **is clearly** :math:`m_z=m_x+m_y`:

.. note::

    **Mean of sum = Sum of means**: 
    
    * :math:`\dp\frac{1}{N}\sum_1^N(x_i+y_i)=\frac{1}{N}\sum_1^Nx_i+\frac{1}{N}\sum_1^Ny_i`.

.. math::

    \rm{E}[x+y]=\sum_i\sum_j p_{ij}(x_i+y_j)=\sum_i\sum_j p_{ij}x_i+\sum_i\sum_j p_{ij}y_j.

    \sum_i\sum_j p_{ij}x_i=\sum_i(p_{i1}+\cds+p_{iN})x_i=\sum_i p_ix_i=\rm{E}[x]

    \sum_i\sum_j p_{ij}y_j=\sum_j(p_{1j}+\cds+p_{nj})y_j=\sum_j p_jy_j=\rm{E}[y]

.. math::

    \sg_z^2&=\sum\sum p_{ij}(x_i+y_j-m_x-m_y)^2

    &=\sum\sum p_{ij}(x_I-m_x)^2+\sum\sum p_{ij}(y_j-m_y)^2+2\sum\sum p_{ij}(x_i-m_x)(y_j-m_y)

**The variance of** :math:`z=x+y` **is** :math:`\sg_z^2=\sg_x^2+\sg_y^2+2\sg_{xy}`.

The Covariance Matrix for :math:`Z=AX`
--------------------------------------

.. note::

    **The covariance matrix of** :math:`Z=AX` **is** :math:`V_Z=AV_XA^T`.

The Correlation :math:`\rho`
----------------------------

**The new** :math:`X=x/\rho_x` **and** :math:`Y=y/\rho_y` **have variance** :math:`\sg_X^2=\sg_Y^2=1`.
**The correlation of** :math:`x` **and** :math:`y` **is the covariance of** :math:`X` **and** :math:`Y`.

.. note::

    **Correlation**: :math:`\dp\rho_{xy}=\frac{\sg_{xy}}{\sg_x\sg_y}=` 
    **covariance of** :math:`\dp\frac{x}{\sg_x}` **and** 
    :math:`\dp\frac{y}{\rho_y}`.
    Always :math:`-1\leq\rho_{xy}\leq 1`.

Zero covariance gives zero correlation.
*Independent random variables produce* :math:`\rho_{xy}=0`.

Since :math:`\sg_{xy}^2\leq\sg_x^2\sg_y^2`, then :math:`\rho_{xy}^2\leq 1`.
Correlation near :math:`\rho=+1` means strong dependence in the same direction.
Negative correlation means that :math:`y` tends to be below its mean when :math:`x` is above its mean.