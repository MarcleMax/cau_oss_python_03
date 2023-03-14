while 1:
    print('\n  Chose your language please.\n  언어를 선택하십시오.\n')

    print(' --ENGLISH[e]--\n --한국어[k]--')
    language = input()
    
    
    if(language == 'e'):
        
        lenth = float(input('Input the lenth: '))
        width = float(input('Input the width: '))
        height = float(input('Input the height: '))
        
        volume = lenth * width * height
        print("The box's volume is %s." %volume)
        break
                
    elif(language == 'k'):
        
        lenth = float(input('가로를 입력해 주십시오: '))
        width = float(input('세로를 입력해 주십시오: '))
        height = float(input('높이를 입력해 주십시오: '))
        volume = lenth * width * height
        print('박스의 부피는%s입니다.' %volume)
        break
        
    else:
        print(' Input the correct letter please.\n 자모를 정확하게 입력해 주십시오.')
        continue
