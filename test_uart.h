/*
인터페이스 제작 예제 uart*/


#include <stdbool.h>
#include <stdio.h>
// 1. Describe functions
// 포인터함수 자료형 정의
typedef bool (*open_t)(void) ;
typedef bool (*close_t)(void);
typedef bool (*write_t)(char *buffer, short length);
typedef bool (*read_t)(char *data);

// 통신 구조체 선언 
// uart_t 구조체에는 open, close, write, read 함수포인터가 포함되어 있음.
typedef struct 
{
    open_t open;
    close_t close;
    write_t write;
    read_t read;
}uart_t;

extern uart_t *init_uart1(void); // 외부에서 사용할수 있도록 extern 사용선언. 