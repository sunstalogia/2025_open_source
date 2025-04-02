# 메뉴 선택 하는 코드를 함수화

def select_menu(i):
    menus[i][1] = menus[i][1] + 1
    print(f"{menus[i][0]} {menus[i][1]}잔 주문...")
    print(f"소계 : {(prices[0] * menus[0][1]) + (prices[1] * menus[1][1]) + (prices[2] * menus[2][1]) + (prices[3] * menus[3][1])}원")


menus = [["아이스 아메리카노", 0], ["카페 라떼", 0], ["유자차", 0], ["자바칩 프라푸치노", 0]]  # [[메뉴, 수량], ...]
prices = [2000, 2500, 2400, 7000]

amount = int(input("몇 잔? "))

menu_lists = ""
for i in range(len(menus)):
    menu_lists = menu_lists + f"{i+1}) {menus[i][0]} "

for _ in range(amount):
    menu = input(f"{menu_lists}: ")
    if menu == "1":
        select_menu(0)
    elif menu == "2":
        select_menu(1)
    elif menu == "3":
        select_menu(2)
    elif menu == "4":
        select_menu(3)
    else:
        print("잘못된 주문입니다")


total_price = 0
for j in range(len(menus)):
    if menus[j][1] > 0:  # 각 메뉴들의 수량이 1 이상이면
        total_price = total_price + (menus[j][1]* prices[j])  # 가격 리스트에서 가격 추출해서 합산

print(f"총 금액은 {total_price}원 입니다.")
#print(f"총 금액은 {(menus[0][1] * 2000) + (menus[1][1] * 2500) + (menus[2][1] * 2400)}원 입니다.")
