#!/usr/local/bin/python
# -*-coding:utf-8-*-
import os

project_paths = ["/Users/huangchangqiang/Downloads/a/",
                 "/Users/huangchangqiang/Downloads/b/",
                 "/Users/huangchangqiang/Downloads/c/",
                 "/Users/huangchangqiang/Downloads/r/"]


class CodeParser:
    def __init__(self):
        pass

    def get_dir_paths(self, root_path, dir_paths, dir_key):
        list_dir = os.listdir(root_path)
        for _dir in list_dir:
            path = os.path.join(root_path, _dir)
            if os.path.isdir(path):
                if dir_key in _dir:
                    dir_paths.append(path)
                    print(path)
                else:
                    self.get_dir_paths(path, dir_paths, dir_key)

    def get_file_paths(self, dir_path, file_paths, file_ext):
        list_dir = os.listdir(dir_path)
        for _dir in list_dir:
            path = os.path.join(dir_path, _dir)
            if os.path.isfile(path):
                splitext = os.path.splitext(path)
                splitext_len = len(splitext)
                if splitext_len > 0 and file_ext in splitext[splitext_len - 1]:
                    file_paths.append(path)
            else:
                self.get_file_paths(path, file_paths, file_ext)

    @staticmethod
    def get_code_lines(file_path):
        return len(open(file_path, 'rU').readlines())


total_code_lines = 0
total_java_code_lines = 0
total_xml_code_lines = 0
codeParser = CodeParser()

for project_path in project_paths:
    # 获取一个工程中所有模块的src目录列表
    src_paths = []
    codeParser.get_dir_paths(project_path, src_paths, 'src')

    # 获取一个工程中所有src目录中的java文件列表
    java_file_paths = []
    for src_path in src_paths:
        codeParser.get_file_paths(src_path, java_file_paths, '.java')
    print('\njava files count is %d in %s' % (len(java_file_paths), project_path))

    # 计算一个工程中所有src目录中的java代码行数
    java_code_lines = 0
    for java_file_path in java_file_paths:
        code_lines = CodeParser.get_code_lines(java_file_path)
        java_code_lines += code_lines
    print('java code lines count is %d in %s \n' % (java_code_lines, project_path))
    total_java_code_lines += java_code_lines

    # 获取一个工程中所有模块的res目录列表
    res_paths = []
    for src_path in src_paths:
        codeParser.get_dir_paths(src_path, res_paths, 'res')

    # 获取一个工程中所有res目录中的xml文件列表
    xml_file_paths = []
    for res_path in res_paths:
        codeParser.get_file_paths(res_path, xml_file_paths, '.xml')
    print('\nxml files count is %d in %s' % (len(xml_file_paths), project_path))

    # 计算一个工程中所有res目录中的xml代码行数
    xml_code_lines = 0
    for xml_file_path in xml_file_paths:
        code_lines = CodeParser.get_code_lines(xml_file_path)
        xml_code_lines += code_lines
    print('xml code lines count is %d in %s \n' % (xml_code_lines, project_path))
    total_xml_code_lines += xml_code_lines

    project_code_lines = java_code_lines + xml_code_lines
    total_code_lines += project_code_lines
    print('code lines count is %d in %s \n' % (project_code_lines, project_path))

print('total java code lines count is %d \n' \
      'total xml code lines count is %d \n' \
      'total code lines count is %d' % \
      (total_java_code_lines, total_xml_code_lines, total_code_lines))
