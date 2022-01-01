## 2.1.0 (2022-01-01)
* Update base url used by scraper
* Make scraper resilient to base url changes
* Run tests against Python 3.10 and add trove classifier
* Action Update 2021-47
* Action Update 2021-48
* Action Update 2021-49
* Action Update 2021-50
* Remove workaround from scraper
* Action Update 2021-52
* Remove support for Python 3.6 due to EOL

## 2.0.2 (2021-10-16)
* Fix scraper and improve error messages
* Stop “caching” prop names
* Fix scraper to deal with AWS doc changes
* Action Update 2021-41

## 2.0.1 (2021-08-30)
* Action Update 2021-29
* Action Update 2021-34
* Action Update 2021-35

## 2.0.0 (2021-07-05)
This release now only supports Python 3.6+
Special thanks to @michael-k for the Python 3 work and tooling improvements.

* Changes for Python 3.6+ (deprecating Python 2.x)
* Update generated files for Python 3.6+
* Update Python3 changes per review feedback
* Do not hardcode partition if region isn't
* Bump httpx[http2] from 0.16.1 to 0.17.0 in /scrape
* Properly chain exception
* Fix imports for 'Amazon Mechanical Turk Crowd'
* Switch from Travis CI to GitHub Actions and use tox
* Update manifest and check it with 'check_manifest'
* Change packaging to use declarative config in setup.cfg
* Add a release workflow
* Tweaks for "make test"
* Format the project files and auto-generate code for black code formatting
* Deprecate legacy ARN generation
* Run black on examples
* Regenerate awacs code with black code formatting
* Black format crowd.py
* Changes for "make test" to work properly with black formatting
* Add new tools to requirements.txt and run black/isort during scrape
* Run isort on project files
* Per review feedback, remove arbitrary indenting and use black for formatting
* Bump httpx[http2] from 0.17.0 to 0.17.1 in /scrape
* Use Python 3 way to call super()
* Add type hints
* Regenerate awacs code with type hints
* Check type hints with mypy
* Add 'py.typed' for PEP 561 compat
* Stop inheriting from object explicitly
* Remove 'u' prefix from strings
* Bump lxml from 4.6.2 to 4.6.3 in /scrape
* Fix scrape breakage by mapping "Amazon API Gateway Management V2" to "apigateway"
* Add mypy dependency
* Action Update 2021-12
* Action Update 2021-14
* New actions for services and adds mgm (application migration service)
* Action Update 2021-15
* Action Update 2021-16
* Action Update 2021-19
* Remove aws.ARN
* Bump pyflakes from 2.3.0 to 2.3.1 in /scrape
* Bump httpx[http2] from 0.17.1 to 0.18.1 in /scrape
* Bump tox from 3.23.0 to 3.23.1 in /scrape
* Bump black from 20.8b1 to 21.5b1 in /scrape
* Bump aiofiles from 0.6.0 to 0.7.0 in /scrape
* Action Update 2021-20
* Add static definitions for Conditions to allow for better linting
* Action Update 2021-26
* Bump black from 21.5b1 to 21.6b0 in /scrape
* Do not remove account and region from non-bucket s3 ARNs
* Bump httpx[http2] from 0.18.1 to 0.18.2 in /scrape
* Bump mypy from 0.812 to 0.910 in /scrape
* Fix syntax error in comment
* Bump isort from 5.8.0 to 5.9.1 in /scrape
* Use PyPA's `build` project to build sdist and wheel
* Action Update 2021-26

## 1.0.4 (2021-03-20)
* Action Update 2021-11
* Fix scrape breakage by mapping "Amazon Simple Email Service v2" to "ses"
* Map lambda to awslambda and remove lambda.py
* Action Update 2021-11
* Update copyright date
* Update "make test" to not use the deleted tools directory
* Fix pycodestyle issue with using a lambda in scrape.py

