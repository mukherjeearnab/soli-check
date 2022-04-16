from tensorflow.keras.models import load_model
import numpy as np


from .prepare import prepare

model = load_model('./model/model_sm_rus_6.h5')

model.summary()


def check(bytecode):
    opcode = prepare(bytecode)
    report, result = detection(opcode)
    if report == 0:
        return True, result
    else:
        return False, result


def detection(vector):
    result = model.predict(np.array(vector))

    print(result)

    report = 1 if result[0][0] > 0.5 else 0

    return report, round(result[0][0] * 100, 2)
