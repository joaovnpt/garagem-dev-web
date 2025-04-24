from rest_framewok.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer