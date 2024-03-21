import { Logger } from "@aws-lambda-powertools/logger";
import { injectLambdaContext } from "@aws-lambda-powertools/logger/middleware";
import middy from '@middy/core';

const logger = new Logger();


const lambdaHandler = async (event: unknown, context: any) => {
  logger.info('This is an INFO log with some context');
}

export const hanlder = middy(lambdaHandler).use(injectLambdaContext(logger));