from fastapi import APIRouter, HTTPException

from app.models.message import Message
from app.models.frequencytable import FrequencyTable
from app.models.models import *

from app.utils.decrypt import decrypt

router = APIRouter()


@router.post("/freqlang")
async def create_freqlang(frequencytable: FrequencyTableIn_Pydantic):
    """Crea un nuevo registro en la tabla FrequencyTable

    Args:
        frequencytable (FrequencyTableIn_Pydantic): Datos en formato 
                                                    JSON de la forma 
                                                    { 
                                                        "freqlang": 
                                                        "string" 
                                                    }

    Returns:
        QuerySet: resultado ingresado en la tabla FrequencyTable
    """
    freqlang_obj = await FrequencyTable.create(**frequencytable.dict())
    return await FrequencyTable_Pydantic.from_tortoise_orm(freqlang_obj)


@router.put("/freqlang")
async def returns_freqlang_pk(pk: int):
    """Retorna el objeto que tiene el id igual al parametro pk

    Args:
        pk (int): Entero que es el id del objeto que se busca en la 
                  base de datos de

    Returns:
        QuerySet: Resultado que contiene la información solicitada con 
                  el put request
    """
    return await FrequencyTable.filter(id=pk).first()


@router.get("/freqlang")
async def get_freqlang():
    """Retorna todos los resultados obtenidos de la tabla FrequencyTable

    Returns:
        QuerySet: Resultado con toda la información obtenida de la tabla 
                  FrequencyTable
    """
    return await FrequencyTable.all()


@router.get("/freqlang/{pk}")
async def get_freqlang(pk: int):
    """Retorna el resultado que es igual a la variable pk solicitada con 
       el get request request

    Args:
        pk (int): Entro que es el iddel objeto quese busca en la base de
                  datos

    Returns:
        QuerySet: Resultado que contiene la información solicitada con 
                  el get request request
    """
    freqlang = await FrequencyTable.get_or_none(id=pk)
    if freqlang != None:
        return freqlang
    raise HTTPException(status_code=404, detail="Item not found")



@router.delete("/freqlang/{pk}")
async def delete_freqlang(pk: int):
    """Borre el registro de id pk

    Args:
        pk (int): Id del objeto a borar

    Returns:
        int: número de objetos eliminados
    """
    deleted_records = await FrequencyTable.get(id=pk).delete()
    if deleted_records > 0:
        return deleted_records
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/freqlang/decrypt")
async def decrypt_message(message: Message):
    """Retorna el mensaje [message] desencriptado haciendo uso del 
       último registro insertado en frequencyTable

    Args:
        message (Message): [description]

    Returns:
        [type]: [description]
    """
    try:
        freqlang = await FrequencyTable.all().order_by('-created').first()
    except Exception as e:
        return Message(message=str(e))
    freqlang = freqlang.freqlang
    encrypted_message = message.message
    decrypted_message = Message(message=decrypt(freqlang
                                                ,encrypted_message))
    return decrypted_message


@router.post("/freqlang/{pk}/decrypt")
async def decrypt_message(pk: int, message: Message):
    try:
        freqlang = await FrequencyTable.filter(id=pk).first()
    except Exception as e:
        return Message(message=str(e))
    freqlang = freqlang.freqlang
    encrypted_message = message.message
    decrypted_message = Message(message=decrypt(freqlang
                                                ,encrypted_message))
    return decrypted_message
