'''A Base64 Encodeing action for the Manipulate plugin for Coda'''

import cp_actions as cp
import base64

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
        try:
            text = base64.b64decode(selection)
            
        # base64decode raises a TypeError if the string doesn't have the right
        # padding, or if it's invalid base64... We'll just catch this error
        # and do nothing at all :)
        except TypeError:
            return
        
        # also, base64decode tends to return an empty string, which is also lame
        if range.length and not len(text):
            return
    
    else:
        text = base64.b64encode(selection)
    
    cp.insert_text(context, text, range)