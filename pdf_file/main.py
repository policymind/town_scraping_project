"""
Goal: to download a pdf and convert it to markdown
WIP
"""

from pathlib import Path
import urllib.request
import pymupdf4llm

#### Will be variables later
SAMPLE_ID = "000000"
SAMPLE_URL ="https://www.townofchesterfieldma.com/sites/g/files/vyhlif7606/f/uploads/general_town_by-laws_2022.pdf"
SAMPLE_DOWNLOAD_DESTINATION = "sample_pdfs/policy_file.pdf"
SAMPLE_CONVERSION_DESTINATION = "belmont.md"

### header, will be constant
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# request and download pdf
req = urllib.request.Request(SAMPLE_URL, headers=HEADERS)
with urllib.request.urlopen(req) as response, open(SAMPLE_DOWNLOAD_DESTINATION, "wb") as f:
    f.write(response.read())
  
# convert format from pdf to md
doc = pymupdf4llm.to_markdown(SAMPLE_DOWNLOAD_DESTINATION)
Path(SAMPLE_CONVERSION_DESTINATION).write_bytes(doc.encode())
