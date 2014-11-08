'''A capitalization action for the Manipulate plugin for Coda'''

import cp_actions as cp
from titlecase import titlecase
from sentencecase import sentencecase

def act(controller, bundle, options):
    '''
    Required action method
    
    Set desired capitalization with 'to_case' option
    '''
    
    context = cp.get_context(controller)
    to_case = cp.get_option(options, 'to_case', 'upper').lower()
    line_ending = cp.get_line_ending(context)
    
    text, range = cp.selection_and_range(context)
    
    # if nothing is selected, assume we're talking about the line.
    if range.length == 0:
        text, range = cp.lines_and_range(context)
        
        # we really only want most of this... lines_and_range returns a newline char at the end
        if text.endswith(line_ending):
            range = cp.new_range(range.location, range.length - len(line_ending))
            text = cp.get_selection(context, range)
    
    if to_case == 'upper':
        text = text.upper()
    elif to_case == 'lower':
        text = text.lower()
    elif to_case == 'title':
        text = line_ending.join([titlecase(x) for x in text.split(line_ending)])
    elif to_case == 'sentence':
        text = sentencecase(text)
    elif to_case == 'invert':
        text = text.swapcase()
    else:
        return
    
    # insert and select the resulting insertion
    cp.insert_text_and_select(context, text, range, cp.new_range(range.location, len(text)))