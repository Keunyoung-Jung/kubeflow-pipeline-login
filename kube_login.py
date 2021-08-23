import requests
from kfp import Client
'''
소유 : Mysterico
작성자 : keyog
최종 업데이트 : 2021.08.10
'''

class KubeInit :
    '''
    쿠버플로우를 dex기반으로 로그인하기 위한 객체 입니다.
    '''
    KUBEFLOW_HOST = 'http://istio-ingressgateway.istio-system/pipeline'
    session_cookie=None
        
    @classmethod
    def login_kubeflow(cls,username,password):
        '''
        requests라이브러리를 통해 dex에 로그인하고, 로그인 세션을 가져옵니다.
        '''
        try :
            session = requests.Session()
            response = session.get(cls.KUBEFLOW_HOST)
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }
            data = {"login": username, "password": password}
            session.post(response.url, headers=headers, data=data)
            cls.session_cookie = session.cookies.get_dict()["authservice_session"]
        except Exception as e :
            print(e)
            print('[Login Error]Wrong Username or Wrong Password')
        else :
            print(f'Succeed Login to \"{username}\"')

    @classmethod
    def get_client(cls,namespace) :
        '''
        로그인 세션을 기반으로 쿠버플로우 네임스페이스의 클라이언트 객체를 받아옵니다.
        '''
        print(f'Client Set Namespace \"{namespace}\"')
        return Client(
            host=cls.KUBEFLOW_HOST,
            cookies=f'authservice_session={cls.session_cookie}',
            namespace=namespace
        )