from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

# TODO: GET VALUES FROM SECRET MANAGER
ENV_VAR_DATABASE_URL = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:application:environment",
    option_name='DATABASE_URL', value='change_this'
)
ENV_VAR_DATABASE_GROW_PAY_URL = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:application:environment",
    option_name='DATABASE_GROW_PAY_URL', value='change_this'
)
ENV_VAR_SYNC_GROW_PAY = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:application:environment",
    option_name='SYNC_GROW_PAY', value='change_this'
)
ENV_VAR_NUM_OF_PROCESSORS_PER_STREAM = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:application:environment",
    option_name='NUM_OF_PROCESSORS_PER_STREAM', value='change_this'
)


def get_env_vars():
    return [
        ENV_VAR_DATABASE_URL,
        ENV_VAR_DATABASE_GROW_PAY_URL,
        ENV_VAR_SYNC_GROW_PAY,
        ENV_VAR_NUM_OF_PROCESSORS_PER_STREAM
    ]
