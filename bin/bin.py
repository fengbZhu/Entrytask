import sys, os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

from lib.main import server

server.run(port=8999, host='0.0.0.0', debug=True)
