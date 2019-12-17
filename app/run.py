#!/usr/bin/env python3

from api import app

if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app._static_folder = "static/"
    app.run()