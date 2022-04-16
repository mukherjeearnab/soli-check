from tensorflow.keras.models import load_model
import numpy as np


from .prepare import prepare


def check(bytecode):
    opcode = prepare(bytecode)
    result = detection(opcode)
    if result == 0:
        return True
    else:
        return False


def detection(vector):
    model = load_model('./model/model_sm_rus_6.h5')

    model.summary()

    # print('PUSSY', np.isnan(vector).any())

    result = model.predict(np.array(vector))

    print(result)

    result = 1 if result[0][0] > 0.5 else 0

    return result
