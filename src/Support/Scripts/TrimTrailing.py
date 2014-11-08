'''Trim trailing whitespace--even the stuff before a semicolon...'''

import cp_actions as cp
import re

def act(controller, bundle, options):
    '''
    Required action method
    '''

    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)

    select_range = range = cp.get_range(context)
    if range.length == 0:
        range = cp.new_range(0, len(context.string()))

    lines, range = cp.lines_and_range(context, range)

    newlines = line_ending.join([re.sub("^(.*?)\s*([;,]?)\s*$", '\\1\\2', x) for x in lines.split(line_ending)])

    if select_range.length == 0:
        prefix = line_ending.join([re.sub("^(.*?)\s*([;,]?)\s*$", '\\1\\2', x) for x in lines[0:select_range.location].split(line_ending)])
        cp.insert_text_and_select(context, newlines, range, cp.new_range(len(prefix), 0))
    else:
        cp.insert_text_and_select(context, newlines, range, cp.new_range(range.location, len(newlines)))
