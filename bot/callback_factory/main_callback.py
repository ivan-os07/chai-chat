from aiogram.filters.callback_data import CallbackData


# Define a callback data class for the inline keyboard
class MainCb(CallbackData, prefix="pre"):
    first_action: str
    last_action: str

    @classmethod
    def create(cls, first_action: str, last_action: str) -> str:
        return cls(
            first_action=first_action, last_action=last_action
        ).pack()
