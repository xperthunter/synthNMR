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


# SynthNMR Command Line Interface   
* SynthNMR can be used in a CLI.  
	- CLI organized in `specdb/specdb.py`.  
	- Commands:  
		- gen => generate images 
		- add => add generated images to a db
		- query => make a query against db
		- config => generate a form to generate images
		- img => make images from a SQL query against db
		- status => number of records in db
		- db => make a connection to a given db file

# Library module for SynthNMR
* libsynthnmr
	- connect to a db
	- generate images
	- query
	- config
	- img
	- status
	
	gen(kwargs?) send in a dictionary of parameters?