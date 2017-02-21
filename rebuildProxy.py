import os

def find_files(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if pattern in filename:
               matches.append(os.path.join(root, filename))
    return matches

confDir='/etc/apache2/conf'
proxyFileOut = open('/etc/apache2/sites-available/000-default.conf', 'w')
proxyHeaderFile = open('/opt/lms/000-default-header.conf', 'r')
proxyTrailerFile = open('/opt/lms/000-default-trailer.conf', 'r')

configFiles = find_files(confDir,'server')

headerText = proxyHeaderFile.read()
trailerText = proxyTrailerFile.read()

proxyFileOut.write(headerText + '\n')

for file in configFiles:
    f = open(file)
    text = f.read()
    proxyFileOut.write(text + '\n')
    f.close()

proxyFileOut.write(trailerText + '\n')
proxyFileOut.close()
