"""
    Filter describes how a filter should be. Can be of three types 'format', 'name' or 'regex'. 
    'format' and 'name' are just specific types of 'regex'.
"""

class Filter():
    """
    The folder that recieves the files that are being organized.
    """

    def __init__(self, type_, pattern) -> None:
        self.type = type_
        self.pattern = pattern

    def set_type(self, type_):
        """
        Setter for the type.
        """
        if isinstance(type_, str):
            return
        self.type = type_

    def set_pattern(self, pattern):
        """
        Setter for the pattern.
        """
        if isinstance(pattern, str):
            return
        self.pattern = pattern
