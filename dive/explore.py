import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_type, is_string_type

# define date VS index VS category VS continuum

# for dates : min date, max date, mode, % NaN, same distribution among diff. years ?
# for index : perfect index ?
# for category : extract of unique values, min, max, mode, % NaN
# for continuum : min, max, mean, std, % NaN

MAX_CLASSIF_TARGET_VALUES = 100
MAX_UNIQUE_RATIO_CATEGORY = 0.4
MIN_UNIQUE_RATIO_CONTINUOUS = 0.8

def is_float_compatible(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def has_only_uniques(data):
	if data.nunique() == len(data):
		return True
	return False

def is_int(data):
	return data.dtype in ['uint8', 'int32', 'int64']

def is_float(data):
	return data.dtype in ['float32', 'float64']

def is_int_castable(data):
	return np.array_equal(data, data.astype(int))

# check if (str) series can be casted to float
def is_float_castable(data):
	return all(data.apply(lambda val: is_float_compatible(val)))

def is_numerical(data):
	if is_int(data) or is_float(data):
		return True
	elif is_string_type(data) and is_float_castable(data):
		return True
	return False

def is_category(data):
	unique_ratio = float(data.nunique()) / len(data)
	if is_string_type(data) and not is_numerical(data):
		return True
	elif unique_ratio < MAX_UNIQUE_RATIO_CATEGORY
		return True
	return False 

def is_continuous(data):
	unique_ratio = float(data.nunique()) / len(data)
	if is_numeric_type(data) and unique_ratio > MIN_UNIQUE_RATIO_CONTINUOUS:
		return True
	return False

def is_date(data):
	return

def is_potential_classif_target(data):
	if is_float(data) and not is_int_castable(data):
		return False
	elif not is_category(data):
		return False
	elif data.nunique() > MAX_CLASSIF_TARGET_VALUES:
		return False
	return True

def eval_type(data):
	if has_only_uniques(data):
		if is_category(data):
			return 'index'
		else:
			return 'continuous'
	else:
		if is_category(data):
			if is_date(data):
				return 'date'
			else:
				return 'categorical'
		return 'continuous'
