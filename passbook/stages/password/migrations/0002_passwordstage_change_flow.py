# Generated by Django 3.0.7 on 2020-06-29 08:51

import django.db.models.deletion
from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from passbook.flows.models import FlowDesignation
from passbook.stages.prompt.models import FieldTypes


def create_default_password_change(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    Flow = apps.get_model("passbook_flows", "Flow")
    FlowStageBinding = apps.get_model("passbook_flows", "FlowStageBinding")

    PromptStage = apps.get_model("passbook_stages_prompt", "PromptStage")
    Prompt = apps.get_model("passbook_stages_prompt", "Prompt")

    UserWriteStage = apps.get_model("passbook_stages_user_write", "UserWriteStage")

    db_alias = schema_editor.connection.alias

    flow, _ = Flow.objects.using(db_alias).update_or_create(
        slug="default-password-change",
        designation=FlowDesignation.STAGE_SETUP,
        defaults={"name": "Change Password"},
    )

    prompt_stage, _ = PromptStage.objects.using(db_alias).update_or_create(
        name="default-password-change-prompt",
    )
    password_prompt, _ = Prompt.objects.using(db_alias).update_or_create(
        field_key="password",
        defaults={
            "label": "Password",
            "type": FieldTypes.PASSWORD,
            "required": True,
            "placeholder": "Password",
            "order": 0,
        },
    )
    password_rep_prompt, _ = Prompt.objects.using(db_alias).update_or_create(
        field_key="password_repeat",
        defaults={
            "label": "Password (repeat)",
            "type": FieldTypes.PASSWORD,
            "required": True,
            "placeholder": "Password (repeat)",
            "order": 1,
        },
    )

    prompt_stage.fields.add(password_prompt)
    prompt_stage.fields.add(password_rep_prompt)
    prompt_stage.save()

    user_write, _ = UserWriteStage.objects.using(db_alias).update_or_create(
        name="default-password-change-write"
    )

    FlowStageBinding.objects.using(db_alias).update_or_create(
        target=flow, stage=prompt_stage, defaults={"order": 0}
    )
    FlowStageBinding.objects.using(db_alias).update_or_create(
        target=flow, stage=user_write, defaults={"order": 1}
    )


def update_default_stage_change(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    PasswordStage = apps.get_model("passbook_stages_password", "PasswordStage")
    Flow = apps.get_model("passbook_flows", "Flow")

    flow = Flow.objects.get(
        slug="default-password-change", designation=FlowDesignation.STAGE_SETUP,
    )

    stages = PasswordStage.objects.filter(name="default-authentication-password")
    if not stages.exists():
        return
    stage = stages.first()
    stage.change_flow = flow
    stage.save()


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_flows", "0006_auto_20200629_0857"),
        ("passbook_stages_password", "0001_initial"),
        ("passbook_stages_prompt", "0001_initial"),
        ("passbook_stages_user_write", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="passwordstage",
            name="change_flow",
            field=models.ForeignKey(
                blank=True,
                help_text="Flow used by an authenticated user to change their password. If empty, user will be unable to change their password.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="passbook_flows.Flow",
            ),
        ),
        migrations.RunPython(create_default_password_change),
        migrations.RunPython(update_default_stage_change),
    ]
