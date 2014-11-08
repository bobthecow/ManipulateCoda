'''
Move words around
@author Justin Hileman <http://justinhileman.com>
'''

import cp_actions as cp

def act(controller, bundle, options):
    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    
    direction = cp.get_option(options, 'direction', 'right')
    
    line_text, line_range = cp.lines_and_range(context)
    selection, select_range = cp.selection_and_range(context)
    if select_range.length == 0:
        selection, select_range = cp.words_and_range(context)
    
    cp.say(context, 'word(s)', '||%s||' % selection)
    return
    
    if direction.lower() == 'left':
        prefix = line_text[:(select_range.location - line_range.location)]
        
        if not prefix.strip():
            cp.beep()
            return
        
        # we care about the original length of line after, not the balanced one we'll get in a second
        len_line_after = len(line_after)
        
        line_after, text = cp.balance_line_endings(line_after, text, line_ending)
        line_delta = len(line_after) - len_line_after
        
        select_start = select_range.location + len(line_after)
        select_end = min(select_start + select_range.length, len(context.string()))
        
        text = line_after + text
        
        select_range = cp.new_range(select_start, max(0,select_end - select_start))
        target_range = cp.new_range(target_range.location, max(0, target_range.length + len(line_after) - (len(line_after) - len_line_after)))
    else:
        line_before = cp.get_line_before(context, target_range)
        if line_before is None: return
        
        # we care about the original length of line before, not the balanced one we'll get in a second
        len_line_before = len(line_before)
        
        text, line_before = cp.balance_line_endings(text, line_before, line_ending)
        
        text = text + line_before
        select_range = cp.new_range(select_range.location - len_line_before, select_range.length)
        target_range = cp.new_range(target_range.location - len_line_before, target_range.length + len_line_before)
    
    cp.insert_text_and_select(context, text, target_range, select_range)