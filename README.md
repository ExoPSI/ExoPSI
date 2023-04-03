# ExoPSI

ExoPSI is an open source Python package which offers similarity indexing of exoplanets in order to assess their habitability. It provides the capability to calculate similarity indices of different planetary candidates with respect to any reference values and any numerical parameter, yielding a more accurate evaluation of the survivability of different species. 

ExoPSI offers the ability to use any planet as a reference point and visualization functions that allow for easy comparison of the similarity between the interior and surface parameters of different planets. ExoPSI aims to help planetary sceince researches by offering a comprehensive solution for evaluating planetary similarities.

<hr>

### Installation

To Install ExoPSI simply use pip and type in the following command `pip install ExoPSI`.

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

The Planet Similarity Index (PSI) is the modified equivalent of the traditional Earth Similarity Index (ESI) and can be calculated for single or multiple planetary properties. As the name suggests it is used to find the simlarity between planets. ExoPSI offers the capability to use any planet as the reference planet. 

To utilise this functionality kindly use the `calc_psi` function.  The `calc_psi` function takes in the following inputs:
1) params - The dataset containing the values of the different parameters for which PSI is to be calculated.
2) upper lim - The list of upper limits for the given parameters.
3) lower lim - The list of lower limits for the given parameters.
4) ref val - The list of reference values for the given parameters.
5) threshold (optional) - The threshold value to be considered for very high similarity (default = 0.8).
6) int param (optional) - List of column names that contribute to interior PSI.
7) surf param (optional) - List of column names that contribute to surface PSI.
8) p index (optional) - A column (passed as a pandas data frame) that is to be used as the index for the table.

An example using the [the PHL’s Exoplanet Catalog]([url](https://phl.upr.edu/projects/habitable-exoplanets-catalog/hec-data-of-potentially-habitable-worlds/phls-exoplanets-catalog)) is given: 

<img width="703" alt="image" src="https://user-images.githubusercontent.com/69034801/229439158-a2306951-0a89-418a-b3bc-9e5ed94fc6b8.png">

and the output is: 

<img width="554" alt="image" src="https://user-images.githubusercontent.com/69034801/229439307-f1ed6ffa-841a-4d1e-bfa6-7b9870ff6679.png">

