from tkinter import *
from tkinter import filedialog


def browse_files():

    global filename
    filename = str(filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files",
                                                                                                "*.txt*"), (
                                                                                                "all files",
                                                                                                "*.*"))))

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + filename)


def analyze_letters():
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
    with open(filename) as fn:
        with open("D:\\Python\\Text_files\\Statistics.txt", "w") as stat:
            checklist = []
            checklist += fn.read()
            while checklist:
                lenght = len(checklist)
                count = 0
                for i in range(lenght):
                    checklist += checklist[count]
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
                    label_file_explorer.configure(text="Analyzed with no error")

                    break


def analyze_words():
    with open(filename) as fn:
        with open("D:\\Python\\Text_files\\Statistics.txt", "w") as stat:
            lenghtcounter = 0
            checklist = []
            checklist += fn.read().split(" ")
            wordlenght_list = []
            wordlist = []

            for word in checklist:
                word_list = []
                filtered_word = []
                filtered_word2 = []
                upper_count = 0

                for character in word:

                    if str(character).isalpha():
                        word_list += character
                        lenghtcounter += 1

                for letter in word_list:
                    if str(letter).isupper():
                        upper_count += 1
                    if upper_count < 2:

                        filtered_word += letter
                    elif upper_count == 2:
                        filtered_word2 += letter
                if len(filtered_word) > 0:
                    wordlenght_list.append(len(filtered_word))

                if len(filtered_word2) > 0:
                    wordlenght_list.append(len(filtered_word2))

    durchschnitt = sum(wordlenght_list) / len(wordlenght_list)
    print(round(durchschnitt, 2))
    print(max(wordlenght_list))
    print(len(wordlenght_list))
    print(lenghtcounter)


def analyze_sentence():
    with open(filename) as fn:
        with open("D:\\Python\\Text_files\\Statistics.txt", "w") as stat:
            lenghtcounter = 0
            checklist = []
            checklist += fn.read().split(".")
            sentencelenght_list = []
            wordlist_splitted = []

            for sentence in checklist:

                wordlist = []
                wordlist += sentence
                sentence_list = []
                wordlist_splitted = []
                for character in wordlist:

                    if str(character).isalpha() and character != " " and character != "[" and character != "]" \
                            and character != "\n":
                        wordlist_splitted.append(character)

                    for i in wordlist_splitted:
                        sentence_list.append(i)

                lenght = len(wordlist_splitted)
                print(wordlist_splitted)
                if lenght > 2:
                    sentencelenght_list.append(lenght)
        print(sentencelenght_list)


def analyze_option():
    selection = str(listbox_1.curselection())

    if selection == "(0,)":
        analyze_letters()
    elif selection == "(1,)":
        analyze_words()
    elif selection == "(2,)":
        analyze_sentence()


top = Tk()
top.geometry("320x320")
label_file_explorer = Label(top, text = "Select a file first", fg = "blue")

label_file_explorer.pack(anchor=N)

button_explore = Button(top,
                        text="Browse Files",
                        command=browse_files)

button_explore.pack(anchor=N)


lbl = Label(text="What should i analyze? ")
lbl.pack()
listbox_1 = Listbox(top, selectmode=EXTENDED)
listbox_1.insert(1, 'Letters')
listbox_1.insert(2, 'Words')
listbox_1.insert(3, 'Sentence')
listbox_1.insert(4, 'Nothing')
listbox_1.insert(5, 'Nothing yet')
listbox_1.pack()
label = Label(top)
label.pack()


button_exit = Button(top,
                     text="Exit", fg="red",
                     command=exit)

button_analyse = Button(top, text="Analyze", command=analyze_option)
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

radio = IntVar()
button_analyse.pack(anchor=N)
button_exit.pack(anchor=N)
top.mainloop()



#                            != "." and character != "," and character != ":" and character != ";"\
#                            and character != "?" and character != "!" and character != '"' and character != "/" \
#                            and character != "%" and character != "-" and character != "+" and character != "*" \
#                            and character != "[" and character != "]" and character != "1" and character != "2" \
#                            and character != "3" and character != "4" and character != "5" and character != "6" \
#                            and character != "7" and character != "8" and character != "9" and character != "0" \
#                            and character != "#" and character != "€" and character != " " and character != "“" \
#                            and character != "=" and character != "(" and character != ")" and character != "" \
#                            and character != "\n":