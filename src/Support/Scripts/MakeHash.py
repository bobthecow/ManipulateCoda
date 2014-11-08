'''
Hash.
@author Justin Hileman <http://justinhileman.com>
'''

import cp_actions as cp
import hashlib, zlib

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    hash_type = cp.get_option(options, 'type', 'md5').lower()
    
    text, target_range = cp.lines_and_range(context)
    
    if hash_type == 'adler-32':
        text = str(zlib.adler32(text))
    elif hash_type == 'crc-32':
        text = str(zlib.crc32(text))
    elif hash_type == 'md5':
        text = hashlib.md5(text).hexdigest()
    elif hash_type == 'rmd160':
        text = hashlib.new('rmd160', string=text).hexdigest()
    elif hash_type == 'sha-1':
        text = hashlib.sha1(text).hexdigest()
    elif hash_type == 'sha-224':
        text = hashlib.sha224(text).hexdigest()
    elif hash_type == 'sha-256':
        text = hashlib.sha256(text).hexdigest()
    elif hash_type == 'sha-384':
        text = hashlib.sha384(text).hexdigest()
    elif hash_type == 'sha-512':
        text = hashlib.sha512(text).hexdigest()
    else:
        return
    
    cp.insert_text(context, text, target_range)