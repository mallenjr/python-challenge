def_alph = "abcdefghijklmnopqrstuvwxyz"
shift_alph = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(def_alph, shift_alph)

in_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr \
        ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(in_str.translate(trantab))

url_str = "map"

print(url_str.translate(trantab))