# Overview

This is a project for infrastructure Python development with CDK.

---

# Stacks

### Lambda-New-Relic-Deployment-Marker-Stack

Lambda Function to mark deployments on new relic APM for the specified application.

Code Pipeline User Parameters Object:

```json
{
  "FunctionVars": {
    "APP_ID": "219510000",
    "API_KEY": "8cf3f63a8fa02aa2c7898ed52aab7696dc000000",
    "APP_NAME": "spyder-java-staging",
    "GIT_REPO": "payops-cdk"
  }
}
```
---

### Lambda-Pipeline-Alerts-Stack

Lambda Function to alert if a CodePipeline Pipeline Execution State Change to Failed.

---

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

# Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
