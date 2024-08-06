from django.core.files.uploadedfile import *
from django.core.files.uploadhandler import *


class myFileUploadHandler(TemporaryFileUploadHandler):
    def new_file(self, *args, **kwargs):
        super().new_file(*args, **kwargs)
        print('这是自定义的文件上传')
        self.file = TemporaryUploadedFile(self.file_name, self.content_type, 0, self.charset, self.content_type_extra)
