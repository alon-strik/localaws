from pprint import pprint
import boto.ec2

conn = boto.ec2.connect_to_region("eu-west-1")
 
for r in conn.get_all_instances():
    pprint (r.__dict__)
#    instance_id = r.__dict__['id']
#    print instance_id
    break

