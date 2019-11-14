from aws_cdk import core, aws_ec2


class CdkAwsPlaygroundStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # TODO: vpc
        vpc_main = aws_ec2.Vpc(self, 'vpc-main-prd', cidr='10.0.0.0/16', max_azs=4)

        # subnet
        subnet_pub_1 = aws_ec2.PublicSubnet(self, 'subnet-pub-1', cidr_block='10.10.10.0/24',
                                            vpc_id=vpc_main.vpc_id,
                                            availability_zone='us-east-1a',
                                            )
        subnet_private_1 = aws_ec2.PrivateSubnet(self, 'subnet-priv-1', cidr_block='10.20.20.0/24',
                                                 vpc_id=vpc_main.vpc_id,
                                                 availability_zone='us-east-1a'
                                                 )

        # TODO: sagemaker
        # TODO: lambda
        # TODO: api gateway
