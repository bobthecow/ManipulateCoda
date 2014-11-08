'''
Remove lines
@author Justin Hileman <http://justinhileman.com>
'''

import cp_actions as cp

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    text, target_range = cp.lines_and_range(context)
    
    cp.insert_text_and_select(context, '', target_range, cp.new_range(target_range.location, 0))
