# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from fun import settings
import os

'''
    处理，下载
'''
class ImageDownloadPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:
            images = []
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)
            
            # 创建存储目录，也就是放图片的地方
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            # 循环下载图片
            for image_url in item['image_urls']:
                # 给图片命名
                us = image_url.split('/')[8:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                # 不重复下载
                if os.path.exists(file_path):
                    continue
                # 响应流写入
                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

            item['images'] = images
        return item
