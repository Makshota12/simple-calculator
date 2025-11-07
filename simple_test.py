import calculator

def test_simple():
    print("🧪 Testing calculator...")
    
    # Test add
    result = calculator.add(2, 2)
    assert result == 4, f"2+2 should be 4, got {result}"
    print("✅ 2 + 2 = 4")
    
    # Test subtract
    result = calculator.subtract(5, 3)
    assert result == 2, f"5-3 should be 2, got {result}"
    print("✅ 5 - 3 = 2")
    
    # Test multiply
    result = calculator.multiply(3, 4)
    assert result == 12, f"3*4 should be 12, got {result}"
    print("✅ 3 * 4 = 12")
    
    print("🎉 All tests passed!")

if __name__ == "__main__":
    test_simple()