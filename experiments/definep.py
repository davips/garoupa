#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
#
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.

from bigfloat import *
from sympy import isprime

a18 = tuple("0123456789abcdefgh")
a17 = tuple("0123456789abcdefg")
a16 = tuple("0123456789abcdef")
com = tuple("0123456789abcdefgh")
a64 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.")
a65 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._")
a40 = tuple("pqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._")
aa = tuple("ghijklmnopqrstuvwxyz")


def dec(string, alphabet):
    rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))
    num = 0
    for char in string:
        num = num * len(alphabet) + rev_alphabet[char]
    return num


def enc(num, alphabet):
    encoded = ""
    while num:
        num, rem = divmod(num, len(alphabet))
        encoded = alphabet[rem] + encoded
    return encoded


def enc2(num):
    encoded = ""
    d = 0
    while num:
        d += 1
        num, rem = divmod(num, 65) if d < 32 else divmod(num, 40)
        encoded = (a65[rem] if d < 32 else a40[rem]) + encoded
    return encoded.rjust(32, "h")


for b, digits in [[156, 40]]:  # , [124, 32], [252, 64], [156, 32]]:
    with precision(150):
        bb = b + 4
        base = 64
        n = pow(2 ** bb, 1 / 4)
        for i in range(int(n) - 100, 2 ** 300):
            if isprime(i):
                p = i
                hibase_digits = digits
                lobase_digits = digits - 1
                g = log(p ** 6) / log(2)

                # representáveis
                comutantes = p ** 4
                naocomutantes = base ** hibase_digits
                tot = naocomutantes + comutantes
                gmx = log(tot) / log(2)

                # print(p, g / gmx, g, gmx)
                if gmx < g:
                    p = pold
                    g = gold
                    gmax = gmaxold
                    print()
                    print(b, int(p), f"base-{base}")
                    print("Z", log(p) / log(2), p / p ** 4, p ** 4 / p ** 6)
                    print("H", log(p ** 4) / log(2))
                    print("G", g)
                    print("Gmax", gmx)
                    print("com", log(comutantes) / log(2))
                    print("ncom", log(naocomutantes) / log(2))
                    print(gmx >= g)
                    break
                pold = p
                gold = g
                gmaxold = gmx
                # print("vale:", p, g / gmx)
        #
        #         # mesclando alfabetos
        #         print()
        #         print("0" * digits)
        #         print("0" * (digits - 2) + "--", (enc(p - 1, a64) + "--").rjust(digits, "0"))
        #         print("0" * (digits - 2) + "1-", enc(2 ** b - 1, a16) + "-")
        #         print(enc(2 ** b - 1, a16) + "-", enc(p ** 4 - 1, aa).rjust(digits - 1, "0") + "-")
        #         print(("0" * (digits - 1)) + "1", enc(p ** 6 - 1 - p ** 4, a64).rjust(digits, "0"))
        #         e1 = 3
        #         e2 = digits - e1 - 1
        #         take = 46
        #         mixed = take ** e1 * 16 ** e2
        #         print("p**4-p = \t", log(p ** 4 - p) / log(2))
        #         print(f"{take}^{e1}*16^{e2}\t", log(mixed) / log(2))
        #         if e1 == 0:
        #             print("ffff..ff-  \t", log(dec(e2 * "f", a16)) / log(2))
        #         elif e2 == 0:
        #             print("ffff..ff-  \t", log(dec(e1 * "f", a64[:take])) / log(2))
        #         else:
        #             print("ffff..ff-  \t", log(dec(e1 * "f", a64[:take]) * dec(e2 * "f", a16)) / log(2))
        #
        #         # favorecendo  hexdigest tanto em 'com' como em 'noncom'
        # 160 bits
        nn = dec("f" * 37, a16) * (16 * 64 + 16)
        print(log(nn + p) / log(2))
        mm = dec("f" * 37, a16) * 64 ** 2
        print(nn / p ** 4, mm / p ** 4)
        res, rem = divmod(p + p ** 4, 64 ** 2)
        print(enc(res, a64) + "_" + enc(rem, a16))
        exit()
        e1 = 0
        e2 = digits - e1 - 1
        take = 46
        mixed = take ** e1 * 16 ** e2
        rest, z1 = p ** 6, 2 ** (bb // 4 - 4)
        print()
        print("0" * digits)
        print("-" + "0" * (digits - 1), "-" + (enc(z1 - 1, a16)).rjust(digits - 1, "0"))
        rest -= z1
        z2 = p - z1
        print("--" + "0" * (digits - 3) + "1", "--" + (enc(z2, a64)).rjust(digits - 2, "0"))
        rest -= z2
        h1 = 2 ** b - p
        #         """
        #         parei aqui
        #         dúvida: H\Z idealmente teria 128 bits (ou 124), mas isso pede G com 384 que requer 64*base64
        #         única solução:
        #
        #         """
        print("0" * (digits - 2) + "1-", (enc(h1, a16) + "-").rjust(digits, "0"))
        print()
        print("0" * (digits - 2) + "1-", enc(2 ** b - 1, a16) + "-")
        print(enc(2 ** b - 1, a16) + "-", enc(p ** 4 - 1, a64).rjust(digits - 1, "0") + "-")
        print(("0" * (digits - 1)) + "1", enc(p ** 6 - 1 - p ** 4, a64).rjust(digits, "0"))
        print("p**4-p = \t", log(p ** 4 - p) / log(2))
        print(f"{take}^{e1}*16^{e2}\t", log(mixed) / log(2))
        if e1 == 0:
            print("ffff..ff-  \t", log(dec(e2 * "f", a16)) / log(2))
        elif e2 == 0:
            print("ffff..ff-  \t", log(dec(e1 * "f", a64[:take])) / log(2))
        else:
            print("ffff..ff-  \t", log(dec(e1 * "f", a64[:take]) * dec(e2 * "f", a16)) / log(2))
        exit()

"""
comuta      0       -> 2^124-1  -0000000000000000000000000000000 -> -fffffffffffffffffffffffffffffff
            2^128   -> p^4-1    -ggggggggggggggggggggggggggggggg -> -ggggggfffffffffffffffffffffffff
não comuta  p^4     -> 62^31-1  _0000000000000000000000000000000 -> _ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
            62^31   -> p^6-1    -0000000000000000000000000000000 -> -...............................
________________________________
124 4294967291 base-64
Z 31.999999998320481924190276249507 1.2621774527617227e-29 5.421010875049297e-20
H 127.99999999328192769676110499803
G 191.99999998992289154514165749734
Gmax 192.00000000000000000007820865606
True
252 18446744073709551557 base-64
Z 63.999999999999999995385689362186 1.5930919111324523e-58 2.938735877055719e-39
H 255.99999999999999998154275744875
G 383.99999999999999997231413617312
Gmax 384.00000000000000000000000000000
True

================================================
124 3948961777 base-63
Z 31.878826257641847570486884584256 1.6238698171825131449924620212117e-29 6.4125998388777222423752914748933e-20
H 127.51530503056739028194753833702
G 191.27295754585108542292130750564
Gmax 191.27295755199732705127482482794
True
252 15594299138352202201 base-63
Z 63.757652517332442340861546828748 2.6369531719222887946128298575521e-58 4.1121436576782854663902873205712e-39
H 255.03061006932976936344618731499
G 382.54591510399465404516928097218
Gmax 382.54591510399465410236462112805
True
--------------------------------------------------------------
128 4294967311 base-74
Z 32.000000005038554215697873037961 1.2621774351293075342787790829219e-29 5.4210108245621989177933681221403e-20
H 128.00000002015421686279149215184         G 192.00000003023132529418723822756
256 18446744073709551629 base-74
Z 64.000000000000000001016712513375 1.5930919111324522736607746612809e-58 2.9387358770557187657798023741112e-39
H 256.00000000000000000406685005350         G 384.00000000000000000610027508066

128 682641389 base-65
Z 39.960342112216916428118534603213 3.1435628743516298810283827397274e-27 2.1459261269562290963991199418701e-18
H 128.00000005544992489926623086780         G 186.69310535093859721336469504422
256 2931922412478934547 base-65
Z 71.960342098354435225388002052845 3.9677342818630848879316048247841e-56 1.1633089067755388719285647385725e-37
H 256.00000000000000008834410066673         G 378.69310526776370999698149974272

128 326909599 base-63
Z 43.147050703953920784954541512680 2.8623120659138016681048144147826e-26 9.3571728968074247188567597030378e-18
H 128.00000019937907026558202387174         G 184.56863319632916991933367877791
256 1404065987943330311 base-63
Z 75.147050654109153114856329880497 3.6127461142053736528097563743828e-55 5.0725339420301955940135225527976e-37
H 255.99999999999999958518917734321         G 376.56863289726056389874440898481
"""

# print("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyzµÆÐØÞæøþðñÑ")
# ÀÁÂÃÄÅ
# Æ
# ÈÉÊËÌÍÎÏ
# ÑÒÓÔÕÖ
# ÙÚÛÜÝ
# àáâãäå
# æ
# ç
# èéêëìíîïðñòóôõö
# ùúûüý

# with precision(220):
#     p = 18446744073709551557
#     p = 1099511627689  # 40
#     p = 4294967291
#     print()
#     ba = 16
#     print(f"b{ba}:", 3 * ba ** 31 > p ** 4, p ** 4 > dec(31 * "f", a64[:ba]))
#     print(f"b{ba}:", (ba ** 31 + 20 ** 30) / p ** 4, p ** 4 > dec(31 * "f", a64[:ba]))
#     print(f"b{ba}:", sum(64 * ba ** i for i in range(30, 1, -1)) * 4 / p ** 4, p ** 4 > dec(31 * "f", a64[:ba]))
#     # print(f"b{ba} digits needed to H:", log(p ** 4) / log(ba), f"p={p}", dec(31 * "f", a64[:ba]) < p ** 4)
#     # print("b64  digits needed to G\H:", log(p ** 6 - p ** 4) / log(64), f"p={p}")
#     # print("b422 digits needed to G\H:", log(p ** 6 - p ** 4) / log(422), f"p={p}")
#     # print(16 ** 29 * 64 ** 2 / p ** 4, p / p ** 4)
#     # print()
#     # print(enc(p ** 4, a16))
#     print(log(((64 ** 64) ** (1 / 6)) ** 4) / log(2))
#     print(enc(p - 1, a64[:16]))
#     print(enc(p ** 4 - 1 - 2 ** 124, a64[16:36]), "___________________________")
#     print(enc(p ** 6 - 1 - p ** 4 + 1, a64))
#     print(enc(p ** 4, a64))
#     print(dec("1111111111111111111111", a64) < p ** 4)
#     exit()
#
#     n = (2 ** 128) ** (1 / 4)
#     # n = (2 ** 256) ** (1 / 4)
#     for i in range(int(n), 2 ** 300):
#         if isprime(i):
#             p = i
#             break
#     print("p", p)
#     print("p", log(p ** 4) / log(2))
#     print("p", log(p ** 6 - p ** 4) / log(2), log(65 ** 63 * 40) / log(2))  # 4294967311
#     # print("p", log(p ** 6 - p ** 4) / log(2), log(65 ** 63 * 40) / log(2))  # 18446744073709551629
#     # print("b65  digits needed to |G\H| / 40:", log((p ** 6 - p ** 4) / 40) / log(65), f"p={p}")
#     """
#     H: 00000000000000000000000000000000 -> ffffffffffffffffffffffffffffffff -> g000003c00000546000034bc0000c5c0
#     G: h0000000000000000000000000000000 -> Z_______________________________
#                                         -> h0000000000000000000000000000000 -> hfffffffffffffffffffffffffffffff (pseudo)
#                                         -> h0000000000000000000000000000000 -> _BxIYmOj_s2FWe1dulyp5v9saqWyb7Dy (real)
#
#     ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._  ~
#     """
#     print(9999999999999, enc(p ** 4 - 2 ** 256 - 1, a64[:16]))
#     print()
#     print(enc2(p ** 6 - p ** 4 - 1))

# all = "".join(re.findall(r"\w+", "".join(chr(i) for i in range(600)
#                                          if chr(i).isalnum()
#                                          and unicodedata.name(chr(i), '').startswith('LATIN ')
#                                          and chr(i) not in "²³¹¼½¾ǄǅǆǇǈǉǊǋǌǤǥǱǲǳǷǺǻʰʱʲʳʴʵʶʷʸʹʺʻɂʼʽʾʿˀˁˆˇˈˉˊˋˌˍˎˏːˑˠˡˢˣˤˬˮ"
#                                          )))
# print(all)
# print(len(all))
# print(unicodedata.name("ǅ"))

"""
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªµºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâã
äåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇň
ŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƒƓƔƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬ
ƭƮƯưƱƲƳƴƵƶƷƸƹƺƻƼƽƾƿǀǁǂǃ
ǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǢǣǦǧǨǩǪǫǬǭǮǯǰǴǵǶǸǹǼǽǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚț
Ȝȝ
ȞȟȠȡ
ȢȣȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȴȵȶȷȸȹȺȻȼȽȾȿɀɁɂɃɄɅɆɇɈɉɊɋɌɍɎɏɐɑɒɓɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɩɪɫɬɭɮɯɰɱɲɳɴɵɶɷɸɹɺɻɼɽɾɿʀʁʂʃʄʅ
ʆʇʈʉʊʋʌʍʎʏʐʑʒʓʔʕʖʗʘʙʚʛʜʝʞʟʠʡʢʣʤʥʦʧʨʩʪʫʬʭʮʯͶͷͺͻͼͽͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμν
ξοπρςστυφχψωϊϋόύώϏϐϑϒϓϔϕϖϗϘϙϚϛϜϝϞϟϠϡϢϣϤϥϦ
"""

# for i in range(2000):
#     print(i, enc2(65 ** 31 - 1000 + i))


"""
H < 2^128 [[campeão]]
    clara e simples separação entre H e G\H
    _ mata 4 bits do hex comutativo
    ñcom livre e b64
    H excedente requer gambiarra: _ + base16  e  __ + base20 (gh...z)
    requer 24 bytes quase exatos 

H > 2^128
    complexa separação entre H e G\H
    bagunça/mata uma letra do hex não-comutativo
    >g indica ñcom e base-65 * base-40
    H excedente requer gambiarra?
    requer 25 bytes mal ocupados 
"""
