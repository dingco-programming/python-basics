balance = 0
products = [
    {"name": "콜라", "price": 2000, "count": 5},
    {"name": "사이다", "price": 750, "count": 5},
    {"name": "환타", "price": 1500, "count": 5}
]

while True:
    # 메뉴 출력
    print("\n\n자판기 프로그램")
    print("-----------------------")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product['name']}({product['count']}개) : {product['price']} 원")
    print("-----------------------")
    print(f"현재 잔액 : {balance} 원")
    print("-----------------------")
    print("")
    print("1. 상품 선택")
    print("2. 돈 투입")
    print("3. 잔액 반환")
    print("4. 종료")
    print("")

    # 메뉴 입력
    try:
        menu = int(input("메뉴 선택 : "))
    except:
        print(f">> 숫자로 메뉴를 입력해주세요!")

    # 메뉴 비교
    if menu == 1:
        # 상품 선택
        num = int(input("상품 번호 입력 : "))
        product = products[num-1]
        if product['count'] > 0 and balance >= product["price"]:
            print(f">> {product['name']}를 구입 했습니다!")
            balance = balance - product["price"]
            product["count"] = product["count"] - 1
        else:
            print(f">> 상품을 구입할 수 없습니다.")
    elif menu == 2:
        # 돈 투입
        money = int(input("투입 금액 입력 (원): "))
        balance = balance + money
        print(f">> {money}원이 투입되었습니다.")
        print(f"현재 잔액 : {balance}")
    elif menu == 3:
        # 잔돈 반환
        print(f">> {balance}원을 반환합니다.")
        balance = 0
        print(f"현재 잔액 : {balance}")
    elif menu == 4:
        print("프로그램 종료")
        break
    else:
        print(f">> 1~4까지 숫자를 입력해주세요!")