MS SEG challenge pre-processed training dataset

Version 2

Corrects registration errors between modalities for some patients.

----------

Version 1

This file contains the pre-processed images for the 15 patients of the challenge training dataset. These patients are coming from three different MRI scanners located in three different centers (see https://portal.fli-iam.irisa.fr/msseg-challenge/data for more details on the centers and scanners). Patients starting with 01 come from a Siemens 3T Verio scanner, those starting with 07 from a Siemens Aera 1.5T scanner, and finally those starting with 08 from a Philips Ingenia 3T scanner.

The provided images include, for each patient:

- 3D FLAIR image
- 3D T1 image
- T2 image
- DP image
- 3D T1 Gd image (post-contrast agent image)

Manual segmentations may be found in the unprocessed dataset. The following pre-processing was applied for each patient:

- denoising with the NL-means algorithm [1] of each image
- rigid registration [2] of each image towards the FLAIR image 
- Brain extraction using the volBrain platform [3] from the T1 image and applied on the other modalities with sinc interpolation
- Bias correction using the N4 algorithm [4]

For any question or remark on the images provided, please contact challenges-iam@inria.fr.

References:

[1] Pierrick Coupé, Pierre Yger, Sylvain Prima, Pierre Hellier, Charles Kervrann, Christian Barillot. "An optimized blockwise nonlocal means denoising filter for 3-D magnetic resonance images." IEEE Transactions on Medical Imaging, 2008, 27 (4), pp.425-41.
[2] Olivier Commowick, Nicolas Wiest-Daesslé, Sylvain Prima. "Block-Matching Strategies for Rigid Registration of Multimodal Medical Images." 9th IEEE International Symposium on Biomedical Imaging (ISBI'2012), May 2012. pp.700-703, 2012.
[3] J. V. Manjón, P. Coupé. "volBrain: An online MRI brain volumetry system", Organization for Human Brain Mapping 15, 2015.
[4] Nicholas J. Tustison, Brian B. Avants, Philip A. Cook, Yuanjie Zheng, Alexander Egan, Paul A. Yushkevich, and James C. Gee. "N4ITK: Improved N3 Bias Correction." IEEE Transactions on Medical Imaging, 2010, 29 (6), pp.1310-1320.
