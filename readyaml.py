import yaml
import sys
import  var_dump
reload(sys)
sys.setdefaultencoding( "utf-8" )


fp=open("jiguang-docs/jpush/mkdocs.yml")
document = fp.read();
yml_doc=yaml.load(document)
var_dump.var_dump(yaml.load(document))