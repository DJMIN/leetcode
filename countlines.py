import sys, os

EXCLUDE = [r'C:\Users\Chen\PycharmProjects\osyl\osyl\utils']
# host = r'C:\Users\Chen\IdeaProjects\Contest2\Contest-src\client\app'
# host = r'C:\Users\Chen\IdeaProjects\Contest2\ContestFrontEnd2\src'
host = r'C:\Users\Chen\PycharmProjects\osyl\osyl'
SUFFIX = [
    'py',
    # 'vue',
    # 'js',
    # 'html',
    # 'java'
]


def count_lines(f_path):
    res = 0
    f = open(f_path, "r", 1, "utf8")
    for lines in f:
        if lines.split():
            res += 1
    return res


if __name__ == '__main__':
    allline = 0
    allfiles = 0
    for root, dirs, files in os.walk(host):
        break_flag = False
        for ex in EXCLUDE:
            if root.startswith('%s%s%s' % (host, os.sep, ex)) or root.startswith(ex):
                break_flag = True
                break

        if break_flag:
            break

        for file_name in files:
            ext = file_name.split('.')
            ext = ext[-1]
            if ext in SUFFIX:
                itpath = '%s%s%s' % (root, os.sep, file_name)
                allfiles += 1
                line = count_lines(itpath)
                allline += line
                print(itpath.replace(host, '.'), '\t', line, '\t', ext)
    print('Total lines:', '\t', allline)
    print('Total: ', '\t', allfiles)
