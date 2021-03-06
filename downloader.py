#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import zipfile
import urllib
import dirconfig
import logging
from autobuild import  autobuild
import commands
import os

from githubdownload import GithubDownload
from repositories import repositories
from ziptool import ZipTool

autobuild()

def git_push():
    print (os.chdir("/opt/push/jpush-docs/jpush-docs/"))
    logging.info(commands.getstatusoutput("git add ."))
    logging.info(commands.getstatusoutput('git commit -m "update the jpush server readme file"'))
    logging.info(commands.getstatusoutput('git push origin renew'))
    print ("git push origin renew")


downloader=GithubDownload()
for file_dic in repositories:
     html_content = downloader.get_html(repositories[file_dic]["url"]+"/releases")
     try:
          title = downloader.get_tile(html_content)
          logging.info("get title success")
     except:
          logging.info("get title fail")
     zip_url = downloader.get_code(html_content)
     release_time = downloader.get_time(html_content)
     release_version = downloader.get_version(html_content)
     zip_folder=os.path.join(dirconfig.conf["zip"],repositories[file_dic]["name"])
     if(not os.path.exists(zip_folder)):
          os.mkdir(zip_folder)
     zip_dir=downloader.get_dir(name=repositories[file_dic]["name"],version=release_version)
     zip_tool=ZipTool()
     if zip_tool.is_zip_exist(zip_dir):
         logging.info("the file exist,pass")
     else:
         logging.info("the file do not exist,replace")
         zip_tool.zip_download(zip_dir,release_version,repositories[file_dic]["url"])
         zip_tool.unzip_file(repositories[file_dic]["name"],release_version)
         zip_tool.replace_readme(repositories[file_dic]["name"],release_version)

if zip_tool.exist_flag>0:
    git_push()
    logging.info("git push")
else:
    logging.info("nothing to push")


