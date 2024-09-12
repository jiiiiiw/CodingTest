from itertools import product

def solution(users, emoticons):
    # 가능한 할인율 리스트 (10%, 20%, 30%, 40%)
    discount_rates = [10, 20, 30, 40]
    # 모든 이모티콘에 대해 할인율을 적용한 경우의 수
    discount_combinations = list(product(discount_rates, repeat=len(emoticons)))
    
    # 결과를 저장할 변수 (최대 가입자 수, 최대 판매액)
    max_subscribers = 0
    max_sales = 0
    
    # 모든 할인율 조합에 대해 반복
    for discounts in discount_combinations:
        subscribers = 0
        sales = 0
        
        # 각 사용자에 대해 처리
        for user_discount, user_budget in users:
            total_purchase = 0  # 사용자가 구매한 이모티콘의 총 가격
            
            # 각 이모티콘에 대해 할인율 적용
            for i in range(len(emoticons)):
                # 이모티콘 할인 적용 가격 계산
                discounted_price = emoticons[i] * (100 - discounts[i]) // 100
                
                # 사용자의 할인율 기준을 만족하는 경우에만 이모티콘 구매
                if discounts[i] >= user_discount:
                    total_purchase += discounted_price
            
            # 사용자가 이모티콘 플러스 가입을 결정할지 여부 확인
            if total_purchase >= user_budget:
                subscribers += 1  # 가입자 수 증가
            else:
                sales += total_purchase  # 이모티콘 판매액 증가
        
        # 더 많은 가입자를 얻은 경우 혹은 같은 가입자 수에서 판매액이 큰 경우 갱신
        if subscribers > max_subscribers or (subscribers == max_subscribers and sales > max_sales):
            max_subscribers = subscribers
            max_sales = sales
    
    return [max_subscribers, max_sales]
