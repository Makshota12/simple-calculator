from calculator import add, subtract, multiply, divide

def run_tests():
    print("Running calculator tests...")
    
    # Test add
    assert add(2, 2) == 4, "2 + 2 should be 4"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    print("✓ Add tests passed")
    
    # Test subtract
    assert subtract(5, 3) == 2, "5 - 3 should be 2"
    assert subtract(10, 10) == 0, "10 - 10 should be 0"
    print("✓ Subtract tests passed")
    
    # Test multiply
    assert multiply(3, 4) == 12, "3 * 4 should be 12"
    assert multiply(0, 5) == 0, "0 * 5 should be 0"
    print("✓ Multiply tests passed")
    
    # Test divide
    assert divide(10, 2) == 5, "10 / 2 should be 5"
    assert divide(1, 1) == 1, "1 / 1 should be 1"
    print("✓ Divide tests passed")
    
    # Test divide by zero
    try:
        divide(10, 0)
        assert False, "Should raise ValueError for division by zero"
    except ValueError:
        print("✓ Division by zero test passed")
    
    print("🎉 All tests passed!")

if __name__ == "__main__":
    run_tests()
