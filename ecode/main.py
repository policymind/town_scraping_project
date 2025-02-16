"""scraping html from ecode and then converting to markdown """


from urllib.parse import urlparse # or should I use posixpath?
from pathlib import Path
import requests
import markdownify


SAMPLE_CODE = "00000"
SAMPLE_URL = "https://ecode360.com/BE3086"

# Extract last part of url string
parsed_url = urlparse(url_string)

last_section = parsed_url[-1]
html_ecode_link = f"https://ecode360.com/output/word_html/{last_section}"

req = requests.get(html_ecode_link, timeout=10)
if req.status_code != 200:
    logger.error('Website status code!=200. Exit program.')
    sys.exit()
results = bs4.BeautifulSoup(req.text, 'html.parser')

markdown_policy = markdownify.markdownify(results, heading_style="ATX")

Path(f"{SAMPLE_CODE}_policy.md").write_bytes(doc.encode())
