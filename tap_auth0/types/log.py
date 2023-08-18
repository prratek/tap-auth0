from singer_sdk.helpers._classproperty import classproperty
from singer_sdk.typing import StringType


class LogTypeType(StringType):
    """https://auth0.com/docs/deploy-monitor/logs/log-event-type-codes"""

    @classproperty
    def type_dict(cls):
        return {
            **super().type_dict,
            "enum": [
                "admin_update_launch",
                "api_limit",
                "cls",
                "cs",
                "depnote",
                "du",
                "f",
                "fapi",
                "fc",
                "fce",
                "fco",
                "fcoa",
                "fcp",
                "fcph",
                "fcpn",
                "fcpr",
                "fcpro",
                "fcu",
                "fd",
                "fdeac",
                "fdeaz",
                "fdecc",
                "fdu",
                "feacft",
                "feccft",
                "fede",
                "fens",
                "feoobft",
                "feotpft",
                "fepft",
                "fepotpft",
                "fercft",
                "fertft",
                "ferrt",
                "fi",
                "flo",
                "fn",
                "fp",
                "fs",
                "fsa",
                "fu",
                "fui",
                "fv",
                "fvr",
                "gd_auth_failed",
                "gd_auth_rejected",
                "gd_auth_succeed",
                "gd_enrollment_complete",
                "gd_otp_rate_limit_exceed",
                "gd_recovery_failed",
                "gd_recovery_rate_limit_exceed",
                "gd_recovery_succeed",
                "gd_send_pn",
                "gd_send_sms",
                "gd_send_sms_failure",
                "gd_send_voice",
                "gd_send_voice_failure",
                "gd_start_auth",
                "gd_start_enroll",
                "gd_tenant_update",
                "gd_unenroll",
                "gd_update_device_account",
                "limit_delegation",
                "/delegation",
                "limit_mu",
                "limit_wc",
                "limit_sul",
                "mfar",
                "mgmt_api_read",
                "pla",
                "pwd_leak",
                "ip",
                "s",
                "sapi",
                "sce",
                "scoa",
                "scp",
                "scph",
                "scpn",
                "scpr",
                "scu",
                "sd",
                "sdu",
                "seacft",
                "seccft",
                "sede",
                "sens",
                "seoobft",
                "seotpft",
                "sepft",
                "sercft",
                "sertft",
                "si",
                "srrt",
                "slo",
                "ss",
                "ssa",
                "sui",
                "sv",
                "svr",
                "sys_os_update_end",
                "sys_os_update_start",
                "sys_update_end",
                "sys_update_start",
                "ublkdu",
                "w",
            ],
        }
