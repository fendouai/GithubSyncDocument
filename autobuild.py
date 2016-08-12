import commands
import os



print (os.chdir("/Users/fendouai/Documents/github/GithubSyncDocument/jiguang-docs/jpush-docs/zh/JPush/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/GithubSyncDocument/jiguang-docs/jpush-docs/zh/JMessage/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/GithubSyncDocument/jiguang-docs/jpush-docs/zh/JSMS/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/index/"))
print (commands.getstatusoutput("mkdocs build --clean"))


print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jpush/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jmessage/"))
print (commands.getstatusoutput("mkdocs build --clean"))
print (os.chdir("/Users/fendouai/Documents/github/jiguang-docs/jsms/"))
print (commands.getstatusoutput("mkdocs build --clean"))

