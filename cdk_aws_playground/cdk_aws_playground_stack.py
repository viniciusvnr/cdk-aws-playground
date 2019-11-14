from aws_cdk import core, aws_ec2


class CdkAwsPlaygroundStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # TODO: vpc
        vpc_main = aws_ec2.Vpc(self, 'vpc-main-pg', 
            cidr='10.0.0.0/16',
            
        )

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
        # TODO: sagemaker
        # TODO: lambda
        # TODO: api gateway
