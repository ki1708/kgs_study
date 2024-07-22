/*
함수포인터와 구조체 동시사용*/

typedef enum 
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


