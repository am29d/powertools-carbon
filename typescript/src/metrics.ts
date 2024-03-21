import { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import { Metrics } from '@aws-lambda-powertools/metrics';

const metrics = new Metrics();
class Lambda implements LambdaInterface {

  @metrics.logMetrics()
  public async handler(_event: unknown, _context: unknown): Promise<void> {
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);