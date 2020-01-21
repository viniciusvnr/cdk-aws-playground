from aws_cdk import (
    aws_sagemaker as _sagemaker,
    aws_s3 as _s3,
    aws_ec2 as _ec2,
    aws_lambda as _lambda,
    aws_apigateway as _apigw,
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

        vpc_main = _ec2.Vpc(self,
                            'vpc-main-prd', cidr='10.0.0.0/16', max_azs=2,
                            subnet_configuration=[
                                _ec2.SubnetConfiguration(name='Ingress', subnet_type=_ec2.SubnetType.PUBLIC,
                                                         cidr_mask=24),
                                _ec2.SubnetConfiguration(name='in-app', subnet_type=_ec2.SubnetType.PRIVATE,
                                                         cidr_mask=24),
                                _ec2.SubnetConfiguration(name='in-db', subnet_type=_ec2.SubnetType.ISOLATED,
                                                         cidr_mask=28)]
                            )

        # Security Group Basics
        ipv4_peer = _ec2.Peer.any_ipv4()
        https_port = _ec2.Port(protocol=_ec2.Protocol.TCP, from_port=443, to_port=443,
                               string_representation='HTTPS-PORT')

        # Security Groups
        sg_lambda_function1 = _ec2.SecurityGroup(self,
                                                 id='lambda-function1', vpc=vpc_main,
                                                 security_group_name='lambda-function1',
                                                 description='SecurityGroup for LambdaFunction1',
                                                 allow_all_outbound=True
                                                 )

        sg_lambda_function1.add_ingress_rule(peer=ipv4_peer, connection=https_port)

        # Tags
        core.Tag.add(sg_lambda_function1, key='Name', value='lambda-function1-SG')

        # TODO: Necessidades em ordem de prioridade
        # 1- Buckets s3:
        # sagemaker-dumps
        # datascience
        # 2- Sagemaker Notebook Instance (conectando no s3 bucket dedicado)
        # 3- Lambda Function
        # 4- API Gateway
        # 5- Infra para Airflow

        # TODO: lambda_s3_bucket
        lambda_code_bucket = _s3.Bucket(self,
                                        'lambdacode', bucket_name='lambda-code-data-2019',
                                        encryption=_s3.BucketEncryption.KMS_MANAGED,
                                        block_public_access=_s3.BlockPublicAccess(restrict_public_buckets=True)
                                        )

        # TODO: lambda
        lambda_function_with_code = _lambda.Function(self,
                                                     id='lambda_function1',
                                                     code=_lambda.Code.asset('lambda'),
                                                     runtime=_lambda.Runtime.PYTHON_3_7,
                                                     handler='lambda-handler.handler',
                                                     vpc=vpc_main,
                                                     vpc_subnets=_ec2.SubnetSelection(
                                                         subnet_type=_ec2.SubnetType.PRIVATE),
                                                     security_group=sg_lambda_function1
                                                     )
        # TODO: api gatewaycd
        api_gtw_lambda = _apigw.LambdaRestApi(self, 'function1Api', handler=lambda_function_with_code)

        # lambda code from bucket
        # lambda_function_s3_code = _lambda.Function(self, id='lambda_function1',
        #                                    code=_lambda.S3Code(bucket=lambda_code_bucket, key='lambda-fn.py'),
        #                                    runtime=_lambda.Runtime.PYTHON_3_7, handler='index.main')

        # TODO: s3bucket
        # bucket = _s3.Bucket(self, 'sageMaker_dumps', bucket_name='sagemaker-dumps',
        #                     encryption=_s3.BucketEncryption.KMS_MANAGED,
        #                     block_public_access=_s3.BlockPublicAccess(restrict_public_buckets=True))

        # TODO: sagemaker
        # subnet_inapp_id = (vpc_main.select_subnets(subnet_name='in-app')).subnet_ids
        # sagemaker_instance = _sagemaker.CfnNotebookInstance(self, id='SMInstanceData',
        #                                                     subnet_id=subnet_inapp_id[0], role_arn='sagemakerarn',
        #                                                     instance_type='ml.t2.medium')
