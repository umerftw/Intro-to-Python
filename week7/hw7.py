#!/usr/bin/env python

"""
This script will ask the user for a URL and a tag to search for and tell the user if
the webpage contains any hyperlinks and what those hyperlinks are.
It will then write that list of hyperlinks to a text file.
"""

import requests
from bs4 import BeautifulSoup

user_url = input("Input a URL to find out if it has hyperlinks on the page: ")
user_tag = input("Input a tag to search for hyperlinks within: ")


# this function takes a user input for a url and a tag and
# outputs a list containing data found with that tag
def url_tag_cruncher(url, tag):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    tag_lines = []
    tag_info = soup.find_all(tag)
    for x in tag_info:
        tag_lines.append(x)
    return tag_lines


# This function takes the outputted list from url_tag_cruncher function and
# finds out if there are hyperlinks in the URL inputted by the user
def link_finder(output):
    links = []
    for x in output:
        link_string = str(x)
        if "https" in link_string:
            links.append(link_string)
            print("The URL you requested contains a hyperlink: {}".format(link_string))
    return links


# This function takes the list of links in string format and stores it in a text file
# called URL_links.txt
def link_to_txt(list_of_links):
    text_file = open("URL_links.txt", "w")
    text_file.write("\n".join(list_of_links))
    text_file.close()


if __name__ == '__main__':
    tag_contents = url_tag_cruncher(user_url, user_tag)
    links_list = link_finder(tag_contents)
    link_to_txt(links_list)
