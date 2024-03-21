import type { LambdaInterface } from "@aws-lambda-powertools/commons/types";
import { Logger } from "@aws-lambda-powertools/logger";
import { Metrics, MetricUnit } from "@aws-lambda-powertools/metrics";
import { Tracer } from "@aws-lambda-powertools/tracer";
import type { Context } from "aws-lambda";
import type { CartCheckedOutEvent } from "./types";

const logger = new Logger();
const metrics = new Metrics();
const tracer = new Tracer();


class Lambda implements LambdaInterface {

  @metrics.logMetrics({ captureColdStartMetric: true })
  @tracer.captureLambdaHandler()
  @logger.injectLambdaContext({ logEvent: true })
  public async handler(event: CartCheckedOutEvent, _context: Context): Promise<void> {
    metrics.addMetric('CartCheckedOut', MetricUnit.Count, 1);

    tracer.putAnnotation('CustomerId', event.customerId);

    metrics.addMetadata('CartDetails', event.cartState);

    // ... rest of the code
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);