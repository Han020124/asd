class DeliveryApp:
    def __init__(self):
        self.restaurant = Restaurant()
        self.rider = DeliveryRider()

    def order_food(self, food_item):
        print("[배달앱] 손님으로부터 음식 주문을 받았습니다:", food_item)
        self.restaurant.prepare_food(food_item)
        self.rider.deliver(food_item)
        print("[배달앱] 음식 배달 완료. 리뷰를 작성해주세요!")

    def submit_review(self, review):
        print("[배달앱] 손님으로부터 리뷰를 전달받았습니다:", review)
        self.restaurant.receive_review(review)


class Restaurant:
    def prepare_food(self, food_item):
        print(f"[음식점] '{food_item}' 주문을 받았습니다.")
        print(f"[음식점] '{food_item}' 준비 완료되었습니다.")
        print(f"[음식점] 준비 완료를 배달앱에 알립니다.")

    def receive_review(self, review):
        print(f"[음식점] 배달앱으로부터 리뷰를 전달받았습니다: \"{review}\" 감사합니다!")


class DeliveryRider:
    def deliver(self, food_item):
        print(f"[배달기사] '{food_item}' 배달 요청을 받았습니다.")
        print(f"[배달기사] '{food_item}' 손님에게 배달 완료했습니다.")


# 실행 예시
if __name__ == "__main__":
    app = DeliveryApp()
    app.order_food("치킨")
    app.submit_review("음식이 정말 맛있었어요! 배달도 빨랐어요 :)")
