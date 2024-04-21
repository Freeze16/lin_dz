import aiml


class HelperBot:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn('settings.xml')
        print("Чем могу быть полезен?")

    def start_bot(self):
        question = input('>> ')
        answer = self.kernel.respond(question)
        if 'Спасибо, ваш отзыв' in answer:
            self.write_report(question)

        print(answer)

    @staticmethod
    def write_report(rep: str):
        with open('reports.txt', 'a+') as file:
            file.write('\n' + rep)


if __name__ == '__main__':
    cb = HelperBot()
    while True:
        cb.start_bot()
