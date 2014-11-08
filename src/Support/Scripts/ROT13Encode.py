'''A ROT13 Encoding action for the Manipulate plugin for Coda'''

import cp_actions as cp

def act(controller, bundle, options):
    '''
    Required action method
    '''
    
    context = cp.get_context(controller)
    selection, range = cp.selection_and_range(context)
    
    # do nothing unless they selected something
    if range.length == 0:
        return
    
    try:
        text = selection.encode('rot13')
    except LookupError:
        # for python 3... hopefully one of the two will do the trick.
        import rot13
        text = rot13.rot13(selection)
    
    cp.insert_text(context, text, range)