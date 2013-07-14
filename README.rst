simplicity
==========

Converts ReStructuredText into JSON

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
    