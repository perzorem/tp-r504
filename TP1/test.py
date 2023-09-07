import pytest
import fonctions as f

def test_1():
	assert f.puissance(2,3) == 8
	assert f.puissance(2,2) == 4

def test_2():
	assert f.puissance(-2,3) == -8
	assert f.puissance(-2,2) == 4

def test_3():
	assert f.puissance(0,-3) == vous ne pouvez pas avoir une puissance négative
	assert f.puissance(0,3) == 0
	assert f.puissance(0,0) == 1
	assert f.puissance(-2,0) == -1
	assert f.puissance(2,0) == 1
