from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

update_policy_max_batch_size = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:updatepolicy:rollingupdate",
    option_name='MaxBatchSize',
    value='1'
)

update_policy_min_instances_in_service = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:updatepolicy:rollingupdate",
    option_name='MinInstancesInService',
    value='1'
)

update_policy_rolling_update_enabled = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:updatepolicy:rollingupdate",
    option_name='RollingUpdateEnabled',
    value='true'
)

update_policy_rolling_update_type = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:updatepolicy:rollingupdate",
    option_name='RollingUpdateType',
    value='Health'
)


def get_update_policy_options():
    return [
        update_policy_max_batch_size,
        update_policy_min_instances_in_service,
        update_policy_rolling_update_enabled,
        update_policy_rolling_update_type
    ]
