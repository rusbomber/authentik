# Generated by Django 3.2.3 on 2021-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_policies_event_matcher", "0014_alter_eventmatcherpolicy_app"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventmatcherpolicy",
            name="app",
            field=models.TextField(
                blank=True,
                choices=[
                    ("authentik.admin", "authentik Admin"),
                    ("authentik.api", "authentik API"),
                    ("authentik.events", "authentik Events"),
                    ("authentik.crypto", "authentik Crypto"),
                    ("authentik.flows", "authentik Flows"),
                    ("authentik.outposts", "authentik Outpost"),
                    ("authentik.lib", "authentik lib"),
                    ("authentik.policies", "authentik Policies"),
                    ("authentik.policies.dummy", "authentik Policies.Dummy"),
                    (
                        "authentik.policies.event_matcher",
                        "authentik Policies.Event Matcher",
                    ),
                    ("authentik.policies.expiry", "authentik Policies.Expiry"),
                    ("authentik.policies.expression", "authentik Policies.Expression"),
                    ("authentik.policies.hibp", "authentik Policies.HaveIBeenPwned"),
                    ("authentik.policies.password", "authentik Policies.Password"),
                    ("authentik.policies.reputation", "authentik Policies.Reputation"),
                    ("authentik.providers.proxy", "authentik Providers.Proxy"),
                    ("authentik.providers.ldap", "authentik Providers.LDAP"),
                    ("authentik.providers.oauth2", "authentik Providers.OAuth2"),
                    ("authentik.providers.saml", "authentik Providers.SAML"),
                    ("authentik.recovery", "authentik Recovery"),
                    ("authentik.sources.ldap", "authentik Sources.LDAP"),
                    ("authentik.sources.oauth", "authentik Sources.OAuth"),
                    ("authentik.sources.plex", "authentik Sources.Plex"),
                    ("authentik.sources.saml", "authentik Sources.SAML"),
                    (
                        "authentik.stages.authenticator_duo",
                        "authentik Stages.Authenticator.Duo",
                    ),
                    (
                        "authentik.stages.authenticator_static",
                        "authentik Stages.Authenticator.Static",
                    ),
                    (
                        "authentik.stages.authenticator_totp",
                        "authentik Stages.Authenticator.TOTP",
                    ),
                    (
                        "authentik.stages.authenticator_validate",
                        "authentik Stages.Authenticator.Validate",
                    ),
                    (
                        "authentik.stages.authenticator_webauthn",
                        "authentik Stages.Authenticator.WebAuthn",
                    ),
                    ("authentik.stages.captcha", "authentik Stages.Captcha"),
                    ("authentik.stages.consent", "authentik Stages.Consent"),
                    ("authentik.stages.deny", "authentik Stages.Deny"),
                    ("authentik.stages.dummy", "authentik Stages.Dummy"),
                    ("authentik.stages.email", "authentik Stages.Email"),
                    (
                        "authentik.stages.identification",
                        "authentik Stages.Identification",
                    ),
                    ("authentik.stages.invitation", "authentik Stages.User Invitation"),
                    ("authentik.stages.password", "authentik Stages.Password"),
                    ("authentik.stages.prompt", "authentik Stages.Prompt"),
                    ("authentik.stages.user_delete", "authentik Stages.User Delete"),
                    ("authentik.stages.user_login", "authentik Stages.User Login"),
                    ("authentik.stages.user_logout", "authentik Stages.User Logout"),
                    ("authentik.stages.user_write", "authentik Stages.User Write"),
                    ("authentik.tenants", "authentik Tenants"),
                    ("authentik.core", "authentik Core"),
                    ("authentik.managed", "authentik Managed"),
                ],
                default="",
                help_text="Match events created by selected application. When left empty, all applications are matched.",
            ),
        ),
    ]
