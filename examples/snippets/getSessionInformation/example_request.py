# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

response = service.get_session_information().get_result()

print(response)
# section: markdown
# For more details on Session Authentication, see [Authentication.](#authentication)
