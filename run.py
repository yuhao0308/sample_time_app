from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    # Get the current UTC time
    time_now_utc = datetime.utcnow()
    # Manually create a 5 hour timedelta
    offset = timedelta(hours=5)
    # Subtract 5 hours to get New York time
    time_now_new_york = time_now_utc - offset
    # Format the time to a string for display
    return time_now_new_york.strftime('%Y-%m-%d %H:%M:%S')

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
