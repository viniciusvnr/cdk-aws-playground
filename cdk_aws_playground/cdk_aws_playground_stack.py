from aws_cdk import (aws_sagemaker as _sagemaker,
                     aws_s3 as _s3,
                     aws_ec2 as _ec2,
                     aws_iam as _iam,
                     core)


class CdkAwsPlaygroundStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # TODO: Criar  IAM Roles
        # sm_role_principal = _iam.IPrincipal('sagemaker.amazonaws.com')
        # sm_managed_policy = _iam.IManagedPolicy('AmazonSageMakerFullAccess')
        # sm_iam_role = _iam.Role(self, id='sagemaker_role', assumed_by=sm_role_principal)

        # TODO: criar security groups do publico pra privada e da privada pra db

        vpc_main = _ec2.Vpc(self, 'vpc-main-prd', cidr='10.0.0.0/16', max_azs=2,
                           subnet_configuration=[
                               _ec2.SubnetConfiguration(name='Ingress', subnet_type=_ec2.SubnetType.PUBLIC, cidr_mask=24),
                               _ec2.SubnetConfiguration(name='in-app', subnet_type=_ec2.SubnetType.PRIVATE, cidr_mask=24),
                               _ec2.SubnetConfiguration(name='in-db', subnet_type=_ec2.SubnetType.ISOLATED, cidr_mask=28)]
                           )

        subnet_inapp_id = (vpc_main.select_subnets(subnet_name='in-app')).subnet_ids

        # TODO: s3bucket
        bucket = _s3.Bucket(self, 'sageMakerdumps', bucket_name='sagemakerdumps',
                           encryption=_s3.BucketEncryption.KMS_MANAGED,
                           block_public_access=_s3.BlockPublicAccess(restrict_public_buckets=True))

        # TODO: sagemaker
        sagemaker_instance = _sagemaker.CfnNotebookInstance(self, id='SMInstanceData',
                                                    subnet_id=subnet_inapp_id[0], role_arn='sagemakerarn',
                                                    instance_type='ml.t2.medium')
        # TODO: lambda
        # TODO: api gateway
