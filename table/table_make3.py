import pprint
import pattern

seg_pat = [
    0b1111110,#0
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b0110011,#4
    0b1011011,#5
    0b1011111,#6
    0b1110010,#7
    0b1111111,#8
    0b1111011#9
]

def pat_to_num(cn):
    for num in range(len(seg_pat)):
        if cn == seg_pat[num]:
            return num
        if cn == (seg_pat[num] | 0b10000000):
            return num
    return 0

def seg_pat_test(normal,inc):
    for cn in range(127):
        num = pat_to_num(cn)
        print(format(cn, '03d'),format(normal[num],'07b'),"(",pat_to_num(normal[num]),")"," => ",format(inc[num],'07b'),"(",pat_to_num(inc[num]),")")


def seg_pat_make(pat):
    bin = list()
    for cn in range(128):
        num = pat_to_num(cn)
        if num < len(pat):
            print(format(cn, '03d'),"(",pat_to_num(cn),")"," => ",format(pat[num],'07b'),"(",pat_to_num(pat[num]),")")
            bin.append(pat[num].to_bytes(1,"little"))
        else:
            print(format(cn, '03d'),"(",pat_to_num(cn),")"," => ",format(pat[0],'07b'),"(",pat_to_num(pat[0]),")")
            bin.append(pat[0].to_bytes(1,"little"))
    return bin

bin = list()

#メモリマップ
# 12h -> *00*
# 24h -> *01*
# 30h -> *10*
#+-------------------+ 12時間制1h
#|0-9 -> 9           | 0000
#|0-2 -> 1           | 0001
#+-------------------+ 24時間制1h
#|0-9 -> 9           | 0010
#|0-3 -> 0           | 0011
#+-------------------+ 30時間制1h
#|0-9 -> 9           | 0100
#|0-0 -> 6           | 0101
#+-------------------+ 分，秒
#|0-9 -> 9           | 0110
#|0-5 -> 0           | 0111
#+-------------------+ 12時間制10h
#|0-1 -> 0           | 1000
#+-------------------+ 24時間制10h
#|0-2 -> 0           | 1001
#+-------------------+ 30時間制10h
#|0-3 -> 0           | 1010
#+-------------------+

########## 12時間制 (分1min兼用)
print("12h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_9_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_9_0["inc"])

print("12h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_2_1["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_2_1["inc"])

########## 24時間制
print("24h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_9_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_9_0["inc"])

print("24h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_3_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_3_0["inc"])

########## 30時間制
print("30h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_9_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_9_0["inc"])

print("30h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_9_6["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_9_6["inc"])

########## 分，秒
print("min,sec")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_9_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_9_0["inc"])

print("24h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_5_0["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_5_0["inc"])

##################

print("12h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_1_0_10h["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_1_0_10h["inc"])

print("24h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_2_0_10h["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_2_0_10h["inc"])

print("30h")
for dmy in range(3):
    bin += seg_pat_make(pattern.p_0_2_0_10h["hold"])
for dmy in range(5):
    bin += seg_pat_make(pattern.p_0_2_0_10h["inc"])

print("================================")
print("binary size =>", len(bin),"Byte")
print("================================")


with open("./seg_table4.bin",mode='wb') as f:
    f.writelines(bin)



########################
########################