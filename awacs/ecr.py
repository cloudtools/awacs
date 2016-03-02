from aws import Action, BaseARN

service_name = 'AWS EC2 Container Registry'
prefix = 'ecr'


class ARN(BaseARN):
    def __init__(self, resource='*', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class ECRAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


BatchCheckLayerAvailability = ECRAction('BatchCheckLayerAvailability')
BatchDeleteImage = ECRAction('BatchDeleteImage')
BatchGetImage = ECRAction('BatchGetImage')
CompleteLayerUpload = ECRAction('CompleteLayerUpload')
CreateRepository = ECRAction('CreateRepository')
DeleteRepository = ECRAction('DeleteRepository')
DeleteRepositoryPolicy = ECRAction('DeleteRepositoryPolicy')
DescribeRepositories = ECRAction('DescribeRepositories')
GetAuthorizationToken = ECRAction('GetAuthorizationToken')
GetDownloadUrlForLayer = ECRAction('GetDownloadUrlForLayer')
GetRepositoryPolicy = ECRAction('GetRepositoryPolicy')
InitiateLayerUpload = ECRAction('InitiateLayerUpload')
ListImages = ECRAction('ListImages')
PutImage = ECRAction('PutImage')
SetRepositoryPolicy = ECRAction('SetRepositoryPolicy')
UploadLayerPart = ECRAction('UploadLayerPart')
