import csv
from lxml import etree

# Namespaces
ns = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "ns0": "http://relaxng.org/ns/structure/1.0",
}

# Create a parser that keeps CDATA sections
parser = etree.XMLParser(strip_cdata=False)

# Read the CSV file
with open("metadata.csv", "r") as file:
    reader = csv.DictReader(file)
    errors = []
    for row in reader:
        try:
            # Get the filename from the "file_name" column
            filename = row["file_name"]
            # Read the XML file
            tree = etree.parse(filename, parser)
            root = tree.getroot()

            # Create the <correspDesc> element
            corresp_desc = etree.Element("{http://www.tei-c.org/ns/1.0}correspDesc")
            corresp_action_sent = etree.SubElement(
                corresp_desc, "{http://www.tei-c.org/ns/1.0}correspAction", type="sent"
            )
            corresp_action_received = etree.SubElement(
                corresp_desc,
                "{http://www.tei-c.org/ns/1.0}correspAction",
                type="received",
            )
            pers_name_sent = etree.SubElement(
                corresp_action_sent,
                "{http://www.tei-c.org/ns/1.0}persName",
                ref=row["sender_ref"],
            )
            pers_name_sent.text = row["sender"]
            pers_name_received = etree.SubElement(
                corresp_action_received,
                "{http://www.tei-c.org/ns/1.0}persName",
                ref=row["receiver_ref"],
            )
            pers_name_received.text = row["receiver"]
            place_name_sent = etree.SubElement(
                corresp_action_sent,
                "{http://www.tei-c.org/ns/1.0}placeName",
                ref=row["sender_place_id"],
            )
            place_name_sent.text = row["sender_place"]
            place_name_received = etree.SubElement(
                corresp_action_received,
                "{http://www.tei-c.org/ns/1.0}placeName",
                ref=row["receiver_place_id"],
            )
            place_name_received.text = row["receiver_place"]
            date = etree.SubElement(
                corresp_action_sent,
                "{http://www.tei-c.org/ns/1.0}date",
                when=row["date"],
            )

            # Add the <correspDesc> element to the header
            header = root.find("tei:teiHeader", ns)
            profile_desc = header.find("tei:profileDesc", ns)
            profile_desc.append(corresp_desc)

            # Write the updated XML file
            with open(filename, "wb") as f:
                f.write(etree.tostring(tree, encoding='UTF-8', doctype='<?xml version="1.0" encoding="UTF-8"?>'))


        except Exception as e:
            errors.append(f"{row['file_name']}: {str(e)}")

    if errors:
        print("Errors occurred while processing the following rows or files:")
        for error in errors:
            print(error)
    else:
        print("Processing completed successfully.")
