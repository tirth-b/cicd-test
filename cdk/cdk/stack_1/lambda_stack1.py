from aws_cdk import core
import aws_cdk.aws_lambda as _lambda
import aws_cdk.aws_iam as iam

class LambdaStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        lambda_function = _lambda.Function(self, "HelloWorldLambda",
                                           runtime=_lambda.Runtime.NODEJS_14_X,
                                           handler="index.handler",  # The handler name is index.handler
                                           code=_lambda.Code.from_asset("cdk/stack_1/lambda/lambda1"),  # Points to the 'lambda' directory
                                           environment={
                                               "EXAMPLE_ENV_VAR": "HelloWorld"
                                           })

        # Grant the Lambda function basic permissions (optional)
        lambda_function.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=["logs:*"],
                resources=["*"]
            )
        )


class LambdaStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Add the LambdaStack to the stage
        lambda_stack = LambdaStack(self, "LambdaStack1")