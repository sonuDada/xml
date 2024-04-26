from lxml import etree
# Load the XML Schema
schema = etree.XMLSchema(etree.parse('./book_schema.xsd'))
# Load the XML document
xml_doc = etree.parse('./book.xml')
# Validate the XML document against the schema
if schema.validate(xml_doc):
    print("Validation successful.")
else:
    print("Validation failed. Errors:")
    for error in schema.error_log:
        print(error)
