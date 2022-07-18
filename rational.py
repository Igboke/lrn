'''Attempt to replcate the rational numbers sequence
Created by Igboke Daniel C.'''
from math import *
class Rational(object):
	"""docstring for Rational"""
	def __init__(self, numer, denom):
		self._numer= numer
		self._denom= denom
		self.reduce=()

	def numer(self):
		return self._numer

	def denom(self):
		return self._denom

	def _gcd(self,a,b):
		#using the Greatest common divisor, following Euclid"s algo.
		(a,b)=(max(a,b),min(a,b))
		if b>0:
			(a,b)=(b,a%b)
		return a

	def _reduce(self):
		divisor=self._gcd(self._numer,self._denom)
		a= self._numer//divisor
		b= self._denom//divisor
		if self._numer%divisor==0 and self._denom%divisor==0:
			return str(a)+'/'+str(b)
		elif gcd(self._numer,self._denom)== min(self._numer,self._denom):
			return str(self._numer) + '/' + str(self._denom)
		else:
			common_denom=gcd(self._numer,self._denom)
			top=self._numer//common_denom
			bottom=self._denom//common_denom
			return Rational(top,bottom)

	def __add__(self,another):
		#the built iin mechanism for addition is x+y= x.__add__(y), so we have to overide this mechanism. self.__add(another)
		if self._denom == another._denom:
			m=self._numer + another._numer
			po=Rational(m,self._denom)
			return po._reduce()
		else:
			numer1=(self._numer*another._denom)+(another._numer*self._denom)
			denom1=self._denom*another._denom
			xo=Rational(numer1,denom1)
			return xo._reduce()

	def __sub__(self,another):
		#the built iin mechanism for subtraction is x-y= x.__sub__(y), so we have to overide this mechanism. self.__sub(another)
		if self._denom == another._denom and self._numer == another._numer:
			return 0
		elif self._denom == another._denom:
			m=self._numer - another._numer
			po=Rational(m,self._denom)
			return po._reduce()
		else:
			numer1=(self._numer*another._denom)-(another._numer*self._denom)
			denom1=self._denom*another._denom
			xo=Rational(numer1,denom1)
			return xo._reduce()

	def __mul__(self,another):
		#the built iin mechanism for multiplication is x*y= x.__mul__(y), so we have to overide this mechanism. self.__mul(another)
		numer1=self._numer*another._numer
		denom1=self._denom*another._denom
		po=Rational(numer1,denom1)
		return po._reduce()

	def __div__(self,another):
		#the built iin mechanism for division is x/y= x.__div__(y), so we have to overide this mechanism. self.__div(another)
		numer1=self._numer*another._denom
		denom1=self._denom*another._numer
		po=Rational(numer1,denom1)
		return po._reduce()

	def __gt__(self,another):
		#compares 2 rationals, returns True if self > another
		val1= self._numer * another._denom
		val2= self._denom * another._numer
		return val1>val2

	def __lt__(self,another):
		#compares 2 rationals, returns True if self < another
		val1= self._numer * another._denom
		val2= self._denom * another._numer
		return val1<val2

	def __eq__(self,another):
		if self is another:
			return True
		elif type(self) != type(another):
			return False
		else:
			#alt=self._numer==another._numer and self._denom==another._denom
			True

	def __str__(self):
		return str(self._numer) + '/' + str(self._denom)