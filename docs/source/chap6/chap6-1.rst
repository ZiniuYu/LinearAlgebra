Chapter 6.1 Introduction to Eigenvalues
=======================================

The key idea is to avoid all the complications presented by the matrix :math:`A`.
Suppose the solution vector :math:`\u(t)` stays in the direction of a fixed vctor :math:`\x`.
Then we only need to find the number (changing with time) that muiltiplies :math:`\x`.
A number is easier than a vector.
**We want "eigenvectors"** :math:`\x` **that don't change direction when you multiply by** :math:`A`.

Almost all vectors change direction, when they are multiplied by :math:`A`.
**Certain exceptional vectors** :math:`\x` **are in the same direction as** :math:`A\x`.
**Those are the "eigenvectors"**.
multiply an eigenvector by :math:`A`, and the vector :math:`A\x` is a number :math:`\ld` times the original :math:`\x`.

.. tip::

    **The basic equation is** :math:`A\x=\ld\x`.
    **The number** :math:`\ld` **is an eigenvalue of** :math:`A`.

The eigenvalue :math:`\ld` tells whether the special vector :math:`\x` is 
stretched or shrunk or reversed or left unchanged--when it is multiplied by 
:math:`A`.
The eigenvalue :math:`\ld` could be zero.
Then :math:`A\x=0\x` means that this eigenvector :math:`\x` is in the nullspace.

If :math:`A` is the identity matrix, every vector has :math:`A\x=\x`.
All vectors are eigenvectors of :math:`I`.
All eigenvalues "lambda" are :math:`\ld=1`.
Most 2 by 2 matrices have *two* eigenvector directions and *two* eigenvalues.
We will show that :math:`\det(A-\ld I)=0`.



.. tip::

    **When** :math:`A` **is squared, the eigenvectors stay the same**.
    **The eigenvalues are squared**.





The Equation for the Eigenvalues
--------------------------------









Determinant and Trace
---------------------









Imaginary Eigenvalues
---------------------









Eigenvalues of :math:`AB` and :math:`A+B`
-----------------------------------------




