========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/rst-2-plain/badge/?style=flat
    :target: https://readthedocs.org/projects/rst-2-plain
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/github/1oglop1/rst-2-plain/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/1oglop1/rst-2-plain

.. |version| image:: https://img.shields.io/pypi/v/rst-2-plain.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/rst-2-plain

.. |wheel| image:: https://img.shields.io/pypi/wheel/rst-2-plain.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/rst-2-plain

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/rst-2-plain.svg
    :alt: Supported versions
    :target: https://pypi.org/project/rst-2-plain

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/rst-2-plain.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/rst-2-plain

.. |commits-since| image:: https://img.shields.io/github/commits-since/1oglop1/rst-2-plain/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/1oglop1/rst-2-plain/compare/v0.0.0...master



.. end-badges

A library and CLI tool to parse and translate reStructuredText into formatted plain text.

* Free software: MIT license

Installation
============

::

    pip install rst-2-plain

You can also install the in-development version with::

    pip install https://github.com/1oglop1/rst-2-plain/archive/master.zip


Documentation
=============


https://rst-2-plain.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
