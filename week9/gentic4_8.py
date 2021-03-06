#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# author: mqh
import time
import numpy as np
import pandas as pd
import math
from FactorModule.mqhBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t
from CalculatorModule.OperatorPool import *
class Factor(FactorBase):
	def __init__(self):
		super(Factor, self).__init__()
		self.neutral = False
		self.factorName = __name__.split('.')[-1]
		self.needFields = list(set([t.HIGH,t.AMOUNT,t.HIGH,t.AMOUNT,t.CLOSE,t.HIGH,t.AMOUNT,t.CLOSE,t.LOW,t.AMOUNT,t.HIGH,t.VOLUME,t.OPEN,t.AMOUNT,t.HIGH,t.VOLUME,t.OPEN,t.LOW]))# 设置需要的字段
	def factor_definition(self):
		s = time.time()
		needData = self.needData  # 计算所需数据
		factor=minus(rank(decaylinear7(add(decaylinear10(corr30(regalpha60(tsmax5(needData[t.HIGH]), mean5(needData[t.AMOUNT])), decaylinear10(corr30(regalpha60(tsmax5(needData[t.HIGH]), mean5(needData[t.AMOUNT])), diff10(regbeta10(needData[t.CLOSE], add(decaylinear10(corr30(regalpha60(tsmax5(needData[t.HIGH]), mean5(needData[t.AMOUNT])), diff10(regbeta10(needData[t.CLOSE], needData[t.LOW])))), corr60(mean60(corr60(needData[t.AMOUNT], needData[t.HIGH])), log10(corr10(needData[t.VOLUME], needData[t.OPEN])))))))))), corr60(mean60(corr60(needData[t.AMOUNT], needData[t.HIGH])), log10(corr10(needData[t.VOLUME], needData[t.OPEN])))))), delay8(needData[t.LOW]))
		print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
		return factor
	def run_factor(self):
		self.run()
fct = Factor()
fct.run_factor()