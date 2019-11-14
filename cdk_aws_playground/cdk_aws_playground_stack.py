from aws_cdk import core
from aws_cdk import ec2

class CdkAwsPlaygroundStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # TODO: vpc
        # subnetConfiguration: [
        #     {
        #     cidrMask: 24,
        #     name: 'ingress',
        #     subnetType: SubnetType.PUBLIC,
        #     },
        #     {
        #     cidrMask: 24,
        #     name: 'application',
        #     subnetType: SubnetType.PRIVATE,
        #     },
        #     {
        #     cidrMask: 28,
        #     name: 'rds',
        #     subnetType: SubnetType.ISOLATED,
        #     }
        #  ]
        
        vpc_main = ec2.Vpc(self, 'mainvpc-pg',
            cidr='10.0.0.0/16',
            
        )




        # TODO: sagemaker
        # TODO: lambda
        # TODO: api gateway
