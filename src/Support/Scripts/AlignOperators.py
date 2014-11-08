'''Line up operators...'''

import cp_actions as cp
import re

def act(controller, bundle, options):
    '''
    Required action method
    '''

    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    lines, range = cp.lines_and_range(context)

    newlines = line_ending.join(balance_operators(lines.split(line_ending)))
    cp.insert_text_and_select(context, newlines, range, cp.new_range(range.location, len(newlines)))


def balance_operators(lines):
    r = re.compile("^(.*[^\s])\s*((?:==?|<<|>>|&|\||\^)=|=[>&\*]|(?<![\.\+\-\*\/~%])[\.\+\-\*\/~%]?=)\s*([^\s].*)$")
    
    vars = []
    ops  = []
    vals = []
    ret  = []
    
    for line in lines:
        result = r.match(line)
        
        if result:
            vars.append(result.group(1))
            ops.append(result.group(2))
            vals.append(result.group(3))
    
    for line in lines:
        result = r.match(line)
        
        if result:
            ret.append(" ".join((result.group(1).ljust(len(max(vars, key=len))), result.group(2).rjust(len(max(ops, key=len))), result.group(3))))
        else:
            ret.append(line)
    
    return ret