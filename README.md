# addcorrespDesc.py

`addcorrespDesc.py` is a Python script designed to add the element `<correspDesc>` to TEI-encoded letters. The element `<correspDesc>` contains information about the sender, receiver, date, and location of the letter/postcard.

There is the (admittedly rather rare) use case that one has a list/overview (CSV) with all relevant information about a letter/postcard, but this information is not yet in the TEI header. This script reads the CSV file and integrates all the relevant information into the `<correspDesc>` element based on the information in the table. The script can be easily adapted to fit the user's specific needs.

As sample data, some letters (with missing `<correspDesc>` elements) and the corresponding CSV from the project ["Forschung Daniel Sanders"](https://sanders.bbaw.de/briefwechsel/korpus) are in the repository.

## Requirements

`addcorrespDesc.py` requires the `lxml` library to be installed. You can install these libraries using `pip` by running the following commands:

`pip install lxml`

## Usage

`python3 addcorrespDesc.py` (XML files and CSV need to be in the same directory as the script)

To use the script, you will need a collection of your TEI-encoded letters and a CSV file containing the metadata for the letters (you can use he sample datat for testing). The CSV file should contain one row of data for each letter, with the following columns:

-   `file_name`: the exact name of the XML file containing the TEI-encoded letter.
-   `sender_ref`: a reference to the person who sent the letter (e.g., a GND or Wikidata ID).
-   `sender`: the name of the person who sent the letter.
-   `receiver_ref`: a reference to the person who received the letter (e.g., a GND or Wikidata ID).
-   `receiver`: the name of the person who received the letter.
-   `sender_place_id`: the identifier of the place where the letter was sent from (e.g., a GeoNames ID).
-   `sender_place`: the name of the place where the letter was sent from.
-   `receiver_place_id`: the identifier of the place where the letter was received (e.g., a GeoNames ID).
-   `receiver_place`: the name of the place where the letter was received.
-   `date`: the date when the letter was sent (in ISO format: YYYY-MM-DD).

The CSV file can be modified to fit the needs, including changing the column names and the order of the columns.

The script will add the `<correspDesc>` element to the XML files based on the metadata in the CSV file. If any errors occur during the processing, the script will output a list of the files or rows that encountered issues.
The script will then read in each XML file, extract the corresponding row of data from the CSV file, and add a new `<correspDesc>` element to the `<teiHeader>` element of the XML file. The new element will contain two `<correspAction>` elements, one for the sender and one for the receiver, each with a `<persName>` element (as well as a `@ref`-attribute) and a `<placeName>` element, as well as a `<date>` element.

>**Note** Please ensure that your CSV file is complete and does not contain any empty cells. If the script attempts to retrieve data from a row with empty cells, it will raise an error and skip over that row, indicating the name of the file and the specific row that caused the error in the output message. The skipped row will not be included in the final output.

Remember that the script overwrites the XML files. If you don't want that and prefer to have copies, use:

```
# Create a new filename for the updated XML file
new_filename = os.path.splitext(filename)[0] + "_corresp.xml"
```
```
# Write the updated XML file to the new filename
with open(new_filename, "wb") as f:
    f.write(etree.tostring(tree, encoding='UTF-8', doctype='<?xml version="1.0" encoding="UTF-8"?>'))
```

You can add these lines after the line that adds the <correspDesc> element to the header, and before the end of the for loop.

Otherwise, the modified XML files will be saved to the same location as the original files, with the same filename.


If you find this script helpful or have any suggestions for improvement, please feel free to contribute.

P.S: I'm still working on this and can't find the bug yet, but seems that there is no way to get `xml_declaration=True` to work in this case (alway changes double quotes `"` to single quotes `'`. However, you can add the desired XML declaration to the output file by using the doctype parameter in the `etree.tostring()`, which is `<?xml version="1.0" encoding="UTF-8"?>` (as implemented in the script right now).
