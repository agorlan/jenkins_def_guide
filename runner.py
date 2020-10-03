"""Module doc"""
import argparse


print('Hello Jenkins world!')

HTML_CONTENT = """
<HTML>
<HEAD>
<TITLE>Your Title Here</TITLE>
</HEAD>
<BODY BGCOLOR="FFFFFF">
<CENTER><IMG SRC="clouds.jpg" ALIGN="BOTTOM"> </CENTER>
<HR>
<a href="http://somegreatsite.com">Link Name</a>
is a link to another nifty site
<H1>This is a Header</H1>
<H2>This is a Medium Header</H2>
Send me mail at <a href="mailto:support@yourcompany.com">
support@yourcompany.com</a>.
<P> This is a new paragraph!
<P> <B>This is a new paragraph!</B>
<BR> <B><I>This is a new sentence without a paragraph break, in bold italics.</I></B>
<HR>
</BODY>
</HTML>
"""

VERSION = '0.0.1'
FILE_NAME = 'index.html'


def main(name, param_x):
    print('\nMain flow started! Version: {}. Parameter X: {}'.format(VERSION, param_x))
    with open(name, 'w') as f:
        f.write(HTML_CONTENT)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--PARAMETER_X', '-px')
    args = parser.parse_args()
    main(FILE_NAME, args.px)
