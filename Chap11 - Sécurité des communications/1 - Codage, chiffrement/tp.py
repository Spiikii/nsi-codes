def code_ascii(texte):
    """ str -> [int]
    Renvoie la liste des codes ascii des caractères du texte """
    return [ord(c) for c in texte]

def decode_ascii(codes):
    """ [int] -> str
    Renvoie la chaîne de caractères correspondant aux codes ascii """
    return "".join([chr(c) for c in codes])

def genere_alphabet_majuscule():
    """ () -> [str]
    Renvoie la liste des 26 lettres de l'alphabet latin en majuscule """
    return [chr(c)
            for c in range(ord('A'), ord('Z') + 1)]
    # return  [chr(ord('A') + c) for c in range(26)]

def decale_car(car, cle):
    """ str, int -> str
    Si car est une majuscule,
    renvoie le caractère correspondant à car, décalé de cle """
    if not ord('A') <= ord(car) <= ord('Z'):
        return car
    res = ord(car) # un nombre entre 65 et 90
    res = res - ord('A') # un nombre entre 0 et 25
    res = (res + cle)%26 # un nombre entre 0 et 25
    res = res + ord('A')
    return chr(res)
    

def chiffre_cesar(clair, cle):
    """ str, int -> str
    Chiffre le clair avec le chiffrement de César (cle = décalage) """
    pass

def dechiffre_cesar(chiffre, cle):
    """ str, int -> str
    Renvoie le texte clair vérifiant chiffre = chiffre_cesar(clair, cle) """
    pass

# Texte de l'énigme
"""
OH 28 DYULO 1942, D ZDVKLQJWRQ G.F.

D TXL GH GURLW.
PD GHFRXYHUWH SRUWH VXU OD VWUXFWXUH GH OD PDFKLQH HQLJPD. HOOH SHUPHW GH IDLUH GHV VXFFHVVLRQV GH VXEVWLWXWLRQV HW GH SHUPXWDWLRQV. M'DL DXVVL O'LPSUHVVLRQ TXH OD VWUXFWXUH GHV PHVVDJHV HFKDQJHV HVW VRXYHQW OD PHPH, FH TXH QRXV DOORQV WHQWHU G'HASORLWHU.

HOLCDEHWK VPLWK IULHGPDQ.
SRVW-VFULSWXP : SRUWHC FH YLHXA ZLVNB DX MXJH EORQG TXL IXPH. 
"""

# Texte déchiffré


def chiffre_vigenere(clair, cle):
    """ str, [int] -> str
    Chiffrement de Vigenère """
    pass

