from django.core.signing import TimestampSigner


class mySigningBackend(TimestampSigner):
    def sign(self, value):
        print(value)
        return value + 'Test'

    def unsign(self, value, max_age=None):
        print(value)
        return value[0:-4]
