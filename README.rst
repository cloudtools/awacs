=====
awacs
=====

.. image:: https://img.shields.io/pypi/v/awacs.svg
    :target: https://pypi.python.org/pypi/awacs

.. image:: https://travis-ci.org/cloudtools/awacs.png?branch=master
    :target: https://travis-ci.org/cloudtools/awacs

.. image:: https://img.shields.io/pypi/l/awacs.svg
    :target: https://opensource.org/licenses/BSD-2-Clause

About
=====

awacs - Amazon Web Access Control Subsystem

The awacs library allows for easier creation of AWS Access Policy
Language JSON by writing Python code to describe the AWS policies.
To facilitate catching  policy format or JSON errors early the
library has property and type checking built into the classes.

**NOTE:** The old *awacs.aws.Policy* object is going to be deprecated in the
future, in preference for the *awacs.aws.PolicyDocument* class. This is due
to confusion that arises between the old object and *troposphere.iam.Policy*
objects.


Installation
============

awacs can be installed using the pip distribution system for python by
issuing:

.. code-block:: sh

  $ pip install awacs

Alternatively, you can run use setup.py to install by cloning this repository
and issuing:

.. code-block:: sh

  $ python setup.py install

Examples
========

An example to use this comes from the `AWS IAM`_ documentation.
This shows creating policy attached to an Amazon S3 bucket:

.. code-block:: python

  from awacs.aws import Action, Allow, PolicyDocument, Principal, Statement
  from awacs.iam import ARN as IAM_ARN
  from awacs.s3  import ARN as S3_ARN

  account = "123456789012"
  user = "user/Bob"

  pd = PolicyDocument(
      Version="2012-10-17",
      Id="S3-Account-Permissions",
      Statement=[
          Statement(
              Sid="1",
              Effect=Allow,
              Principal=Principal("AWS", [IAM_ARN(user, '', account)]),
              Action=[Action("s3", "*")],
              Resource=[S3_ARN("my_corporate_bucket/*"),],
          ),
      ],
  )
  print(pd.to_json())

would produce this json policy:

.. code-block:: json

  {
      "Id": "S3-Account-Permissions", 
      "Statement": [
          {
              "Action": [
                  "s3:*"
              ], 
              "Effect": "Allow", 
              "Principal": [
                  {
                      "AWS": [
                          "arn:aws:iam::123456789012:user/Bob"
                      ]
                  }
              ], 
              "Resource": [
                  "arn:aws:s3:::my_corporate_bucket/*"
              ], 
              "Sid": "1"
          }
      ], 
      "Version": "2012-10-17"
  }

Community
=========

We have a google group, cloudtools-dev_, where you can ask questions and
engage with the cloudtools/awacs community.  Issues & pull requests are always
welcome!

.. _`AWS IAM`: http://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html
.. _cloudtools-dev: https://groups.google.com/forum/#!forum/cloudtools-dev

Contributing new actions
========================

To update actions there is a generator tool which will pull policies from
an AWS resource and auto-generate new files.
The following commands can be run to update the repo:

.. code-block:: sh

  $ pip install -r tools/requirements.txt
  $ rm -rf generated/
  $ python tools/gen.py
  $ diff -u awacs generated
  $ mv generated/*.py awacs
  $ git diff

Since not all of the actions appear in the AWS policy file it is sometimes
required to add these extra actions to the tools/gen.py file.
