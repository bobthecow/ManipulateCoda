'''
Copy lines
@author Justin Hileman <http://justinhileman.com>
'''

from AppKit import *
from Foundation import *

import cp_actions as cp

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    text, target_range = cp.lines_and_range(context)
    
    # copy text to the clipboard
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    pb.setString_forType_(text, NSStringPboardType)
