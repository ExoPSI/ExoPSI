# ExoPSI

ExoPSI is an open source Python package which offers similarity indexing of exoplanets in order to assess their habitability. It provides the capability to calculate similarity indices of different planetary candidates with respect to any reference values and any numerical parameter, yielding a more accurate evaluation of the survivability of different species. 

ExoPSI offers the ability to use any planet as a reference point and visualization functions that allow for easy comparison of the similarity between the interior and surface parameters of different planets. ExoPSI aims to help planetary sceince researches by offering a comprehensive solution for evaluating planetary similarities.

<hr>

### Getting Started

To utilize the functions available in ExoPSI, import the library and instantiate an object of the _`exopsi`_ class.

<img width="196" alt="image" src="https://user-images.githubusercontent.com/69034801/229033184-e12cc1ea-a19d-4a4f-b761-57f76d09c3aa.png">

<hr>

### Importing Datasets 

ExoPSI can only handle datasets of the type `pandas.core.frame.DataFrame`. As a result, any dataset to be used has to be imported as a pandas data frame.  

For example, [the PHL’s Exoplanet Catalog]([url](https://phl.upr.edu/projects/habitable-exoplanets-catalog/hec-data-of-potentially-habitable-worlds/phls-exoplanets-catalog)) (PHL-EC) of the Planetary Habitability Laboratory can be imported as:

<img width="346" alt="image" src="https://user-images.githubusercontent.com/69034801/229121374-51837e5f-94a0-492b-a1c0-70dcce567dc9.png">





