import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num=1/0
        
    assert 'divide by zero' in str(e.value)


#import pytest

#def test_divide_by_zero():
#  with pytest.raises(ZeroDivisionError) as e:
#    num = 1 / 0

#  assert 'division by zero' in str(e.value) 
