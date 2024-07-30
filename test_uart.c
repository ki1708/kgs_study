#include "test_uart.h"

static bool open(void);
static bool close(void);
static bool write(char *buffer, short length);
static bool read(char *data);

//extern static uart_t *init_uart1(void)
extern uart_t *init_uart1(void)
{
    static uart_t uart;
    uart.open = open;
    uart.close = close;
    uart.write = write ;
    uart.read = read;
    return &uart;
}

static bool open(void)
{
    printf("uart open\n\r");
    fflush(stdout);
    return 1 ;
}


static bool close(void)
{
    printf("uart close\n\r");
    return 1 ;
}

static bool write(char *buffer, short length)
{
    printf("uart write\n\r");
    return 1 ;
}

static bool read(char *data)
{
    printf("uart read\n\r");
    return 1 ;
}

