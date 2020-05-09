from secretsharing import secret_int_to_points, points_to_secret_int
from secretsharing import SecretSharer
import binascii


myshares = [(1, 9608474170977308238036624146101441469538628637045706610338073590812843162969037926492967854559828114435865261425719619743472419864336210874222029453059741L),
            (2, 68500755079349789351078524541708453870296292990294021018027228505078681492284299873863659247273461856762128786874833326789786067325816477066780304059822843L),
            (3, 224183841656780872927678242626279871433733831057475254917387185998520511272846647279913467443558309288829498488402883425874249712684215384203475752039681175L),
            (4, 524164732834933988556388319839274528391312080836319720002737667326861328789556912063222725295339950383555529443266354316704089242529615243887408038702736241L),
            (5, 1015950427545472565825761297620151258974491880324557727968398393745824130327315926142371765654543965113857776728721730398986530543452098367721676829359089545L)]



# for item in myshares:
#     print(hex(item[1]).rstrip("L").lstrip("0x"))

# get the int Long secret from the shares
s = points_to_secret_int(myshares)
print("Secret INT: {}".format(s))
# convert to hex, but remove 0x and L (LONG) from it
myhex = hex(int(s)).replace("0x", "").replace("L","")
# print(myhex)
# convert to b64
mybase64 = binascii.b2a_base64(binascii.unhexlify(myhex)).replace("\n", "")
# print(mybase64)
# convert base64 to raw
myraw = binascii.a2b_base64(mybase64).decode()
print("Flag: {}".format(myraw))