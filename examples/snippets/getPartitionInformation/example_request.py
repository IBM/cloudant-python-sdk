# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_partition_information(
  db='events',
  partition_key='ns1HJS13AMkK'
).get_result()

print(response)
