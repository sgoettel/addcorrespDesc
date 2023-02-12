# addcorrespDesc.py

There is the (admittedly rather rare) use case that one has a list (CSV) with all relevant information about a letter, but this information is not yet in the TEI header. This script reads the CSV file and integrates all the relevant information into the `<correspDesc>` element based on the information in the table. The script can be easily adapted to fit the user's specific needs.

`addcorrespDesc.py` is a Python script designed to add the element `<correspDesc>`  to TEI-encoded letters in XML format. The element `<correspDesc>` contains information about the sender, receiver, date, and location of the letter, and can be used to extract metadata from the letters for analysis or visualization.

As sample data, some letters and the corresponding CSV from the project ["Forschung Daniel Sanders"](https://sanders.bbaw.de/briefwechsel/korpus) are in the repository.

## Usage

To use the script, you will need a collection of your TEI-encoded letters and a CSV file containing the metadata for the letters. The CSV file should contain one row of data for each letter, with the following columns:

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
    f.write(etree.tostring(tree, encoding='utf-8', pretty_print=True))
```

You can add these lines after the line that adds the <correspDesc> element to the header, and before the end of the for loop.

The modified XML files will be saved to the same location as the original files, with the same filename.

## Requirements

`addcorrespDesc.py` requires the `lxml` and `csv` libraries to be installed. You can install these libraries using `pip` by running the following commands:

`pip install lxml`
`pip install csv` 


If you find this script helpful or have any suggestions for improvement, please feel free to contribute to the project on GitHub.
