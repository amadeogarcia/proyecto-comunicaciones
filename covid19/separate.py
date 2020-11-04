'''
FILENAME: separate.py
AUTHOR:   Amadeo García Torrano
CONTACT:  amadeogarciatorrano@gmail.com
VERSION:  1.0
WEBSITE:  https://github.com/amadeogarcia

UPDATES:
    Version 0.0.0
    2020/10/27:1130>
        Release version.
    
    Version 0.1.0
    2020/10/29:1240>
        Simplified version.
        Documentation improved.

    Version 1.0>
    2020/11/04:1530>
        Added extract feature.
        Description modified.
        Structure improved.

DESCRIPTION:
    This script takes a big file HTML, reads only its 100th line and then splits it into small HTML
    files to distribute them using iframes.

DISCLAIMER:
    This code is in the public domain. Please feel free to modify,
    use, etc however you see fit. But, please give reference to
    original authors as a courtesy to Open Source developers.

'''

#······································ Definition of functions ······································#

# See explanation below #
def extract_substr(s, open, close, start = 0):
    ipos = s.find(open, start)
    fpos = s.find(close, ipos)
    if( ipos != -1 and fpos != -1 ):
        ipos += len(open)
        return s[ipos:fpos], fpos
    else: return "ERROR", -1

'''
extract_substr(s, open, close, start):
    This function finds and returns the first occurrence of a substring of s preceded by open and
    followed by close. It also returns the position in which substring ends, easing the process of
    searching recursively the same substring. When no substring is valid, returns "ERR".

    EXAMPLE:
    >>> s = "Hello <b>World</b>!"
    >>> substr_1 = extract_substr(s, '<b>', '</b>')
    >>> substr_1
    'World'

'''

# Adds some HTML lines to the string so the iframe looks prettier #
def beautify(s):
    STYLE_LN = '<link rel="stylesheet" type="text/css" href="../styles.css">\r\n'
    return str(STYLE_LN + '<div>' + s + '</div>')

#··································· Extracting the line number 100 ····································#

line = "" ; count = 1
# Open the whole HTML file #
with open(r"C:\Users\amade\Documents\web-comunicaciones\.httrack\x-y.es\argentina.html", "r", encoding='utf-8-sig') as html:
    for ln in html:         # Scan it line by line #
        if count == 100:
            line = ln       # Extract the 100th line #
            break
        count += 1

#······································ Now the splitting starts ·······································#

line = extract_substr(line, '<tbody>', '</tbody>')[0]   # Extract only the tbody part #
# Delete classes so all  <td> elements are the same #
line = line.replace(' class="sube"', '')
line = line.replace(' class="baja"', '')

i = 0; j = 0; count_row = 1; count_elem = 1
row = ""; elem = ""
# Will only use 10 rows or less #
while( i > -1 and count_row <= 10 ):
    row, i = extract_substr(line, '<tr>', '</tr>', i)           # Read a row #
    # Reset element iterators #
    j = 0
    count_elem = 1
    while( j > -1 ):
        elem, j = extract_substr(row, '<td>', '</td>', j)    # Read an element inside that row #
        # Will avoid the sixth and seventh elements (I don't want any deaths in my page) #
        if( j > -1 and count_elem not in range(6, 8) ):
            # Prepare the HTML styling code #
            elem = beautify(elem)
            # Create and write the file #
            with open(r"C:\Users\amade\Documents\web-comunicaciones\covid19\row_" + str(count_row) + r"\elem_" + str(count_elem) + r".html", "w") as ef:
                ef.write(elem)
        count_elem += 1
    count_row += 1