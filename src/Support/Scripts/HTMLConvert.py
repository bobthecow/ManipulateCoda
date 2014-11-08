'''An HTML conversion action for the Coda Plugin Skeleton'''

import cp_actions as cp

from markdown import markdown
from textile import textile
from html2text import html2text
from html2textile import html2textile
from rest2html import rest2html
from html2rest_wrapper import html2rest

def act(controller, bundle, options):
    '''
    Required action method
    '''
    
    context = cp.get_context(controller)
    
    from_lang = cp.get_option(options, 'from', 'markdown').lower()
    to_lang = cp.get_option(options, 'to', 'html').lower()
    
    selection, range = cp.selection_and_range(context)
    
    # grab the whole document if they haven't selected anything...
    if range.length == 0:
        selection = context.string()
        range = cp.new_range(0, len(selection))
    
    # what are we coming from?
    if from_lang == 'markdown':
        html = markdown(selection)
    elif from_lang == 'textile':
        html = textile(selection)
    elif from_lang == 'rest':
        html = rest2html(selection)
    elif from_lang == 'html':
    	html = selection
    else:
    	return
    
    # what are we going to?
    if to_lang == 'markdown':
    	text = html2text(html)
    elif to_lang == 'textile':
    	text = html2textile(html)
    elif to_lang == 'rest':
        text = html2rest(html)
    elif to_lang == 'html':
    	text = html
    else:
    	return
    
    cp.insert_text(context, text, range)