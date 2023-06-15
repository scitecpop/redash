import json

from redash.settings import WEBPACK_MANIFEST_PATH, FRONTEND_DIR_ROOT, CDN_PREFIX

def get_asset(path):
    assets_info = json.load(open(WEBPACK_MANIFEST_PATH))
    return f'{CDN_PREFIX}{assets_info.get(path, path)}'
