Manipulate Coda
===============

A text manipulation plug-in for Panic's [Coda][1].

Manipulate Coda is a text-manipulation plug-in for [Panic's Coda][1]. It is
built using the [Coda Plugin Skeleton][2], an open source framework for writing
Cocoa plug-ins for Coda using Python. It was originally inspired by Ian Beck's
amazing [TEA for Coda][3] plugin.

Because Manipulate Coda is a Cocoa (native) Coda plug-in, it's crazy fast. For
example, the "Move Lines" commands are instant for any file that's not hampered
by Coda's (sometimes slothlike) syntax highlighting. It doesn't bat an eye at
moving or duplicating 10k lines of code.

Because Manipulate Coda is written in Python, it can leverage the strengths of
all sorts of interesting Python libraries. Manipulate Markup can change text
from Textile or Markdown or reStructuredText to HTML and back. It's pretty hot.

   [1]: http://panic.com/coda/
   [2]: http://github.com/bobthecow/coda-plugin
   [3]: http://onecrayon.com/tea/coda/


Manipulate Case
---------------

Manipulate Case changes selected text to upper, lower, sentence, title or
inverted case.


Manipulate Clipboard
--------------------

Manipulate Clipboard is a couple of handy clipboard extensions: Swap With
Clipboard and Append To Clipboard. Enjoy!


Manipulate Code
---------------

A relative newcomer, Manipulate Code currently contains only a couple of code
formatting actions, namely:

Aligning operators in a block of code. For example:

    // from this:
    $that = array(
        'foo' => 'bar',
        'bar' => 'baz',
        'qux' => 'qux',
        'quuux' => 'quuux',
    );
    
    // to this with a hotkey...
    $that = array(
        'foo'   => 'bar',
        'bar'   => 'baz',
        'qux'   => 'qux',
        'quuux' => 'quuux',
    );

... Trimming whitespace. This particular whitespace trim will remove any
trailing whitespace, as well as removing whitespace preceding a final
semicolon or comma, e.g.:

    // this
    $foo = 1        ;   
    $bar = 2 ;          
    $baz = 3    ;       
    
    // becomes
    $foo = 1;
    $bar = 2;
    $baz = 3;

And finally, reflowing comments. This one is a little weird. For it to work, you
should select a "paragraph" in your comment, for example, if you have this
ugly comment:

    /**
     * Lorem ipsum dolor sit amet
     *
     * Consectetur
     * adipisicing elit, sed do eiusmod tempor
     * incididunt ut labore et dolore magna
     * aliqua. Ut enim ad minim veniam, quis
     * nostrud exercitation ullamco laboris nisi
     * ut aliquip ex ea commodo consequat. Duis
     * aute irure dolor in reprehenderit in
     * voluptate velit esse cillum dolore eu
     * fugiat nulla pariatur. Excepteur sint
     * occaecat cupidatat non proident, sunt in
     * culpa qui officia deserunt mollit anim id
     * est laborum.
     */

... select the paragraph starting with Consectetur (but not the last line of the
comment tag). Hit Cmd+Option+/ and it'll magically re-wrap the comment!


Manipulate Encoding
-------------------

Manipulate Encoding encodes and decodes HTML entities, URL entities, ROT13 and
base64 text.


Manipulate Hash
---------------

Manipulate Hash creates hashes for selected text. So far it can create Adler,
SHA, CRC and MD5 hashes. Note that some of these hash algorithms (Adler and CRC)
are intended as checksums as they _not_ secure algorithms. Make sure you pick
the appropriate algorithm for hashing your secrets.


Manipulate Lines
----------------

Manipulate Lines includes commands to delete, move, duplicate, insert, yank and
put lines. It makes quick work of reorganizing code. You have to try it to
understand just how cool this plug-in is.

Note that the "duplicate" function has been duplicated by Panic in Coda 1.7,
but I still like my implementation better :)


Manipulate Markup
-----------------

Manipulate Markup translates between Textile, Markdown, reStructuredText and
HTML. It's pretty rad.
