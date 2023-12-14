#! /bin/env python

import requests
import re
import sys
import time

requrl = "http://{}/.hidden/"
found_set = set()


def make_request(url):
    # print(f"Getting {url}")
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"ON URL: {url} -- Error: {e}")
        return
    html_content = response.text
    url_pattern = re.compile(r'href=[\'"]?([^\'" >]+)')
    urls = url_pattern.findall(html_content)
    if len(urls) == 0:
        html_content = html_content.strip()
        if html_content not in found_set:
            print(f"In {url}, got {html_content}")
        found_set.add(html_content)
        return
    for link in urls:
        if "." in link:
            continue
        time.sleep(0.03)
        make_request(f"{url}{link}")


def main():
    ip = sys.argv[1]
    make_request(requrl.format(ip))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing target ip/hostname")
        exit(1)
    main()
