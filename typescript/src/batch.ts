import { BatchProcessor, EventType, processPartialResponse, } from '@aws-lambda-powertools/batch';
import type { SQSEvent, SQSRecord, Context, SQSBatchResponse } from 'aws-lambda';

const processor = new BatchProcessor(EventType.SQS);

const recordHandler = async (record: SQSRecord): Promise<void> => {
  const payload = record.body;
};

export const handler = async (
  event: SQSEvent,
  context: Context
): Promise<SQSBatchResponse> => {
  return processPartialResponse(event, recordHandler, processor, {context});
};