#include <stdio.h>

//static short count = 0;

//static 정적변수 테스트 
/*
프로그램 실행시 할당되고 , 프로그램 종료시 파괴됨.
외부에서는 참조할 수 없음 -> 반환해줘야 참조가능.
(내부정적변수일때는 다른함수에서, 외부정적변수일때는 다른 소스파일에서)*/

short test_static_count(void)
{
    static short count = 0;
    count ++;
    printf("static count = %d \n" , count);
    return count;
}

short test_count(void)
{
    short count = 0 ;
    count ++;
    printf("count = %d \n" , count);
    return count ;
}

void main(void)
{
    

    while(1)
    {
        test_static_count();
        test_count();
        //printf("static global count = %d \n" , count);
    }
}
