# import json
# import tempfile
#
# from audiocrawl.audiocrawl.spiders import crawl_audio_db
# from audio_db import *
#
#
# class testA(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# def test():
#     # tl = []
#     # testa = testA(1, 3)
#     # ta = testa.__dict__
#     # testb = testA(4, 5)
#     # tb = testb.__dict__
#     # tl.append(ta)
#     # tl.append(tb)
#     # jsont = json.dumps(tl)
#     # print("jsont:" + jsont)
#     # # crawl_audio_db.init()
#     ads = crawl_audio_db.getAudioListById(11)
#     print("lengh:" + str(ads[0].audio_title))
#     j = json.dumps(ads[0], cls=AudioDetaiListlDbDec, ensure_ascii=False)
#     print("j:" + j)
#
#     a = crawl_audio_db.have_classify_count("网游小说")
#     print("a:" + str(a))
#
#     b = crawl_audio_db.have_audio_count("单田芳")
#     print("b:" + str(b))
#
#     c = crawl_audio_db.have_audio_deitail_item_count("无上神帝1", "第30集")
#     print("c:" + str(c))
#     # # print("js_version:"+json.__version__)
#     # data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
#     # print('DATA:', repr(data))
#
#     # unsorted = json.dumps(data)
#     # print('JSON:', json.dumps(data))
#     # print('SORT:', json.dumps(data, sort_keys=True))
#
#     # obj = MyObj('helloworld')
#     # print("obj:" + str(obj))
#     # try:
#     #     print
#     #     json.dumps(obj)
#     # except TypeError as err:
#     #     print('ERROR:', err)
#     #
#     # print(json.dumps(obj, default=convert_to_builtin_type))
#     # encoded_object = '[{"s":"helloworld","__module__":"__main__","__class__":"MyObj"}]'
#     # myobj_instance = json.loads(encoded_object, object_hook=dict_to_object)
#     # print(myobj_instance)
#
#     #
#     # obj = MyObj('helloworld')
#     # print(obj)
#     #
#     # print(MyEncoder().encode(obj))
#
#     data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
#
#     # f = tempfile.NamedTemporaryFile(mode='w+')
#     # json.dump(data, f)
#     # f.flush()
#
#
# # class MyEncoder(json.JSONEncoder):
# #     print('default(', repr(obj), ')')
# #     # Convert objects to a dictionary of their representation
# #     d = {'__class__': obj.__class__.__name__,
# #          '__module__': obj.__module__,
# #          }
# #     d.update(obj.__dict__)
# #     return d
# #
# #
# # class MyObj(object):
# #     def __init__(self, s):
# #         self.s = s
# #
# #     def __repr__(self):
# #         return '<MyObj(%s)>' % self.s
# #
# #
# # # 转换函数
# # def convert_to_builtin_type(obj):
# #     print('default(', repr(obj), ')')
# #     # 把MyObj对象转换成dict类型的对象
# #     d = {'__class__': obj.__class__.__name__,
# #          '__module__': obj.__module__,
# #          }
# #     d.update(obj.__dict__)
# #     return d
# #
# #
# # def dict_to_object(d):
# #     if '__class__' in d:
# #         class_name = d.pop('__class__')
# #         module_name = d.pop('__module__')
# #         module = __import__(module_name)
# #
# #         print("MODULE:", module)
# #
# #         class_ = getattr(module, class_name)
# #
# #         print("CLASS", class_)
# #
# #         args = dict((key.encode('utf-8'), value) for key, value in d.items())
# #
# #         print('INSTANCE ARGS:', args)
# #
# #         inst = class_(**args)
# #     else:
# #         inst = d
# #     return inst
#
#
# if __name__ == '__main__':
#     test()
