'''
Append selection to the clipboard
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
    
    old = pb.stringForType_(NSStringPboardType)
    
    if old:
        text = old + text
    
    pb.clearContents()
    pb.setString_forType_(text, NSStringPboardType)
