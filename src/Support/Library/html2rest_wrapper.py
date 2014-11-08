from cStringIO import StringIO
import html2rest as crappylibrary

def html2rest(txt):
    s = StringIO()
    crappylibrary.html2rest(txt, s)
    s.seek(0)
    return s.read()