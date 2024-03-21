from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities import LambdaContext
from aws_lambda_powertools.utilities.data_masking import DataMasking

logger = Logger()
data_masker = DataMasking()

def lambda_handler(event, context: LambdaContext):
    data = event.get("body", {})
    
    logger.info("Erasing fields email, address.street, and company_address")
    
    erased = data_masker.erase(data, fields=["email", "address.street", "company_address"])
    
    return erased