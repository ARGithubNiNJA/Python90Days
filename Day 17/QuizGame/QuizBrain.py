#TODO question no. to keep the track of the question

class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0

    def new_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1

        current_answer = input(
            f"Q.{self.question_no}: {current_question.text} (True/False): "
        ).lower()

        self.check_Answer(current_answer, current_question.answer)

        print(f"Current Score: {self.score}/{self.question_no} \n\n")



    def still_has_question(self):
        len_question=len(self.question_list)
        curr_len=self.question_no
        if len_question==curr_len:
            return False
        else:
            return True

    def check_Answer(self,current_answer, correct_answer):
        if current_answer.lower()==correct_answer.lower():
            print("Correct")
            self.score+=1

        else:
            print("Incorrect")
            print(f"Correct Answer: {correct_answer}")

