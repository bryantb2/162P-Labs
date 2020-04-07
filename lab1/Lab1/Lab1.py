# Check if A is Power of B
def is_first_power_of_second(a, b):
    # standard cases (both must be true):
        # a modulus b, check if 0
        # divide a/b and then modulus, check if 0
    # default cases (only one must be true):
        # b raised to 0 equals a
        # b raised to 1 equals a
    is_power = False;
    if (a % b == 0 and ((a/b) % b) == 0) :
        is_power = True;
    elif (b**0 == a or b**1 == a) :
        is_power = True;
    print('Is ' + str(a) + ' power of ' + str(b) + ': ' + str(is_power));
    return is_power;

# Setup Tests
def test_power_function():
    # dictionary for a & b values
    testData = [
        {
            "a": 5,
            "b": 5
        },
        {
            "a": 25,
            "b": 5
        },
        {
            "a": 125,
            "b": 25
        },
        {
            "a": 1,
            "b": 13
        },
        {
            "a": 64,
            "b": 4
        },
        {
            "a": 27,
            "b": 4
        },
        {
            "a": 256,
            "b": 2
        }
    ];
    # Call test foreach set
    for dataPair in testData:
        is_first_power_of_second(dataPair["a"],dataPair["b"]);


# Run Test
test_power_function();