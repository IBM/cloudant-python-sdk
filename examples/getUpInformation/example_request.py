# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_up_information().get_result()

print(response)
