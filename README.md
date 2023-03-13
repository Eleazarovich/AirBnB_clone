![HBNB Image](https://camo.githubusercontent.com/70996d3dcffa41c27a6f5d59f56a42d978a4684c/687474703a2f2f696d6775722e636f6d2f4a42434d4844502e706e67)

# AirBnB_clone

## Description
The goal of the project is to deploy on the server a simple copy of the AirBnB website
This is the first step towards building your first full web application: the AirBnB clone.

## Usage
- First, clone the repository into your directory.
    ```
    $ git clone https://github.com/Eleazarovich/AirBnB_clone
    ```

- Run the executable `./console.py`

- Type help for a list of the commands available with console.py.
    help is an action provided by default by cmd.
    Enter help + command for information about respective command and usage.

### Documented commands (type help <topic>):
========================================

```
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help   show

(hbnb) create City
4af7890c-007f-42ff-97d8-074214f1094f
(hbnb) show City 4af7890c-007f-42ff-97d8-074214f1094f
[City] (4af7890c-007f-42ff-97d8-074214f1094f) {'id': '4af7890c-007f-42ff-97d8-074214f1094f',
 'updated_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679386), '__class__': 'City',
 'created_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679362)}
(hbnb)$
```

- quit -- exits the program

- EOF -- exits the program

### Execution
#### interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Files
 | File | Description |
 | ------------- | ------------- |
 | console.py | entry point of the command interpreter |
 | models/init.py | creates an instance of FileStorage |
 | models/base_model.py | class BaseModel that defines all common attributes/methods for other classes |
 | models/amenity.py | class Amenity, inherits from BaseModel |
 | models/city.py | class City, inherits from BaseModel |
 | models/place.py | class Place, inherits from BaseModel |
 | models/review.py | class Review, inherits from BaseModel |
 | models/state.py | class State, inherits from BaseModel |
 | models/user.py | class User, inherits from BaseModel |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | tests/ | folder where are all the tests of the program |

 ## Bugs
No known bugs at this time. 

## Authors
**Eleazar Nhamuave**

## License
Public Domain. No copy write protection.
