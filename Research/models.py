from django.db import models
from django.contrib.auth.models import User


class ResearchArticles(models.Model):
    Rtitle = models.TextField(max_length=100, verbose_name='论文名称')
    Rauthor = models.ForeignKey(User, related_name="Article", on_delete=models.CASCADE, verbose_name='第一作者')
    # Rauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    Rinstitution = models.CharField(max_length=100, verbose_name='所属机构')
    Rintroduction = models.TextField(verbose_name='简介')
    Rpublish = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    Rcategory = models.CharField(max_length=100, verbose_name='类别')
    Rfund = models.IntegerField(default=0, verbose_name='研究经费(元)')
    Rrank = models.CharField(max_length=100, verbose_name='检索分类')
    Rjournal = models.CharField(max_length=100, verbose_name='来源期刊')

    class Meta:
        ordering = ("-Rpublish",)
        verbose_name_plural = '论文管理'


class Projects(models.Model):
    proj_name = models.TextField(max_length=50, verbose_name='项目名')  # 项目名
    proj_id = models.IntegerField(verbose_name='项目序号')  # 项目序号
    contract_id = models.IntegerField(verbose_name='合同序号')  # 合同序号
    proj_type = models.CharField(max_length=30, verbose_name='项目类型')  # 项目类型
    endpoint = models.DateTimeField(auto_now=True, verbose_name='结题时间')  # 结题时间
    charge_man = models.CharField(max_length=30, verbose_name='负责人')  # 负责人
    charge_dept = models.CharField(max_length=50, verbose_name='负责人院别')  # 负责人院别
    start_time = models.DateTimeField(auto_created=False, verbose_name='立项时间')  # 立项时间
    delegated_dept = models.CharField(max_length=50, verbose_name='委托单位')  # 委托单位
    contract_funds = models.IntegerField(verbose_name='合同经费(元）')  # 合同经费
    equip_funds = models.IntegerField(verbose_name='设备经费（元)')  # 设备经费
    check_date = models.DateTimeField(verbose_name='鉴定日期')  # 鉴定日期
    valid_time = models.IntegerField(verbose_name='有效期限(天）')  # 有效期限
    money_in_1 = models.IntegerField(verbose_name='到账金额1（元)')  # 到账金额
    money_in_date_1 = models.DateTimeField(auto_now=True, verbose_name='到款日期')  # 到款日期
    money_in_2 = models.IntegerField(verbose_name='到账金额2(元)')  # 到账金额
    money_in_date_2 = models.DateTimeField(auto_now=True, verbose_name='到款日期')  # 到款日期
    money_in_3 = models.IntegerField(verbose_name='到账金额3(元)')  # 到账金额
    money_in_date_3 = models.DateTimeField(auto_now=True, verbose_name='到款日期')  # 到款日期
    money_in_4 = models.IntegerField(verbose_name='到账金额4(元)')  # 到账金额
    money_in_date_4 = models.DateTimeField(auto_now=True, verbose_name='到款日期')  # 到款日期
    proj_intro = models.TextField(max_length=100, verbose_name='项目简介')  # 项目简介
    money_in_all = models.IntegerField(verbose_name='总到账金额(元)')  # 到账金额
    accomplish = models.CharField(max_length=100, verbose_name='项目完成情况')  # 项目完成情况
    participator_1 = models.CharField(max_length=30, verbose_name='参与者1')  # 参与者1
    participator_2 = models.CharField(max_length=30, verbose_name='参与者2', default="无")  # 参与者2
    participator_3 = models.CharField(max_length=30, verbose_name='参与者3', default="无")  # 参与者3
    participator_4 = models.CharField(max_length=30, verbose_name='参与者4', default="无")  # 参与者4
    participator_5 = models.CharField(max_length=30, verbose_name='参与者5', default="无")  # 参与者5
    participator_6 = models.CharField(max_length=30, verbose_name='参与者6', default="无")  # 参与者6
    participator_7 = models.CharField(max_length=30, verbose_name='参与者7', default="无")  # 参与者7
    participator_8 = models.CharField(max_length=30, verbose_name='参与者8', default="无")  # 参与者8
    participator_9 = models.CharField(max_length=30, verbose_name='参与者9', default="无")  # 参与者9
    participator_10 = models.CharField(max_length=30, verbose_name='参与者10', default="无")  # 参与者10

    class Meta:
        verbose_name_plural = '横向项目管理'
