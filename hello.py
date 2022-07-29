#本git库不更新 ，依赖的 代码库也不更新？
from qgb import py,U,T,F




def app(env, start_response):
    #import requests
    #code=requests.get('https://qmm0.pythonanywhere.com/-r=code',).text
    
    # r=f'''{U.stime()}\n{env}\n{"="*77}\n{start_response}'''
    
    code=T.url_decode(env['RAW_URI'][1:] )
    
    start_response('200 OK', [('Content-Type','text/plain;charset=utf-8')])
    rb=U.execResult(code,globals=py.globals(),locals=py.locals()).encode('utf-8')
    return [rb]

app=U._import('qgb.N.mirror_cache').app
