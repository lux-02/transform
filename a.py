def check_encoding(input_value):
    if isinstance(input_value, str):
        try:
            # UTF-8 인코딩 확인
            input_value.encode('utf-8')
            print("[UTF-8]", input_value)
        except UnicodeEncodeError:
            pass
        try:
            # ASCII 인코딩 확인
            input_value.encode('ascii')
            print("[ASCII]", input_value)
        except UnicodeEncodeError:
            pass
    else:
        print("[NONE]", input_value)

# 사용 예
check_encoding("Hello, World!")  # ASCII 및 UTF-8 인코딩 가능 문자열
check_encoding("안녕하세요!")      # UTF-8에서만 인코딩 가능한 문자열
