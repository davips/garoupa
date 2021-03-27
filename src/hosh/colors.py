from hashlib import md5

import colored
from colored import stylize


def b62enc(num):
    encoding = ""
    while num:
        num, rem = divmod(num, 62)
        encoding = alphabet[rem] + encoding
    return encoding


def paint(txt, fgr, fgg, fgb):
    fgcolor = f"#{hex(fgr)[2:].rjust(2, '0')}{hex(fgg)[2:].rjust(2, '0')}{hex(fgb)[2:].rjust(2, '0')}"
    return stylize(txt, colored.fg(fgcolor) + colored.attr("bold"))


alphabet = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))


def b62dec(string):
    num = 0
    for char in string:
        num = num * 62 + rev_alphabet[char]
    return num


def lim(x):
    return min(255, max(0, x))


def colorize128bit(id, ampl=0.8, change=0.1):
    numbers = md5(id.encode()).digest()
    margin = 60
    base = numbers[0]
    ch = 255 * change
    fgr = margin + (base ^ numbers[1]) * ampl
    fgg = margin + (base ^ numbers[2]) * ampl
    fgb = margin + (base ^ numbers[3]) * ampl
    out = ""
    for i, c in enumerate(id):
        quot, dr = divmod(b62dec(c), 4)
        quot, dg = divmod(quot, 4)
        db = quot % 4
        r = max(margin, lim(fgr + ch * (dr - 2)))
        g = max(margin, lim(fgg + ch * (dg - 2)))
        b = max(margin, lim(fgb + ch * (db - 2)))
        out += f"{paint(c, int(r), int(g), int(b))}"
    return out
