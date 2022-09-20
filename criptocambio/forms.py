from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, HiddenField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MovimientosForm(FlaskForm):

    monedas = ["EUR", "ETH", "BNB", "LUNA", "SOL",
               "BTC", "BCH", "LINK", "ATOM", "USDT"]
    id = HiddenField()
    fecha = DateField("Fecha", validators=[DataRequired(
        message="Debes introducir una fecha")])
    tipo = RadioField(
        choices=[monedas],
        validators=[DataRequired(message="Elige una moneda")]
    )
    cantidad = FloatField("Cantidad", validators=[
        DataRequired(message="Debes especificar un número")])

    submit = SubmitField("Guardar", render_kw={"class": "blue-button"})
