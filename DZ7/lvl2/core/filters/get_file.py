import os


def get_file(file: str) -> str:
    documents = {''.join(document.split('.')[:-1]): document for document in os.listdir('core/filters/files/') if
                 document.split('.')[-1] != 'jpg'}

    return documents[file]


def get_all_files() -> list[str]:
    return [''.join(document.split('.')[:-1]) for document in os.listdir('core/filters/files/')]
