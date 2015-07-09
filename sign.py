import couchdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("rqsettings.ini")

server = couchdb.Server(url=config.get("Server", "url"))
