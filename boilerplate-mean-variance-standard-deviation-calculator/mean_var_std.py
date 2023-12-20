import numpy as np


def calculate(list):
  if (len(list) != 9):
    raise ValueError("List must contain nine numbers.")

  npArrFlat = np.array(list)
  npArr = np.split(npArrFlat, 3)

  dat = {
    'mean': [
      np.mean(npArr, axis=0).tolist(),
      np.mean(npArr, axis=1).tolist(),
      np.mean(npArrFlat).tolist()
    ],
    'variance': [
      np.var(npArr, axis=0).tolist(),
      np.var(npArr, axis=1).tolist(),
      np.var(npArrFlat).tolist()
    ],
    'standard deviation': [
      np.std(npArr, axis=0).tolist(),
      np.std(npArr, axis=1).tolist(),
      np.std(npArrFlat).tolist()
    ],
    'max': [
      np.max(npArr, axis=0).tolist(),
      np.max(npArr, axis=1).tolist(),
      np.max(npArrFlat).tolist()
    ],
    'min': [
      np.min(npArr, axis=0).tolist(),
      np.min(npArr, axis=1).tolist(),
      np.min(npArrFlat).tolist()
    ],
    'sum': [
      np.sum(npArr, axis=0).tolist(),
      np.sum(npArr, axis=1).tolist(),
      np.sum(npArrFlat).tolist()
    ]
  }

  return dat
