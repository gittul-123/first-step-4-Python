# main.py

class Quiz:
    """
    퀴즈 문제를 나타내는 클래스.
    문제(question)와 정답(answer) 속성을 가집니다.
    """
    def __init__(self, question, answer):
        # 퀴즈 객체가 생성될 때 문제와 정답을 받아서 저장합니다.
        self.question = question
        self.answer = answer

# --- 클래스가 잘 만들어졌는지 테스트하는 코드 ---

# 1. Quiz 클래스를 이용해 첫 번째 퀴즈 '객체(object)'를 만듭니다.
quiz1 = Quiz("파이썬의 공식 마스코트 이름은 무엇일까요?", "파이썬")

# 2. 두 번째 퀴즈 객체도 만들어 봅니다.
quiz2 = Quiz("Git에서 브랜치를 새로 만드는 명령어는 무엇일까요?", "git branch")


# 3. 객체에 정보가 잘 저장되었는지 출력해서 확인해 봅시다.
print(f"문제 1: {quiz1.question}")
print(f"정답 1: {quiz1.answer}")
print("--------------------")
print(f"문제 2: {quiz2.question}")
print(f"정답 2: {quiz2.answer}")
