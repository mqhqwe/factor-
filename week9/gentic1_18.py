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
		self.needFields = [t.AMOUNT,t.VOLUME,t.INCRCASHLYR,t.SHR,t.PDD]# 设置需要的字段
	def factor_definition(self):
		s = time.time()
		needData = self.needData  # 计算所需数据
		factor=regbeta10(regbeta5(min7(needData[t.AMOUNT]), mean10(regalpha30(needData[t.VOLUME], needData[t.INCRCASHLYR]))), reverse(diff6(minus(needData[t.SHR], needData[t.PDD]))))
		print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
		return factor
	def run_factor(self):
		self.run()
fct = Factor()
fct.run_factor()