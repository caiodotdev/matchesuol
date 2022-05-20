from django.db import models


class Timestamp(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Competicao(Timestamp):
    # Fields
    nome = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.nome)


class Time(Timestamp):
    # Fields
    id_time = models.IntegerField(blank=True, null=True)
    nome_completo = models.CharField(max_length=255, blank=True, null=True)
    nome_comum = models.CharField(max_length=255, blank=True, null=True)
    brasao = models.URLField(blank=True, null=True)
    sigla = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.nome_comum)


class Match(Timestamp):
    # Fields
    id_match = models.IntegerField(blank=True, null=True)
    competicao = models.ForeignKey(
        Competicao, on_delete=models.CASCADE, blank=True, null=True)
    id_competicao = models.CharField(max_length=255, blank=True, null=True)
    time1 = models.ForeignKey(
        Time, on_delete=models.CASCADE, blank=True, null=True, related_name="time1")
    time2 = models.ForeignKey(
        Time, on_delete=models.CASCADE, blank=True, null=True, related_name="time2")
    data = models.DateTimeField(blank=True, null=True)
    horario = models.CharField(max_length=255, blank=True, null=True)
    local = models.CharField(max_length=255, blank=True, null=True)
    estadio = models.CharField(max_length=255, blank=True, null=True)
    rodada = models.IntegerField(blank=True, null=True)
    posicao = models.IntegerField(blank=True, null=True)
    placar1 = models.IntegerField(blank=True, null=True)
    placar2 = models.IntegerField(blank=True, null=True)
    penalti1 = models.CharField(max_length=255, blank=True, null=True)
    penalti2 = models.CharField(max_length=255, blank=True, null=True)
    eliminou_jogo_volta = models.BooleanField()
    classificou_gols_fora = models.BooleanField()
    datahora = models.BigIntegerField(blank=True, null=True)
    desempate_time1 = models.IntegerField(blank=True, null=True)
    desempate_time2 = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    predict_score = models.CharField(max_length=255, blank=True, null=True)
    predict_result = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.pk)
