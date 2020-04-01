# Obtain dictionary and clean it if
# key == key and key == value


def clean_dups(topology_example):
    cleaned_dict = {}
    start = True
    for key, value in topology_example.items():
        if start:
            cleaned_dict[key] = value
            start = False
        else:
            if key in cleaned_dict.keys() or value in cleaned_dict.keys():
                continue
            else:
                cleaned_dict[key] = value
    return cleaned_dict
