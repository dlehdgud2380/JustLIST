#list 프로그램
import random

powermethod = input("프로그램을 실행하시겠습니까?(Y/N)=> ") #무한반복을 위한 구실에 불가하다...

while powermethod == "Y" or powermethod == "y" : #프로그램을 전체 반복

    print("\n\n\n\n\n\n\n\n\n\n\n\n\nJustLIST 0.1 by scoutlee\n\n")

    print("LIST를 생성하겠습니다...")

    input_menu = int(input("LIST를 어떻게 생성 하시겠습니까? \n(1)자동생성(숫자로만 생성됩니다.)\n(2)직접입력\n\n번호선택: ")) #이 변수값을 통해서 리스트에 어떻게 아이템 입력이 될것인지 달라진다.

    if input_menu == 1:

        list=[]

        for i in range(1, 6):

            random_value = random.randrange(100)
            print (random_value)
            list.append(random_value)

        print("\n생성된 LIST는 다음과 같습니다.", (list))


    elif  input_menu == 2:

        input_mod = int(input("데이터 입력 모드를 선택하세요.\n(1)string모드(모두 입력가능)\n(2)int모드(순수 숫자만 입력할때, 단어 및 모음 입력등등은 지원 안됨)\n\n번호선택: "))

        if input_mod == 1:

            a = input("(1): ")
            b = input("(2): ")
            c = input("(3): ")
            d = input("(4): ")
            e = input("(5): ")

            list = [a, b, c, d, e]

        elif input_mod == 2:

            a = int(input("(1): "))
            b = int(input("(2): "))
            c = int(input("(3): "))
            d = int(input("(4): "))
            e = int(input("(5): "))

            list = [a, b, c, d, e]

        print("\n사용자가 입력하신 LIST는 다음과 같습니다.", list)

    while list == list:

        work_menu = int(input("\nLIST를 어떻게 하시겠습니까?\n(1)item값 추가\n(2)item값 수정\n(3)LIST 자른 결과값 출력\n(4)item값 삭제\n(5)LIST에서 item찾기\n(6)LIST 정렬하기\n(7)LIST값 상태\n(8)Just List 정보\n(9)Just LIST 새로시작(LIST가 초기화 됩니다!!)\n(10)Just LIST 종료\n번호입력: "))

        if work_menu == 1:

            append_menu = int(input("(1)1개의 item 추가\n(2)다중 item 추가\n번호입력: "))

            if append_menu == 1:

                append_mod = int(input("int모드와 string모드중 선택해주세요.\n(1)int모드(순수 숫자만 입력할때, 단어 및 모음 입력등등은 지원 안됨), (2)string모드(모두 입력 가능)\n번호입력: "))

                if append_mod == 1:
                    list.insert( int(input("몇번째 자리에 넣고 싶은 가요?(1,2,3,4,5중 택1): "))-1 ,int(input("수정할 item값을 입력: ")) )

                if append_mod == 2:
                    list.insert( int(input("몇번째 자리에 넣고 싶은 가요?(1,2,3,4,5중 택1): "))-1 , input("수정할 item값을 입력: "))

                print ("수정된 list는 %s입니다." %list)


            elif append_menu == 2:

                extend_mod = int(input("int모드와 string모드중 선택해주세요.\n(1)int모드(순수 숫자만 입력할때, 단어 및 모음 입력등등은 지원 안됨), (2)string모드(모두 입력 가능)\n번호입력: "))

                if extend_mod == 1:
                    list.extend(int(input("추가할 item들을 입력하시요(,와 띄움없이): ")))

                elif extend_mod == 2:
                    list.extend(input("추가할 item들을 입력하시요(,와 띄움없이): "))

                print("수정된 list는 %s입니다." %list)

        elif work_menu == 2:

            edit_mod = int(input("int모드와 string모드중 선택해주세요.\n(1)int모드(순수 숫자만 입력할때, 단어 및 모음 입력등등은 지원 안됨), (2)string모드(모두 입력 가능)\n번호입력:"))

            if edit_mod == 1:
                print("\n%s\n" %list)
                list[int(input("몇번째의 item을 수정하고 싶으신가요?(1,2,3,4,5중 택1): "))-1] = int(input("넣을 item값을 입력하시요: "))

            elif edit_mod == 2:
                print("\n%s\n" %list)
                list[int(input("몇번째의 item을 수정하고 싶으신가요?(1,2,3,4,5중 택1): "))-1] = input("넣을 item값을 입력하시요: ")

            print("수정된 list는 %s입니다." %list)

        elif work_menu == 3:

            print("\n*LIST 자르기를 도와드리겠습니다.*\n")
            print("\n%s\n" %list)
            start_value = int(input("몇번째 item부터(1,2,3,4,5중 택1): "))-1
            last_value = int(input("몇번째 item까지(1,2,3,4,5중 택1): "))
            print( "LIST를 자른 결과는 %s 입니다."%list[start_value:last_value ])

        elif work_menu == 4:

            del_menu = int(input("LIST 삭제 방법을 선택하세요:\n(1)지정 item값 삭제\n(2)인덱스 해당 아이템 삭제\n번호입력: "))

            if del_menu == 1:

                print("\n%s\n" %list)
                list.remove(input("삭제할 item값을 입력하시요: "))

            elif del_menu == 2:

                print("\n%s\n" %list)
                del list[int(input("몇번째 값을 삭제 하시겠습니까?(1,2,3,4,5중 택1): "))-1]

            print("수정된 list는 %s입니다." %list)

        elif work_menu == 5:

            print("\n*item 검색을 도와드리겠습니다*\n")

            findITEM = input("찾으실 item을 입력해주세요: ")

            if findITEM in list:
                print("\nitem이 LIST에 있습니다. => %s" %findITEM)

                locate_findITEM = list.index(findITEM)+1

                print("LIST의 %d번째에 있습니다." %locate_findITEM)

            elif findITEM not in list:

                int_findITEM = int(findITEM)

                print("\nitem이 LIST에 있습니다. => %s" %int_findITEM)

                locate_findITEM = list.index(int_findITEM)+1

                print("LIST의 %d번째에 있습니다." %locate_findITEM)

            else:
                print("찾으시는 item이 LIST에 없습니다.")

        elif work_menu == 6:

            print("\n*LIST를 정렬하겠습니다.*\n")
            list.sort()
            print("정렬된 list는 %s입니다." %list)

        elif work_menu == 7:

            print("\n%s\n" %list)

        elif work_menu == 8:

             print("\n\n\nJustLIST 0.1 by scoutlee\ndlehdgud2380@kookmin.ac.kr\n\n그냥 리스트 시험공부겸으로 만들어본 프로그램\n\n")

        elif work_menu == 9:
            break

        elif work_menu == 10:
            break

    if work_menu == 10:
        print("\n\n사용해주셔서 감사합니다. \n피드백: dlehdgud2380@kookmin.ac.kr ")

        break








