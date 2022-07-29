#本git库不更新 ，依赖的 代码库也不更新？
from qgb import py,U,T,F




def app(env, start_response):
    code=env['PATH_INFO'][1:]
    code=T.url_decode(code)
    if code.endswith('/'):code=code[:-1]
    
    # r=f'''{U.stime()}\n{env}\n{"="*77}\n{start_response}'''
    start_response('200 OK', [('Content-Type','text/plain;charset=utf-8')])
    return [U.execResult(code,globals=py.globals(),locals=py.locals())]
