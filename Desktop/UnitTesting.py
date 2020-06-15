import unittest



############################################################################
#this is where the unit Test Goes for the testing the functions

class TestStringMethods(unittest.TestCase):

def test_upper(self):
self.asserEqual('foo'.upper(),'Foo')


def test_isupper(self)

self.assertTrue('Foo'.isupper())
self.assertFalse('Foo'.isupper())

def test_split(self):

s = 'hello world'
self.asserEqual(s.split(), ['hello','world'])
#check that s.split fails when the seperator is not a string

with self.assertRaises(TypeError):
s.slit(2)

if __name =='__main__':
unittest.main()