
from utils import utils as u

def test_utils_private_correctInput():
    """
    Tests the private function for ensuring correct input
    """
    #test ints
    output = u._correctInput(123)
    assert output == 123
    
    #test floats
    output = u._correctInput(123.9)
    assert output == 123
    
    #test strings
    output = u._correctInput("123")
    assert output == 123
    
    output = u._correctInput("123.9")
    assert output == 123
    
    #test other
    try:
        u.formatter([])
    except:
        pass #error expected
    else:
        raise Exception("Didnt throw error on incorrect input")

def test_utils_reversed():
    """
    Test the reversed
    """
    assert u.reversed(12345) == 54321
    

def test_utils_formatter():
    """
    Test formatter
    """
    binary, octal = u.formatter(12345)
    assert binary == "0b11000000111001"
    assert octal == "0o30071"
    

if __name__ == "__main__":
    """
    Test the utils methods
    """
    test_utils_private_correctInput()
    
    test_utils_reversed()
    
    test_utils_formatter()
    
    #success
    print("passed all tests")
