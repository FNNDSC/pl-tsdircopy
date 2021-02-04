pl-tsdircopy
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-tsdircopy
    :target: https://hub.docker.com/r/fnndsc/pl-tsdircopy

.. image:: https://img.shields.io/github/license/fnndsc/pl-tsdircopy
    :target: https://github.com/FNNDSC/pl-tsdircopy/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-tsdircopy/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-tsdircopy/actions


.. contents:: Table of Contents


Abstract
--------

A plugin ts app to copy filtered output directories from many input plugin instances


Description
-----------

``tsdircopy`` is a ChRIS-based application to copy filtered output directories from many
input plugin instances.


Usage
-----

.. code::

    python tsdircopy.py
            [-h] [--help]
            [--json]
            [--man]
            [--meta]
            [--savejson <DIR>]
            [-v <level>] [--verbosity <level>]
            [--version]
            <outputDir>
            [--plugininstances <instances>]
            [-f <filter>] [--filter <filter>]


Arguments
~~~~~~~~~

.. code::

        [-h] [--help]
        If specified, show help message and exit.

        [--json]
        If specified, show json representation of app and exit.

        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.

        [--savejson <DIR>]
        If specified, save json representation file to DIR and exit.

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number and exit.

        [--plugininstances <instances>]
        If specified, it's a string representing a comma-separated list of plugin
        instance ids.

        [-f <filter>] [--filter <filter>]
        If specified, it's a string representing a comma-separated list of regular
        expressions.


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-tsdircopy tsdircopy --man

Run
~~~

You need you need to specify the output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u) -v $(pwd)/out:/outgoing      \
        fnndsc/pl-tsdircopy tsdircopy /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-tsdircopy .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-tsdircopy nosetests

Examples
--------

This example will copy all files in the output directories of plugin instances with id 1,3
and 7 that have `.dcm` extension.

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing fnndsc/pl-tsdircopy    \
    tsdircopy /outgoing --plugininstances "1,3,7" --filter "\.dcm$"


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
