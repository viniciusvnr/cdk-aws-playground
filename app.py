#!/usr/bin/env python3

from aws_cdk import core

from cdk_aws_playground.cdk_aws_playground_stack import CdkAwsPlaygroundStack


app = core.App()
CdkAwsPlaygroundStack(app, "cdk-aws-playground")

app.synth()
