from django.core.exceptions import ValidationError
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params = {'value':value},
        )


def clean_full_name(value):
    full_name = value
    if not " " in full_name:
        raise ValidationError("Andika majina yako yasipungue mawili")



#
# def m_amount_clean(value):
#     m_amount = value
#     if TransactionPayeerForm.package == 'Silver':
#         if m_amount >= 10:
#             return m_amount
#         else:
#             raise ValidationError("weka pesa ya kutosha")







