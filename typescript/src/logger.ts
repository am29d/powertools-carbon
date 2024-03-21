import { Logger } from '@aws-lambda-powertools/logger';
import type { LambdaInterface } from '@aws-lambda-powertools/commons/types';
import type { Context } from 'aws-lambda';

const logger = new Logger();

class Lambda implements LambdaInterface {

  @logger.injectLambdaContext({ logEvent: true })
  public async handler(event: unknown, context: Context): Promise<void> {
    logger.info('This is an INFO log with some context');
  }
}

const myFunction = new Lambda();
export const handler = myFunction.handler.bind(myFunction);