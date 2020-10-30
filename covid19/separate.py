'''
FILENAME: separate.py
AUTHOR:   Amadeo García Torrano
CONTACT:  amadeogarciatorrano@gmail.com
VERSION:  0.1.0
WEBSITE:  https://github.com/amadeogarcia

UPDATES:
    Version 0.0.0
    2020/10/27:1130>
        Release version.
    
    Version 0.1.0
    2020/10/29:1240>
        Simplified version.
        Documentation improved.

DESCRIPTION:
    This script takes a big line of HTML code and splits it
    into small HTML files to distribute them using iframes.

DISCLAIMER:
    This code is in the public domain. Please feel free to modify,
    use, etc however you see fit. But, please give reference to
    original authors as a courtesy to Open Source developers.

'''

# See explanation below #
def extract_substr(str, open, close, start):
    substr = ""
    ipos = str.find(open, start)
    fpos = str.find(close, ipos)
    if( ipos == -1 or fpos == -1 ): return "ERR", -1
    else:
        ipos += len(open)
        for i in range(ipos, fpos):
            substr += str[i]
        return substr, fpos

'''
extract_substr(s, open, close, start):
    This function finds and returns the first occurrence of a substring of s preceded by open and followed by close.
    Also returns the position in which substring ends, easing the process of searching recursively the same substring.
    When no substring is valid, returns "ERR".

    EXAMPLE:
    >>> s = "Hello <b>World</b>!"
    >>> substr_1 = extract_substr(s, '<b>', '</b>', 0)
    >>> substr_1
    'World'

'''

# Adds some HTML lines to the string so the iframe looks prettier #
def beautify(s):
    style_ln = '<link rel="stylesheet" type="text/css" href="../styles.css">'
    crlf = '\r\n'
    open_div = '<div>'
    close_div = '</div>'
    return str(style_ln + crlf + open_div + s + close_div)

# Open a chunk of HTML code #
with open("/mnt/c/users/amade/documents/github/proyecto-comunicaciones/covid19/raw_line.html") as rl:
    s = rl.read()
s, null = extract_substr(s, '<tbody>', '</tbody>', 0)   # Extract only the tbody part #
# Delete classes so all  <td> elements are the same #
s = s.replace(' class="sube"', '')
s = s.replace(' class="baja"', '')

i = 0; j = 0; count_row = 1; count_elem = 1
row = ""; elem = ""
# Will only use 10 rows or less #
while( i != -1 and count_row <= 10 ):
    row, i = extract_substr(s, '<tr>', '</tr>', i)           # Read a row #
    # Reset element iterators #
    j = 0
    count_elem = 1
    while( j != -1 ):
        elem, j = extract_substr(row, '<td>', '</td>', j)    # Read an element inside that row #
        # Will avoid the sixth and seventh elements (I don't want any deaths in my page) #
        if( j != -1 and count_elem != 6 and count_elem != 7 ):
            # Prepare the HTML styling code #
            elem = beautify(elem)
            # Create and write the file #
            with open("/mnt/c/users/amade/documents/github/proyecto-comunicaciones/covid19/files/row_" + str(count_row) + "/elem_" + str(count_elem) + ".html", "w") as elem_file:
                elem_file.write(elem)
        count_elem += 1
    count_row += 1