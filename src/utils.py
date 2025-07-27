def calculate_hash(block):
    import hashlib
    import json

    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def get_current_timestamp():
    from time import time
    return time()