from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

OPCODE_SIZE = 150
OPCODE_SEQ_LEN = 1800
TRUNC_TYPE = 'post'
PADDING_TYPE = 'post'
OOV_TOKEN = '<OOV>'


def re_hex_val(opcode):
    opcode = str(opcode)
    opcode = opcode.replace('|', '')
    regex = '(0x|0X)[a-fA-F0-9]+ '
    import re
    opcode = re.sub(regex, '', opcode)
    opcode = opcode.strip()
    return opcode


def tokenizer(opcode):
    tokenized_opcodes = tokenizer.texts_to_sequences([opcode])
    padded_opcodes = pad_sequences(
        tokenized_opcodes, maxlen=OPCODE_SEQ_LEN, padding=PADDING_TYPE, truncating=TRUNC_TYPE)

    return np.array(padded_opcodes)
