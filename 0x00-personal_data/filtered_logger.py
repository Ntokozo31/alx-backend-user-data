#!/usr/bin/env python3

"""
This module give us regex
"""
import re


def filter_datum(fields, redaction, message, separator):
    pattern = r'({}=).*?{}'.format('|'.join(map(re.escape, fields)), re.escape(separator))
    return re.sub(pattern, lambda match: match.group(1) + redaction + separator, message)
