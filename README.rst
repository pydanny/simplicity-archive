==========
simplicity
==========

Converts ReStructuredText into JSON. 

* **Sections** are JSON list dictionary elements 
* **Section Headers**  become list titles.
* **Field** definitions become key/value representations

Example
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
        {"title": "Python", "age": 22, "typing": "dynamic, strong"}
        {"title": "Java", "age": 18, "typing": "static, strong"}
    ]
    
Usage
------

.. code-block:: bash

    $ git clone git@github.com:pydanny/simplicity.git
    $ cd simplicity/
    $ python simplicity.py sample.rst
    [
        {
            "description": "A fun programming language.\n\nUsed to build simplicity!",    
            "title": "Python",
            "price": 0.0,
            "typing": "dynamic, strong",
            "age": 22,
            "mascot": "snake"
        },
        {
            "age": 18,
            "typing": "static, strong",
            "mascot": "???",
            "title": "Java"
        },
        {
            "url": "https://github.com",
            "mascot": "Octocat",
            "title": "GitHub"
        }
    ]


Best Used With
----------------

Simplicity is designed to be used with these packages:

* Complexity_: A refreshingly simple static site generator, for those who like to work in HTML.
* `redis-py`_: Redis Python Client

.. _Complexity: https://github.com/audreyr/complexity
.. _`redis-py`: https://github.com/andymccurdy/redis-py


Know of any other good uses for Simplicity? Let me know and I'll add it to the list!

Examples
---------

* https://github.com/pydanny/simplicity-complexity-example
