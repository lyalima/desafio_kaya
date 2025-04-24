from django.db import models
from multipleselectionfield import MultipleSelectionField


gender_choices = (
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Outro', 'Outro'),
)

state_choices = (
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
)

service_choices = (
    ('Adolescentes', 'Adolescentes'),
    ('Adultos', 'Adultos'),
    ('Crianças', 'Crianças'),
    ('Idosos', 'Idosos'),
)

class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name='Especalidade')

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    gender = models.CharField(max_length=9, choices=gender_choices, verbose_name='Gênero')
    photo = models.ImageField(upload_to='doctors/', verbose_name='Foto', null=True, blank=True)
    crm = models.CharField(max_length=6, unique=True, verbose_name='CRM')
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='specialties', verbose_name='Especialidade')
    value = models.CharField(max_length=255, null=True, blank=True, verbose_name='Valor')
    city = models.CharField(max_length=255, verbose_name='Cidade')
    state = models.CharField(max_length=2, choices=state_choices, verbose_name='Estado')
    instagram = models.URLField(null=True, blank=True, verbose_name='Instagram')
    facebook = models.URLField(null=True, blank=True, verbose_name='Facebook')
    linkedin = models.URLField(null=True, blank=True, verbose_name='Linkedin')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    pathologies = models.TextField(null=True, blank=True, verbose_name='Patologias')
    services = MultipleSelectionField(choices=service_choices, verbose_name='Atendimento')
    accepts_agreement = models.BooleanField(verbose_name='Aceita Convênio')
    feedback_followup= models.TextField(max_length=255, verbose_name='Retorno e Acompanhamento', default='Não informado')
    cannabis_experience = models.TextField(verbose_name='Experiência com prescrição de produtos à base de cannabis', default='Não informado')

    def __str__(self):
        return f'{self.name} | {self.specialty}'


class Education(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='educations')
    university = models.CharField(max_length=255, verbose_name='Universidade')
    course = models.CharField(max_length=255, verbose_name='Curso')

    def __str__(self):
        return f'{self.doctor} | {self.university} | {self.course}'
