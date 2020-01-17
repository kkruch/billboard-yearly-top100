import datetime
import json
import re
import sys

from bs4 import BeautifulSoup
import requests

"""Accessing Billboard yearly charts"""

#css selectors
_YE_ENTERY_RANK_ATTR = "ye-chart-item__rank"
_YE_ENTERY_TITLE_ATTR = "ye-chart-item__title"
_YE-ENTERY_ARTIST_ATTR = "ye-chart-item__artist"

