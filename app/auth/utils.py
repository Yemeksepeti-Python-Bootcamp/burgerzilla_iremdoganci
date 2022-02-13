from marshmallow import Schema, fields
from marshmallow.validate import Regexp, Length


class LoginSchema(Schema):
    """ /auth/login [POST]

    Parameters:
    - Email
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])


class RegisterSchema(Schema):
    """ /auth/register [POST]
    Parameters:
    - Email
    - Name (Str)
    - Password (Str)
    """

    email = fields.Email(required=True, validate=[Length(max=64)])

    name = fields.Str(
        validate=[
            Regexp(
                r"^[A-Za-z]+((\s)?((\'|\-|\.)?([A-Za-z])+))*$", error="Invalid name!",
            )
        ]
    )
    password = fields.Str(required=True, validate=[Length(min=8, max=128)])
    address = fields.Str(required=True, validate=[Length(max=128)])
    user_type = fields.Str(required=True, validate=[Length(max=128)])