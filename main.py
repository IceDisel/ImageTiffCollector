import os
from PIL import Image


def collect_image_folders(folder_list: list[str]) -> list[Image]:
    """
    Собирает изображения из списка папок.
    :param folder_list: Список папок для поиска изображений.
    :return: Список объектов изображений PIL.
    """

    images = []
    for folder in folder_list:
        folder = os.path.abspath(folder)

        if not os.path.exists(folder):
            print(f"Папка не существует: {folder}")
            continue

        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                img_path = os.path.join(folder, filename)
                try:
                    img = Image.open(img_path)
                    images.append(img)
                except Exception as e:
                    print(f"Не удалось открыть изображение {img_path}: {e}")

    return images


def save_image_to_tiff(images: list[Image.Image], output_path: str) -> None:
    """
    Сохраняет список изображений в один TIFF файл.

    :param images: Список объектов изображений PIL.
    :param output_path: Путь для сохранения итогового TIFF файла.
    :return: None
    """

    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:])


def main() -> None:
    """
    Основная функция программы.
    """

    folder_list = ['1388_12_Наклейки 3-D_3', '1369_12_Наклейки 3-D_3', '1388_2_Наклейки 3-D_1',
                   '1388_6_Наклейки 3-D_2', '1']

    output_path = 'Result.tif'

    images = collect_image_folders(folder_list)
    save_image_to_tiff(images, output_path)

    print(f'Собраны {len(images)} изображений в файл {output_path}')


if __name__ == '__main__':
    main()
