=======
Tombola
=======

*La Vida Es Una Tombola*

Tombola is a small web application prototype written in Python that shows
random words from a dictionary in cycle.

That its, the dictionary is randomly shuffled and then words are served until
exhausted. Then the dictionary is randomly shuffled again and the process
repeats.


Deployment
==========

.. code-block:: text

   docker run --detach --publish=8000:8000 kuralabs/tombola:latest

To create your own words dictionary create a file `words.txt` with one word(s)
to show per line. For example:

.. code-block:: text

   hello world
   good bye
   my friend

Then, mount it to the container as follows:

.. code-block:: text

   docker run --volume /path/to/mywords.txt:/src/words.txt --detach --publish=8000:8000 kuralabs/tombola:latest


Development
===========

A Python environment with Tox_ is required.

.. _Tox: https://tox.readthedocs.io/

To run the application in development mode:

.. code-block:: text

   tox

The application will be available in http://localhost:8000/

Optionally, the Docker image can be built with:

.. code-block:: text

   tox -e build


License
=======

.. code-block:: text

   Copyright (C) 2020 KuraLabs S.R.L

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.
