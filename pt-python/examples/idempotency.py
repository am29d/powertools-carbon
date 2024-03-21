from aws_lambda_powertools.utilities import LambdaContext
from aws_lambda_powertools.utilities.idempotency import (
    DynamoDBPersistenceLayer,
    idempotent,
)

ddbPersistenStore = DynamoDBPersistenceLayer(table_name="IdempotencyTable")

@idempotent(persistent_store=ddbPersistenStore)
def lambda_handler(event: dict, context: LambdaContext):
    try: 
      payment = create_subscription_payment(event)
      return {
        "payment_id": payment.id,
        "statusCode": 200,
        "body": payment
      }
    except Exception as e:
      raise ValueError(f"Failed to create payment: {e}")

def create_subscription_payment(event: dict):
  # Create payment
  pass