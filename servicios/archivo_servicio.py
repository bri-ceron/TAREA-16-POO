import json
from pathlib import Path


class ArchivoServicio:

    @staticmethod
    def cargar(ruta):

        ruta = Path(ruta)

        if not ruta.exists():
            return []

        try:

            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except (json.JSONDecodeError, OSError):

            return []

    @staticmethod
    def guardar(ruta, datos):

        ruta = Path(ruta)

        ruta.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            ruta,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )