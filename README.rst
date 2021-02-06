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

A plugin ts app to efficiently copy one or more obj storage directories.


Description
-----------

``tsdircopy`` is a ChRIS-based application to efficiently copy the *contents* of one or more obj
storage directories, given by the `--dir` argument, to its output directory. This argument is a
string containing one or more directories separated by comma.
Unlike `dircopy` it doesn't create a new feed and unlike `dsdircopy` it doesn't require
a input dir positional argument.


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
            [--dir <DIR>]
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

        <outputDir>
        Output directory.

        [--dir <DIR>]
        Required, it's a string representing a comma-separated list of one or more
        directories.

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
        fnndsc/pl-tsdircopy tsdircopy /outgoing --dir <DIR>


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

This example will copy all files in the `cube/uploads` and `SERVICES/PACS/BCH` directories
into the output dir. Note: This is a utility 'ts' plugin that only works in the context of
the ChRIS platform.

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing fnndsc/pl-tsdircopy    \
    tsdircopy /outgoing --dir 'cube/uploads,SERVICES/PACS/BCH'


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
