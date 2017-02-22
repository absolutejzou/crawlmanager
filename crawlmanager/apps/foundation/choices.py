from djchoices import DjangoChoices, ChoiceItem


class Sex(DjangoChoices):
    MALE = ChoiceItem(0)
    FEMALE = ChoiceItem(1)


class UserStatus(DjangoChoices):
    NORMAL = ChoiceItem(0)
    DISABLED = ChoiceItem(1)
