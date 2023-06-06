#0-1->0
p_0_1_0_10h = {
    "hold":[
    0b1111110,#0
    0b10110000,#1  10hは特別
    ],
    "inc":[
    0b10110000,#1
    0b1111110#0   10hは特別
    ]
}
#0-2->0
p_0_2_0_10h = {
    "hold" : [
    0b1111110,#0
    0b0110000,#1
    0b11101101,#2  10hは特別
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b11111110#0
    ]
}
#0-3->0
p_0_3_0_10h = {
    "hold" : [
    0b1111110,#0
    0b0110000,#1
    0b11101101,#2  10hは特別
    ],
    "inc" : [
    0b0110000,#1
    0b11101101,#2
    0b1111110#0
    ]
}

p_0_9_0 = {
    "hold" : [
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
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b0110011,#4
    0b1011011,#5
    0b1011111,#6
    0b1110010,#7
    0b1111111,#8
    0b1111011,#9
    0b11111110#0
    ]
}
p_0_2_1 = {
    "hold" : [
    0b1111110,#0
    0b0110000,#1
    0b1101101,#2
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b10110000,#1
    ]
}

p_0_3_0 = {
    "hold" : [
    0b1111110,#0
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b11111110#0
    ]
}

p_0_0_6 = {
    "hold" : [
    0b1111110,#0
    ],
    "inc" : [
    0b11011111,#6
    ]
}

p_0_5_0 = {
    "hold" : [
    0b1111110,#0
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b0110011,#4
    0b1011011,#5
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b0110011,#4
    0b1011011,#5
    0b11111110#0
    ]
}

p_0_9_6 = {
    "hold" : [
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
    ],
    "inc" : [
    0b0110000,#1
    0b1101101,#2
    0b1111001,#3
    0b0110011,#4
    0b1011011,#5
    0b1011111,#6
    0b1110010,#7
    0b1111111,#8
    0b1111011,#9
    0b11011111,#6
    ]
}