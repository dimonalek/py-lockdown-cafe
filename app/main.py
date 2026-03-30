import app.cafe as cafe_pkg
import app.errors as errors_pkg


def go_to_cafe(friends: list[dict], cafe: cafe_pkg.Cafe) -> str:
    group_cant_visit = False
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors_pkg.VaccineError:
            group_cant_visit = True
            message = "All friends should be vaccinated"
        except errors_pkg.NotWearingMaskError:
            group_cant_visit = True
            masks_to_buy = sum(
                1 for friend in friends if not friend.get("wearing_a_mask")
            )
            message = f"Friends should buy {masks_to_buy} masks"
    if group_cant_visit:
        return message
    return f"Friends can go to {cafe.name}"
