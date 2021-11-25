import re
from urllib import robotparser
import requests


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

def split_name(name):
    # split name into first name and last name
    name = name.split()
    if len(name) > 1:
        return name[0], name[-1]
    return ' '.join(name)

def download(url, num_retries=2, user_agent=USER_AGENT, proxies=None):
    print('Downloading:', url)
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e)
        html = None
    return html


def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp


def get_links(html):
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)


def jsonify(list1, list2):
    return {k:v for k,v in list(zip(list1, list2))}

def remove_html_tags(text):
    html_tags = re.compile('<.*?>')
    return re.sub(html_tags, '', text)