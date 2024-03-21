
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.metrics import MetricUnit
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
metrics = Metrics()
tracer = Tracer()

@metrics.log_metrics(capture_cold_start_metric=True)
@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event: dict, context: LambdaContext):
  metrics.add_metric(name="CartCheckedOut", unit=MetricUnit.Count, value=1)
  
  cart_state = event.cart_state
  
  tracer.put_annotation(key="CusomderId", value=cart_state.customer_id)
  metrics.add_metadata(key="CartDetails", value=cart_state)
  
  # ... rest of the code