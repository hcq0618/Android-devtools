#!/usr/local/bin/python
# -*-coding:utf-8-*-
import os
import xml
import zipfile

import shutil
from xml.sax import make_parser, ContentHandler

gradle_cache_path = '/Users/huangchangqiang/.gradle/caches/modules-2/files-2.1/'


class PermissionHandler(ContentHandler):
    zip_dir_path = None

    def __init__(self):
        ContentHandler.__init__(self)

    def set_zip_dir_path(self, zip_dir_path):
        self.zip_dir_path = zip_dir_path

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        if tag == 'uses-permission' or tag == 'permission':
            if 'android:name' in attributes:
                name = attributes['android:name']
                if self.zip_dir_path:
                    print self.zip_dir_path
                    self.zip_dir_path = None
                print name


class AARParser:
    def __init__(self):
        self.permissionParser = make_parser()
        # turn off namespaces
        self.permissionParser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.permissionHandler = PermissionHandler()
        self.permissionParser.setContentHandler(self.permissionHandler)

    def get_aar_file_path(self, root_path, _aar_file_paths):
        list_dir = os.listdir(root_path)
        for _dir in list_dir:
            path = os.path.join(root_path, _dir)
            if os.path.isfile(path):
                splitext = os.path.splitext(path)
                splitext_len = len(splitext)
                if splitext_len > 0 and '.aar' in splitext[splitext_len - 1]:
                    aar_file_paths.append(path)
                    # print path
            else:
                self.get_aar_file_path(path, _aar_file_paths)

    def parse(self, _aar_file_paths):
        for aar_file_path in _aar_file_paths:
            # aar复制成zip
            zip_file_path = aar_file_path.replace('.aar', '.zip')
            # print zip_file_path
            if not os.path.exists(zip_file_path):
                open(zip_file_path, "wb").write(open(aar_file_path, "rb").read())

            # 解压zip
            zip_dir_path = zip_file_path.replace('.zip', '')
            if not os.path.exists(zip_dir_path):
                _zip = zipfile.ZipFile(zip_file_path, 'r')
                _zip.extractall(path=zip_dir_path)
                _zip.close()

            # 解析权限
            self.parse_permissions(zip_dir_path)

    def parse_permissions(self, zip_dir_path):
        list_dir = os.listdir(zip_dir_path)
        for _dir in list_dir:
            path = os.path.join(zip_dir_path, _dir)
            if os.path.isfile(path) and 'AndroidManifest.xml' in path:
                self.permissionHandler.set_zip_dir_path(zip_dir_path)
                self.permissionParser.parse(path)
                break

    @staticmethod
    def delete_unneeded_files(_aar_file_paths):
        for _aar_file_path in _aar_file_paths:
            root_path = os.path.dirname(_aar_file_path)
            list_dir = os.listdir(root_path)
            for _dir in list_dir:
                path = os.path.join(root_path, _dir)
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print path
                elif '.aar' in path or '.zip' in path:
                    continue
                else:
                    os.remove(path)
                    print path


aarParser = AARParser()

aar_file_paths = []
aarParser.get_aar_file_path(gradle_cache_path, aar_file_paths)
print 'aar files count is %d' % len(aar_file_paths)

# AARParser.delete_unneeded_files(aar_file_paths)
aarParser.parse(aar_file_paths)
