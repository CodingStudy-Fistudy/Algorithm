def solution(brown, yellow):
    for y in range(1,yellow//2+2):
        if yellow%y==0:
            w,h=yellow//y,y
            if (w+2)*2+h*2==brown:
                return [w+2,h+2]
            
        
