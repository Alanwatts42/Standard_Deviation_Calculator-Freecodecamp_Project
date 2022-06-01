import numpy as np


def listify(a):
  r = a.tolist()
  return r

def calculate(list):
  size = len(list)
  if size != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    matrix = np.array(list).reshape(3,3)
    flat = np.array(list)

    m1 = np.mean(matrix, 0)
    mean1 = listify(m1)
    m2 = np.mean(matrix, 1)
    mean2 = listify(m2)
    m3 = np.mean(flat)
    mean3 = listify(m3)

    v1 = np.var(matrix, 0)
    var1 = listify(v1)
    v2 = np.var(matrix, 1)
    var2 = listify(v2)
    v3 = np.var(flat)
    var3 = listify(v3)

    s1 = np.std(matrix, 0)
    std1 = listify(s1)
    s2 = np.std(matrix, 1)
    std2 = listify(s2)
    s3 = np.std(flat)
    std3 = listify(s3)

    mx1 = np.max(matrix, 0)
    max1 = listify(mx1)
    mx2 = np.max(matrix, 1)
    max2 = listify(mx2)
    mx3 = np.max(flat)
    max3 = listify(mx3)

    mn1 = np.min(matrix, 0)
    min1 = listify(mn1)
    mn2 = np.min(matrix, 1)
    min2 = listify(mn2)
    mn3 = np.min(flat)
    min3 = listify(mn3)

    sm1 = np.sum(matrix, 0)
    sum1 = listify(sm1)
    sm2 = np.sum(matrix, 1)
    sum2 = listify(sm2)
    sm3 = np.sum(flat)
    sum3 = listify(sm3)

    calculations = {
      'mean': [mean1, mean2, mean3],
      'variance': [var1, var2, var3],
      'standard deviation': [std1, std2,   std3],
      'max': [max1, max2, max3],
      'min': [min1, min2, min3],
      'sum': [sum1, sum2, sum3]
      }
    return calculations