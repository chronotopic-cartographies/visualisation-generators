# Test for well-formedness
from xml.sax.handler import ContentHandler
from xml.sax import make_parser

def parse_file(file):
    parser = make_parser(  )
    parser.setContentHandler(ContentHandler(  ))
    parser.parse(file)

def check_xml_is_well_formed(file):
    try:
        parse_file(file)
        print("XML is well-formed")
    except Exception as e:
        print("XML is NOT well-formed! %s" % (e))