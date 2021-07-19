Chapter 7.1 Image Processing by Linear Algebra
==============================================

**The singular value theorem for** :math:`A` **is the eigenvalue theorem for** :math:`A^TA` **and** :math:`AA^T`.

:math:`A` has *two* sets of singular vectors (the eigenvectors of :math:`A^TA` and :math:`AA^T`).
There is *one* set of positive singular values (because :math:`A^TA` has the same positive eigenvalues as :math:`AA^T`).
:math:`A` is often rectangular, but :math:`A^TA` and :math:`AA^T` are square, symmetric, and positive semidefinite.

**The Singular Value Decomposition (SVD) separates any matrix into simple pieces**.

Each piece is a column vector times a row vector.
An :math:`m` by :math:`n` matrix has :math:`m` times :math:`n` entries (a big 
number when the matrix represents an image).
But a colkumn and a row only have :math:`m+n` components, far less than :math:`m` times :math:`n`.

Think of an image as a large rectangular matrix.
The entries :math:`a_{ij}` tell the grayscales of all the pixels in the image.
Major success in compression will be impossible if every :math:`a_{ij}` is an independent random number.
We totally depend on the fact that *nearby pixels generally have similar grayscales*.
An edge produces a sudden jump when you cross over it.
Cartoons are more compressible than real-world images, with edges everywhere.

For a video, the number :math:`a_{ij}` don't change much between frames.
**We only transmit the small changes**.
This is *difference coding* in the H.264 video compression standard.
We compress each change matrix by linear algebra (and by nonlinear 
"quantization" for an efficient step to integers in the computer).

Low Rank Images (Examples)
--------------------------

For a matrix :math:`A` has the same grayscale :math:`g` in every entry: :math:`d_{ij}=g`.
When :math:`g=1` and :math:`m=n=6`, here is an extreme example of the central SVD dogma of image processing:

.. math::

    \rm{Don't\ send\ }A=\bb 1&1&1&1&1&1\\1&1&1&1&1&1\\1&1&1&1&1&1\\1&1&1&1&1&1\\1&1&1&1&1&1\\1&1&1&1&1&1 \eb\quad
    \rm{Send\ }A=\bb 1\\1\\1\\1\\1\\1 \eb\bb 1&1&1&1&1&1 \eb.

If we define the all-ones vector :math:`\x` in advance, we only have to send **one number**.
That number would be the constant grayscale :math:`g` that multiplies :math:`\x\x^T` to produce the matrix.

If there are special vectors like :math:`\x=` **ones** that can usefully be 
defined in advace, then image processing can be extremely fast.
The battle is between **preselected bases** (the Fourier basis allows speed-up 
for the FFT) and **adaptive bases** determined by the image.
The SVD produces bases from the image itself--this is adaptive and it can be expensive.

.. math::

    \rm{Don't\ send\ }A=\bb a&a&c&c&e&e\\a&a&c&c&e&e\\a&a&c&c&e&e\\a&a&c&c&e&e\\a&a&c&c&e&e\\a&a&c&c&e&e \eb\quad
    \rm{Send\ }A=\bb 1\\1\\1\\1\\1\\1 \eb\bb a&a&c&c&e&e \eb.

This matrix has 3 values but it still has rank 1.
We still have one column times one row.
But when the rank moves up to :math:`r=2`, we need :math:`\u_1\v_1^T+\u_2\v_2^T`.
Here is one choice:

.. note::

    **Embedded square**: :math:`\bb 1&0\\1&1 \eb` is equal to :math:`A=\bb 1\\1 \eb\bb 1&1 \eb-\bb 1\\0 \eb\bb 0&1 \eb`.

**The SVD chooses rank one pieces in order of importance**.
If the rank of :math:`A` is much higher than 2, as we expect for real images, 
then :math:`A` will add up many rank one pieces.
We want the small ones to be really small--they can be discarded with no loss to visual quality.
Image compression becomes lossy, but good image compression is virtually undetectable by the human visual system.

Eigenvectors for the SVD
------------------------

**Use the eigenvectors** :math:`\u` **of** :math:`AA^T` **and the eigenvectors** :math:`\v` **of** :math:`A^TA`.

Since :math:`AA^T` and :math:`A^TA` are automatically symmetric (but not usually 
equal!) the :math:`\u`'s will be one orthogonal set and the eigenvectors 
:math:`\v` will be another orthogonal set.
We can and will make them all unit vectors: :math:`\lv\u_i\rv=1` and :math:`\lv\v_i\rv=1`.
Then our rank 2 matrix will be :math:`A=\sg_1\u_1\v_1^T+\sg_2\u_2\v_2^T`.
The size of those numbers :math:`\sg_1` and :math:`\sg_2` will decide whether they can be ignored in compression.
*We keep larger* :math:`\sg`'s, *we discard small* :math:`\sg`'s.

The :math:`\u`'s from the SVD are called **left singular vectors** (unit eigenvectors of :math:`AA^T`).
The :math:`\v`'s are **right singular vectors** (unit eigenvectors of :math:`A^TA`).
The :math:`\sg`'s are **singular values**, square roots of the equal eigenvalues of :math:`AA^T` and :math:`A^TA`:

.. note::

    **Choices from the SVD**:

    * :math:`AA^T\u_i=\sg_i^2\u_i \quad A^TA\v_i=\sg_i^2\v_i \quad A\v_i=\sg_i\u_i`.

.. note::

    :math:`A=\bb \\\ \u_1&\u_2 \\\ \eb\bb \sg_1\\&\sg_2 \eb\bb \v_1^T\\\v_2^T \eb`
    or more simply 
    :math:`A\bb \\\ \v_1&\v_2 \\\ \eb=\bb \\\ \sg_1\u_1&\sg_2\u_2 \\\ \eb`

*Important*: The key point is not that images tend to have low rank.
**No**: Images mostly have full rank.
But they do have **low effective rank**.
This means: Many singular values are small and can be set to zero.
*We transmit a low rank approximation*.

**Visual quality can be preserved even with a big reduction in the rank**.