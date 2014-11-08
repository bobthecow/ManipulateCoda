'''URL Encoding action for the Manipulate plugin for Coda'''

import cp_actions as cp
import urllib

def act(controller, bundle, options):
    '''
    Required action method
    
    Setting decode=True will decode instead of encoding
    '''
    
    context = cp.get_context(controller)
    decode = cp.get_option(options, 'decode', False)
    
    selection, range = cp.selection_and_range(context)
    
    # do nothing unless they selected something
    if range.length == 0:
        return
    
    if decode:
        text = urllib.unquote(selection)
    else:
        text = urllib.quote(selection)
    
    cp.insert_text(context, text, range)