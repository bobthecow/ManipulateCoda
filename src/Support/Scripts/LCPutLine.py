'''
Paste lines
@author Justin Hileman <http://justinhileman.com>
'''

from AppKit import *
from Foundation import *

import cp_actions as cp

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    selection, current_range = cp.lines_and_range(context)
    insert_range = cp.new_range(current_range.location + current_range.length, 0)
    
    # copy text from the clipboard
    text = NSPasteboard.generalPasteboard().stringForType_(NSStringPboardType)
    
    if not text:
        return
    
    if not selection.endswith(line_ending):
        text = line_ending + text
    elif not text.endswith(line_ending):
        text = text + line_ending
    
    cp.insert_text_and_select(context, text, insert_range, cp.new_range(insert_range.location, len(text)))