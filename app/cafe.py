import datetime
import app.errors as errors_pkg


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor or not visitor["vaccine"]:
            raise errors_pkg.NotVaccinatedError("Visitor is not vaccinated")
        elif visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise errors_pkg.OutdatedVaccineError(
                "Visitor has an outdated vaccine"
            )
        elif "wearing_a_mask" not in visitor or not visitor["wearing_a_mask"]:
            raise errors_pkg.NotWearingMaskError(
                "Visitor is not wearing a mask"
            )
        else:
            return f"Welcome to {self.name}"
