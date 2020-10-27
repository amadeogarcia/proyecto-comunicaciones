'''
mk_substr():
    A function that creates a substring from parts of the original string. Useful for extracting data from HTML files.
    EXAMPLE:
    >>> str = "<p>Lorem ipsum...</p><br><p>...dolor sit amet.</p>"
    >>> substr_1 = mk_substr(str, '<p>', '</p>', 0)
    >>> substr_1
    'Lorem ipsum...'
    >>> substr_2 = mk_substr(str, '<p>', '</p>', 21)
    >>> substr_2
    '...dolor sit amet.'

    See that this function returns a tuple with the final position of the main string, making it easy to use inside a loop,
    extracting multiple substrings from longs string, starting each time from a subsequent position.
'''

# See explanation above #
def mk_substr(str, ielem, felem, inicio):
    substr = ""
    ipos = str.find(ielem, inicio)
    fpos = str.find(felem, ipos)
    if( ipos == -1 or fpos == -1 ): return "ERR", -1
    else:
        ipos += len(ielem)
        for i in range(ipos, fpos):
            substr += str[i]
        return substr, fpos

# Open a chunk of HTML code #
rl = open("/mnt/c/users/amade/documents/github/proyecto-comunicaciones/covid19/raw_line.txt")
s = rl.read()
s, null = mk_substr(s, '<tbody>', '</tbody>', 0)    # Extract only the tbody part #

i = 0; j = 0; k = 0; count_row = 1; count_elem = 1; count_var = 1
row = ""; elem = ""; var = ""
# Will only use 10 rows or less #
while( i != -1 and count_row <= 10 ):
    row, i = mk_substr(s, '<tr>', '</tr>', i)           # Read a row #
    # Reset element iterators #
    j = 0
    count_elem = 1
    while( j != -1 ):
        elem, j = mk_substr(row, '<td>', '</td>', j)    # Read an element inside that row #
        # Will avoid the fourth element (I don't want any deaths in my page) #
        if( j != -1 and count_elem != 4 ):
            # Create the file #
            f_elem = open("/mnt/c/users/amade/documents/github/proyecto-comunicaciones/covid19/files/row_" + str(count_row) + "/elem_" + str(count_elem) + ".html", "w")
            f_elem.write(elem)
        count_elem += 1
    # Reset varioation iterators #
    k = 0
    count_var = 1
    # The element 'variation' is treated differently within this HTML file #
    while( k != -1 ):
        var, k = mk_substr(row, '<td class="sube">', '</td>', k)                # Search and read a positive variation #
        if( k == -1 ): var, k = mk_substr(row, '<td class="baja">', '</td>', k) # If there isn't, search and read a negative variation #
        # Will avoid third variation, it's the variation of deaths #
        if( k != -1 and count_var != 3 ):
            # Create the file #
            f_var = open("/mnt/c/users/amade/documents/github/proyecto-comunicaciones/covid19/files/row_" + str(count_row) + "/var_" + str(count_var) + ".html", "w")
            f_var.write(var)
        count_var += 1
    count_row += 1