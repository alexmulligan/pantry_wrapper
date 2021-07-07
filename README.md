# pantry_wrapper - A tiny and simple Python wrapper for the Pantry API

## Purpose

pantry_wrapper aims to cut down the code you need to make calls to the Pantry API.

"Pantry is a free service that provides perishable data storage for small projects." Basically, it's a JSON-based database with an simple API. Learn more about Pantry [on their website](https://getpantry.cloud) and [on their GitHub page](https://github.com/imRohan/Pantry)

It started as some functions I wrote for a personal project to get rid of repetitive code for API calls.  I wanted to package it up and publish the source so I could easily use it for future projects and so others could use it too.

However, it doesn't include any new or special features, just a few functions which make calls to the API.  The wrapper is meant to turn ~5 lines of repetitive code into 1 each time you make an API call.

<br>

## Features

The main features of pantry_wrapper are:

* Lightweight - it's a very simple wrapper, around 40 lines of actual code in just one file
* Simple - the repetitive things like making the URL, setting headers, and choosing request type are already done; all you need to make an API call is a single function
* Compatibility - Works with Python 3.6+ on any platform, and the only dependency is the [requests](https://pypi.org/project/requests/) package

<br>

## Installing

Here's some ways you can install/use pantry_wrapper:

* Clone this repository and include the ```pantry_wrapper.py``` file in your project's source directory
* Clone this repository and copy the ```pantry_wrapper.py``` file to the ```site-packages``` folder of your Python installation to manually install it
* PyPi package coming soon

<br>

## Documentation

### Quick Example - getting data from Pantry basket:

```python
from pantry_wrapper import *

my_pantry_id = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'

try:
	data = get_contents(my_pantry_id, 'my_basket', return_type='body')
	print(data)
	
except:
	print('Error: call failed')
```

In this example, we made a call to the Pantry API to get the data stored in a basket called 'my_basket'.  For the ```get_contents()``` function, you only need your pantry id (get one [here](https://getpantry.cloud)) and the basket name.  However, here we explicity tell it to return the body of the response.  This will automatically convert the JSON data in the body from a string to a Python dict.  
(See the Configuration part under Documentation for more information about the return type.)

It's also worth noting that we use a try/except structure in our example code.  TODO: finish this part

<br>

### Functions

TODO: write documentation for each function

<br>

### Configuration

There is actually only one option to configure - the return type for all the functions.

There is a value defined at the top of the ```pantry_wrapper.py``` file, called ```DEFAULT_RETURN_TYPE``` which is normally defined as ```'response'```  
This can either be 'response' or 'body'.  TODO: finish this part

<br>

## Contact

Alexander Mulligan - alexjmulligan@gmail.com - [github.com/alexmulligan](https://github.com/alexmulligan)

Project Link: https://github.com/alexmulligan/pantry_wrapper

<br>

## Acknowledgements

Rohan Likhite - creator of Pantry - [github.com/imRohan](https://github.com/imRohan)

Pantry - [Website](https://getpantry.cloud) - [Github](https://github.com/imRohan/Pantry)
