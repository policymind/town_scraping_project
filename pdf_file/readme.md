The simplest of the functions, but perhaps it could be called by the other modules if needed?
> :exclamation: update: not true!

PDF challenges:
 - adobe pdf vs regular pdf: pdfs needs to be flattened
 - _native_ pdfs vs _scanned_ pdfs: required Optical Character Recognition (OCR)

Different packages I've explored:

| package: | specific use here | will use for this project |
|:----|:------|:--------|
| orcmypdf |  |   |
| pymupdf4llm | takes flat `pdf` and converts to `md` |   |
| pytesseract |   |   |
| pymupdf  |  testing if ocr is needed   |   |
| PyPDF2  | flatting the `pdf` |  yes |






The advantage of ecode and municode is while scraping you can track the document structure within the json you are creating.
How to we derive that structure from a pdf?

Perhaps this is a good resource: https://lasha-dolenjashvili.medium.com/building-document-parsing-pipelines-with-python-3c06f62569ad
