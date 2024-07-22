#include <time.h>
#include <stdio.h>

typedef void (*handler_t)(void); // 함수포인터 자료형을 새로 정의 , 이렇게 정의해놓으면 함수의인자로 함수포인터를 사용할때 편리함.

static void timer(handler_t handler); // 함수포인터를 인자로 받는 함수 , 인자에 원하는 함수를 넣어서 동작되도록 구성할 수 있음.
static void timer_callback(void); // 타이머 콜백함수 , 실제 동작되는 함수, 함수포인터의 주소에 넣어서 호출됨.

void delay_ms(clock_t ms) // ms단위 지연함수
{
    clock_t start = clock();
    while(clock() - start <= ms );
}

void main (void)
{
    timer(timer_callback); // 타이머함수에 콜백함수를 넣어서 호출
}

static void timer (handler_t handler)
{
    while(1)
    {
        handler();
        //delay_ms(5000); // 1초 지연
        sleep(1);
        //return ;
    }
}


static void timer_callback(void)
{
    printf("Timer call back \n\r");
}
