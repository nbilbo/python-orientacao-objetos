class HttpResponseStatus:

    @classmethod
    def RESPONSE_200_OK(cls):
        print('200 ok')
    
    @classmethod
    def RESPONSE_201_CREATED(cls):
        print('201 created')

    @classmethod
    def RESPONSE_202_ACCEPTED(cls):
        print('202 accepted')

    @classmethod
    def RESPONSE_203_NON_AUTHORITATIVE_INFORMATION(cls):
        print('203 non authoritative information')

    @classmethod
    def RESPONSE_204_NO_CONTENT(cls):
        print('204 no content')


if __name__ == '__main__':
    HttpResponseStatus.RESPONSE_200_OK()
    HttpResponseStatus.RESPONSE_201_CREATED()
    HttpResponseStatus.RESPONSE_202_ACCEPTED()
    HttpResponseStatus.RESPONSE_203_NON_AUTHORITATIVE_INFORMATION()
    HttpResponseStatus.RESPONSE_204_NO_CONTENT()
