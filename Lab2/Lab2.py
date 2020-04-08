# Find A raised to power of B
def raise_base_to_pwr(a, b):
    # check if even power
    is_evn_pwr = False if b % 2 != 0 else True;
    # base cases
    if(b <= 0) :
        return 1;
    if(b == 1) :
        return a;
    if(is_evn_pwr) :
        half_power = b/2;
        return raise_base_to_pwr(a, half_power) * raise_base_to_pwr(a, half_power);
    else :
        power_minus_one = b - 1;
        return a * raise_base_to_pwr(a, power_minus_one);

# Setup Tests
def test_power_function():
    # dictionary for a & b values
    testData = [
        {
            "a": 5,
            "b": 1,
            "answer": 5
        },
        {
            "a": 2,
            "b": 13,
            "answer": 8192
        },
        {
            "a": 3,
            "b": 6,
            "answer": 729
        },
        {
            "a": 5,
            "b": 8,
            "answer": 390625
        },
        {
            "a": 27,
            "b": 0,
            "answer": 1
        },
        {
            "a": 13,
            "b": -1,
            "answer": 1
        }
    ];
    # Call test foreach set
    for dataPair in testData:
        a = dataPair["a"];
        b = dataPair["b"];
        expectedAnswer = dataPair["answer"];
        calculatedAnswer = raise_base_to_pwr(a,b);
        print("Rose base '" + str(a) + "' to '" + str(b) + 
              "', expecting '" + str(expectedAnswer) + 
              "', got '" + str(calculatedAnswer) + "'.");


# Run Test
test_power_function();