# This script generates a UTC+2 ISO 8601 timestamp for use as the versionDate parameter in the AltStore JSON file.
from datetime import datetime, timezone, timedelta
print(datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=2))).strftime('%Y-%m-%dT%H:%M:%S%z'))
