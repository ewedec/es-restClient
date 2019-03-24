import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")
conf = configparser.ConfigParser()
conf.read(configPath)
config = {}

esServer= conf.get("elasticsearch", "esServer")
port = conf.get("elasticsearch", "port")
log_grade = conf.get("log", "log_grade")
