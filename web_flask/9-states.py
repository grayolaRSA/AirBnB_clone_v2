#!/usr/bin/python3
"""minimal flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def get_states(state_id=None):
    """display states and in alphabetical order"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown(exception):
    """ handles teardown of app"""
    storage.close()


if __name__ == '__main__':
    # Change the host parameter from '127.0.0.1' to '0.0.0.0'
    app.run(host='0.0.0.0', port=5000)
