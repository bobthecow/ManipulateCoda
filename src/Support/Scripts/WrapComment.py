'''(re)Wrap comments'''

import cp_actions as cp
import re
import textwrap

def act(controller, bundle, options):
    '''
    Required action method
    '''

    context = cp.get_context(controller)
    line_ending = cp.get_line_ending(context)
    lines, range = cp.lines_and_range(context)

    if lines.endswith(line_ending):
        lines = lines[:-len(line_ending)]
        range = cp.new_range(range.location, range.length - len(line_ending))

    try:
        newlines = line_ending.join(wrap_comment(
            lines.split(line_ending),
            context.tabWidth(),
            cp.get_option(options, 'width'),
            cp.get_option(options, 'min_width')
        ))
        cp.insert_text_and_select(context, newlines, range, cp.new_range(range.location, len(newlines)))
    except:
        cp.beep()
        raise


def wrap_comment(lines, tab_width, width=80, min_width=36):
    "Take an array of comment lines and rewrap them to the specified width"

    chunks = re.match("\s*(?:#|//+|\*|--)\s*", commonprefix(lines))
    if not chunks: raise Exception("not a comment.")

    plen = len(chunks.group())
    chunks = re.match("\s*(?:#|//+|\*|--)\s*", commonprefix([ l for l in lines if l[plen:].strip() ]))
    if not chunks: raise Exception("not a comment.")

    prefix = chunks.group()

    plen = len(prefix)
    linegroups = [[]]
    for line in [ l[plen:] for l in lines ]:
        if line.strip():
            linegroups[-1].append(line.rstrip())
        elif linegroups[-1]:
            linegroups.append([])

    prefix_width = len(prefix) + (re.match("\s*", prefix).group().count("\t") * (tab_width - 1))

    wrapper = textwrap.TextWrapper()
    wrapper.width = max(min_width, width - prefix_width)
    wrapper.expand_tabs = False
    wrapper.replace_whitespace = False
    wrapper.break_long_words = False

    newlines = []
    for group in linegroups:
        newlines += wrapper.wrap(" ".join(group))
        newlines.append('')
    newlines.pop()

    return [ (prefix + l).rstrip() for l in newlines ]


def commonprefix(m):
    "Given a list of strings, returns the longest common prefix"
    if not m: return ''
    if len(m) == 1: return m[0]
    s1, s2 = min(m), max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1
