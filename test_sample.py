def f(a):
    return a+1

def g(a):
    return a-1

def test_f():
    assert f(2)==3
    assert f(3)==4

def test_g():
    assert g(2)==1.0
    assert g(3)==3
