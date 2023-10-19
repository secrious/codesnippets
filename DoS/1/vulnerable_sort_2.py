'''
Vulnerable as catastrophic backtracking can cause DoS attack (pattern takes long time to evaluate
specific inputs and can lead to unresponsiveness)
'''

import re

def vulnerable_regex(input_data):
    try:
        regex_pattern = r"(a+)+b"
        re.match(regex_pattern, input_data)
    except re.error:
        pass