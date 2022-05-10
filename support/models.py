from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    title = models.TextField(verbose_name = '제목', null = False, default="무제")
    content = models.TextField(verbose_name = '질문')
    category = models.CharField(
        max_length=256, 
        choices=[('General', '일반'), ('Account', '계정') , ('Etc', '기타')]
    )
    writer = models.ForeignKey(verbose_name = '생성자', to = User, on_delete  = models.CASCADE, null = True, blank = True, related_name='writer')
    answer = models.TextField(verbose_name = '답변')
    created_at  = models.DateTimeField(verbose_name = '생성일시' , auto_now_add = True)
    last_modifier = models.ForeignKey(verbose_name = '최종 수정자', to = User, on_delete=models.SET_NULL, null = True, blank = True, related_name='last_modifer')
    modifed_at  = models.DateTimeField(verbose_name = '최종 수정일시' , auto_now = True)


class Inquiry(models.Model):
    title = models.CharField( max_length=256,  verbose_name = '제목', default="무제")
    category = models.CharField(
        max_length=256, 
        choices=[('General', '일반'), ('Account', '계정') , ('Etc', '기타')]
    )
    state = models.CharField(
        max_length=256, 
        choices=[('Register', '문의 등록'), ('Accept', '접수 완료') , ('Finish', '답변 완료')],
        default=('Register', '문의 등록')
    )
    writer = models.ForeignKey(verbose_name = '생성자', to = User, editable=False, on_delete  = models.CASCADE, null = True, blank = True)
    e_mail = models.CharField(max_length=256, verbose_name = '이메일 주소')
    phone_number = models.CharField(max_length=256, verbose_name = '전화번호')
    content = models.TextField(verbose_name = '문의')
    image = models.ImageField(verbose_name = '이미지', null = True, blank = True)
    created_at  = models.DateTimeField(verbose_name = '생성일시' , auto_now_add = True)
    modifed_at  = models.DateTimeField(verbose_name = '최종 수정일시' , auto_now = True)

class Answer(models.Model):
    inquiry = models.ForeignKey( verbose_name = '문의', to = Inquiry , on_delete = models.CASCADE, null = False, blank = False)
    
    content = models.TextField(verbose_name = '답변')
    writer = models.ForeignKey(verbose_name = '답변자', to = User, editable=False, on_delete  = models.CASCADE, null = True, blank = True )
    last_modifier = models.ForeignKey(verbose_name = '최종 답변자', to = User, editable = False, on_delete  = models.CASCADE, null = True, blank = True, related_name = 'last_answer_writer')
    created_at  = models.DateTimeField(verbose_name = '답변 일시' , auto_now_add = True)
    modifed_at  = models.DateTimeField(verbose_name = '최종 답변 일시' , auto_now = True)



