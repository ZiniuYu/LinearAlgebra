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
    \bb x_i-m_1\\y_j-m_2 \eb\bb x_i-m_1 y_j-m_2 \eb.

*Every matrix* :math:`UU^T` *is positive semidefinite*.
Sothe whole matrix :math:`V` (combining these matrices :math:`UU^T` with weights 
:math:`p_{ij}\geq 0`) is **at least semidefinite**.

**The covariance matrix** :math:`V` **is positive definite unless the experiments are dependent**.

.. note::

    **Covariance matrix**: :math:`V=\rm{E}[(\X-\bar{\X})(\X-\bar{\X})^T]

.. math::

    \rm{Variance\ of\ }c^T\X=\rm{E}[(c^T\X-c^T\bar{\X})(c^T\X-c^T\bar{\X})^T]
    
    =c^T\rm{E}[(\X-\bar{\X})(\X-\bar{\X})]c=c^TVc

The Mean and Variance of :math:`z=x+y`
--------------------------------------









The Covariance Matrix for :math:`Z=AX`
--------------------------------------