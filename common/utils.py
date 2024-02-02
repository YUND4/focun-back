from django.db.models import Model


def get_model(model: str) -> type[Model]:
    app, model = model.split('.')
    module = __import__(f'{app}.models', fromlist=[model])
    return getattr(module, model)