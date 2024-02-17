import re

from text_parsers.from_file_to_text.annotations import Annotations

def _find_class(line):
    class_pattern = r'class\s+(\w+)'
    match = re.match(class_pattern, line)
    if not match:
        return None
    return match.group(1)


def _is_property(line):
    method_pattern = r'\s+def\s+\w+'
    return not re.match(method_pattern, line)


def _is_visible_property(line, properties):
    property_name_pattern = r'\s+(\w+)\s+='
    match = re.match(property_name_pattern, line)
    if not match or not properties:
        return False
    return match.group(1) in properties

def _is_method_visible(line):
    is_visible_pattern = f'\s+@{Annotations.VISIBLE.value}'
    return re.match(is_visible_pattern, line)

def _get_method_name(line):
    is_public_pattern = r'\s+def\s+(.+)\('
    return re.match(is_public_pattern, line).group(1)

def _is_private_method(name):
    return name.startswith('_')

def _wrap__private_method(func):
    def wrapper(file_iter):
        method = ''
        method_name_line = next(file_iter)
        name = _get_method_name(method_name_line)
        is_private_method = _is_private_method(name)

        method+= method_name_line
    
        method += func(file_iter)

        if is_private_method:
            method = f'<font color=#FF0000>\n{method}\n</font>'
        
        return method

    return wrapper

@_wrap__private_method
def _get_method(file_iter):
    method = ''

    for line in file_iter:
        if not line.strip():
            return method
        method += line
    return method

def parse_file(file, properties=None):
    text = ''
   
    class_name = ''
    file_iter = iter(file)

    for line in file_iter:
        if not class_name:
            name =  _find_class(line)
            if name:
                class_name += name
                text += line
            continue
        
        if _is_property(line):
            if _is_visible_property(line, properties):
                text += '\n' + line
                continue
        
        if _is_method_visible(line):
            text += '\n' +  _get_method(file_iter)
            continue
            
    return text
