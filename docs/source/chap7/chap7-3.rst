Chapter 7.3 Principal Component Analysis (PCA by the SVD)
=========================================================

For eaech of :math:`n` samples we are measuring :math:`m` variables.
The data matrix :math:`A_0` has :math:`n` columns and :math:`m` rows.

Graphically, the columns of :math:`A_0` are :math:`n` points in :math:`\R^m`.
After we subtract the average of each row to reach :math:`A`, the :math:`n`
points are often clustered along a line orr close to a plane (or other low-
dimensional subspace of :math:`\R^m`).

**Sample covariance matrix**:

.. math::

    S=\frac{AA^T}{n-1}.

:math:`A` shows the distance :math:`a_{ij}-\mu_i` from each measurement to the row average :math:`\mu_i`.

**The SVD of** :math:`A` **(centered data) shows the dominant direction in the scatter plot.**

The Essentials of Principal Component Analysis (PCA)
----------------------------------------------------

PCA gives a way to understand a data plot in dimension :math:`m =` the number of measured variables.
*The crucial connection to linear algebra* is in the singular values and singular vectors of :math:`A`.
Those come from the eigenvalues :math:`\ld=\sg^2` and the eigenvectors 
:math:`\u` of the sample covariance matrix :math:`S=AA^T/(n-1)`.

* The total variance in the data is the sum of all eigenvalues and of sample variances :math:`s^2`:

  **Total variance** :math:`T=\sg^2_1+\cds+\sg^2_m=s^2_1+\cds+s^2_m=` **trace** (*diagonal sum*).

* The first eigenvector :math:`\u_1` of :math:`S` points in the most significant direction of the data.
  That direction accounts for (or *explains*) a fraction :math:`\sg^2_1/T` of the total variance.

* The next eigenvector :math:`\u_2` (orthogonal to :math:`\u_1`) accounts for a smaller fraction :math:`\sg^2_2/T`.

* Stop when those fractions are small.
  You have the :math:`R` directions that explain most of the data.
  The :math:`n` data points are very near an :math:`R`-dimensional subspace with basis :math:`\u_1` to :math:`\u_R`.
  These :math:`u`'s are the **princpal components** in :math:`m`-dimensional space.

* :math:`R` is the "effective rank" of :math:`A`.
  The true rank :math:`r` is probably :math:`m` or :math:`n`: full rank matrix.

Perpendicular Least Squares
---------------------------

**The sum of squared distances from the points to the line is a minimum**.

**Proof**: Separate each column :math:`\a_j` into its components along the :math:`u_1` line and :math:`u_2` line:

    * **Right triangles** :math:`\dp\sum_{j=1}^n\lv\a_j\rv^2=\sum_{j=1}^n|\a_j^T\u_1|^2+\sum_{j=1}^n|\a_j^T\u_2|^2`.

    The sum on the left is fixed by the data points :math:`\a_j` (columns of :math:`A`).
    The first sum on the right is :math:`\u_1^TAA^T\u_1`.
    So when we maximize that sum in PCA by choosing the eigenvector :math:`\u_1`, we minimize the second sum.
    That second sum (squared distances from the data points to the best line) is 
    a minimum for perpendicular least squares.

The Sample Correlation Matrix
-----------------------------

If scaling is a problem, **we change from covariance matrix** :math:`S` **to correlation matrix** :math:`C`:

    A diagonal matrix :math:`D` rescales :math:`A`.
    Each row of :math:`DA`` has length :math:`\sqrt{n-1}`.
    **The sample correlation matrix** :math:`C=DAA^TD/(n-1)` **has 1's on its diagonal**.

Genetic Variation in Europe
---------------------------

The first singular vectors of genetic variation SNP matrix almost reproduce a map of Europe.

Eigenfaces
----------

**PCA provides a mechanism to recognize geometric/photometric similarity through algebraic means**.

Applications of Eigenfaces
--------------------------

The first commercial use of PCA face recognition was for law enforcement and security.

Model Order Reduction
---------------------

**A reduced model tries to identify important states of the system**.

Searching the Web
-----------------

#. The site may be an **autority**: *Links come in* from many sites.
   Especially from hubs.

#. The site may be a **hub**: *Links go out* to many sites in the list.
   Especially to authorities.   

* **Authority/Hub**: :math:`\x_i^1/y_i^1=` Add up :math:`\y_j^0/x_j^0` for all 
  links **into** :math:`i/` **out from** :math:`i`.

* **Authority**: :math:`\x^2=A^T\y^1=A^TA\x^0`.
  
* **Hub**: :math:`\y^2=A\x^1=AA^T\y^0`.

**When we take powers, the largest eigenvalues** :math:`\sg_1^2` **begins to dominate**.

PCA in Finance: The Dynamics of Interest Rates
----------------------------------------------

The application of PCA is the **yield cur for treasury securities**.