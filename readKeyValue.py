import ConfigParser
import StringIO
import sys

CATEGORY = "tomcat"

def load_prop(prop_filename):
    config = ConfigParser.RawConfigParser()
    config.optionxform = str
    config.read(prop_filename)
    return config


def main():

    filename = 'x.txt'
    cp = load_prop(filename)
    print 'Parsing %s...' % filename

    for option in cp.options(CATEGORY):
        print "%s = %s" % (option, cp.get(CATEGORY, option))

if __name__ == "__main__":
    main()
