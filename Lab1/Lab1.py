# Check if A is Power of B
def is_first_power_of_second(a, b):
    # standard cases (both must be true):
        # a modulus b, check if 0
        # divide a/b and then modulus, check if 0
    # default cases (only one must be true):
        # b raised to 0 equals a
        # b raised to 1 equals a
    if (a % b == 0 and ((a/b) % b) == 0) :
        return True;
    elif (b**0 == a or b**1 == a) :
        return True;
    return False;

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
        a = dataPair["a"];
        b = dataPair["b"];
        is_power = is_first_power_of_second(a,b);
        print('Is ' + str(a) + ' power of ' + str(b) + ': ' + str(is_power));


# Run Test
test_power_function();