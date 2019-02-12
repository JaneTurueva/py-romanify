romanify
====

.. image:: https://coveralls.io/repos/github/JaneTurueva/py-romanify/badge.svg?branch=master
    :target: https://coveralls.io/github/JaneTurueva/py-romanify?branch=master
    :alt: Coveralls

.. image:: https://travis-ci.org/JaneTurueva/py-romanify.svg
    :target: https://travis-ci.org/JaneTurueva/py-romanify
    :alt: Travis CI

.. image:: https://img.shields.io/pypi/v/romanify.svg
    :target: https://pypi.python.org/pypi/romanify/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/wheel/romanify.svg
    :target: https://pypi.python.org/pypi/romanify/

.. image:: https://img.shields.io/pypi/pyversions/romanify.svg
    :target: https://pypi.python.org/pypi/romanify/

.. image:: https://img.shields.io/pypi/l/romanify.svg
    :target: https://pypi.python.org/pypi/romanify/


Roman numbers converting library.

Library uses following mapping:

========  ===========
Arabic    Roman
========  ===========
M         1000
CM        900
D         500
CD        400
C         100
XC        90
L         50
XL        40
X         10
IX        9
V         5
IV        4
I         1
========  ===========

Installation
------------

.. code-block:: shell

    pip install romanify


Command-line usage
------------------
.. code-block:: shell

    romanify 101
    > CI


Library usage
-------------
.. code-block:: shell

    from romanify import arabic2roman

    print(arabic2roman(101))


Versioning
==========

This software follows `Semantic Versioning`_

.. _Semantic Versioning: http://semver.org/