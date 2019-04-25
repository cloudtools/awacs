## 0.9.0 (2019-04-16)
* Add missing actions (#115)
* Add missing services (#116)

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
