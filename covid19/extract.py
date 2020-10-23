def substring(str, ipos, fpos):
    substr = ""
    for i in range(ipos, fpos):
        substr += str[i]
    return substr

raw = open("raw_line.txt")
s = raw.read()
tri = '<tr>'
trf = '</tr>'
i = 4582

while(1):
    ipos = s.find(tri, i)
    fpos = s.find(trf, ipos) + 5
    row = substring(s, ipos, fpos)
    f = open("test.html", "w")
    f.write(row)
    break