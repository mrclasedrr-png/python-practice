import sys
import requests

print("Python:", sys.version)
print("requests:", requests.__version__)

r = requests.get("https://api.github.com", timeout=10)
print("GitHub API status:", r.status_code)