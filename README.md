# ImageTiffCollector

ImageTiffCollector — это Python-скрипт, который собирает изображения из списка папок и объединяет их в один TIFF файл.

## Описание

Этот проект предназначен для автоматической сборки изображений из указанных папок и сохранения их в один TIFF файл. Скрипт проходит по каждой папке, собирает все изображения с поддерживаемыми расширениями и сохраняет их в результирующий файл `Result.tif`.

## Требования

- Python 3.6 или выше
- Библиотека Pillow

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/IceDisel/ImageTiffCollector.git
    cd ImageTiffCollector
    ```

2. Установите необходимые зависимости:
    ```sh
    pip install Pillow
    ```

## Использование

1. Поместите папки с изображениями в корневую директорию проекта. Например, `1388_12_Наклейки 3-D_3`.
2. Измените список папок в `main` функции в файле `main.py`:
    ```python
    folder_list = ['1388_12_Наклейки 3-D_3']
    ```

3. Запустите скрипт:
    ```sh
    python main.py
    ```

4. Результат будет сохранен в файле `Result.tif` в корневой директории проекта.


После выполнения скрипта `Result.tif` будет содержать все изображения из папки `1388_12_Наклейки 3-D_3`.

### Цель проекта
Код написан в образовательных целях.

## Автор

Владимир Титов — [tvv-vg@yandex.ru, https://github.com/IceDisel]


