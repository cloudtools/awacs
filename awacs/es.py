from aws import Action, BaseARN

service_name = 'Amazon Elasticsearch Service'
prefix = 'es'


class ARN(BaseARN):
    def __init__(self, resource="*", region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


class ESAction(Action):
    def __init__(self, action=None):
        self.prefix = prefix
        self.action = action


AddTags = ESAction('AddTags')
CreateElasticsearchDomain = ESAction('CreateElasticsearchDomain')
DeleteElasticsearchDomain = ESAction('DeleteElasticsearchDomain')
DescribeElasticsearchDomain = ESAction('DescribeElasticsearchDomain')
DescribeElasticsearchDomains = ESAction('DescribeElasticsearchDomains')
DescribeElasticsearchDomainConfig = \
    ESAction('DescribeElasticsearchDomainConfig')
ESHttpDelete = ESAction('ESHttpDelete')
ESHttpGet = ESAction('ESHttpGet')
ESHttpHead = ESAction('ESHttpHead')
ESHttpPost = ESAction('ESHttpPost')
ESHttpPut = ESAction('ESHttpPut')
ListDomainNames = ESAction('ListDomainNames')
ListTags = ESAction('ListTags')
RemoveTags = ESAction('RemoveTags')
UpdateElasticsearchDomainConfig = ESAction('UpdateElasticsearchDomainConfig')
