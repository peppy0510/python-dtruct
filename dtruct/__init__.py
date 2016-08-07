# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


try:
	from .dtruct import dtruct
	from .dtruct import compress_dict
	from .dtruct import decompress_dict
except:
	from dtruct import dtruct
	from dtruct import compress_dict
	from dtruct import decompress_dict
