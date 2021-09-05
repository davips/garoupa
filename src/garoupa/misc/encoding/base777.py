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
#  part of this work is illegal and is unethical regarding the effort and
#  time spent here.

"""
Base to enable shorter ids, but at the expense of heavily adopting utf-8 (up to 2-byte) chars

777 chars provide 19.99631153679756 and 39.99262307569413 digits for 32 and 64 versions.
The choice is not arbitrary. 777 is ideal to balance variability even in the most significant digit
for any version (UT32.4, UT40.4, UT64.4, ...) of Hosh.
"""
alphabet = tuple(
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzµÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåç"
    "èéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĴĵĶķĸĹĺĻĽĿŁłŃńŅņŇňŉŊŋŌōŎŏŐő"
    "ŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƈƉƊƋƌƍƎƏƐƑƓƕƖƗƘƙƚƛƜƝƞƟƠơƢƣƤƥƦƧƨƩƪƫƬƭƮƯưƱƲƳƴƵƶƹƺƻ"
    "ƼƽƾƿǍǎǏǐǑǒǓǔǕǖǗǘǙǚǛǜǝǞǟǠǡǦǧǨǩǪǫǬǭǮǯǰǴǵǸǹǾǿȀȁȂȃȄȅȆȇȈȉȊȋȌȍȎȏȐȑȒȓȔȕȖȗȘșȚțȞȟȠȤȥȦȧȨȩȪȫȬȭȮȯȰȱȲȳȽɃɄɅɆɌɍɐɑɒɓ"
    "ɔɕɖɗɘəɚɛɜɝɞɟɠɡɢɣɤɥɦɧɨɪɫɬɯɰɱɲɳɴɵɷɸʀʁʂʉʊʋʌʍʎʏʐʑʒʓʘʙʚʛʜʝʞʟʠͶͷͻͼͽͿΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήί"
    "ΰαβγδεζηθικλμνξοπρςστυφχψωϊϋόύώϒϓϔϕϖϘϙϜϤϫϰϱϲϳϴϵϷϸϹϺϻϼϽϾϿЀЁЂЃЄЅІЇЈЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЧШЪЬЭЯаб"
    "вгдежзийклмнопрстуфхчшъьэяѐёђѓєѕіїјћќѝўџѢѣѲѳҐґҒғҖҗҘҙҪҫҮүҰұҲҳҺһӀӁӂӏӐӑӒӓӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳ"
    "ԀԐԑԚԛԜԝԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖաբգդեզէըթժիխծկհձղճմնոպռսվտրցւփօև"
)
rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))


def b777dec(string):
    """
    Usage:

    >>> b777dec("ևև") == 777**2 - 1
    True

    Parameters
    ----------
    string

    Returns
    -------

    """
    num = 0
    for char in string:
        num = num * 777 + rev_alphabet[char]
    return num


def b777enc(num, digits):
    """
    Usage:

    >>> b777enc(123456, 10)
    '00000000ģӪ'
    >>> n = b777dec(b777enc(123456, 10))
    >>> n == 123456
    True
    """
    encoded = ""
    while num:
        num, rem = divmod(num, 777)
        encoded = alphabet[rem] + encoded
    return encoded.rjust(digits, "0")
