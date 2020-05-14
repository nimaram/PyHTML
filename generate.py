# created by nima aram.
from utils.tags import *
from utils.run import *
@headTag
@styleTag
def head():
	return '''div{color:red}'''
@h1Tag
def header():
	return 'hello'
@h2Tag	
def aside():
	return 'this is a aside'
@divTag
def footer():
	return 'this is a my footer'
@divTag
def end():
	return '''<h2>i come with pyhtml</h2>
	<h3> we in a div!</h3>
	'''
@freeTag
def comment():
	return '''
	<!--check my github for new fuetres!-->
	<!--fork me please!-->'''
html_array += [
	head(),
	header(),
	aside(),
	footer(),
	end(),
	comment(),
]
mycode = runHTML()
print(mycode)
buildHTML()
