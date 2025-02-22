import os
import simplejson
from flask import url_for
import pathlib


from redash.settings import WEBPACK_MANIFEST_PATH, CDN_PREFIX

def configure_webpack(app):
    app.extensions["webpack"] = {"assets": None}

    def get_asset(path):
        assets = app.extensions["webpack"]["assets"]
        # in debug we read in this file each request
        if assets is None or app.debug:
            try:
                with open(WEBPACK_MANIFEST_PATH) as fp:
                    assets = simplejson.load(fp)
            except IOError:
                app.logger.exception("Unable to load webpack manifest")
                assets = {}
            app.extensions["webpack"]["assets"] = assets
        # return url_for("static", filename=assets.get(path, path))
        return f'{CDN_PREFIX}{assets.get(path, path)}'

    @app.context_processor
    def webpack_assets():
        return {"asset_url": get_asset}
