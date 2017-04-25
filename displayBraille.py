# -*- coding: utf-8 -*-
# mapping of chair to braille dots

braille = dict()
braille[1] = 1
braille[2] = 2
braille[3] = 3
braille[4] = 4
braille[5] = 5
braille[6] = 6

vibration = dict()
vibration["letter"] = 1
vibration["capital"] = 2
vibration["number"] = 3
vibration["special"] = 1

# cells representation of characters
cells = dict()
# a - z
cells["a"] = [braille[1]]
cells["b"] = [braille[1], braille[2]]
cells["c"] = [braille[1], braille[4]]
cells["d"] = [braille[1], braille[4], braille[5]]
cells["e"] = [braille[1], braille[5]]
cells["f"] = [braille[1], braille[2], braille[4]]
cells["g"] = [braille[1], braille[2], braille[4], braille[5]]
cells["h"] = [braille[1], braille[2], braille[5]]
cells["i"] = [braille[2], braille[4]]
cells["j"] = [braille[2], braille[4], braille[5]]
cells["k"] = [braille[1], braille[3]]
cells["l"] = [braille[1], braille[2], braille[3]]
cells["m"] = [braille[1], braille[3], braille[4]]
cells["n"] = [braille[1], braille[3], braille[4], braille[5]]
cells["o"] = [braille[1], braille[3], braille[5]]
cells["p"] = [braille[1], braille[2], braille[3], braille[4]]
cells["q"] = [braille[1], braille[2], braille[3], braille[4], braille[5]]
cells["r"] = [braille[1], braille[2], braille[3], braille[5]]
cells["s"] = [braille[2], braille[3], braille[4]]
cells["t"] = [braille[2], braille[3], braille[4], braille[5]]
cells["u"] = [braille[1], braille[3], braille[6]]
cells["v"] = [braille[1], braille[2], braille[3], braille[6]]
cells["w"] = [braille[2], braille[4], braille[5], braille[6]]
cells["x"] = [braille[1], braille[3], braille[4], braille[6]]
cells["y"] = [braille[1], braille[3], braille[4], braille[5], braille[6]]
cells["z"] = [braille[1], braille[3], braille[5], braille[6]]

# A - Z
cells["A"] = [braille[1]]
cells["B"] = [braille[1], braille[2]]
cells["C"] = [braille[1], braille[4]]
cells["D"] = [braille[1], braille[4], braille[5]]
cells["E"] = [braille[1], braille[5]]
cells["F"] = [braille[1], braille[2], braille[4]]
cells["G"] = [braille[1], braille[2], braille[4], braille[5]]
cells["H"] = [braille[1], braille[2], braille[5]]
cells["I"] = [braille[2], braille[4]]
cells["J"] = [braille[2], braille[4], braille[5]]
cells["K"] = [braille[1], braille[3]]
cells["L"] = [braille[1], braille[2], braille[3]]
cells["M"] = [braille[1], braille[3], braille[4]]
cells["N"] = [braille[1], braille[3], braille[4], braille[5]]
cells["O"] = [braille[1], braille[3], braille[5]]
cells["P"] = [braille[1], braille[2], braille[3], braille[4]]
cells["Q"] = [braille[1], braille[2], braille[3], braille[4], braille[5]]
cells["R"] = [braille[1], braille[2], braille[3], braille[5]]
cells["S"] = [braille[2], braille[3], braille[4]]
cells["T"] = [braille[2], braille[3], braille[4], braille[5]]
cells["U"] = [braille[1], braille[3], braille[6]]
cells["V"] = [braille[1], braille[2], braille[3], braille[6]]
cells["W"] = [braille[2], braille[4], braille[5], braille[6]]
cells["X"] = [braille[1], braille[3], braille[4], braille[6]]
cells["Y"] = [braille[1], braille[3], braille[4], braille[5], braille[6]]
cells["Z"] = [braille[1], braille[3], braille[5], braille[6]]

