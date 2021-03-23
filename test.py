#coding:utf8
import numpy as np


datas = np.load('tang.npz', allow_pickle=True)
data = datas['data']
ix2word = datas['ix2word'].item()

poem = data[0]
poem_txt = [ix2word[ii] for ii in poem]

print(''.join(poem_txt))