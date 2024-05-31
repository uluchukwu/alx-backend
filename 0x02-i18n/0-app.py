#!/usr/bin/env python3
"""
A basic Flask application with a single route that renders an HTML page.

This module sets up a Flask application and serves an index page with a title
and a header.
"""

from flask import Flask, render_template, Response
from typing import Any

app: Flask = Flask(__name__)

@app.route('/')
def index() -> Response:
    """
    Render the index.html template.

    Returns:
        Response: The rendered HTML page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)