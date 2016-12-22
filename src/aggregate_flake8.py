#!/usr/env python
# -*- encoding: utf-8 -*-
"""get all .flake8 from GitHub."""

import time

import unirest

API_URL = 'https://api.github.com/search/'
TOKEN = '&access_token='
OUTPUT_PATH = './github_flake8.txt'
ERROR_LOG = './error.log'


class API403Exception(Exception):
    """exception class."""

    pass


def main():
    """main function."""
    input_file = './repo_list.txt'
    with open(input_file, 'r') as f:
        repository_names = f.readlines()

    file_name = '.flake8'
    with open(OUTPUT_PATH, 'w') as f:
        remain_repository_names = []
        remain_dl_urls = []
        for repository_name in repository_names:
            f.write(repository_name)
            repository_name = repository_name.replace('\n', '')
            try:
                file_json = search_with_filename(file_name, repository_name)
            except API403Exception:
                # list up failed repository_name and try later.
                print '[ERROR]: 403' + repository_name
                remain_repository_names.append(repository_name)
            except Exception:
                # another error status will be ignored.
                print '[ERROR]: unknown ' + repository_name
                continue
            for items_json in file_json['items']:
                dl_url = search_dl_url(items_json)
                try:
                    dl_result = get_file(dl_url)
                    f.write(dl_result)
                except API403Exception:
                    # list up failed dl_url and try later.
                    print '[ERROR] 403 ' + dl_url
                    remain_dl_urls.append(dl_url)
                except Exception:
                    # another error status will be ignored.
                    print '[ERROR] unknown ' + dl_url
                    continue

    with open(ERROR_LOG, 'w') as f:
        f.write('remain_repositories\n')
        f.write('\n'.join(remain_repository_names))
        f.write('remain_download_urls\n')
        f.write('\n'.join(remain_dl_urls))

    return


def search_with_filename(file_name, repository_name):
    """search code by file_name in repository_name and return json."""
    query_string = API_URL + 'code?q=filename:' + file_name + '+repo:' + repository_name
    data_json = api_json_dict(query_string)
    return data_json


def search_dl_url(items_json):
    """search download url from items json."""
    query_string = items_json['url']
    data_json = api_json_dict(query_string)
    dl_url = data_json['download_url']
    return dl_url


def get_file(dl_url):
    """get file with dl_url."""
    return dl_file(dl_url)


def dl_file(dl_url):
    """download plain text from dl_url."""
    print dl_url
    response = unirest.get(dl_url)
    return response.body
    if response.code == 403:
        print '[ERROR]: 403 ' + dl_url
        time.sleep(30)
        raise API403Exception(dl_url)
    raise API403Exception(dl_url)
    if response.code != 200:
        print '[ERROR]: ' + str(response.code) + ' ' + dl_url
        raise Exception
    return response.body


def api_json_dict(query_string):
    """return json dict from API_URL + query_string."""
    print query_string
    response = unirest.get(query_string + TOKEN)
    if response.code == 403:
        print '[ERROR]: 403 ' + query_string
        time.sleep(30)
        raise API403Exception(query_string)
    if response.code != 200:
        print '[ERROR]: ' + str(response.code) + ' ' + query_string
        raise Exception
    return response.body


if __name__ == "__main__":
    main()
