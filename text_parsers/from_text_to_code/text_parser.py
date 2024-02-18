import re
from text_parsers.from_text_to_code.PlayerDieException import PlayerDieException


def _check_has_code_privates(text):
    pattern1 = r'\.\s*_+[a-zA-Z].*'
    pattern2 = r'\'\s*_+[a-zA-Z].*'
    return re.search(pattern1, text) or re.search(pattern2, text)


def _check_has_code_classes(text):
    pattern = r'\.*class\.*'
    return re.search(pattern, text)


def _check_code_for_bs(text):
    patterns = [r'\.*globals()\.*', r'\.*locals()\.*', r'\bfork\b',
                r'\bexec\b', r'\.?__dict__\.?']
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False


def _check_code_for_imports(text):
    pattern = r'\.*import\s+'
    return re.search(pattern, text)


def _check_code(text):
    checks = [_check_has_code_privates, _check_has_code_classes,
              _check_code_for_bs, _check_code_for_imports]
    for check in checks:
        if check(text):
            return True
    return False


def to_code(text, globals):
    if _check_code(text):
        raise PlayerDieException("Naughty, naughty! Check your python")

    try:
        exec(text, globals)
    except Exception:
        raise PlayerDieException("Compilation error. Check your code.")
