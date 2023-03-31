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

<img width="344" alt="image" src="https://user-images.githubusercontent.com/69034801/229121497-06b1cdc4-6258-4b39-b082-086b039a79be.png">

<hr>

### Calculating weights for Similarity Indices

All similarity indices rely on parameters,to calculate the similarity of planets. The weights of individual parameters can be computed by providing the reference value, the lower and upper limits for the parameter (where, lower limit ≤ referance value ≤ upper limit). Optionally, a threshold value of the similarity index (default = 0.8) can also be provided. 

The `calc_weight` function calculates the weight parameters and takes in ref val, upper lim, lower lim and threshold (optional) for the reference values, upper limits, lower limits and threshold value, respectively.

The below example uses planetary radius, density, escape velocity (in Earth Units) and temperature(K) as the parameters.

<img width="379" alt="image" src="https://user-images.githubusercontent.com/69034801/229123072-22587fdd-ee4d-4787-9986-10b44493b358.png">

and the following output is received:

<img width="342" alt="image" src="https://user-images.githubusercontent.com/69034801/229123200-996b1095-e792-4b4c-9276-c124b6b04177.png">

<hr>

### Calculating Planet Similarity Index (PSI)



