from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Add New Pitch',validators = [Required()])
    submit = SubmitField('Submit')

# class PitchForm(FlaskForm):
#     title = StringField('Title', validators = [Required()])
#     text = TextAreaField('Pitch',validators = [Required()])
#     category = SelectField('Category', choices = [('pickup lines', 'Pickup lines'),('interview','Interview'), ('product','Product'),('promotion','Promotion')], validators = [Required()])
#     submit = SubmitField('Post')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')
