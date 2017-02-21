import boto.cloudformation

conn = boto.cloudformation.connect_to_region('eu-west-1')
stack_id = 'LMS-VPC-alon-0120132430'

resources = conn.list_stack_resources(stack_id)
for resource in resources:
    print(resource.last_updated_time)
    print(resource.logical_resource_id)
    print(resource.physical_resource_id)
    print(resource.status)
    print(resource.resource_type)
