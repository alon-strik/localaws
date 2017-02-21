import datetime
import boto3
import sys

client = boto3.client('rds')
action = sys.argv[1:]
vpc = sys.argv[2:]
DBId = ''
snapshotId = ''


# Create new snapshot
def createsnapshot(DBInstanceIdentifier):
    global snapshotId
    snapshotId = DBInstanceIdentifier + '-RC45-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    client.create_db_snapshot(
        DBSnapshotIdentifier=snapshotId,
        DBInstanceIdentifier=DBInstanceIdentifier)
    print snapshotId


# Get snapshot status
def getsnapshotstatus(snapshotId, DBId):
    response = client.describe_db_snapshots(
        DBInstanceIdentifier=DBId,
        DBSnapshotIdentifier=snapshotId,
        SnapshotType='manual')

    db_snapshots = response['DBSnapshots']
    print db_snapshots[0]['Status']


# Find instance id for vpc
def getfacts(db_instances):
    # get DB Instance Identifier base on VPC id selected
    global DBId
    for db_instance in db_instances:
        if db_instance['DBSubnetGroup']['VpcId'] == vpc[0]:
            DBId = db_instance['DBInstanceIdentifier']
            ep = open('/opt/lms/endpoint', 'w')
            ep.write(db_instance['Endpoint']['Address'])
            ep.close()

            # get DB list of snapshot for Identifier
            # response = client.describe_db_snapshots(DBInstanceIdentifier=DBId)
            # db_snapshots=response['DBSnapshots']
            # for db_snapshot in db_snapshots:
            #    f.write(db_snapshot['DBSnapshotIdentifier'])
            #    f.write('\n')
            # f.close()


response = client.describe_db_instances()
db_instances = response['DBInstances']

if action[0] == 'facts':
    getfacts(db_instances)

if action[0] == 'snapshot':
    getfacts(db_instances)
    createsnapshot(DBId)

if action[0] == 'status':
    getfacts(db_instances)
    snapshotId = sys.argv[2:]
    getsnapshotstatus(snapshotId[0], DBId)