## 1.0.3 (2021-03-08)
* Fix typo in CHANGELOG
* Action Update 2021-04
* Update scrape requirements versions
* Action Update 2021-05
* Fix scrape breakage by mapping "Amazon Lex V2" to "lex"
* Allow manual workflow via workflow_dispatch
* Action Update 2021-10

## 1.0.2 (2021-01-20)
* Action Update 2020-44
* Action Update 2020-45
* Action Update 2020-46
* Action Update 2020-47
* Action Update 2020-48
* Action Update 2020-49
* Action Update 2020-50
* Action Update 2020-51
* Action Update 2020-52
* Action Update 2020-53
* Action Update 2021-01
* Action Update 2021-02
* Fix scrape script breakage
* Action Update 2021-03

## 1.0.1 (2020-10-19)
* Action Update 2020-42
* Action Update 2020-43

## 1.0.0 (2020-10-04)
* Big thanks to @michael-k for the greatly improved code generation!
* Replace the generator tool
* Add all missing actions, fix service names, and remove duplicates
* Add a GitHub Action that regularly updates the IAM actions
* Drop support for Python 3.5
* [travis] Remove `./scrape` if Python <3.6 to avoid invalid syntax errors

## 0.9.9 (2020-09-26)
* Add 291 new actions (#142)
* Add codeartifact actions (#145)
* Add 380 new actions (#148)
* change isinstance AWSHelperFn to inspect class names (#141)

## 0.9.8 (2020-02-25)
* Add 375 new actions (#140)

## 0.9.7 (2019-12-08)
* Make Python 3.8 support official (#136)
* Add 98 new actions from updates in August/September (#134)
* Add 121 new actions from updates in October and 1/3 November (#138)

## 0.9.6 (2019-08-25)
* Add 95 new actions from updates in first half of August (#133)

## 0.9.5 (2019-07-29)
* Add 60 new actions from July updates (#132)

## 0.9.4 (2019-06-25)
* Add 52 new actions from June updates (#130)

## 0.9.3 (2019-06-23)
* Include 'Periodic update - 05/28/19-10:23am PDT' (#128)
* Bugfix cognito_idp deleted actions, and add 'ManageConnections' to execute_api: (#129)

## 0.9.2 (2019-05-19)
- Add missing glue actions using the official latest docs (#120)
- Support Python 3.6 and 3.7; discourage usage of 3.4 (#122)
- Add new actions (#123)

## 0.9.1 (2019-05-05)
- Add missing glue actions using the official latest docs (#120)
- Support Python 3.6 and 3.7; discourage usage of 3.4 (#122)
- Add new actions (#123)

## 0.9.0 (2019-04-16)
- Add missing actions (#115)
- Add missing services (#116)

## 0.8.3 (2019-02-23)
- Fix condition string spelling (#112)
- Add missing actions for Firehose (#113)
- Unify shell prompt and add missing newline in README (#114)

## 0.8.2 (2019-01-22)
- Update actions to kinesis (#106)
- Adding missing ssmmessages (#107)
- Add secrets manager  (#108)
- Add actions for QuickSight (#109)
- Fix a typo in tools/gen.py (#110)
- Misc changes from running gen.py

## 0.8.1 (2018-09-10)
- Add new glue actions

## 0.8.0 (2018-07-22)
- Define hash and equality (#87)
- Add ObjectOwnerOverrideToBucketOwner and ReplicateTags to S3 (Replaces #88)
- Add UpdateInstanceInformation to SSM (Replaces #89)
- Add CloudWatch dashboard actions (Fixes #91)
- Updating actions (#102)
- Emit proper ARN's for regionless services (#103)
- Add overrides to include dynamodb DescribeTimeToLive and UpdateTimeToLive
- refactor awacs/helpers/trust.py
- Output type error correctly
- Added support for Lambda@Edge execution role
- Added version
- Remove deprecated 3.3

## 0.7.2 (2017-10-27)
- Update actions as of 10-26-17 (#86)
- Update extra_actions list to relect policies.js updates

## 0.7.1 (2017-09-23)
- Update services
- Add instructions for adding new actions
- Tweak ARN partition method and add tests
- Allow CanonicalUser for  Principal (Fixes #80)
- Introduce PolicyDocument class (#81)
- Update actions to include GetParametersByPath (#82)
- Update gen.py (#83)
- Generate valid ARNs for GovCloud and CN partitions of AWS in BaseARN (#85)
- Add SSM GetParameter
- Add ssm GetParametersByPath override

## 0.7.0 (2017-07-25)
- Create generic assume role policy generator (#64)
- Create CODE_OF_CONDUCT.md (#69)
- Update example in README (#71)
- Add kms tagresource/untagresource actions (#73)
- Add actions for HTTP methods in ES (#74)
- Add helper for get_ecs_task_assumerole_policy (#76)
- Adding in missing lambda actions (#77)
- Enable early validation of Principal strings (#78)
- Don't try to use `type` since it is never set (#79)
- Add support for ForAllValues and ForAnyValues
- Add MultiFactorAuthPresent policy condition constant
- Add SourceAccount constant
- Add codedeploy trust helper
- Colorize README.rst
- Add extra actions missing from AWS policies.js via gen.py
- Update actions
  - Added new codecommit and cloudformation actions
  - Sorted the action lists
- Update services
  - Update all services
  - Add new services:
    - athena, clouddirectory, codestar, dax, lex, organizations
    - snowball, states, tag

## 0.6.2 (2017-02-20)
- Service updates
  - Update all services
  - Add new services: batch, cognito_idp, cur, mobiletargeting, waf_regional
- Add update of github Releases page to RELEASE doc

## 0.6.1 (2016-12-30)
- Service updates
  - Update all services
  - Add new services:
    application_autoscaling, budgets, codebuild, health, kinesisanalytics,
    lightsail, opsworks_cm, polly, rekognition, servicecatalog, shield, xray
- Fix pycodestyle issues with tests

## 0.6.0 (2016-07-07)
- Add Null Condition operator (#42)
- Update services (#47)
   - Update services to latest IAM policies
   - Add Action helper to each service
   - Update generator tool for new ARN and input workarounds
   - Make sure filenames don't use illegal "-"
   - Remove renamed zocalo and deprecated whispersync
- Rename lambda to awslambda and update services (Fixes #44) (#51)

## 0.5.4 (2016-03-01)
- Add Elasticsearch Service [GH-29]
- Add KMS [GH-30]
- Update Elasticache, add CodeDeploy & CodeCommit [GH-31]
- Add ARN to CodeDeploy module [GH-33]
- Lambda Trust Policy [GH-35]
- EC2 Container Registry [GH-36]

## 0.5.3 (2015-09-07)
- Add EC2 Action [GH-26]
- Add Kinesis Calls [GH-27]
- Add Cloudformation actions [GH-28]

## 0.5.2 (2015-07-19)
- Add ECS Assume Role policy trust helper - GH-24
- Add new Route53 Actions - GH-23
- Add ELB ARN & update actions - GH-22

## 0.5.1 (2015-05-05)
- Add ECS support GH-18
- Add get\_default\_assumerole\_policy GH-17
- Add EnterStandby, ExitStandby Actions - GH-13
- Allow "\*" Principal - GH-16, GH-19

## 0.5.0 (2015-02-27)
- New/update actions - GH-7
- Support wildcard action - GH-8
- Added new autoscaling API endpoints - GH-10
- Add EC2 specific ARN class - GH-11

## 0.4.2 (2014-07-31)
- Base ARN class has extra self bug

## 0.4.1 (2014-07-29)
- Typo on SDB ARN class fix.

## 0.4.0 (2014-07-28)
- Moved to new style ARN classes, using existing service namespaces.
