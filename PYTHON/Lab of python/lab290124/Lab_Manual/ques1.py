# Example of integer
x = 10
print("x is of type:", type(x))
print("Identity of x:", id(x))

decimal_num = 42

print("Decimal to Binary:", bin(decimal_num))
print("Binary to Decimal:", int('0b101010',2))
    
print("Decimal to Octal:", oct(decimal_num))
print("Octal to Decimal:", int('0o52',8))
    
print("Decimal to Hexadecimal:", hex(decimal_num))
print("Hexadecimal to Decimal:", int('0x2a',16))



def demonstrate_type_conversion():
    # Integer to String
    integer_value = 42
    string_value = str(integer_value)
    print("Integer to String:", string_value, type(string_value))

    # String to Integer
    string_value = "42"
    integer_value = int(string_value)
    print("String to Integer:", integer_value, type(integer_value))

    # Float to String
    float_value = 3.14
    string_value = str(float_value)
    print("Float to String:", string_value, type(string_value))

    # String to Float
    string_value = "3.14"
    float_value = float(string_value)
    print("String to Float:", float_value, type(float_value))

    # Integer to Float
    integer_value = 42
    float_value = float(integer_value)
    print("Integer to Float:", float_value, type(float_value))

    # Float to Integer
    float_value = 3.14
    integer_value = int(float_value)
    print("Float to Integer:", integer_value, type(integer_value))

    # Boolean to String
    bool_value = True
    string_value = str(bool_value)
    print("Boolean to String:", string_value, type(string_value))

    # String to Boolean
    string_value = "True"
    bool_value = bool(string_value)
    print("String to Boolean:", bool_value, type(bool_value))

    # Integer to Boolean
    integer_value = 0
    bool_value = bool(integer_value)
    print("Integer to Boolean:", bool_value, type(bool_value))

    # Boolean to Integer
    bool_value = True
    integer_value = int(bool_value)
    print("Boolean to Integer:", integer_value, type(integer_value))


def main():
    demonstrate_type_conversion()


if __name__ == "__main__":
    main()



