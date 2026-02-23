#!/usr/bin/env python3
"""
Module for filtering and obfuscating sensitive data in log messages.
"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message using a single regex.
    """
    return re.sub(rf'({"|".join(fields)})=[^{separator}]*',
                  rf'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to filter sensitive information from logs.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter with a list of fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, masking the sensitive fields.
        """
        formatted_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            formatted_message, self.SEPARATOR)
