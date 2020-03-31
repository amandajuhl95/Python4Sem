import os
import urllib.request as req 
from urllib.parse import urlparse


def download(url, to=None):

    parsed_python_url = urlparse(url)
    if(to == None):
        to = os.path.basename(parsed_python_url.path)

    req.urlretrieve(url, to)
      