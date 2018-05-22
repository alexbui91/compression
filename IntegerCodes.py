"""
This module supplies functions that implement various
codes for integers, some of them self-delimiting.
 (a) regular binary   - encode: dec_to_bin(n,d) ;    decode: bin_to_dec(cl,d,0)
 (b) headless binary  - encode: dec_to_headless(n) ; decode: bin_to_dec(cl,d,1)
 (c) C_alpha(n)       - encode: encoded_alpha(n)   ; decode: get_alpha_integer(cl)
 (d) Fibonacci code (Figital) - encode: to_fiboanacci(n); decoder: from_fibonacci(string) or from_fibonacci2(clist)
 (e) byte code (bases 3, 7, 15, 31,...)
   (This code is allowed to encode integers from 0 upwards, unlike the others, which take n>=1 only)
   
C_alpha(n) is a self-delimiting code for integers.
Neither regular binary nor headless binary is a self-delimiting code,
hence their decoders must be supplied with a parameter d that tells
how many bits to read.

See
   Information Theory, Inference, and Learning Algorithms. (Ch 7: Codes for Integers)
   http://www.inference.phy.cam.ac.uk/mackay/itila/

This package uses the doctest module to test that it is functioning correctly.
IntegerCodes.py is free software (c) David MacKay December 2005. License: GPL
"""
## For license statement see  http://www.gnu.org/copyleft/gpl.html

import sys


def dec_to_bin(n, digits):
    """ n is the number to convert to binary;  digits is the number of bits you want
    Always prints full number of digits
    >>> print dec_to_bin( 17 , 9)
    000010001
    >>> print dec_to_bin( 17 , 5)
    10001
    
    Will behead the standard binary number if requested
    >>> print dec_to_bin( 17 , 4)
    0001
    """
    if(n<0) :
        sys.stderr.write( "warning, negative n not expected\n")
        pass
    i = digits-1
    ans = ""
    while i >= 0 :
        b = (((1<<i)&n)>0) 
        i -= 1
        ans = ans + str(int(b))
    return ans


def ceillog( n ) : ## ceil( log_2 ( n ))   [Used by LZ.py]
    """
    >>> print ceillog(3), ceillog(4), ceillog(5)
    2 2 3
    """
    assert n>=1
    c = 0
    while 2**c<n :
        c += 1
    return c


def to_byte( n, bytesize):
    """
    Self-delimiting code using end of file character.
    Encode integer n>=0 into base B=2**bytesize - 1. Use the all-1 symbol as end-of-file symbol.
    Is this called "Rice Coding"?
    >>> print to_byte( 10, 2 ) ## 10 = 9 + 0 + 1 --> 01 00 01 11
    01000111
    >>> print to_byte( 10, 3 ) ## 10 = 7 + 3     --> 001 011 111
    001011111
    """
    assert(bytesize>1) ## this coder does base 3, 7, 15,...
    assert (n>=0)
    B = (1<<bytesize) - 1
    answer=""
    while n>0 :
        rem = n % B
        answer=dec_to_bin(rem,bytesize)+answer
#        print n,B,rem,answer
        n = n/B
        pass
    answer=answer+"1"*bytesize
    return answer


def from_byte( clist, bytesize):
    """
    Takes a list of binary digits. Returns an integer, and destroys the elements of the
    list that it has read.
    >>> print from_byte( list("01000111"), 2 ) ## 10 = 9 + 0 + 1 --> 01 00 01 11
    10
    >>> print from_byte( list("001011111"), 3 ) ## 10 = 7 + 3     --> 001 011 111
    10
    """
    assert (len(clist)>=0)
    B = (1<<bytesize) - 1
    n=0
    while 1:
        d = bin_to_dec(clist,bytesize)
        if (d == B):
            return n
        else:
            n = n*B + d
            pass
        pass
    pass


def dec_to_headless( n ): 
    """Return the headless binary representation of n, an integer >= 1
    
    >>> [(n,dec_to_headless(n)) for n in range(1,8)]
    [(1, ''), (2, '0'), (3, '1'), (4, '00'), (5, '01'), (6, '10'), (7, '11')]
    >>> dec_to_headless(42)
    '01010'
    """
    assert(n>=1)
    ans=""
    while n>1 :
        b = ((1&n)>0) 
        ans =  str(int(b)) + ans
        n >>= 1
        pass
    return ans
    pass


def bin_to_dec( clist , c , tot=0 ):
    """Implements ordinary binary to integer conversion if tot=0
    and HEADLESS binary to integer if tot=1
    clist is a list of bits; read c of them and turn into an integer.
    The bits that are read from the list are popped from it, i.e., deleted

    Regular binary to decimal 1001 is 9...
    >>> bin_to_dec(  ['1', '0', '0', '1']  ,  4  , 0 )
    9

    Headless binary to decimal [1] 1001 is 25...
    >>> bin_to_dec(  ['1', '0', '0', '1']  ,  4  , 1 )
    25
    """
    while (c>0) :
        assert ( len(clist) > 0 ) ## else we have been fed insufficient bits.
        tot = tot*2 + int(clist.pop(0))
        c-=1
        pass
    return tot


def get_unary(n):
    tmp = ""
    for x in xrange(n):
        tmp += "1"
    tmp += "0"
    return tmp