상자 = ['사과', '배', '콩', '두부']
def 아침업무(박스):
    
    물건 = '사과'
    if 물건 == '사과':
        print(f"{물건}는 냉장실로")
    elif 물건 == '아이스크림':
        print(f"{물건}은 냉동실로")
    else:
        print(f"{물건}은 폐기처분")
        
출근=True #출근 안 한 상태

if 출근:
    박스=['콩', '참치', '사과', '아이스크림']
    아침업무(박스)
