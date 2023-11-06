``python-pushover2`` aims at providing comprehensive Python bindings for the API
of the `Pushover Notification Service`_ as documented here__.

.. _Pushover Notification Service: https://pushover.net/ 
.. __: https://pushover.net/api

**This is a fork of python-pushover with patches for Python 3**

**No other changes have been made**

Installation
------------

You can install python-pushover2 from Pypi_ with:

.. code-block:: bash

    $ pip install python-pushover2

Or you can install it directly from GitHub_:

.. code-block:: bash

    git clone https://github.com/m4rkw/python-pushover2.git
    cd python-pushover2
    pip install .

.. _Pypi: https://pypi.python.org/pypi/python-pushover2/
.. _GitHub: https://github.com/m4rkw/python-pushover2

Overview
--------

After being imported, the module must be initialized by calling the ``init``
function with a valid application token. Thus, a typical use of the
``pushover`` module looks like this:

.. code-block:: python

    from pushover import init, Client

    init("<token>")
    Client("<user-key>").send_message("Hello!", title="Hello")

You can also pass the ``api_token`` optional argument to ``Client`` to
initialize the module at the same time:

.. code-block:: python

    from pushover import Client

    client = Client("<user-key>", api_token="<api-token>")
    client.send_message("Hello!", title="Hello")

Attachments can be sent with the ``attachment`` parameter which takes as
argument as file object:

.. code-block:: python

    with open('/path/to/my/image.png', 'rb') as image:
        client.send_message('Message with image', attachment=image)

Command line
~~~~~~~~~~~~

``python-pushover2`` also comes with a command line utility ``pushover`` that
you can use as follows:

.. code-block:: bash

    pushover --api-token <api-token> --user-key <user-key> "Hello!"

Use ``pushover --help`` to see the list of available options.

Configuration
~~~~~~~~~~~~~

Both the ``pushover`` module and the ``pushover`` command line utility support
reading arguments from a configuration file.

The most basic configuration file looks like this:

.. code-block:: ini

    [Default]
    api_token=aaaaaa
    user_key=xxxxxx

You can have additional sections and specify a device as well:

.. code-block:: ini

    [Sam-iPhone]
    api_token=bbbbbb
    user_key=yyyyyy
    device=iPhone

``python-pushover2`` will attempt to read the configuration from
``~/.pushoverrc`` by default. The section to read can be specified by using the
``profile`` argument. With the configuration file above, you can send a message
by simply doing:

.. code-block:: python

    from pushover import Client

    Client().send_message("Hello!", title="Hello")

or ``pushover --title "Hello" "Hello!"`` from the command line.

API
---

You can access the full API documentation here__.

.. __: http://pythonhosted.org/python-pushover/#module-pushover
