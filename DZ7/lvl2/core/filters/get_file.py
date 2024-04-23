import os


def get_file(file: str) -> str:
    documents = {''.join(document.split('.')[:-1]): document for document in os.listdir('core/filters/files/') if
                 document.split('.')[-1] != 'jpg'}

    return documents[file]
