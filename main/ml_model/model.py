from tensorflow.keras.models import load_model
import numpy as np


from .prepare import prepare


def check(bytecode):
    opcode = prepare(bytecode)
    detection(opcode)
    if bytecode == 'hello':
        return True
    else:
        return False


def detection(vector):
    model = load_model('./model/model_sm_rus_128.h5')

    # print('PUSSY', np.isnan(vector).any())

    result = model.predict(np.array(vector))

    print('RES', result)
