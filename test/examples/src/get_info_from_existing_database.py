import json

from ibmcloudant.cloudant_v1 import CloudantV1

# 1. Create a Cloudant client with "EXAMPLES" service name ============
client = CloudantV1.new_instance(service_name="EXAMPLES")

# 2. Get server information ===========================================
server_information = client.get_server_information(
).get_result()

print(f'Server Version: {server_information["version"]}')

# 3. Get database information for "animaldb" ==========================
db_name = "animaldb"

db_information = client.get_database_information(
    db=db_name
).get_result()

# 4. Show document count in database ==================================
document_count = db_information["doc_count"]

print(f'Document count in \"{db_information["db_name"]}\" '
      f'database is {document_count}.')

# 5. Get zebra document out of the database by document id ============
document_about_zebra = client.get_document(
    db=db_name,
    doc_id="zebra"
).get_result()

print(f'Document retrieved from database:\n'
      f'{json.dumps(document_about_zebra, indent=2)}')
