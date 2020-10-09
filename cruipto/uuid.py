from functools import lru_cache
from math import factorial

import cruipto.alphabets as alph
from cruipto.avatar import avatar
from cruipto.classproperty import ClassProperty
from cruipto.encoders import enc, dec
from cruipto.linalg import int2pmat, pmat_transpose, pmat_mult, pmat2int, print_binmatrix


# HINT: xxxxxxxxxxxx is the last MD5 value, so no original uuid starts with a digit larger than x.  <- TODO define x
# number of digits >= log(factorial(35) - 1, len("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")) = 22.32449128323706
# last number = 35! - 1 = 10333147966386144929666651337523199999999

class UUID:
    """Flexible representation of a (non-standard) universal unique identifier.
    Intended to be an extension and "replacement" of MD5 (or SHA256) hashes.

    This implementation intrinsically cannot comply with RFC 4122,
    ISO/IEC 9834-8:2005, nor any related standards; since it is deterministic,
    no time-dependant, and forms a non-abelian group over multiplication which
    needs fredom to operate on all bits.

    It allows cummulative and reversible combination of UUID objects.
    For a fixed number of 'bits' (132 or 260), a UUID object represents any
    given decimal integer, permutation matrix (see bellow), bytes or strings;
    provided they are within certain bounds related to 'bits'.

    The bit-size options 132 and 260 were defined to accomodate the usual 128
    and 256-bit hashes.
    The increase was necessary due to the mismatch between the amount of
    possible (128/256-bit) numbers and the amount of possible permutation
    matrices (sized 35x35/58x58).

    E.g., for MD5 128-bit hashes, some 35x35 matrices resulting from UUID
    operations will represent a number that exceeds the highest
    number (2^128 - 1), becoming a 133-bit number (log2(35)) in the worst case.
    Therefore, for a fixed-size exchangeable representation, one should choose
    whether to use uuid.n which is at most a 133-bit (or 261-bit) number,
    or uuid.id which is a fixed-size string with 14 (or 27) characters, which
    is intended to be faster and visually shorter at the expense of using more
    bytes.

    Note that, despite the bit-size options (namely 132/260), the real limit
    is somewhere between 132/260 and 133/261. So, it is highly recommended to
    provide only up to 132/260 bits when generating a new UUID object directly
    from binary information (not a common, expected scenario).
    It will be represented by 16/32 bytes anyway (128/256 bits) in the hardware.

        Parameters
        ----------
        identifier
        bits
    """

    # Default values for 128 bits.
    bits = 128
    side = 35
    digits = 23

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    alphabetrev = {char: idx for idx, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")}
    lower_limit = 1  # Zero has cyclic inversions and should not be used: Z*Z=I  Z-¹=Z
    identity = ClassProperty("identity_")

    # Lazy starters.
    _n = None  # number
    _m = None  # matrix
    _id = None  # pretty
    _isfirst = None
    _t = None  # inverse (also transpose) pmatrix
    _identity = None

    def __init__(self, identifier=None, bits=128, ignore_call=False):
        self.ignore_call = ignore_call
        if identifier is None:
            identifier = self.first_matrix

        # Handle internal representation for the provided number of bits.
        if bits == 256:
            self.bits = bits
            self.side = 58
            self.digits = 27
            raise NotImplementedError("256 bits still not implemented.")

        elif bits != 128:
            raise NotImplementedError("Only 128 and 256 bits are implemented.")

        # Handle different types of the provided identifier.
        if isinstance(identifier, list):
            side = len(identifier)
            if side != self.side:
                print_binmatrix(identifier)
                raise Exception(f"Permutation matrix should be {self.side}x{self.side}!" f" Not {side}x{side}")
            self._m = identifier
        elif isinstance(identifier, int):
            if identifier > self.upper_limit or identifier < self.lower_limit:
                raise Exception(f"Number should be in the interval [{self.lower_limit}," f"{self.upper_limit}]!")
            self._n = identifier
        elif isinstance(identifier, str):
            size = len(identifier)
            if size != self.digits:
                raise Exception(f"Str id should have {self.digits} chars! Not {size}!")
            self._id = identifier
        elif isinstance(identifier, bytes):
            from cruipto.encoders import md5_int

            self._n = md5_int(identifier)
        else:
            raise Exception("Wrong argument type for UUID:", type(identifier))

    def print_matrix(self):
        print_binmatrix(self.m)

    @staticmethod  # Needs to be static to avoid self.__hash__ starting calculation of lazy values
    @lru_cache()
    def _lazy_upper_limit(side: int) -> int:
        # Identity matrix has special properties: A*I=A  I-¹=I
        return factorial(side) - 2  # (side! - 1) is identity

    @staticmethod  # Needs to be static to avoid self.__hash__ starting calculation of lazy values
    @lru_cache()
    def _lazy_first_matrix(side):
        return int2pmat(1, side=side)

    @classmethod
    def identity_(cls, side=35):
        """UUID corresponding to a 35x35 identity permutation matrix.
        It is enough to represent MD5 hashes."""
        if cls._identity is None:
            cls._identity = UUID(int2pmat(UUID._lazy_upper_limit(side) + 1, side=side))
        return cls._identity

    @property
    def upper_limit(self):
        return self._lazy_upper_limit(self.side)

    @property
    def first_matrix(self):
        return self._lazy_first_matrix(self.side)

    @property  # Avoiding lru, due to the need of a "heavy" hashable function.
    def t(self):
        """Transpose, but also inverse matrix."""
        if self._t is None:
            self._t = UUID(pmat_transpose(self.m), ignore_call=self.ignore_call)
        return self._t

    @property  # Cannot be lru, because id may come from init.
    def id(self):
        """'Pretty' printing version, proper for use in databases also."""
        if self._id is None:
            self._id = enc(self.n, self.alphabet, padding=self.digits)
        return self._id

    @property  # Cannot be lru, because m may come from init.
    def m(self):
        """Id as a permutation matrix (list of numbers)."""
        if self._m is None:
            self._m = int2pmat(self.n, self.side)
        return self._m

    @property  # Cannot be lru, because n may come from init.
    def n(self):
        """Id as a natural number."""
        if self._n is None:
            if self._m:
                self._n = pmat2int(self.m)
            elif self._id:
                self._n = dec(self.id, self.alphabetrev)
            else:
                raise Exception("UUID broken, missing data to calculate n!")
        return self._n

    @property  # Cannot be lru, because id may come from init.
    def isfirst(self):
        """Is this the origin of all UUIDs?"""
        if self._isfirst is None:
            self._isfirst = self.m == self.first_matrix
        return self._isfirst

    def generate_avatar(self, file="uuid-avatar-{id}.jpg"):
        """Colorful visual representation of UUID.

        <$id> at the filename will be replace by the string representation of this UUID object."""
        if "{id}" in file:
            file = file.replace("{id}", self.id)
        avatar(self, file)

    # @staticmethod
    # def load_avatar(file="/tmp/avatar.jpg"):
    #     # chars = alph.letters800
    #     langs = "afr+all+amh+ara+asm+aze+aze-cyrl+bel+ben+bod+bos+bre+bul+cat+ceb+ces+chi-sim+chi-sim-vert+chi-tra" \
    #             "+chi-tra-vert+chr+cos+cym+dan+deu+div+dzo+ell+eng+enm+epo+est+eus+fao+fas+fil+fin+fra+frk+frm+fry" \
    #             "+gla+gle+glg+guj+hat+heb+hin+hrv+hun+hye+iku+ind+isl+ita+ita-old+jav+jpn+jpn-vert+kan+kat+kat-old" \
    #             "+kaz+khm+kir+kor+kor-vert+kur-ara+lao+lat+lav+lit+ltz+mal+mar+mkd+mlt+mon+mri+msa+mya+nep+nld+nor" \
    #             "+oci+ori+osd+pan+pol+por+pus+que+ron+rus+san+script-arab+script-armn+script-beng+script-cans+script" \
    #             "-cher+script-cyrl+script-deva+script-ethi+script-frak+script-geor+script-grek+script-gujr+script" \
    #             "-guru+script-hang+script-hang-vert+script-hans+script-hans-vert+script-hant+script-hant-vert+script" \
    #             "-hebr+script-jpan+script-jpan-vert+script-khmr+script-knda+script-laoo+script-latn+script-mlym" \
    #             "+script-mymr+script-orya+script-sinh+script-syrc+script-taml+script-telu+script-thaa+script-thai" \
    #             "+script-tibt+script-viet+sin+slk+slv+snd+spa+spa-old+sqi+srp+srp-latn+sun+swa+swe+syr+tam+tat+tel" \
    #             "+tgk+tha+tir+ton+tur+uig+ukr+urd+uzb+uzb-cyrl+vie+yid+yor"
    #     # txt = image_to_string(Image.open(file), lang=langs, config=f"-c tessedit_char_whitelist={chars}")
    #     txt = image_to_string(Image.open(file), lang="por")
    #     return txt.replace("\n", "")

    def __mul__(self, other):
        """Flexible merge/unmerge with another UUID.

         Non commutative: a * b != b * a
         Invertible: (a * b) / b = a
                     a.inv * (a * b) = b
         Associative: (a * b) * c = a * (b * c)
         """
        return UUID(pmat_mult(self.m, other.m), ignore_call=self.ignore_call)

    def __truediv__(self, other):
        """Bounded unmerge from last merged UUID."""
        if self.m == self.first_matrix:
            raise Exception(f"Cannot divide by UUID={self}!")
        return UUID(pmat_mult(self.m, other.t.m), ignore_call=self.ignore_call)

    def __eq__(self, other):
        if not isinstance(other, UUID):
            return False
        return self.n == other.n if self._m is None else self.m == other.m

    def __hash__(self):
        return self.n

    def __str__(self):
        return self.id

    def __call__(self, uuid):
        return self if self.ignore_call else self * uuid

    # __repr__ = __str__  # TODO: is this needed?
