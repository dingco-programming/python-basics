class VendingMachine:
    def __init__(self, products):
        self.products = products
        self.balance = 0

    def display_menu(self):
        print("\n\n자판기 프로그램")
        print("-----------------------")
        for i, product in enumerate(self.products):
            print(f"{i + 1}. {product['name']}({product['count']}개) : {product['price']} 원")
        print("-----------------------")
        print(f"현재 잔액 : {self.balance} 원")
        print("-----------------------")
        print("")
        print("1. 상품 선택")
        print("2. 돈 투입")
        print("3. 잔액 반환")
        print("4. 종료")
        print("")


    def select_product(self):
        num = int(input("상품 번호 입력 : "))
        product = self.products[num-1]
        if product['count'] > 0 and self.balance >= product["price"]:
            print(f">> {product['name']}를 구입 했습니다!")
            self.balance = self.balance - product["price"]
            product["count"] = product["count"] - 1
        else:
            print(f">> 상품을 구입할 수 없습니다.")

    def insert_money(self):
        money = int(input("투입 금액 입력 (원): "))
        self.balance = self.balance + money
        print(f">> {money}원이 투입되었습니다.")
        print(f"현재 잔액 : {self.balance}")

    def return_balance(self):
        print(f">> {self.balance}원을 반환합니다.")
        self.balance = 0
        print(f"현재 잔액 : {self.balance}")


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