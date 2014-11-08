'''
Swap selection with clipboard
@author Justin Hileman <http://justinhileman.com>
'''

from AppKit import *
from Foundation import *

import cp_actions as cp

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    text, target_range = cp.selection_and_range(context)
    pb = NSPasteboard.generalPasteboard()
    
    # get the old clipboard contents
    old = pb.stringForType_(NSStringPboardType)
    
    # copy text to the clipboard
    pb.clearContents()
    pb.setString_forType_(text, NSStringPboardType)
    
    # replace the current selection with the clipboard contents
    cp.insert_text_and_select(context, old, target_range, cp.new_range(target_range.location, len(old)))
