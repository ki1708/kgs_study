//2024-07-30

test_uart.c파일을 활용해서 .o 오브젝트 파일을 만든 후
libtest_uart.a로 정적라이브파일 생성해서 main.c로 컴파일할때 라이브러리로 설정해서 실행파일 생성
gcc -o exec main.c -L. -ltest_uart -I../include

햇갈린점 :
main.c에서 테스트용으로 쓴 test_uart의 open함수가 static 함수여서 컴파일을 정상적으로 해도 실제 동작이 안되었음.

main.c에서 init_uart1();을 써서 인스턴스를 생성해서 함수에 접근하니 성공. 
