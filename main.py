from vending_machine import VendingMachine

products = [
    {"name": "콜라", "price": 2000, "count": 5},
    {"name": "사이다", "price": 750, "count": 5},
    {"name": "환타", "price": 1500, "count": 5}
]
vm = VendingMachine(products)

while True:
    vm.display_menu()
    
    try:
        menu = int(input("메뉴 선택 : "))
    except:
        print(f">> 숫자로 메뉴를 입력해주세요!")

    if menu == 1:
        balance = vm.select_product()
    elif menu == 2:
        balance = vm.insert_money()
    elif menu == 3:
        balance = vm.return_balance()
    elif menu == 4:
        print("프로그램 종료")
        break
    else:
        print(f">> 1~4까지 숫자를 입력해주세요!")