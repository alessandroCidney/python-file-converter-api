# Python File Converter

## Run on Localhost
To run the project on <http://localhost:8000>, use the following command:
```bash
fastapi dev
```

## Current Features

### Convert JPG to PDF
Merge multiple JPG files into a single PDF file. 

Route: /convert/jpg-to-pdf

#### Body parameters
**files**: A list of JPG files to be converted.

#### Response
A file with "Content-Type: application/pdf".