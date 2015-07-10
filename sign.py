import couchdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("rqsettings.ini")

server = couchdb.Server(url=config.get("Server", "url"))
message_db = server[config.get("Server", "message_db")]
project_name = config.get("Project", "name")

for change in message_db.changes(feed='continuous', since='now', heartbeat=1000, filter='project/by_name',
                                 name=project_name, include_docs=True):
    print change['doc']