# 0 - 9
cells["no"] = [braille[3], braille[4], braille[5], braille[6]]
cells["1"] = [braille[1]]
cells["2"] = [braille[1], braille[2]]
cells["3"] = [braille[1], braille[4]]
cells["4"] = [braille[1], braille[4], braille[5]]
cells["5"] = [braille[1], braille[5]]
cells["6"] = [braille[1], braille[2], braille[4]]
cells["7"] = [braille[1], braille[2], braille[4], braille[5]]
cells["8"] = [braille[1], braille[2], braille[5]]
cells["9"] = [braille[2], braille[4]]
cells["0"] = [braille[2], braille[4], braille[5]]

# punctuations
cells[" "] = []
cells[","] = [braille[2]]
cells[";"] = [braille[2], braille[3]]
cells[":"] = [braille[2], braille[5]]
cells["."] = [braille[2], braille[5], braille[6]]
cells["."] = [braille[2], braille[5], braille[6]]
cells["?"] = [braille[2], braille[3], braille[6]]
cells["!"] = [braille[2], braille[3], braille[5]]
cells["\""] = [braille[2], braille[3], braille[5], braille[6]]
cells["("] = [braille[2], braille[3], braille[5], braille[6]]
cells[")"] = [braille[2], braille[3], braille[5], braille[6]]
cells["["] = [braille[2], braille[3], braille[5], braille[6]]
cells["]"] = [braille[2], braille[3], braille[5], braille[6]]
cells["‘"] = [braille[3]]
cells["’"] = [braille[3]]
cells["'"] = [braille[3]]
cells["“"] = [braille[2], braille[3], braille[6]]
cells["”"] = [braille[3], braille[5], braille[6]]
cells["/"] = [braille[3], braille[4]]
#cells["\\"] = 456 16
cells["–"] = [braille[3], braille[6]]
cells["–"] = [braille[3], braille[6]]
cells["—"] = [braille[3], braille[6]]
cells["-"] = [braille[3], braille[6]]
cells["@"] = [braille[3], braille[4], braille[5]]
cells["*"] = [braille[3], braille[5]]
cells["#"] = [braille[3], braille[4], braille[5], braille[6]]

#Frequency Vibration of characters
freq = dict()
# a - z
freq["a"] = vibration["letter"]
freq["b"] = vibration["letter"]
freq["c"] = vibration["letter"]
freq["d"] = vibration["letter"]
freq["e"] = vibration["letter"]
freq["f"] = vibration["letter"]
freq["g"] = vibration["letter"]
freq["h"] = vibration["letter"]
freq["i"] = vibration["letter"]
freq["j"] = vibration["letter"]
freq["k"] = vibration["letter"]
freq["l"] = vibration["letter"]
freq["m"] = vibration["letter"]
freq["n"] = vibration["letter"]
freq["o"] = vibration["letter"]
freq["p"] = vibration["letter"]
freq["q"] = vibration["letter"]
freq["r"] = vibration["letter"]
freq["s"] = vibration["letter"]
freq["t"] = vibration["letter"]
freq["u"] = vibration["letter"]
freq["v"] = vibration["letter"]
freq["w"] = vibration["letter"]
freq["x"] = vibration["letter"]
freq["y"] = vibration["letter"]
freq["z"] = vibration["letter"]

# A - Z
freq["A"] = vibration["capital"]
freq["B"] = vibration["capital"]
freq["C"] = vibration["capital"]
freq["D"] = vibration["capital"]
freq["E"] = vibration["capital"]
freq["F"] = vibration["capital"]
freq["G"] = vibration["capital"]
freq["H"] = vibration["capital"]
freq["I"] = vibration["capital"]
freq["J"] = vibration["capital"]
freq["K"] = vibration["capital"]
freq["L"] = vibration["capital"]
freq["M"] = vibration["capital"]
freq["N"] = vibration["capital"]
freq["O"] = vibration["capital"]
freq["P"] = vibration["capital"]
freq["Q"] = vibration["capital"]
freq["R"] = vibration["capital"]
freq["S"] = vibration["capital"]
freq["T"] = vibration["capital"]
freq["U"] = vibration["capital"]
freq["V"] = vibration["capital"]
freq["W"] = vibration["capital"]
freq["X"] = vibration["capital"]
freq["Y"] = vibration["capital"]
freq["Z"] = vibration["capital"]

