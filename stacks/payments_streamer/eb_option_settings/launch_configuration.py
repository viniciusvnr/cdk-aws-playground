from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

launch_configuration_iam_instance_profile = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:launchconfiguration",
    option_name='IamInstanceProfile',
    value='"Fn::ImportValue": "payments-api-beanstalk-role-production"'  # TODO: check how to use fn::ImportValue
)


def get_launch_configuration_options():
    return [
        launch_configuration_iam_instance_profile
    ]


'''      
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "IamInstanceProfile",
    "Value": {
      "Fn::ImportValue": "payments-api-beanstalk-role-production"
    }
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "InstanceType",
    "Value": "t3.medium"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "EC2KeyName",
    "Value": "payments-api"
  },
  {
    "Namespace": "aws:autoscaling:launchconfiguration",
    "OptionName": "SecurityGroups",
    "Value": {
      "Ref": "ElasticBeanstalkSecurityGroup"
    }
  }
'''
