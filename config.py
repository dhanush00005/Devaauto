from os import environ

API_ID = int(environ.get("API_ID", "21427459"))
API_HASH = environ.get("API_HASH", "cb23f6f9c4fe9783a0d948c7e2178d26")
BOT_TOKEN = environ.get("BOT_TOKEN", "8085380955:AAFIj7d6INM3b4wrkqBkvlxZ_zmAh9lvqGs")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002390130291"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002331124008"))
ADMINS = int(environ.get("ADMINS", "1868438972 842433366 5798247275"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
