# ChineseRemainderTheorem
Application of Chinese Remainder Theorem with both integers and polynomials

It makes use of the [Euclid GCD](https://github.com/kristopher-pellizzi/EuclidGCD "Euclid GCD") module to easily compute quotients, remainders and/or multiplications between polynomials, and, of course, the GCD of values.

## usage: 
CRT.py [-h] [--poly] [-m modulus] vals [vals ...]

Application of Chinese Remainder Theorem (CRT) to compute solution of a system of modular equations

### positional arguments:
  - *vals*: couples of values representing the modular equations of which a solution is needed. It accepts both couples of integers or polynomials, separated by a symbol '%'. Considering equations of the form x = ai (mod mi), the value preceding '%' is ai, while the one following it is mi.  
  At least 2 values are needed to compute a solution.  
  Example: **python3 CRT.py 1%2 3%5 2%11** => *13 mod 110*

### optional arguments:
  -h, --help  show this help message and exit
  - --poly: required in order to work with polynomials. By using this argument, you are informing the program that it must interpret your input as couples of polynomials. Inserting polynomials representations without using this option will raise an error.  
  Example: **python3 CRT.py --poly 1,2,1%1,1 1,1%1,2** => (1.0 x + 1.0) mod (1.0 x^2 + 3.0 x + 2.0)
  - -m: modulus representing the cardinality of the support of the finite field the polynomials coefficients are taken from. Example: -m 5 means all coefficients are mod 5, so they are all numbers between 0 and 4.  
  ***NOTE:* this option can be used only combined with --poly option. If --poly is not used, this option will be simply ignored**
