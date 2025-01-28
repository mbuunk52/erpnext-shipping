# Copyright (c) 2020, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ParcelService(Document):
    pass

def get_parcel_service_providers():
    return ["LetMeShip", "SendCloud", "HST"]
