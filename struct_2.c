/*
함수포인터와 구조체 동시사용*/
#include <stdio.h>
static void open(void);
static void close(void);
static void read(void);
static void write(void);


enum 
{
    LCD_DRIVER,
    SEGMENT_DRIVER
};

// 구조체 선언 함수포인터 포함.
typedef struct {
    char driver_id;
    void (*open)(void);
    void (*close)(void);
    void (*read)(void);
    void (*write)(void);
}driver_t;


static driver_t lcd =
{
    .driver_id = LCD_DRIVER,
    .open = open,
    .close = close,
    .read = read,
    .write = write
};






void main(void)
{
    lcd.open();
    lcd.close();
    lcd.read();
    lcd.write();
}

static void open(void)
{
    printf("open\n\r");
}

static void close(void)
{
    printf("close\n\r");
}

static void read(void)
{
    printf("read\n\r");
}


static void write(void)
{
    printf("write\n\r");
}



