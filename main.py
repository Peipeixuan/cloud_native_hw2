def is_positive_number(num: int) -> bool:
    return num > 0

if __name__ == "__main__":
    # 測試輸入
    test_input = 5  # success-branch = 5, fail-branch = -3
    result = is_positive_number(test_input)
    print(f"Input: {test_input}, Result: {result}")
    if not result:
        exit(1)
