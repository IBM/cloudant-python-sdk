# section: code
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.api_exception import ApiException

service = CloudantV1.new_instance()
try:
    response = service.head_up_information()

    print("Service is up and healthy")
except ApiException as ae:
    if ae.code == 503:
        print(f"Service is unavailable, status code: {ae.code}")
    else:
        print(f"Issue performing health check, status code: {ae.code}, message: {ae.http_response.reason}")
