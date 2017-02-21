import boto

localIP=boto.utils.get_instance_metadata()['local-ipv4'][1]
region=boto.utils.get_instance_metadata()['local-hostname'].split('.')[1]
hostname=boto.utils.get_instance_metadata()['local-hostname']


