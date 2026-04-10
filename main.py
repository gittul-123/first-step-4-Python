# Quiz 클래스 정의 (이전과 동일)
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

# 1. 퀴즈 데이터 준비 (기존 코드)
quizzes = [
    Quiz("가장 큰 과일은 무엇일까요?", ["수박", "딸기", "사과"], "수박"),
    Quiz("노란색이고 신 맛이 나는 과일은 무엇일까요?", ["포도", "오렌지", "레몬"], "레몬"),
    Quiz("보통 껍질을 깎아먹는 과일은 무엇일까요?", ["사과", "블루베리", "체리"], "사과"),
    Quiz("세상에서 가장 인기 있는 과일은 무엇일까요?", ["바나나", "토마토", "망고"], "토마토"),
    Quiz("여름이 제철인 과일은 무엇일까요?", ["귤", "복숭아", "석류"], "복숭아")
]

# 퀴즈 풀기 로직 시작
def run_quiz():
    # 5. 퀴즈가 없는 경우 처리
    if not quizzes:
        print("풀 수 있는 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
        return # 함수를 즉시 종료

    score = 0
    # 1. 저장된 퀴즈를 하나씩 출제
    for idx, quiz in enumerate(quizzes):
        print(f"\n--- 문제 {idx + 1} ---")
        print(quiz.question)

        # 보기 출력
        for i, choice in enumerate(quiz.choices):
            print(f"{i + 1}. {choice}")

        # 2. 사용자가 정답을 입력
        user_answer = input("정답을 입력해주세요: ")

        # 3. 정답/오답 여부 판정
        if user_answer == quiz.answer:
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"아쉽네요. 정답은 '{quiz.answer}' 입니다.")

    # 4. 모든 문제를 풀면 결과 표시
    print("\n--- 모든 문제를 다 풀었습니다! ---")
    total_questions = len(quizzes)
    print(f"총 {total_questions}문제 중 {score}문제를 맞혔습니다.")
    
    # 정답률도 계산해서 보여주기 (선택 사항)
    accuracy = (score / total_questions) * 100
    print(f"정답률: {accuracy:.1f}%")


# 프로그램 실행
if __name__ == "__main__":
    run_quiz()
