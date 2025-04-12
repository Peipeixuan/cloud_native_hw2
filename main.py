import requests

def is_positive_number(num: int) -> bool:
    return num > 0

if __name__ == "__main__":
    # 測試輸入
    test_input = 5 
    result = is_positive_number(test_input)
    print(f"Input: {test_input}, Result: {result}")
    if not result:
        exit(1)

    # 測試 requests 套件
    try:
        response = requests.get('https://api.github.com')
        print(f"GitHub API response status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        exit(1)
