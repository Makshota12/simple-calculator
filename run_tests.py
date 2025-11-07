from calculator import add, subtract, multiply

def test_add():
    result = add(2, 2)
    assert result == 4, f"2 + 2 should be 4, but got {result}"
    print("✅ test_add passed")

def test_subtract():
    result = subtract(5, 3)
    assert result == 2, f"5 - 3 should be 2, but got {result}"
    print("✅ test_subtract passed")

def test_multiply():
    result = multiply(3, 4)
    assert result == 12, f"3 * 4 should be 12, but got {result}"
    print("✅ test_multiply passed")

def run_all_tests():
    print("🧪 Running Calculator Tests...")
    test_add()
    test_subtract()
    test_multiply()
    print("🎉 All tests passed!")

if __name__ == "__main__":
    run_all_tests()