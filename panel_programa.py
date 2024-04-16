from typing import List, Any, TypeVar, Callable, Type, cast
from datetime import datetime

T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)

def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ProgramaLuces:
    canales: List[int]
    tiempo: float

    def __init__(self, canales: List[int], tiempo: float) -> None:
        self.canales = canales
        self.tiempo = tiempo

    @staticmethod
    def from_dict(obj: Any) -> 'ProgramaLuces':
        assert isinstance(obj, dict)
        canales = from_list(from_int, obj.get("canales"))
        tiempo = from_float(obj.get("tiempo"))
        return ProgramaLuces(canales, tiempo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["canales"] = from_list(from_int, self.canales)
        result["tiempo"] = to_float(self.tiempo)
        return result


class Horario:
    programa: int
    semana: str
    hora_inicio: str
    hora_fin: str
    programa_luces: List[ProgramaLuces]

    def __init__(self, programa: int, semana: str, hora_inicio: str, hora_fin: str, programa_luces: List[ProgramaLuces]) -> None:
        self.programa = programa
        self.semana = semana
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.programa_luces = programa_luces

    @staticmethod
    def from_dict(obj: Any) -> 'Horario':
        assert isinstance(obj, dict)
        programa = int(from_str(obj.get("programa")))
        semana = from_str(obj.get("semana"))
        hora_inicio = from_str(obj.get("hora_inicio"))
        hora_fin = from_str(obj.get("hora_fin"))
        programa_luces = from_list(ProgramaLuces.from_dict, obj.get("programa_luces"))
        return Horario(programa, semana, hora_inicio, hora_fin, programa_luces)

    def to_dict(self) -> dict:
        result: dict = {}
        result["programa"] = from_str(str(self.programa))
        result["semana"] = from_str(self.semana)
        result["hora_inicio"] = self.hora_inicio.isoformat()
        result["hora_fin"] = self.hora_fin.isoformat()
        result["programa_luces"] = from_list(lambda x: to_class(ProgramaLuces, x), self.programa_luces)
        return result


class PanelPrograma:
    nodo: int
    horarios: List[Horario]

    def __init__(self, nodo: int, horarios: List[Horario]) -> None:
        self.nodo = nodo
        self.horarios = horarios

    @staticmethod
    def from_dict(obj: Any) -> 'PanelPrograma':
        assert isinstance(obj, dict)
        nodo = int(from_str(obj.get("nodo")))
        horarios = from_list(Horario.from_dict, obj.get("horarios"))
        return PanelPrograma(nodo, horarios)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nodo"] = from_str(str(self.nodo))
        result["horarios"] = from_list(lambda x: to_class(Horario, x), self.horarios)
        return result
    
    def verificar_horario(self) -> List[ProgramaLuces]:
        for horario in self.horarios:
            # Obtener la fecha y hora actual
            fecha_actual = datetime.now()

            # Convertir la hora específica a un objeto datetime
            fecha_hora_inicio = datetime.strptime(horario.hora_inicio, "%H:%M:%S")
            fecha_hora_fin = datetime.strptime(horario.hora_fin, "%H:%M:%S")

            # Asignar una hora específica (por ejemplo, 15:30:00)
            fecha_inicio = fecha_hora_inicio.replace(year=fecha_actual.year, month=fecha_actual.month, day=fecha_actual.day)
            fecha_fin = fecha_hora_fin.replace(year=fecha_actual.year, month=fecha_actual.month, day=fecha_actual.day)
            
            # Esto es para que no se apage un minuto y se vuelva a encender
            if fecha_actual.hour == 23 and fecha_actual.minute == 59:
                return horario.programa_luces
            if fecha_inicio <= fecha_actual <= fecha_fin: 
                return horario.programa_luces
            return []
        return []

def panel_programa_from_dict(s: Any) -> PanelPrograma:
    return PanelPrograma.from_dict(s)

def panel_programa_to_dict(x: PanelPrograma) -> Any:
    return to_class(PanelPrograma, x)

def get_datos_local():
    panel_programa = panel_programa_from_dict({
  "nodo": "31",
  "horarios": [
    {
      "programa": "33",
      "semana": "M",
      "hora_inicio": "10:00:01",
      "hora_fin": "22:40:00",
      "programa_luces": [
        {
          "canales": [
            4,
            2,
            10
          ],
          "tiempo": 5
        },
        {
          "canales": [
            4,
            2,
            12
          ],
          "tiempo": 5
        }
      ]
    },
    {
      "programa": "33",
      "semana": "M",
      "hora_inicio": "23:00:01",
      "hora_fin": "23:55:00",
      "programa_luces": [
        {
          "canales": [
            4,
            2,
            10
          ],
          "tiempo": 5
        },
        {
          "canales": [
            4,
            2,
            12
          ],
          "tiempo": 5
        }
      ]
        }
    ]
    })
    return panel_programa
