def gcd(a:int,b:int) -> int:
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

assert gcd(3,5) == 1
assert gcd(2,10) == 2
assert gcd(6,15) == 3
