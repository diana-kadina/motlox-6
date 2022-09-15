import os
import sys

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}


EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            sort_files(folder, file)
        elif file != EXTENSIONS.keys():
            subfolder = os.path.join(folder, file) #not imag, arch, aud, doc, vid
            if not os.listdir(subfolder): #nothing
                os.rmdir(subfolder) #clean
            
                return
            clean(subfolder)


def sort_files(folder: str, file: str):
    file_name, file_suffix = file.rsplit('.', maxsplit=1)

    for folder_name, extensions in EXTENSIONS.items():
        if file.endswith(extensions):
            new_folder = os.path.join(folder, folder_name)

            os.makedirs(new_folder, exist_ok=True)

            new_file_name = normalize(file_name)

            file_path = os.path.join(folder, new_file_name)

            new_file = os.path.join(new_folder, new_file_name + file_suffix)

            os.replace(file_path, new_file)

            if folder_name == 'archives':
                archive_folder = os.path.join(new_folder, new_file_name)

                archive_unpack(new_file, archive_folder)
            break

    else:
        new_file_name = normalize(file_name)

        new_file = os.path.join(folder, new_file_name + file_suffix)

        os.replace(file, new_file)



for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
def normalize(file_name):
    text = " "
    return file_name.normalize(TRANS)
    



def archive_unpack(file: str, folder: str):
    # створюємо каталог із назвою архіву, але назва повиння бути без розширення
    os.makedirs(folder, exist_ok=True)

    # тут потрібно архів (file) розпакувати у каталог folder


def main():
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    root_folder = sys.argv[1]

    if (not os.path.exists(root_folder)) and (not os.path.isdir(root_folder)):
        print('Path incorrect')
        exit()

    #root_folder = "C:\\Users\\38063\OneDrive\\Робочий стіл\\GoIT\\Разное"
    clean(root_folder)


if __name__ == "__main__":
    main()

print('done')