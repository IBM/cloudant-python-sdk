# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.put_database(db='events', partitioned=True).get_result()

print(response)
