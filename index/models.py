from django.db import models


# Create your models here.

class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'


class PersonInfo2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hire_date = models.DateField(null=True, blank=True)
    live = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'
        app_label = 'user'
        db_table = 'personinfo'


class Vocation(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    name = models.ForeignKey(PersonInfo, on_delete=models.CASCADE, related_name='personinfo')
    # 新增字段必须设置null=True, blank=True
    payment = models.IntegerField(null=True, blank=True)
    # person = models.ForeignKey(PersonInfo, on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '职位信息'


class Performer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    masterpiece = models.CharField(max_length=50)


class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)


class Performer_info(models.Model):
    id = models.AutoField(primary_key=True)
    performer = models.OneToOneField(Performer, on_delete=models.CASCADE)
    birth_date = models.CharField(max_length=20)
    elapse = models.CharField(max_length=20)


class Province(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '城市信息表'
        app_label = 'index'
        db_table = 'city'


class Person(models.Model):
    name = models.CharField(max_length=20)
    living = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


def createModel(name, fields, app_label, options=None):
    """
    创建模型类
    :param name: 模型类名称
    :param fields: 字段
    :param app_label: 应用名称
    :param options: Meta选项
    :return:返回模型对象
    """

    class Meta:
        pass

    setattr(Meta, 'app_label', app_label)
    if options:
        for key, value in options.items():
            setattr(Meta, key, value)
    attrs = {'__module__': f'{app_label}.models', 'Meta': Meta}
    attrs.update(fields)
    return type(name, (models.Model,), attrs)


def createDb(model):
    """
    创建数据库
    :param model: 模型对象
    :return:
    """
    from django.db import connection
    from django.db.backends.base.schema import BaseDatabaseSchemaEditor
    try:
        with BaseDatabaseSchemaEditor(connection) as editor:
            editor.create_model(model=model)
    except Exception as e:
        print(f"Error creating table: {e}")


def createNewTab(model_name):
    """
    创建新表
    :param model_name: 表名
    :return：返回模型对象，便于视图进行增删改查
    """
    fields = {
        'id': models.AutoField(primary_key=True),
        'product': models.CharField(max_length=20),
        'sales': models.IntegerField(),
        '__str__': lambda self: str(self.id), }
    options = {
        'verbose_name': model_name,
        'db_table': model_name
    }
    m = createModel(model_name, fields, 'index', options)
    createDb(m)
    return m
