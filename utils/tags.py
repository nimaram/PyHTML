# html tags as decorators
'''
author : nima aram
'''
def h1Tag(func):
	def wrapper():
		func()
		outpot_htag = f'<h1>{func()}</h1>'
		return outpot_htag 
	return wrapper
def h2Tag(func):
	def wrapper():
		func()
		outpot_h2tag = f'<h2>{func()}</h2>'
		return outpot_h2tag 
	return wrapper
def h3Tag(func):
	def wrapper():
		func()
		outpot_h3tag = f'<h3>{func()}</h3>'
		return outpot_h3tag 
	return wrapper
def h4Tag(func):
	def wrapper():
		func()
		outpot_h4tag = f'<h4>{func()}</h4>'
		return outpot_h4tag 
	return wrapper
def h5Tag(func):
	def wrapper():
		func()
		outpot_h5tag = f'<h5>{func()}</h5>'
		return outpot_h5tag 
	return wrapper
def divTag(func):
	def wrapper():
		func()
		outpot_divtag = f'<div>{func()}</div>'
		return outpot_divtag
	return wrapper
def headTag(func):
	def wrapper():
		func()
		outpot_headtag = f'<head>{func()}</head>'
		return outpot_headtag
	return wrapper
def styleTag(func):
	def wrapper():
		func()
		outpot_styletag = f'<style>{func()}</style>'
		return outpot_styletag
	return wrapper
def freeTag(func):
	def wrapper():
		func()
		outpot_freetag = f'{func()}'
		return outpot_freetag
	return wrapper