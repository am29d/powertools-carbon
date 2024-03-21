
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict, context: LambdaContext) -> dict:
  # Retrieve a single parameter
  endpoint_comments = parameters.get_parameter("/lambda-powertools/endpoint_comments")

  # An API-KEY is a sensitive data and should be stored in SecretsManager
  api_key = parameters.get_secret("/lambda-powertools/api-key")
    
  # Retrieve a single parameter
  posts_param = parameters.get_app_config(name="config", environment="dev", application="posts")
