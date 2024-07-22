#include <stdio.h>
#include "test_uart.h"


void main(void)
{
    char *buffer = "hello";
    char data ;
    uart_t *uart1 ;

    uart1 = init_uart1();
    uart1->open();
    uart1->write(buffer,5);

    return ;
}

