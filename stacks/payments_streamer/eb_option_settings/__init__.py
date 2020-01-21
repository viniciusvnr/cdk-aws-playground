from . import (
    deployment_policy,
    environment_config,
    general_config,
    launch_configuration
)
from .auto_scaling import (
    auto_scaling_asg,
    auto_scaling_trigger,
    auto_scaling_updatepolicy

)


def get_config_list():
    d_policy = deployment_policy.get_deployment_policy()
    e_config = environment_config.get_environment_policy()
    g_config = general_config.get_general_options()
    l_configuration = launch_configuration.get_launch_configuration_options()
    as_asg = auto_scaling_asg.get_asg_options()
    as_trigger = auto_scaling_trigger.get_auto_scaling_trigger_options()
    as_update_policy = auto_scaling_updatepolicy.get_update_policy_options()

    options_list = [
        *d_policy,
        *e_config,
        *g_config,
        *l_configuration,
        *as_asg,
        *as_trigger,
        *as_update_policy
    ]

    return options_list
