import numbers


def generate_literal_oc_string(json_object, indent_level, start_indent_length, indent_length, ordered, is_root_container):
    if isinstance(json_object, bool):
        return '@YES' if json_object else '@NO'
    elif isinstance(json_object, str):
        return f"@\"{json_object}\""
    elif isinstance(json_object, numbers.Number):
        return f"@({json_object})"
    elif isinstance(json_object, dict) or isinstance(json_object, list):
        literal_string = ''
        indent_for_container = ' ' * (indent_level * indent_length + start_indent_length)
        indent_for_element = ' ' * ((indent_level + 1) * indent_length + start_indent_length)

        if is_root_container:
            literal_string = ' ' * start_indent_length

        is_first_element = True
        container_char_open = '{' if isinstance(json_object, dict) else '['
        container_char_close = '}' if isinstance(json_object, dict) else ']'

        literal_string += '@%s\n' % container_char_open
        for key in json_object:
            if isinstance(json_object, dict):
                if isinstance(key, str):
                    value = json_object[key]
                else:
                    continue
            else:
                value = key

            sub_literal_string = generate_literal_oc_string(value, indent_level + 1, start_indent_length, indent_length, ordered, False)
            if isinstance(sub_literal_string, str):
                if not is_first_element:
                    literal_string += ',\n'

                literal_string += f"{indent_for_element}@\"{key}\" : {sub_literal_string}" \
                    if isinstance(json_object, dict) else f"{indent_for_element}{sub_literal_string}"
                is_first_element = False

        literal_string += '\n%s%s' % (indent_for_container, container_char_close)

        return literal_string
    elif json_object is None:
        return '[NSNull null]'
    else:
        # a dummy tuple for else return
        return ()
