from aws_cdk import core
import aws_cdk.pipelines as pipelines
import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as cp_actions
from aws_cdk.pipelines import CodePipelineSource
from cdk.stack_1.lambda_stack1 import LambdaStage

class LambdaPipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        github_token =core.SecretValue.plain_text('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')

        source = CodePipelineSource.git_hub("tirth-b/cicd-test", "main", authentication=github_token)

        pipeline = pipelines.CodePipeline(self, "LambdaPipeline",
                                          pipeline_name="LambdaDeployPipeline",
                                          synth=pipelines.ShellStep("Synth",
                                                                    input=source,
                                                                    commands=[
                                                                        # Install Python dependencies
                                                                        "python3 -m venv .env",
                                                                        "source .env/bin/activate",
                                                                        "pip install -r requirements.txt",
                                                                        # Synthesize the CDK app
                                                                        "cdk synth"
                                                                    ]))
        pipeline.add_stage(LambdaStage(self, "LambdaStage1"))
