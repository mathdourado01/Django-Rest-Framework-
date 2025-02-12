# Generated by Django 4.2.13 on 2024-07-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("escola", "0003_rename_nome_curso_codigo_curso_alter_curso_nivel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="nivel",
            field=models.CharField(
                choices=[("A", "Avançado"), ("I", "Intermediário"), ("B", "Básico")],
                default="B",
                max_length=1,
            ),
        ),
        migrations.CreateModel(
            name="Matricula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "periodo",
                    models.CharField(
                        choices=[
                            ("M", "Matutino"),
                            ("V", "Vespertino"),
                            ("N", "Noturno"),
                        ],
                        default="M",
                        max_length=1,
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.aluno"
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="escola.curso"
                    ),
                ),
            ],
        ),
    ]