# 0 - 9
freq["1"] = vibration["number"]
freq["2"] = vibration["number"]
freq["3"] = vibration["number"]
freq["4"] = vibration["number"]
freq["5"] = vibration["number"]
freq["6"] = vibration["number"]
freq["7"] = vibration["number"]
freq["8"] = vibration["number"]
freq["9"] = vibration["number"]
freq["0"] = vibration["number"]

# punctuations
freq[" "] = vibration["letter"]
freq[","] = vibration["special"]
freq[";"] = vibration["special"]
freq[":"] = vibration["special"]
freq["."] = vibration["special"]
freq["?"] = vibration["special"]
freq["!"] = vibration["special"]
freq["\""] =vibration["special"]
freq["“"] = vibration["special"]
freq["”"] = vibration["special"]
freq["‘"] = vibration["special"]
freq["’"] = vibration["special"]
freq["'"] = vibration["special"]
freq["("] = vibration["special"]
freq[")"] = vibration["special"]
freq["/"] = vibration["special"]
#freq["\\"] = 456 16vibration["special"]
freq["–"] = vibration["special"]
freq["–"] = vibration["special"]
freq["—"] = vibration["special"]
freq["-"] = vibration["special"]
freq["@"] = vibration["special"]
freq["*"] = vibration["special"]
freq["#"] = vibration["special"]
freq["["] = vibration["special"]
freq["]"] = vibration["special"]

"""
~
#
$
%
^
&
*
_
+
,
;
:
.
?
'
‘
’
\
/
"
“
”
(
)
[
]
{
}
-
!
@
*
"""

# cells to chars conversion
cellsToChars = dict()
cellsToChars[0] = ' '
cellsToChars[91] = '1'
cellsToChars[1] = 'a'
cellsToChars[912] = '2'
cellsToChars[12] = 'b'
cellsToChars[123] = 'l'
cellsToChars[1234] = 'p'
cellsToChars[12345] = 'q'
cellsToChars[1235] = 'r'
cellsToChars[1236] = 'v'
cellsToChars[9124] = '6'
cellsToChars[124] = 'f'
cellsToChars[91245] = '7'
cellsToChars[1245] = 'g'
cellsToChars[9125] = '8'
cellsToChars[125] = 'h'
cellsToChars[13] = 'k'
cellsToChars[134] = 'm'
cellsToChars[1345] = 'n'
cellsToChars[13456] = 'y'
cellsToChars[1346] = 'x'
cellsToChars[135] = 'o'
cellsToChars[1356] = 'z'
cellsToChars[136] = 'u'
cellsToChars[914] = '3'
cellsToChars[14] = 'c'
cellsToChars[9145] = '4'
cellsToChars[145] = 'd'
cellsToChars[915] = '5'
cellsToChars[15] = 'e'
cellsToChars[2] = ','
cellsToChars[23] = ';'
cellsToChars[234] = 's'
cellsToChars[2345] = 't'
cellsToChars[235] = '!'
cellsToChars[2356] = '"'
cellsToChars[2356] = '('
cellsToChars[2356] = ')'
cellsToChars[2356] = '['
cellsToChars[2356] = ']'
cellsToChars[236] = '?'
cellsToChars[236] = '“'
cellsToChars[924] = '9'
cellsToChars[24] = 'i'
cellsToChars[9245] = '0'
cellsToChars[245] = 'j'
cellsToChars[2456] = 'w'
cellsToChars[25] = ':'
cellsToChars[256] = '.'
cellsToChars[3] = '\''
cellsToChars[34] = '/'
cellsToChars[345] = '@'
cellsToChars[3456] = '#'
cellsToChars[35] = '*'
cellsToChars[356] = '”'
cellsToChars[36] = '-'