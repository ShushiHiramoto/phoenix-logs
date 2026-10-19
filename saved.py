import gzip
import sqlite3

connection = sqlite3.connect("db/2026.db")

cursor = connection.cursor()

cursor.execute("""
SELECT log_id, log_content
FROM logs
WHERE is_processed = 1
LIMIT 1
""")

log_id, compressed = cursor.fetchone()

xml = gzip.decompress(compressed)

with open(f"{log_id}.mjlog", "wb") as f:
    f.write(xml)

print("saved")