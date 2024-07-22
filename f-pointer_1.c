/*
함수포인터를 사용해서 함수 호출 방법*/

static void test1(void)
{
    printf("TEST 1 fuction\n");
}

static void test2(void)
{
    printf("TEST 2 fuction\n");
}

void main(void)
{
    /*  // 일반적인 함수포인터 선언 및 사용 방법
    void (*F_ptr)(void); // 함수포인터 선언 - 자료형 (*포인터변수명)(매개변수자료형)
    F_ptr = test1 ; // 함수포인터에 함수주소를 대입
    F_ptr(); // 함수포인터로 함수를 호출.

    F_ptr = test2 ; // 함수포인터에 다른 함수주소를 대입
    F_ptr(); // 함수포인터로 함수를 호출.
    */

    // tydef 사용 함수포인터 사용방법
    // 똑같은 형식의 함수포인터를 여러개 선언할때 편리함.
    typedef void (*F_ptr)(void); // 함수포인터 자료형을 새로 정의
    F_ptr ptr1;
    F_ptr ptr2;

    ptr1 = test1; // 함수포인터에 함수주소를 대입
    ptr1();       // 함수포인터로 함수를 호출.

    ptr2 = test2; // 함수포인터에 다른 함수주소를 대입
    ptr2();       // 함수포인터로 함수를 호출.
}