import pytest
from project import add,sub,mul,div

def test_add():
    assert 1+2==3.0
    assert 10+3==13.0

def test_sub():
    assert 2-1==1.0
    assert 20-4==16.0

def test_mul():
    assert 4*5==20.0
    assert 6*2==12.0

def test_div():
    assert 10/2==5.0
    assert 20/5==4.0
    with pytest.raises(ZeroDivisionError):
         100/0



def main():
    test_add()
    test_sub()
    test_mul()
    test_div()


if __name__ ==  "__main__ ":
    main()