class UserPrompts:
    @staticmethod
    def display_message(message):
        print(message)


def get_user_input(prompt, set_to_upper=True):
    answer = input(prompt)
    if set_to_upper:
        answer = answer.upper()

    return answer
