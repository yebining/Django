class 업무():
    def 아침업무(self,  박스): 
    #self : 내부 변수를 움직이기 위해서 self 
        for 물건 in 박스:
            if 물건 == '사과':
                print(f'{물건}은 냉장실에 넣기')
            elif 물건 == '아이스크림':
                print(f'{물건}은 냉동실에 넣기')
            else:
                print(f'{물건}은 폐기처분')

출근 = True
if 출근:
    박스=['콩', '참치', '사과', '아이스크림']
    
    출근후업무=업무()
    출근후업무.아침업무(박스)
    
class 필수업무():
    아침업무유무=False #초기값
    
    def 아침업무체크(self):
        self.아침업무유무=True
        
    def 아침업무(self, 박스):
        for 물건 in 박스:
            if 물건 == '사과':
                print(f'{물건}은 냉장실에 넣기')
            elif 물건 == '아이스크림':
                print(f'{물건}은 냉동실에 넣기')
            else:
                print(f'{물건}은 폐기처분')
        
        self.아침업무체크()
        
출근=True
if 출근:
    박스=['콩', '참치', '사과', '아이스크림']
    
    예빈_업무=필수업무()
    print(예빈_업무.아침업무유무)
    
    예빈_업무.아침업무(박스)
    print(예빈_업무.아침업무유무)
    
    영현_업무 = 필수업무()
    print(영현_업무.아침업무유무)
    
    명헌_업무 = 필수업무()
    print(명헌_업무.아침업무유무)
    
    #class : 독립적인 객체로 할당 받아 사용