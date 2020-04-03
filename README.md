# synthNMR
Python module to make synthetic protein NMR spectra.

# Repository Organization
```
synthNMR                                                                       
├── data                                                                         
├── docs                                                                         
├── synthnmr                                                                     
│   └── tests                                                                    
└── tools 
```
* **data**
	- Save images
	- Statistics or metrics
	- Database versions
* **docs**
	- Documentation for making synthetic spectra 
		- Methods: Random, Uniform, Chemical-Shift
		- Usage of SQLite to store spectra and experiments 
* **synthnmr**
	- Will be the module we are building
	- both the spectra construction and spectra saving
		- do we want to worry about spectra saving in synthnmr?
		- only worry about synthetic nmr data set construction?
		- also would like to make time-domain data as well 
* **tools**
	- auxillary tools for synthNMR
	- using synthnmr functions
	
