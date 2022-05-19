# section: code
from ibmcloudant.cloudant_v1 import CloudantV1

service = CloudantV1.new_instance()

security_object = {'nobody':['_reader']}
response = service.put_cloudant_security_configuration(
  db='products',
  cloudant=security_object
).get_result()

print(response)
# section: markdown
# The `nobody` username applies to all unauthenticated connection attempts. For example, if an application tries to read data from a database, but didn't identify itself, the task can continue only if the `nobody` user has the role `_reader`.
# section: markdown
# If instead of using Cloudant's security model for managing permissions you opt to use the Apache CouchDB `_users` database (that is using legacy credentials _and_ the `couchdb_auth_only:true` option) then be aware that the user must already exist in `_users` database before adding permissions. For information on the `_users` database, see <a href="https://cloud.ibm.com/docs/Cloudant?topic=Cloudant-work-with-your-account#using-the-users-database-with-cloudant-nosql-db" target="_blank">Using the `_users` database with Cloudant</a>.
