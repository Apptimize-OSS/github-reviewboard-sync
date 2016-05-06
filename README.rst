===============================
github-reviewboard-sync
===============================

.. image:: https://img.shields.io/pypi/v/github-reviewboard-sync.svg
        :target: https://pypi.python.org/pypi/github-reviewboard-sync

.. image:: https://img.shields.io/travis/Apptimize-OSS/github-reviewboard-sync.svg
        :target: https://travis-ci.org/timmartin19/github-reviewboard-sync

.. image:: https://readthedocs.org/projects/github-reviewboard-sync/badge/?version=latest
        :target: http://github-reviewboard-sync.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Syncs pull requests with ReviewBoard submissions allowing you to create a pull request and review board submission at the same time

* Free software: MIT license
* Documentation: https://github-reviewboard-sync.readthedocs.org


Overview
--------

This tool allows you to easily create a pull request and reviewboard submission at the same time

.. code-block:: bash

    grs open my-feature-branch --github-username=MyUsername

You can also simply provide an environment variable ``GITHUB_USERNAME`` instead of
passing in your github username.  To add it to your bash profile simply run the following

.. code-block:: bash

    echo 'export GITHUB_USERNAME=MyUsername' >> ~/.bash_profile

If you want to compare against a different branch and open a pull request to that branch

.. code-block:: bash

    grs open my-feature-branch --base=version-branch

If you want to update an existing review board submission

.. code-block:: bash

    grs open my-feature-branch -u


Installation
------------

.. code-block:: bash

    pip install github-reviewboard-sync

Or if you prefer

.. code-block:: bash

    easy_install github-reviewboard-sync

Features
--------

* Opens a pull request on github with a sane name and message based on commits
* Opens/updates a submission on review board with a sane summary and description based on commits
* Adds github pull request url to review board submission and vice versa

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
