import string
import os

def scan_disks():
    return ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


import os
import fnmatch

def find_cache_files(disk, patterns):
    cache_files = []
    for dirpath, dirnames, filenames in os.walk(disk):
        for pattern in patterns:
            for filename in fnmatch.filter(filenames, pattern):
                cache_files.append(os.path.join(dirpath, filename))
    return cache_files

# Пример использования
if __name__ == "__main__":
    # Укажите диск для поиска, например, 'C:\\'
    disk = 'C:\\'

    # Шаблоны для поиска кэш-файлов
    cache_patterns = ['*.tmp', '*.cache', '*.log', '*.temp', '*.bak']

    found_cache_files = find_cache_files(disk, cache_patterns)

    print(f"Найдено кэш-файлов: {len(found_cache_files)}")
    input()
    for file in found_cache_files:
        try:
            os.remove(file)
            print(f'removed {file}')
        except Exception as e:
            print(f'Failed to remove {file} with error {e}')
