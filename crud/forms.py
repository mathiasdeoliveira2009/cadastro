from django import forms
from crud.models.cadastro_model import CadastroModel

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroModel
        fields = ["documento", "nome", "endereco"]
        error_messages = {
            "documento": {
                "max_length": "O documento deve ter no máximo 14 caracteres.",
                "required": "O campo Documento é obrigatório.",
            },
            "nome": {
                "required": "O campo Nome é obrigatório.",
            },
            "endereco": {
                "required": "O campo Endereço é obrigatório.",
            },
        }

    def clean_documento(self):
        documento = self.cleaned_data.get("documento")
        if not documento.isdigit():
            raise forms.ValidationError("O documento deve conter apenas números.")
        if len(documento) not in [11, 14]:  # CPF = 11, CNPJ = 14
            raise forms.ValidationError("O documento deve ter 11 ou 14 dígitos.")
        return documento