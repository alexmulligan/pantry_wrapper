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

It's also worth noting that we use a try/except structure in our example code. pantry_wrapper purposely does not perform any error handling or response checking - this is because I believe it's simpler and more efficient to let the user handle errors, the way they want to handle them. If pantry_wrapper did more than just make API calls, error handling could be useful.  But right now, I think it's better to wrap the pantry_wrapper function in a try/except structure and handle errors however they should be handled for each program.

<br>

### Functions

To better understand the calls these functions make, read through the [Pantry API Documentation](https://documenter.getpostman.com/view/3281832/SzmZeMLC) as well

<br>

pantry_info

> returns info about the pantry, including a list of baskets stored inside

Usage:

```python
pantry_info(pantry_id: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]
```

Example:

```python
>>> pantry_info(my_pantry_id, return_type='body')
{
	'name': 'pantrydb',
	'description': 'defaultDescription',
	'errors': [],
	'notifications': True,
	'percentFull': 1,
	'baskets': ['picnic']
}
```

<br>

get_contents

> returns full contents of a basket

Usage:

```python
get_contents(pantry_id: str, name: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]
```

Example:

```python
>>> get_contents(my_pantry_id, 'my_basket', return_type='body')
{
	'first_name': 'John',
	'last_name': 'Smith',
	'age': 27,
	'colors': ['blue', 'red', 'yellow']
}
```

<br>

create_basket

> creates a new basket or replaces an existing one

Usage:

```python
create_basket(pantry_id: str, name: str, contents: dict, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]
```

Example:

```python
>>> data = {
	'first_name': 'Izzy',
	'last_name': 'Barnes',
	'colors': ['orange']
}

>>> create_basket(my_pantry_id, 'my_other_basket', data, return_type='body')
'Your Pantry was updated with basket: my_other_basket!'
```

<br>

append_basket

> appends contents to new or existing basket; will overwrite values of existing keys and append values to nested objects or arrays.  
> returns the updated contents of the basket

Usage:

```python
append_basket(pantry_id: str, name: str, contents: dict, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]
```

Example:

```python
>>> data = {
	'age': 24,
	'colors': ['green', 'purple']
}

>>> append_basket(my_pantry_id, 'my_other_basket', data, return_type='body')
{
	'first_name': 'Izzy',
	'last_name': 'Barnes',
	'age': 24,
	'colors': ['orange', 'green', 'purple']
}
```

<br>

delete_basket

> deletes entire basket and its contents

Usage:

```python
delete_basket(pantry_id: str, name: str, return_type: str=DEFAULT_RETURN_TYPE) -> Union[str, dict]
```

Example:

```python
>>> delete_basket(my_pantry_id, 'my_other_basket', return_type='body')
'my_other_basket was removed from your Pantry!'
```

<br>

### Configuration

There is actually only one option to configure - the return type for all the functions.

There is a value defined at the top of the ```pantry_wrapper.py``` file, called ```DEFAULT_RETURN_TYPE``` which is normally defined as 'response'. This can be defined as either 'body' or 'response'.

'response' will return an entire Response object from the requests module.  From here, you can get the header, the body, the response code, etc.

'body' will return the just the body of the response.  If the body is JSON, it will automatically convert the data and return a Python dict.  If not, it will just return the data as a string.

If you want to globally change the return type, you can manually edit the ```pantry_wrapper.py``` file and change the ```DEFAULT_RETURN_TYPE``` value (at the top).

If you want to specify the return type each time you call a function, you can pass the optional keyword argument ```return_type```.  Like before, this can either be 'response' or 'body', and it will change the return type for the current function.  To see this used, look at the code under the Quick Example section.

<br>

## Contact

Alexander Mulligan - alexjmulligan@gmail.com - [<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/alexmulligan)

Project Link: https://github.com/alexmulligan/pantry_wrapper

<br>

## Acknowledgements

Rohan Likhite - creator of Pantry - [<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/imRohan)

Pantry - [Website](https://getpantry.cloud) - [<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>](https://github.com/imRohan/Pantry)
