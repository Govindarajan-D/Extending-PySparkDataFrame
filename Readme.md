# Wheel package Instructions
## Files
EnhancedDataFrame <br/>
--__init__.py - Imports * from the .py file <br/>
--EnhancedDataFrame.py - Contains the newly defined methods <br/>
setup.py - Contains the code for setting up the wheel file <br/>

## Creating and using wheel package
Run the following code and in the dist directory, you will find the whl package. 
```
 python setup.py sdist bdist_wheel
```
You can install this in the Databricks cluster, use the following command and you will be able to use the functions with the DataFrame object
```
import EnhancedDataFrame
```
