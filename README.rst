simplicity
==========

Converts ReStructuredText into JSON.

Usage
-------

Input

.. code-block:: RestructuredText

    Python
    ------
    :age: 22
    :typing: dynamic, strong
    
    Java 
    ----
    :age: 18
    :typing: static, strong
    
Output

.. code-block:: JavaScript

    [
        {"Python":
            {"age": 22, "typing": "dynamic, strong"}
        },
        {"Java":
            {"age": 18, "typing": "static, strong"}
        },
    ]
    
Try it out!
------------

.. code-block:: bash

    $ git clone git@github.com:pydanny/simplicity.git
    $ cd simplicity/
    $ python simplicity.py sample.rst
    <type 'str'>
    [{"Python": {"age": 22, "typing": "dynamic, strong"}},
    {"Java ": {"age": 18, "typing": "static, strong"}},
    {"GitHub": {"url": "https://github.com", 
        "description": "Build software better, together."}}]
