Contributing
------------

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:


Types of Contributions
======================

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/rockymeza/django-local-requests/issues.

If you are reporting a bug, please include:

-  Your operating system name and version.
-  Any details about your local setup that might be helpful in troubleshooting.
-  Detailed steps to reproduce the bug.

Fix Bugs or Implement Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for bugs reports or feature requests. Should you
find anything interesting, please feel free to submit a pull request for it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

django-local-requests could always use more documentation, whether as
part of the official django-local-requests docs, in docstrings, or
even on the web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/rockymeza/django-local-requests/issues.

If you are proposing a feature:

-  Explain in detail how it would work.
-  Keep the scope as narrow as possible, to make it easier to implement.
-  Remember that this is a volunteer-driven project, and that contributions are
   welcome :)


Get Started!
============

Ready to contribute? Here's how to set up `django-local-requests` for local development.

1.  Fork the `django-local-requests` repo on GitHub.

2.  Clone your fork locally::

    $ git clone git@github.com:your_name_here/django-local-requests.git

3.  Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for local
    development::

    $ mkvirtualenv local_requests
    $ cd django-local-requests/
    $ pip install -r requirements-dev.txt

4.  Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass lint and the
    tests::

    $ make test
    $ make lint
    $ make test-all  # will test on different versions of Python and Django

6.  Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7.  Submit a pull request through the GitHub website.


Pull Request Guidelines
=======================

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.

2.  If the pull request adds functionality, the docs should be updated.

3.  Add your change to the ``HISTORY.rst`` section for the next release.

4.  The pull request should work for all the versions of Python and Django that
    we need to support. Check https://travis-ci.org/rockymeza/django-local-requests/pull_requests
    and make sure that the tests pass for all supported Python and Django
    versions. You can also run ``make test-all`` to test on all the target
    versions.
