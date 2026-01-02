from rest_framework.renderers import JSONRenderer

class SEADRenderer(JSONRenderer):
    """
    Formateur global pour le projet SEAD.
    Emballe toutes les réponses API dans un format standard.
    """
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        
        # On détermine le succès en fonction du code HTTP (2xx = True)
        success = True if response.status_code < 400 else False

        # Structure finale demandée par le guide
        res = {
            "success": success,
        }

        if success:
            res["data"] = data
            # Optionnel : Ajout de meta pour la pagination si présente
            if isinstance(data, dict) and 'results' in data:
                res["data"] = data['results']
                res["meta"] = {
                    "total": data.get('count'),
                    "next": data.get('next'),
                    "previous": data.get('previous')
                }
        else:
            # En cas d'erreur, on formate selon le guide
            res["error"] = {
                "code": "API_ERROR",
                "message": "Une erreur est survenue",
                "details": data
            }

        return super().render(res, accepted_media_type, renderer_context)