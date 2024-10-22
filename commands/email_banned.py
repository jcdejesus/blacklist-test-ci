from commands.base_command import BaseCommannd
from utils.blacklist_utils import get_blacklist_by_email


class EmailBanned(BaseCommannd):
    def __init__(self, email):
        self.email = email

    def execute(self):
        record = get_blacklist_by_email(self.email)
        if record is None:
            return {"email_found": False, "reason": "", "updated_at": "22/10/2024:00:00:00" }
        return {"email_found": True, "reason": record.reason,  "updated_at": "22/10/2024:00:00:00"}
