# section: code
from ibmcloudant.cloudant_v1 import CloudantV1, ActivityTrackerEvents

service = CloudantV1.new_instance()

response = service.post_activity_tracker_events(
  types=[
    ActivityTrackerEvents.TypesEnum.MANAGEMENT,
    ActivityTrackerEvents.TypesEnum.DATA
  ]
).get_result()

print(response)
