#本git库不更新 ，依赖的 代码库也不更新？
from qgb import py,U,T,F




def app(env, start_response):
    #U.pprint(env)
    import requests
    code=requests.get('https://qmm0.pythonanywhere.com/-r=code',).text
    
    # r=f'''{U.stime()}\n{env}\n{"="*77}\n{start_response}'''
    start_response('200 OK', [('Content-Type','text/plain;charset=utf-8')])
    return [U.execResult(code,globals=py.globals(),locals=py.locals())]
