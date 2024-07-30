#include <stdio.h>
#include <stdbool.h>
#include "test_uart.h"

// bool open(void);
uart_t *init_uart1(void);

void main(void)
{
    uart_t *uart1;

    printf("main start\n");
    // open();
    uart1 = init_uart1();

    uart1->open();
    fflush(stdout);
}
