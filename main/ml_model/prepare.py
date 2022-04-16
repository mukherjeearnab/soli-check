from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

OPCODE_SIZE = 150
OPCODE_SEQ_LEN = 1800
TRUNC_TYPE = 'post'
PADDING_TYPE = 'post'
OOV_TOKEN = '<OOV>'

with open('./model/tokenizer.pickle', 'rb') as fh:
    tokenizer = pickle.load(fh)


def re_hex_val(opcode):
    opcode = str(opcode)
    opcode = opcode.replace('|', '')
    regex = '(0x|0X)[a-fA-F0-9]+ '
    import re
    opcode = re.sub(regex, '', opcode)
    opcode = opcode.strip()
    return opcode


def tokenize(opcode):
    tokenized_opcodes = tokenizer.texts_to_sequences([opcode])
    padded_opcodes = pad_sequences(
        tokenized_opcodes, maxlen=OPCODE_SEQ_LEN, padding=PADDING_TYPE, truncating=TRUNC_TYPE)

    return np.array(padded_opcodes)


def prepare(opcode):
    # Remove Operands
    opcode = re_hex_val(opcode)

    # Tokenize the Opcode Sequence
    opcode = tokenize(opcode)

    print(opcode)

    return opcode
