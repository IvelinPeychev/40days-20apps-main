import zipfile


def extract_archive(archivepath, destination_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(destination_dir)


if __name__ == '__main__':
    extract_archive('C:\\Users\\peych\\PycharmProjects\\pythonMegaCourse40Days20Apps\\ToDo\\bonus\\dest\\test1\\comprased.zip',
                    'C:\\Users\\peych\\PycharmProjects\\pythonMegaCourse40Days20Apps\\ToDo\\bonus\\dest\\test1')
