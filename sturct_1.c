enum{
    MAN,
    WOMAN
};

struct person
{
    char * name ;
    char * id;
    char sex;
};

void main(void)
{
    struct person p1 ;

    p1.name = "hong";
    p1.id = "1234";
    p1.sex = MAN ;

    printf("%s의 이름은 %s 입니다.\n\r", "P1", p1.name) ;
    printf("%s의 아이디는 %s 입니다. \n\r", "P1", p1.id);
   // char * temp = (p1.sex == MAN)?("남자"):("여자") ;

    
    printf("%s의 성별은 %s 입니다. \n\r","P1" ,(p1.sex == MAN)?("남자"):("여자") );
}