from math import sqrt


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        return (numer, denom)
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)

def quadratic_function(a,b,c):
    if (b**2-4*a*c >= 0):
        x1 = (-b+sqrt(b**2-4*a*c))/(2*a)
        print "Quadratic Formula" + str(x1)
        x2 = (-b-sqrt(b**2-4*a*c))/(2*a)
        print "Quadratic Formula" + str(x2)

        # Added a "-" to these next 2 values because they would be moved to the other side of the equation
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction(a,mult1)
        (num2,den2) = simplify_fraction(a,mult2)
        if ((num1 > a) or (num2 > a)):
            # simplify fraction will make too large of num and denom to try to make a sqrt work
            print("No factorization")
        else:
            # Getting ready to make the print look nice
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            print("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
    else:
        # if the part under the sqrt is negative, you have a solution with i
        print("Solutions are imaginary")
    return

while True:
	typeOfEq = raw_input("sqrt, distance, gcd, or factor: ")
	if typeOfEq == "distance":
		x1 = int(raw_input("X1: "))
		y1 = int(raw_input("Y1: "))
		x2 = int(raw_input("X2: "))
		y2 = int(raw_input("Y2: "))
		preciseDistance = ((x2-x1)**2)+((y2-y1)**2)
		distance = sqrt( ((x2-x1)**2)+((y2-y1)**2) )

		print "PreciseDistance: sqrt of " + str(preciseDistance)
		print "Decimal Distance: " + str(distance)

	elif typeOfEq == 'sqrt':
		num = int(raw_input("Sqrt: "))
		print str(num ** .5)
	elif typeOfEq == 'factor':
		a = int(raw_input("A: "))
		b = int(raw_input("B: "))
		c = int(raw_input("C: "))
		quadratic_function(a, b, c)
	elif typeOfEq == 'gcd':
		gcdAns = gcd(int(raw_input("A: ")), int(raw_input("B: ")))
		print gcdAns