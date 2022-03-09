text = 'X-DSPAM-Confidence:    0.8475'

pos = text.find(':')
print(pos)
piece = text[pos+2:]
print(piece)
value = float(piece)
print(value)
