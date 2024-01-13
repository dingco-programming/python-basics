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