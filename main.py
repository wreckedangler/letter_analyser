import requests
from bs4 import BeautifulSoup
inputWeb = input("Enter web_page name: ")
url = "https://"f"{inputWeb}/"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = []
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    "font",
    "style",
    "html"
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:

    if t.parent.name not in blacklist:
        output += t
        print(t)

# print(output)

file = "D:\\Python\\Text_files\\some text.txt"
input = input("Name of Status_file: ")


def read_file(output, input):
    ca = 0
    cb = 0
    cc = 0
    cd = 0
    ce = 0
    cf = 0
    cg = 0
    ch = 0
    ci = 0
    cj = 0
    ck = 0
    cl = 0
    cm = 0
    cn = 0
    co = 0
    cp = 0
    cq = 0
    cr = 0
    cs = 0
    ct = 0
    cu = 0
    cv = 0
    cw = 0
    cx = 0
    cy = 0
    cz = 0
    special = 0

    with open("D:\\Python\\Text_files\\"f"{input}""_stats"".txt", "w") as stat:
        checklist = []

        while output:
            lenght = len(output)
            count = 0
            for i in range(lenght):
                checklist += output[count]
                count += 1

            for c in checklist:
                if str(c).upper() == "A":
                    ca += 1
                elif str(c).upper() == "B":
                    cb += 1
                elif str(c).upper() == "C":
                    cc += 1
                elif str(c).upper() == "D":
                    cd += 1
                elif str(c).upper() == "E":
                    ce += 1
                elif str(c).upper() == "F":
                    cf += 1
                elif str(c).upper() == "G":
                    cg += 1
                elif str(c).upper() == "H":
                    ch += 1
                elif str(c).upper() == "I":
                    ci += 1
                elif str(c).upper() == "J":
                    cj += 1
                elif str(c).upper() == "K":
                    ck += 1
                elif str(c).upper() == "L":
                    cl += 1
                elif str(c).upper() == "M":
                    cm += 1
                elif str(c).upper() == "N":
                    cn += 1
                elif str(c).upper() == "O":
                    co += 1
                elif str(c).upper() == "P":
                    cp += 1
                elif str(c).upper() == "Q":
                    cq += 1
                elif str(c).upper() == "R":
                    cr += 1
                elif str(c).upper() == "S":
                    cs += 1
                elif str(c).upper() == "T":
                    ct += 1
                elif str(c).upper() == "U":
                    cu += 1
                elif str(c).upper() == "V":
                    cv += 1
                elif str(c).upper() == "W":
                    cw += 1
                elif str(c).upper() == "X":
                    cx += 1
                elif str(c).upper() == "Y":
                    cy += 1
                elif str(c).upper() == "Z":
                    cz += 1
                else:
                    if str(c) != " " and str(c) != "\n" and str(c) != "":
                        special += 1

            else:
                chartlist_val = [ca, cb, cc, cd, ce, cf, cg, ch, ci, cj, ck, cl, cm, cn, co, cp, cq, cr, cs, ct, cu,
                                 cv, cw, cx, cy, cz]
                chartlist_let = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                                 "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

                chartlist_val, chartlist_let = (list(t) for t in zip(*sorted(zip(chartlist_val, chartlist_let))))
                counter = 0
                for let in chartlist_let:
                    stat.write(f"{let} = {chartlist_val[counter]}" + "\n")
                    counter += 1
                stat.write("\n")

                stat.write(f"Vokale = {ca + ce + ci + co + cu}" + "\n")
                stat.write(f"Konsonanten ="
                           f" {cb + cc + cd + cf + cg + ch + cj + ck + cl + cm + cn + cp + cq + cr + cs + ct + cv + cw + cx + cy + cz}" + "\n")
                stat.write(f"Sonstige Zeichen und Zahlen = {special}" + "\n")
                total = 0
                for i in chartlist_val:
                    total += i
                total = total + special
                stat.write("\n")
                stat.write(f"Total Zeichen = {total}")
                print("analyzed with no error")

                break


read_file(output, input)
