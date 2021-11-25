USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

def split_name(name):
    # split name into first name and last name
    name = name.split()
    if len(name) > 1:
        return name[0], name[-1]
    return ' '.join(name)