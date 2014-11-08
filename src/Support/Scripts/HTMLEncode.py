'''An HTML Encoding action for the Manipulate plugin for Coda'''

import cp_actions as cp
import html_encode as enc

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
        text = enc.htmlDecode(selection)
    else:
        text = enc.htmlEncode(selection)
    
    cp.insert_text(context, text, range)