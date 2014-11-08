from docutils.core import publish_parts

def rest2html(text):
    parts = publish_parts(
        source=text,
        settings_overrides={'file_insertion_enabled':0, 'raw_enabled':0},
        writer_name='html'
    )
    return parts['body']