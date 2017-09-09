Postdown
=========

|Python Version| |PyPI version|

  *Generate markdown API document from Postman.*

Installation
-------------

.. code:: shell

  pip install postdown


Usage
------

* **Export JSON from postman**
 Export your collection from Postman(Only support to Collection v2 for now).
 You could get a JSON file.

 .. figure:: https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-1.png

 Step One: Select the collection which you wanna export.


 .. figure:: https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-2.png

 Step Two: Find the import button and click it.


 .. figure:: https://raw.githubusercontent.com/TitorX/Postdown/master/imgs/step-3.png

 Step Three: Export your collection as *collection v2*.



* **Run** ``postdown`` **to generate markdown document.**
 .. code:: shell

   postdown xxx.json xxx.md


And you will get your API document which is markdown formatting.

`Click here to see an example generated. <https://github.com/TitorX/Postdown/tree/master/demo>`_





.. |Python Version| image:: https://img.shields.io/badge/python-2&3-brightgreen.svg?style=flat-square
  :target: https://pypi.python.org/pypi/Postdown
.. |PyPI version| image:: https://img.shields.io/pypi/v/Postdown.svg?style=flat-square
  :target: https://pypi.python.org/pypi/Postdown


