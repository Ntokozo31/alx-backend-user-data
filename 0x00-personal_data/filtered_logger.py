#!/usr/bin/env python3

"""
This module gives regexing
"""


import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str, message: str,
        separator: str) -> str:
    pattern = r'({}=).*?{}'.format(
        '|'.join(map(re.escape, fields)),
        re.escape(separator)
    )
    return re.sub(
        pattern,
        lambda match: match.group(1) + redaction + separator,
        message
    )
