# Not the optimum solution because starting backwards checking elements in the input path complicates
# things unnecessarily. Yet it was useful to practice some concepts.

from collections import deque


def normalize_path(file_path):
    normalized = deque()
    file_path = file_path.strip()
    starting_separator = file_path[0] if file_path[0] == '/' else None
    path_list = file_path.split('/')
    pre_normalized = [ele for ele in path_list if ele != '.' and ele != '']
    idx = 0

    while pre_normalized:
        consecutive_double = 0
        current_dir = pre_normalized[-1]
        idx = len(pre_normalized) - 1

        if current_dir != '..':
            pre_normalized.pop()
            normalized.appendleft(current_dir)
            continue

        consecutive_double += 1

        for k in range(idx - 1, -1, -1):
            if pre_normalized[k] != '..':
                cut_length = min(consecutive_double, len(pre_normalized)) * 2
                pre_normalized = pre_normalized[:len(pre_normalized) - cut_length]
                break

            consecutive_double += 1

    if starting_separator:
        normalized[0] = starting_separator + normalized[0]

    return '/'.join(normalized)


assert (normalize_path('/home/user/../user/folder/./file.txt')
        == normalize_path('/home/./user/folder/file.txt')
        == normalize_path('/home/user/folder/file.txt'))

assert (normalize_path('./folder/subfolder/../file.txt')
        == normalize_path('folder/./file.txt')
        == normalize_path('folder/file.txt'))

print(normalize_path('/home/user/../user/folder/./file.txt'))
print(normalize_path('/home/./user/folder/file.txt'))
print(normalize_path('/home/user/folder/file.txt'))
print(normalize_path('./folder/subfolder/../file.txt'))
print(normalize_path('folder/./file.txt '))
print(normalize_path('folder/file.txt'))
print(normalize_path('/home/user/subfolder/../../user/folder/./file.txt'))
