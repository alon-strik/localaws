## Get List of logback.xml files per module

import os


def find_files(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
#           full_path = os.path.join(root, filename)
            if pattern in filename:
               matches.append(os.path.join(root, filename))

    return matches


files = find_files('/home/alon/LMSprojects/lms/nl-core/nl-be','logback.xml')
fileout = open('/home/alon/logback.xml', 'a')

linePattern1 = 'xml version="1.0" encoding'
linePattern2 = '<configuration'
linePattern3 = '</configuration'
linePattern4 = '<configuration scan'


header1='<?xml version="1.0" encoding="UTF-8"?>'
header2='<configuration scan="true" scanPeriod="30 seconds">'
endline='</configuration>'

fileout.write(header1 + '\n')
fileout.write(header2 + '\n')

for file in files:
    print file
    f = open(file)
    lines = f.readlines()
    for line in lines:
        if (not (not ((linePattern1 not in line) and (linePattern2 not in line) and (
                    linePattern3 not in line)) or not (linePattern4 not in line))):
            fileout.write(line)

fileout.write('\n' + endline)
fileout.close()
